from pathlib import Path
from typing import Final

ROOT_DIR: Final = Path(__file__).parent.parent.parent
DATA_DIR: Final = ROOT_DIR / "data"

DEFAULT_DATASET_PATH: Final = DATA_DIR / "dataset.csv"
DEFAULT_INDIVIDUAL_DATASET_PATH: Final = DATA_DIR / "individual.csv"

DEFAULT_LOCATIONS_DATASET_PATH: Final = DATA_DIR / "locations.csv"
DEFAULT_MAP_PATH: Final = DATA_DIR / "map.html"
