import os
import json

BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

config_path = os.path.join(BASE_DIR, "configs", "config.json")

with open(config_path, "r") as f:
    config = json.load(f)

print(config)