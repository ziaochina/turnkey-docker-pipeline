"""
Unit Tests for Health Reporter
"""
from pipeline.monitoring import HealthReporter

def test_health_reporter():
    reporter = HealthReporter()
    reporter.record_success()
    reporter.record_success()
    reporter.record_failure()
    stats = reporter.finalize()

    assert stats.total_records == 3
    assert stats.valid_records == 2
    assert stats.invalid_records == 1
    assert stats.throughput_rps > 0
