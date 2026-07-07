WITH payment_per_order AS (
    SELECT 
        order_id,
        SUM(payment_value) AS order_value
    FROM payments
    GROUP BY order_id
)

SELECT
    c.customer_state,
    COUNT(DISTINCT o.order_id) AS total_orders,
    COUNT(DISTINCT c.customer_unique_id) AS total_customers,
    ROUND(SUM(p.order_value), 2) AS total_revenue,
    ROUND(AVG(p.order_value), 2) AS avg_order_value
FROM orders o
JOIN customers c
    ON o.customer_id = c.customer_id
LEFT JOIN payment_per_order p
    ON o.order_id = p.order_id
WHERE o.order_status = 'delivered'
GROUP BY c.customer_state
ORDER BY total_revenue DESC
LIMIT 10;
