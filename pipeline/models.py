"""
Pydantic V2 Data Contracts & Strict Schema Validation
"""
from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel, Field, field_validator

class ExtractionRecord(BaseModel):
    id: int = Field(gt=0, description="Unique primary key")
    source_domain: str = Field(min_length=3, description="Target domain source")
    sku_title: str = Field(min_length=1, max_length=255, description="Sanitized item title")
    price_usd: float = Field(gt=0, description="Cleaned numerical price in USD")
    inventory_status: str = Field(pattern="^(IN_STOCK|LOW_STOCK|BACKORDER|OUT_OF_STOCK)$")
    timestamp_iso: str = Field(description="ISO-8601 UTC timestamp")

    @field_validator("sku_title")
    @classmethod
    def clean_title(cls, v: str) -> str:
        return " ".join(v.split()).strip()

class PipelineStats(BaseModel):
    total_records: int = 0
    valid_records: int = 0
    invalid_records: int = 0
    elapsed_seconds: float = 0.0
    throughput_rps: float = 0.0
