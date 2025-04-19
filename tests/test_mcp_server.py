import pytest
from data_product_test_api import test_data_product
from mcp.client import MCPClient
from pydantic import ValidationError

# Stub governance HTTP call
@pytest.fixture(autouse=True)
def patch_httpx(monkeypatch):
    import data_product_test_api.server as srv
    class Dummy:
        def raise_for_status(self): pass
        def json(self): return {'reportId': 'rpt-001'}
    class Client:
        def post(self, url, json): return Dummy()
    monkeypatch.setattr(srv.httpx, 'Client', lambda: Client())
    yield

client = MCPClient(base_url='http://localhost:8000')

valid = {
    'id':'123','displayName':'Test','environment':'dev',
    'resourceType':'dataset','descriptor':'sample','labels':[]
}

def test_run_tool():
    res = client.run_tool(name='Data Product Test', input=valid)
    assert res == {'reportId':'rpt-001'}


def test_missing_id():
    bad = valid.copy(); bad.pop('id')
    with pytest.raises(ValidationError):
        client.run_tool(name='Data Product Test', input=bad)