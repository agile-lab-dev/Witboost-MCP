import yaml
from pathlib import Path

# Load config.yaml from project root
cfg_path = Path(__file__).parents[1] / 'config.yaml'
with cfg_path.open('r', encoding='utf-8') as f:
    cfg = yaml.safe_load(f)

GOVERNANCE_EVAL_URL = cfg.get(
    'governance_eval_url',
    'http://localhost:8080/governance/v1/computational-governance/evaluate'
)