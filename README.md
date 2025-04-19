# Witboost-MCP


# Data Product Test API

A FastMCP-based API to evaluate data products against computational policies.

## Setup

```bash
python -m venv venv   # create a venv
source venv/bin/activate
pip install -r requirements.txt
```

## Configuration

Edit config.yaml:
```
governance_eval_url: "http://localhost:8080/governance/v1/computational-governance/evaluate"
```


## Running Locally

```
python mcp_server.py
```

