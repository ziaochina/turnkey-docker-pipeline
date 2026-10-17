"""
Pipeline Health & Execution Metrics
"""
import time
from .models import PipelineStats

class HealthReporter:
    def __init__(self):
        self.start_time = time.time()
        self.stats = PipelineStats()

    def record_success(self):
        self.stats.total_records += 1
        self.stats.valid_records += 1

    def record_failure(self):
        self.stats.total_records += 1
        self.stats.invalid_records += 1

    def finalize(self) -> PipelineStats:
        self.stats.elapsed_seconds = max(0.001, time.time() - self.start_time)
        self.stats.throughput_rps = round(self.stats.valid_records / self.stats.elapsed_seconds, 2)
        return self.stats
