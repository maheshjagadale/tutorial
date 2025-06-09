import yaml
import pandas as pd
# Load data into a CSV file

def load(df, config_path):
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)
    df.to_csv(config["output_path"], index=False)
