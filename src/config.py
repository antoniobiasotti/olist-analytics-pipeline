from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_RAW = BASE_DIR / "data" / "raw"
DATA_WAREHOUSE = BASE_DIR / "data" / "warehouse"

DUCKDB_PATH = DATA_WAREHOUSE / "olist.duckdb"
