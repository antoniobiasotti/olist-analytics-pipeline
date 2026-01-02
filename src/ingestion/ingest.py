import duckdb
import pandas as pd
from src.config import DATA_RAW, DUCKDB_PATH


TABLES = {
    "orders": "olist_orders_dataset.csv",
    "order_items": "olist_order_items_dataset.csv",
    "customers": "olist_customers_dataset.csv",
    "products": "olist_products_dataset.csv",
    "reviews": "olist_order_reviews_dataset.csv",
    "payments": "olist_order_payments_dataset.csv",
    "sellers": "olist_sellers_dataset.csv",
}


def ingest_csv(table_name: str, file_name: str, con):
    print(f"Ingesting {file_name} -> table {table_name}")
    df = pd.read_csv(DATA_RAW / file_name)
    con.execute(f"CREATE OR REPLACE TABLE {table_name} AS SELECT * FROM df")


def main():
    con = duckdb.connect(DUCKDB_PATH)

    for table, file in TABLES.items():
        ingest_csv(table, file, con)

    con.close()
    print("Ingestion completed successfully.")


if __name__ == "__main__":
    main()
