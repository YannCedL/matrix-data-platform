from matrix_data_platform import pipeline_status

def test_pipeline_status():
    c = pipeline_status()
    assert c.result["overall_status"] == "healthy"
    assert len(c.result["pipelines"]) > 0
