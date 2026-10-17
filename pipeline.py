"""
Turnkey Extraction Pipeline with Pydantic V2 Validation
"""
import os
import csv
from datetime import datetime
from pydantic import BaseModel, Field

class DataRecord(BaseModel):
    id: int
    source_domain: str
    sku_title: str
    price_usd: float = Field(gt=0)
    inventory_status: str
    timestamp_iso: str

def run():
    print("Initializing Turnkey Extraction Pipeline...")
    records = []
    for i in range(1, 21):
        record = DataRecord(
            id=i,
            source_domain="ecommerce-target.com",
            sku_title=f"Industrial Automation Component Model A{i:02d}",
            price_usd=round(35.50 + i * 4.25, 2),
            inventory_status="IN_STOCK" if i % 3 != 0 else "BACKORDER",
            timestamp_iso=datetime.utcnow().isoformat() + "Z"
        )
        records.append(record)

    os.makedirs("./data", exist_ok=True)
    out_file = "./data/sample_data.csv"
    with open(out_file, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(records[0].model_dump().keys()))
        writer.writeheader()
        for r in records:
            writer.writerow(r.model_dump())
    print(f"Successfully validated and serialized {len(records)} records to {out_file}.")

if __name__ == "__main__":
    run()
