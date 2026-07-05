import duckdb
from pathlib import Path

base_path = Path(__file__).resolve().parent.parent

orders_file = base_path / "olist_orders_dataset.csv"
reviews_file = base_path / "olist_order_reviews_dataset.csv"

query = f"""
WITH delivery_status AS (
    SELECT
        order_id,
        CASE
            WHEN order_delivered_customer_date IS NULL THEN 'Not Delivered'
            WHEN CAST(order_delivered_customer_date AS TIMESTAMP) 
                 > CAST(order_estimated_delivery_date AS TIMESTAMP) THEN 'Late'
            ELSE 'On Time / Early'
        END AS delivery_status,

        CASE
            WHEN order_delivered_customer_date IS NOT NULL THEN
                date_diff(
                    'day',
                    CAST(order_estimated_delivery_date AS TIMESTAMP),
                    CAST(order_delivered_customer_date AS TIMESTAMP)
                )
            ELSE NULL
        END AS delay_days

    FROM read_csv_auto('{orders_file.as_posix()}')
),

reviews AS (
    SELECT
        order_id,
        AVG(review_score) AS review_score
    FROM read_csv_auto('{reviews_file.as_posix()}')
    GROUP BY order_id
)

SELECT
    d.delivery_status,
    COUNT(d.order_id) AS total_orders,
    COUNT(r.review_score) AS reviewed_orders,
    ROUND(AVG(r.review_score), 2) AS avg_review_score,
    ROUND(AVG(d.delay_days), 2) AS avg_delay_days
FROM delivery_status d
LEFT JOIN reviews r
    ON d.order_id = r.order_id
GROUP BY d.delivery_status
ORDER BY avg_review_score DESC;
"""

result = duckdb.query(query).to_df()

print(result)
