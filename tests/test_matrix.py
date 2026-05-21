from matrix_data_platform.monitor import pipeline_status

def test_pipeline_status():
    c = pipeline_status()
    assert "global_system_health" in c.result
    assert len(c.result["pipelines"]) > 0
