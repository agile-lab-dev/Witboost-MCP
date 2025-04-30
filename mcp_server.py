from fastmcp import FastMCP
from pydantic import BaseModel, Field
from typing import List, Dict, Any
import httpx
from config import GOVERNANCE_URL


class DataProductTest(BaseModel):
    id: str = Field(..., description='Unique identifier')
    displayName: str = Field(..., description='Human‑readable name')
    environment: str = Field(..., description='dev/test/prod')
    resourceType: str = Field(..., description='Type of resource')
    descriptor: str = Field(..., description='Descriptor YAML or JSON')
    labels: List[str] = Field(default_factory=list)

# MCP app
mcp = FastMCP('DataProductTest')

@mcp.tool(name='evaluateDataProduct', description='Evaluate a data product against the registered governance policies')
def eval_data_product(data: DataProductTest) -> Dict:
    payload = data.model_dump()
    try:
        with httpx.Client() as client:
            resp = client.post(f"{GOVERNANCE_URL}/v1/computational-governance/evaluate", json=payload)
            resp.raise_for_status()
            report = resp.json()
            return {"reportId": report["reportId"]}
    except httpx.HTTPError as e:
        return {"error": str(e)}

@mcp.tool(name='getEvaluationStatus', description='Retrieve the evaluation report by ID. If status is pending, the evaluation is still running and this endpoint should be called again.')
def get_evaluation_status(report_id: str) -> Dict[str, Any]:
    """Retrieve evaluation report details given an evaluation report ID."""
    try:
        with httpx.Client() as client:
            resp = client.get(f"{GOVERNANCE_URL}/v1/computational-governance/evaluation-reports/{report_id}")
            resp.raise_for_status()
            return resp.json()
    except httpx.HTTPError as e:
        return {"error": str(e)}

if __name__ == '__main__':
    mcp.run()