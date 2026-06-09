"""FastAPI entrypoint for Property Maintenance Triage.

Database status: Mongo-ready contract only. This app intentionally uses an
in-memory repository until MongoDB credentials, collections, indexes, and
retention rules are approved.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.routers import admin, assessments, health, intakes


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.app_name,
        version=settings.app_version,
        description=settings.description,
        docs_url="/docs",
        redoc_url="/redoc",
    )
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.allowed_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(health.router)
    app.include_router(intakes.router, prefix="/intakes", tags=["intakes"])
    app.include_router(assessments.router, prefix="/assessments", tags=["assessments"])
    app.include_router(admin.router, prefix="/admin", tags=["admin"])
    return app


app = create_app()
