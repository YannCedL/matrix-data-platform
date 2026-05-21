# test du moteur de supervision de pipelines Matrix
from matrix_data_platform.monitor import pipeline_status

def test_pipeline_status():
    contract = pipeline_status()
    assert contract is not None
    assert len(contract.result["pipelines"]) >= 1
    assert len(contract.evidence) >= 1
