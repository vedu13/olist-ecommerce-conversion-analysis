WITH payment_per_order AS (
    SELECT 
        order_id,
        SUM(payment_value) AS order_value
    FROM payments
    GROUP BY order_id
)

SELECT 
    o.order_status,
    COUNT(DISTINCT o.order_id) AS total_orders,
    ROUND(SUM(p.order_value), 2) AS total_revenue,
    ROUND(AVG(p.order_value), 2) AS avg_order_value
FROM orders o
LEFT JOIN payment_per_order p
    ON o.order_id = p.order_id
GROUP BY o.order_status
ORDER BY total_revenue DESC;
