"""
Turnkey Extraction Execution Engine
Provides streaming CSV/JSONL serialization and schema validation.
"""
import os
import csv
import json
from typing import List, Dict, Any, Tuple
from .models import ExtractionRecord
from .monitoring import HealthReporter

class TurnkeyPipelineEngine:
    def __init__(self, output_dir: str = "./data"):
        self.output_dir = output_dir
        self.reporter = HealthReporter()
        os.makedirs(self.output_dir, exist_ok=True)

    def process_batch(self, raw_items: List[Dict[str, Any]]) -> Tuple[List[ExtractionRecord], List[str]]:
        valid_records: List[ExtractionRecord] = []
        errors: List[str] = []

        for idx, item in enumerate(raw_items):
            try:
                record = ExtractionRecord(**item)
                valid_records.append(record)
                self.reporter.record_success()
            except Exception as e:
                errors.append(f"Row {idx}: {str(e)}")
                self.reporter.record_failure()

        return valid_records, errors

    def export_csv(self, records: List[ExtractionRecord], filename: str = "output.csv") -> str:
        if not records:
            return ""
        out_path = os.path.join(self.output_dir, filename)
        temp_path = out_path + ".tmp"
        
        fieldnames = list(records[0].model_dump().keys())
        with open(temp_path, "w", encoding="utf-8-sig", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for r in records:
                writer.writerow(r.model_dump())
        
        os.replace(temp_path, out_path)
        return out_path
