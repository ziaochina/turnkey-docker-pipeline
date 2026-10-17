"""
Main Execution Script for Turnkey Extraction Pipeline
"""
import os
import sys
from datetime import datetime, timezone
from pipeline.engine import TurnkeyPipelineEngine

def main():
    print("[*] Launching Turnkey Production Extraction Pipeline...")
    engine = TurnkeyPipelineEngine(output_dir="./data")
    
    # Generate 50 realistic enterprise records
    raw_payloads = []
    for i in range(1, 51):
        raw_payloads.append({
            "id": i,
            "source_domain": "industrial-supply.example.com",
            "sku_title": f"  High-Precision CNC Milling Cutter Model #{i:03d}   ",
            "price_usd": round(42.50 + i * 3.75, 2),
            "inventory_status": "IN_STOCK" if i % 4 != 0 else "BACKORDER",
            "timestamp_iso": datetime.now(timezone.utc).isoformat()
        })

    valid, errors = engine.process_batch(raw_payloads)
    stats = engine.reporter.finalize()

    out_file = engine.export_csv(valid, "sample_data.csv")
    print(f"[+] Output written to: {out_file}")
    print(f"[+] Records Processed: {stats.total_records} (Valid: {stats.valid_records}, Errors: {stats.invalid_records})")
    print(f"[+] Execution Rate: {stats.throughput_rps} records/sec")

if __name__ == "__main__":
    main()
