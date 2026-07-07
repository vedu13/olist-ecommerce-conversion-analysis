import duckdb
from pathlib import Path

base_path = Path(__file__).resolve().parent.parent

orders_file = base_path / "olist_orders_dataset.csv"
order_items_file = base_path / "olist_order_items_dataset.csv"
products_file = base_path / "olist_products_dataset.csv"

query = f"""
SELECT
    COALESCE(p.product_category_name, 'Unknown') AS product_category,
    COUNT(DISTINCT o.order_id) AS total_orders,
    COUNT(oi.order_item_id) AS total_items_sold,
    ROUND(SUM(oi.price), 2) AS total_revenue,
    ROUND(AVG(oi.price), 2) AS avg_item_price
FROM read_csv_auto('{orders_file.as_posix()}') o
JOIN read_csv_auto('{order_items_file.as_posix()}') oi
    ON o.order_id = oi.order_id
LEFT JOIN read_csv_auto('{products_file.as_posix()}') p
    ON oi.product_id = p.product_id
WHERE o.order_status = 'delivered'
GROUP BY product_category
ORDER BY total_revenue DESC
LIMIT 10;
"""

result = duckdb.query(query).to_df()

print(result)
