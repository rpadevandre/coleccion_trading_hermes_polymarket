"""Domain models for the read-only Polymarket research MVP."""

from __future__ import annotations

from dataclasses import dataclass
import json
from typing import Any


def _parse_json_list(value: Any) -> list[Any]:
    if value is None or value == "":
        return []
    if isinstance(value, list):
        return value
    if isinstance(value, str):
        try:
            parsed = json.loads(value)
        except json.JSONDecodeError:
            return []
        return parsed if isinstance(parsed, list) else []
    return []


def _as_float(value: Any, default: float = 0.0) -> float:
    try:
        if value is None or value == "":
            return default
        return float(value)
    except (TypeError, ValueError):
        return default


@dataclass(frozen=True)
class Market:
    market_id: str
    question: str
    condition_id: str
    slug: str
    outcomes: list[str]
    outcome_prices: list[float]
    clob_token_ids: list[str]
    volume: float
    liquidity: float
    active: bool
    closed: bool

    @classmethod
    def from_gamma(cls, raw: dict[str, Any]) -> "Market":
        outcomes = [str(x) for x in _parse_json_list(raw.get("outcomes"))]
        outcome_prices = [_as_float(x) for x in _parse_json_list(raw.get("outcomePrices"))]
        clob_token_ids = [str(x) for x in _parse_json_list(raw.get("clobTokenIds"))]
        return cls(
            market_id=str(raw.get("id") or raw.get("marketId") or raw.get("conditionId") or ""),
            question=str(raw.get("question") or raw.get("title") or ""),
            condition_id=str(raw.get("conditionId") or raw.get("condition_id") or ""),
            slug=str(raw.get("slug") or ""),
            outcomes=outcomes,
            outcome_prices=outcome_prices,
            clob_token_ids=clob_token_ids,
            volume=_as_float(raw.get("volume")),
            liquidity=_as_float(raw.get("liquidity")),
            active=bool(raw.get("active", True)),
            closed=bool(raw.get("closed", False)),
        )

    def to_db_tuple(self) -> tuple[Any, ...]:
        return (
            self.market_id,
            self.question,
            self.condition_id,
            self.slug,
            json.dumps(self.outcomes, ensure_ascii=False),
            json.dumps(self.outcome_prices),
            json.dumps(self.clob_token_ids),
            self.volume,
            self.liquidity,
            int(self.active),
            int(self.closed),
        )


@dataclass(frozen=True)
class ScoreBreakdown:
    total_score: int
    recommendation: str
    dimensions: dict[str, int]
    reasoning: list[str]


@dataclass(frozen=True)
class Signal:
    market: Market
    score: ScoreBreakdown
    created_at: str
