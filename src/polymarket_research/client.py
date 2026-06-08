"""Read-only async client for public Polymarket APIs."""

from __future__ import annotations

import asyncio
from collections.abc import Mapping
from typing import Any

import aiohttp

from .models import Market


class PolymarketClientError(RuntimeError):
    """Raised when a Polymarket public API request fails."""


class PolymarketClient:
    def __init__(
        self,
        *,
        gamma_base_url: str = "https://gamma-api.polymarket.com",
        clob_base_url: str = "https://clob.polymarket.com",
        data_base_url: str = "https://data-api.polymarket.com",
        timeout_seconds: int = 20,
        max_retries: int = 3,
    ) -> None:
        self.gamma_base_url = gamma_base_url.rstrip("/")
        self.clob_base_url = clob_base_url.rstrip("/")
        self.data_base_url = data_base_url.rstrip("/")
        self.timeout = aiohttp.ClientTimeout(total=timeout_seconds)
        self.max_retries = max_retries

    async def _get_json(self, url: str, params: Mapping[str, Any] | None = None) -> Any:
        last_error: Exception | None = None
        for attempt in range(1, self.max_retries + 1):
            try:
                async with aiohttp.ClientSession(timeout=self.timeout) as session:
                    async with session.get(url, params=params) as response:
                        if response.status in {429, 529, 502, 503, 504} and attempt < self.max_retries:
                            await asyncio.sleep(2 ** (attempt - 1))
                            continue
                        if response.status >= 400:
                            body = await response.text()
                            raise PolymarketClientError(f"GET {url} failed with HTTP {response.status}: {body[:300]}")
                        return await response.json()
            except (aiohttp.ClientError, asyncio.TimeoutError) as exc:
                last_error = exc
                if attempt < self.max_retries:
                    await asyncio.sleep(2 ** (attempt - 1))
                    continue
                break
        raise PolymarketClientError(f"GET {url} failed after {self.max_retries} attempts: {last_error}")

    async def markets(self, *, limit: int = 20, order: str = "volume") -> list[Market]:
        payload = await self._get_json(
            f"{self.gamma_base_url}/markets",
            params={"limit": limit, "active": "true", "closed": "false", "order": order, "ascending": "false"},
        )
        if not isinstance(payload, list):
            raise PolymarketClientError(f"Unexpected markets payload: {type(payload)!r}")
        return [Market.from_gamma(item) for item in payload]

    async def market_by_slug(self, slug: str) -> Market | None:
        payload = await self._get_json(f"{self.gamma_base_url}/markets", params={"slug": slug})
        if isinstance(payload, list) and payload:
            return Market.from_gamma(payload[0])
        return None

    async def search(self, query: str, *, limit: int = 10) -> list[Market]:
        payload = await self._get_json(f"{self.gamma_base_url}/public-search", params={"q": query})
        markets: list[Market] = []
        for event in payload.get("events", []) if isinstance(payload, dict) else []:
            for raw_market in event.get("markets", []):
                markets.append(Market.from_gamma(raw_market))
                if len(markets) >= limit:
                    return markets
        return markets

    async def spread(self, token_id: str) -> float | None:
        if not token_id:
            return None
        payload = await self._get_json(f"{self.clob_base_url}/spread", params={"token_id": token_id})
        try:
            return float(payload.get("spread"))
        except (AttributeError, TypeError, ValueError):
            return None
