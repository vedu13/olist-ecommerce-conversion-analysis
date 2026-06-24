SELECT 
    order_status,
    COUNT(order_id) AS total_orders,
    ROUND(
        COUNT(order_id) * 100.0 / SUM(COUNT(order_id)) OVER (), 
        2
    ) AS percentage
FROM orders
GROUP BY order_status
ORDER BY total_orders DESC;
