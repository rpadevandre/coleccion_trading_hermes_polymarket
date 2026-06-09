"""Static contract tests for Property Maintenance Triage backend scaffold.

These tests avoid importing FastAPI so they can run before dependencies are
installed. Runtime API tests should be added once the backend is promoted
from scaffold to active MVP.
"""
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_required_files_exist() -> None:
    for relative in [
        "app/main.py",
        "app/config.py",
        "app/schemas.py",
        "app/services.py",
        "app/repository.py",
        "app/routers/health.py",
        "app/routers/intakes.py",
        "app/routers/assessments.py",
        "app/routers/admin.py",
        "requirements.txt",
        ".env.example",
    ]:
        assert (ROOT / relative).exists(), relative


def test_mongo_is_documented_but_not_connected() -> None:
    config = (ROOT / "app/config.py").read_text(encoding="utf-8")
    repo = (ROOT / "app/repository.py").read_text(encoding="utf-8")
    assert "enable_mongo: bool = False" in config
    assert "mongo_uri" in config
    assert "InMemoryRepository" in repo
    assert "does not open a" in repo


def test_business_specific_contract() -> None:
    meta = (ROOT / "app/routers/health.py").read_text(encoding="utf-8")
    assert "maintenance_request" in meta
    assert "triage_ticket" in meta
