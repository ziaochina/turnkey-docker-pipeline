"""
Unit Tests for Pydantic Schema Contracts
"""
import pytest
from pydantic import ValidationError
from pipeline.models import ExtractionRecord

def test_valid_record():
    r = ExtractionRecord(
        id=1,
        source_domain="example.com",
        sku_title="  Test SKU Title  ",
        price_usd=19.99,
        inventory_status="IN_STOCK",
        timestamp_iso="2026-10-17T12:00:00Z"
    )
    assert r.sku_title == "Test SKU Title"
    assert r.price_usd == 19.99

def test_invalid_price():
    with pytest.raises(ValidationError):
        ExtractionRecord(
            id=2,
            source_domain="example.com",
            sku_title="Bad Price",
            price_usd=-5.0,
            inventory_status="IN_STOCK",
            timestamp_iso="2026-10-17T12:00:00Z"
        )

def test_invalid_inventory():
    with pytest.raises(ValidationError):
        ExtractionRecord(
            id=3,
            source_domain="example.com",
            sku_title="Bad Status",
            price_usd=10.0,
            inventory_status="SOME_UNKNOWN_STATUS",
            timestamp_iso="2026-10-17T12:00:00Z"
        )
