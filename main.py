from etl.extract import extract_from_csv
from etl.transform import clean_data, create_dim_artist, create_dim_album, create_dim_track, create_fact_audio
from etl.load import load_data

def run_etl():
    print('Extracting data...')
    data_raw = extract_from_csv('SpotifyFeatures.csv')

    print('Transforming data...')
    data_clean = clean_data(data_raw)
    dim_artist = create_dim_artist(data_clean)
    dim_album = create_dim_album(data_clean)
    dim_track = create_dim_track(data_clean)
    fact_audio = create_fact_audio(data_clean)

    print('Loading data to SQL Server...')
    load_data(dim_artist, 'dim_artist')
    load_data(dim_album, 'dim_album')
    load_data(dim_track, 'dim_track')
    load_data(fact_audio, 'fact_audio')

    print('ETL completed successfully!')

if __name__ == "__main__":
    run_etl()
