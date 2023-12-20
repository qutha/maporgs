from pathlib import Path

import gdown
import pandas as pd


def download_dataset(id: str, output_path: Path) -> None:
    gdown.download(id=id, output=str(output_path), quiet=False)


def generate_dataset(dataset: pd.DataFrame, option_number: int, step: int):
    return dataset.iloc[option_number::step]


def load_dataset(path: Path) -> pd.DataFrame:
    return pd.read_csv(str(path))


def save_dataset(dataset: pd.DataFrame, output_path: Path) -> None:
    dataset.to_csv(str(output_path), index=False)
