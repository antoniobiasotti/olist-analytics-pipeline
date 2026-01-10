import duckdb
from src.config import DUCKDB_PATH


def main() -> None:
    con = duckdb.connect(DUCKDB_PATH)

    con.execute(
        """
        CREATE OR REPLACE TABLE fact_orders AS
        SELECT
            o.order_id,
            o.customer_id,
            o.order_status,
            o.order_purchase_timestamp,
            agg.number_of_items,
            agg.total_items_price,
            agg.total_freight
        FROM orders o
        LEFT JOIN (
            SELECT
                order_id,
                COUNT(*) AS number_of_items,
                SUM(price) AS total_items_price,
                SUM(freight_value) AS total_freight
            FROM order_items
            GROUP BY order_id
        ) agg
        ON o.order_id = agg.order_id
        """
    )

    con.close()
    print("fact_orders created successfully.")


if __name__ == "__main__":
    main()
