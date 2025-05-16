import pandas as pd 

def extract_from_csv(file_path: str) -> pd.DataFrame:
    """ """
    data = pd.read_csv(file_path)
    return data