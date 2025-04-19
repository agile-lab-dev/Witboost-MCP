from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel, Field
from typing import List, Dict
import httpx
from .config import GOVERNANCE_EVAL_URL

class DataProductTest(BaseModel):
    id: str = Field(..., description='Unique identifier')
    displayName: str = Field(..., description='Human‑readable name')
    environment: str = Field(..., description='dev/test/prod')
    resourceType: str = Field(..., description='Type of resource')
    descriptor: str = Field(..., description='Descriptor YAML or JSON')
    labels: List[str] = Field(default_factory=list)

# MCP app
mcp = FastMCP('Data Product Test API')

@mcp.tool(name='Data Product Test')
def test_data_product(data: Dict) -> Dict:
    '''Proxy to governance evaluation.'''
    with httpx.Client() as client:
        resp = client.post(GOVERNANCE_EVAL_URL, json=data)
        resp.raise_for_status()
        return resp.json()

if __name__ == '__main__':
    mcp.run()