import duckdb
from pathlib import Path

base_path = Path(__file__).resolve().parent.parent

orders_file = base_path / "olist_orders_dataset.csv"

query = f"""
SELECT
    CASE
        WHEN order_delivered_customer_date IS NULL THEN 'Not Delivered'
        WHEN CAST(order_delivered_customer_date AS TIMESTAMP) 
             > CAST(order_estimated_delivery_date AS TIMESTAMP) THEN 'Late'
        ELSE 'On Time / Early'
    END AS delivery_status,

    COUNT(order_id) AS total_orders,

    ROUND(
        COUNT(order_id) * 100.0 / SUM(COUNT(order_id)) OVER (), 
        2
    ) AS percentage

FROM read_csv_auto('{orders_file.as_posix()}')
GROUP BY delivery_status
ORDER BY total_orders DESC;
"""

result = duckdb.query(query).to_df()

print(result)
