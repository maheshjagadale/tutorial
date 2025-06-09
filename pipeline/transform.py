def transform(df):
    # Add a new column 'age_group'
    df["age_group"] = df["age"].apply(lambda x: "Adult" if x >= 30 else "Minor")
    return df
