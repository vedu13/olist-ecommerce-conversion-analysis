import duckdb
from pathlib import Path

base_path = Path(__file__).resolve().parent.parent

orders_file = base_path / "olist_orders_dataset.csv"
payments_file = base_path / "olist_order_payments_dataset.csv"

query = f"""
WITH payment_per_order AS (
    SELECT 
        order_id,
        SUM(payment_value) AS order_value
    FROM read_csv_auto('{payments_file.as_posix()}')
    GROUP BY order_id
)

SELECT 
    o.order_status,
    COUNT(DISTINCT o.order_id) AS total_orders,
    ROUND(SUM(p.order_value), 2) AS total_revenue,
    ROUND(AVG(p.order_value), 2) AS avg_order_value
FROM read_csv_auto('{orders_file.as_posix()}') o
LEFT JOIN payment_per_order p
    ON o.order_id = p.order_id
GROUP BY o.order_status
ORDER BY total_revenue DESC;
"""

result = duckdb.query(query).to_df()

print(result)
