import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [24, 43, 24, 56],
    "City": ["New York", "LA", "Chicago", "Houston"],
}

df = pd.DataFrame(data)

df.head(2)

df = df.replace("Alice", "Alan")
