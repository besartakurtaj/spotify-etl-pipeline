import pandas as pd

def clean_data(data: pd.DataFrame) -> pd.DataFrame:
    """Basic cleaning."""
    data.drop_duplicates(subset=['track_name', 'artist_name'], inplace=True)

    key_cols = ['danceability', 'energy', 'popularity', 'tempo']
    data.dropna(subset=key_cols, inplace=True)

    data['track_name'] = data['track_name'].str.lower().str.strip()
    data['artist_name'] = data['artist_name'].str.lower().str.strip()

    return data

def create_dim_artist(data: pd.DataFrame) -> pd.DataFrame:
    return data[['artist_name']].drop_duplicates().reset_index(drop=True)

def create_dim_album(data: pd.DataFrame) -> pd.DataFrame:
    return data[['track_name']].drop_duplicates().reset_index(drop=True)

def create_dim_track(data: pd.DataFrame) -> pd.DataFrame:
    return data[['track_id', 'track_name', 'artist_name']].drop_duplicates().reset_index(drop=True)

def create_fact_audio(data: pd.DataFrame) -> pd.DataFrame:
    fact_columns = ['track_id', 'popularity', 'acousticness', 'danceability', 'duration_ms', 'energy',
                    'instrumentalness', 'key', 'liveness', 'loudness', 'mode', 'speechiness', 'tempo',
                    'time_signature', 'valence']
    return data[fact_columns]
