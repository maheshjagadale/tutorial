import pandas as pd
from pipeline.transform import transform

def test_transform():
    data = pd.DataFrame({
        "id": [1, 2],
        "name": ["Test1", "Test2"],
        "age": [17, 25]
    })
    result = transform(data)
    assert result.loc[0, "age_group"] == "Minor"
    assert result.loc[1, "age_group"] == "Adult"
