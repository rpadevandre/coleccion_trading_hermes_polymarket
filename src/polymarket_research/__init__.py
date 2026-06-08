"""Read-only Polymarket research package for Hermes."""

from .client import PolymarketClient
from .models import Market, ScoreBreakdown
from .paper import PaperTradingConfig, PaperPosition, maybe_open_paper_position, portfolio_summary
from .scorer import score_market

__all__ = [
    "Market",
    "PolymarketClient",
    "ScoreBreakdown",
    "PaperTradingConfig",
    "PaperPosition",
    "maybe_open_paper_position",
    "portfolio_summary",
    "score_market",
]
