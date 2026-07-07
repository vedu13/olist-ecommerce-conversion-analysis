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

    FROM orders
),

reviews_summary AS (
    SELECT
        order_id,
        AVG(review_score) AS review_score
    FROM reviews
    GROUP BY order_id
)

SELECT
    d.delivery_status,
    COUNT(d.order_id) AS total_orders,
    COUNT(r.review_score) AS reviewed_orders,
    ROUND(AVG(r.review_score), 2) AS avg_review_score,
    ROUND(AVG(d.delay_days), 2) AS avg_delay_days
FROM delivery_status d
LEFT JOIN reviews_summary r
    ON d.order_id = r.order_id
GROUP BY d.delivery_status
ORDER BY avg_review_score DESC;
