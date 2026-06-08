# Fast Market Strategy — Weather / Same-Day Paper Trading

Purpose: make the paper-trading loop resolve quickly enough to measure win/loss rate. Long-horizon markets such as elections, IPOs, or sports championships can stay open for months and do not produce useful feedback for a small experiment.

## Rule

Default scanner behavior should prefer markets whose Polymarket `endDate` is within 24 hours.

```text
POLYMARKET_MAX_HOURS_TO_CLOSE=24
```

This is still read-only/paper-only. No wallets. No real orders.

## Why weather is a good fit

Weather markets often resolve same day or next day and can be benchmarked against external forecast sources.

Good categories:

- daily high / low temperature;
- rain / precipitation probability;
- snowfall amount;
- wind speed thresholds;
- storm landfall / advisory markets when resolution is near.

Avoid for now:

- seasonal hurricane totals;
- annual climate records;
- markets without a clear end date;
- low-liquidity markets where prices are stale.

## Proposed prediction flow

1. Scan only markets closing within 24h.
2. Detect weather-related markets from question/slug keywords.
3. Extract location, date, variable and threshold from the question.
4. Pull external forecasts from multiple sources when available:
   - weather.gov / NWS for USA;
   - Open-Meteo for global forecasts;
   - Meteostat or NOAA historical normals for sanity checks;
   - local meteorological agencies when the city/country is outside USA.
5. Convert forecasts into an estimated probability.
6. Compare estimated probability against Polymarket YES/NO prices.
7. Open only a fictional paper position if:
   - market closes <= 24h;
   - external forecasts agree enough;
   - implied probability has a clear gap vs market price;
   - spread/liquidity gates pass;
   - exposure caps allow it.
8. Resolve automatically after close and track win rate/loss rate.

## Useful AI components

- `WeatherQuestionParserAI`: extracts city, date, metric, threshold and side.
- `ForecastConsensusAI`: summarizes multiple forecast sources and flags disagreement.
- `ProbabilityCalibrator`: converts deterministic/ensemble forecast values into probability bands.
- `MarketEdgeExplainer`: explains why the paper position was or was not opened.

## Cyber/risk controls

- Public forecast APIs only; no scraping credentials.
- Cache source payloads with timestamps for auditability.
- Never use LLM output as the only prediction source.
- Require deterministic parser tests for market-question extraction.
- Keep all positions paper-only until there is enough resolved history.

## Current implementation status

Implemented now:

- `Market.end_date` parsing from Gamma API.
- `Market.hours_to_close()` helper.
- `PolymarketClient.markets(max_hours_to_close=...)` filter.
- `scripts/scan_markets.py --max-hours-to-close` CLI flag.
- `scripts/cron_polymarket_scan.sh` defaults to `POLYMARKET_MAX_HOURS_TO_CLOSE=24`.

Next:

- add weather-specific parser/scorer;
- add Open-Meteo/NWS read-only adapters;
- add weather probability edge calculation;
- report resolved fast-market win/loss rate separately from legacy long-horizon positions.
