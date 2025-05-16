# Spotify ETL Pipeline

A simple ETL (Extract, Transform, Load) pipeline built in Python to process and load Spotify track data into a SQL Server database.


## Dataset

The dataset used is the ["Spotify Features"](https://www.kaggle.com/datasets/geomack/spotifyclassification) dataset from Kaggle, which includes audio features for thousands of tracks.

## How It Works

1. **Extract**  
   Loads the CSV into a pandas DataFrame.

2. **Transform**  
   - Cleans duplicate and null data.
   - Normalizes text.
   - Creates dimension and fact tables:
     - `dim_artist`
     - `dim_album`
     - `dim_track`
     - `fact_audio`

3. **Load**  
   - Loads each table into a SQL Server database using SQLAlchemy.
   - SQL Server credentials are read from `config.json`.

### Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/spotify-etl-pipeline.git
cd spotify-etl-pipeline

2. Install required packages:

pip install -r requirements.txt

3. Create a config.json file in the root directory:

{
  "server": "YOUR_SERVER_NAME",
  "database": "YOUR_DATABASE_NAME",
  "trusted_connection": true
}

4. Place the SpotifyFeatures.csv file in the project root (or update the path in main.py).

5. Run the ETL process:

  python main.py

