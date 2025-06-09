from pipeline.extract import extract
from pipeline.transform import transform
from pipeline.load import load

def main():
    config_path = "config/config.yaml"
    df = extract(config_path)
    df = transform(df)
    load(df, config_path)
    print("Pipeline executed successfully.")

if __name__ == "__main__":
    main()
