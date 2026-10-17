"""
Unit Tests for Pipeline Execution Engine
"""
import os
import tempfile
from pipeline.engine import TurnkeyPipelineEngine

def test_batch_processing():
    with tempfile.TemporaryDirectory() as tmpdir:
        engine = TurnkeyPipelineEngine(output_dir=tmpdir)
        raw = [
            {"id": 1, "source_domain": "a.com", "sku_title": "Item 1", "price_usd": 10.0, "inventory_status": "IN_STOCK", "timestamp_iso": "2026-10-17T00:00:00Z"},
            {"id": 2, "source_domain": "b.com", "sku_title": "Item 2", "price_usd": -1.0, "inventory_status": "IN_STOCK", "timestamp_iso": "2026-10-17T00:00:00Z"}
        ]
        valid, errors = engine.process_batch(raw)
        assert len(valid) == 1
        assert len(errors) == 1

        out = engine.export_csv(valid, "test.csv")
        assert os.path.exists(out)
