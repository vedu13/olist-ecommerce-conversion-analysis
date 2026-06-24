import duckdb
from pathlib import Path

base_path = Path(__file__).resolve().parent.parent
orders_file = base_path / "olist_orders_dataset.csv"

query = f"""
SELECT 
    order_status,
    COUNT(order_id) AS total_orders,
    ROUND(
        COUNT(order_id) * 100.0 / SUM(COUNT(order_id)) OVER (), 
        2
    ) AS percentage
FROM read_csv_auto('{orders_file.as_posix()}')
GROUP BY order_status
ORDER BY total_orders DESC;
"""

result = duckdb.query(query).to_df()

print(result)
