import duckdb
from pathlib import Path
import matplotlib.pyplot as plt

base_path = Path(__file__).resolve().parent.parent

orders_file = base_path / "olist_orders_dataset.csv"
reviews_file = base_path / "olist_order_reviews_dataset.csv"
visuals_path = base_path / "visuals"
visuals_path.mkdir(exist_ok=True)

query = f"""
WITH delivery_status AS (
    SELECT
        order_id,
        CASE
            WHEN order_delivered_customer_date IS NULL THEN 'Not Delivered'
            WHEN CAST(order_delivered_customer_date AS TIMESTAMP) 
                 > CAST(order_estimated_delivery_date AS TIMESTAMP) THEN 'Late'
            ELSE 'On Time / Early'
        END AS delivery_status
    FROM read_csv_auto('{orders_file.as_posix()}')
),

reviews_summary AS (
    SELECT
        order_id,
        AVG(review_score) AS review_score
    FROM read_csv_auto('{reviews_file.as_posix()}')
    GROUP BY order_id
)

SELECT
    d.delivery_status,
    ROUND(AVG(r.review_score), 2) AS avg_review_score
FROM delivery_status d
LEFT JOIN reviews_summary r
    ON d.order_id = r.order_id
GROUP BY d.delivery_status
ORDER BY avg_review_score DESC;
"""

df = duckdb.query(query).to_df()

plt.figure(figsize=(8, 6))
plt.bar(df["delivery_status"], df["avg_review_score"])
plt.title("Delivery Status vs Average Review Score")
plt.xlabel("Delivery Status")
plt.ylabel("Average Review Score")
plt.ylim(0, 5)
plt.tight_layout()

plt.savefig(visuals_path / "delivery_review_score.png")
plt.show()

print("Chart saved as visuals/delivery_review_score.png")
