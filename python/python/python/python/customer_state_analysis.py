import duckdb
from pathlib import Path

base_path = Path(__file__).resolve().parent.parent

orders_file = base_path / "olist_orders_dataset.csv"
customers_file = base_path / "olist_customers_dataset.csv"
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
    c.customer_state,
    COUNT(DISTINCT o.order_id) AS total_orders,
    COUNT(DISTINCT c.customer_unique_id) AS total_customers,
    ROUND(SUM(p.order_value), 2) AS total_revenue,
    ROUND(AVG(p.order_value), 2) AS avg_order_value
FROM read_csv_auto('{orders_file.as_posix()}') o
JOIN read_csv_auto('{customers_file.as_posix()}') c
    ON o.customer_id = c.customer_id
LEFT JOIN payment_per_order p
    ON o.order_id = p.order_id
WHERE o.order_status = 'delivered'
GROUP BY c.customer_state
ORDER BY total_revenue DESC
LIMIT 10;
"""

result = duckdb.query(query).to_df()

print(result)
