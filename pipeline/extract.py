import pandas as pd
import yaml

def extract(config_path):
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)
    data = pd.read_csv(config["data_source"])
    return data
