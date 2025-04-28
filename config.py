import yaml
from pathlib import Path

# Load config.yaml from project root
cfg_path = Path(__file__).parents[0] / 'config.yaml'
with cfg_path.open('r', encoding='utf-8') as f:
    cfg = yaml.safe_load(f)

GOVERNANCE_URL = cfg.get(
    'governance_url',
)