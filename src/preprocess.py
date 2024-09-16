import pandas as pd

def preprocess_data(data):
    df = pd.DataFrame(data)
    # Convert tags from list to space-separated string
    df['tags'] = df['tags'].apply(lambda x: ' '.join(x))
    return df
