import pandas as pd
from pathlib import Path

DATA_URL = "https://www.football-data.co.uk/mmz4281/{season}/E0.csv"

SEASONS = [
    "1617",
    "1718",
    "1819",
    "1920",
    "2021",
    "2122",
    "2223",
    "2324",
    "2425",
    "2526",
]

RAW_DATA_DIR = Path("data/raw")


def download_season(season):
    url = DATA_URL.format(season=season)

    print(f"Downloading {season}...")

    df = pd.read_csv(url)

    output_path = RAW_DATA_DIR / f"E0_{season}.csv"
    df.to_csv(output_path, index=False)

    print(f"Saved {output_path}")


def main():
    RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

    for season in SEASONS:
        download_season(season)


if __name__ == "__main__":
    main()
