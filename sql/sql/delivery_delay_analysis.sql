SELECT
    CASE
        WHEN order_delivered_customer_date IS NULL THEN 'Not Delivered'
        WHEN CAST(order_delivered_customer_date AS TIMESTAMP) 
             > CAST(order_estimated_delivery_date AS TIMESTAMP) THEN 'Late'
        ELSE 'On Time / Early'
    END AS delivery_status,

    COUNT(order_id) AS total_orders,

    ROUND(
        COUNT(order_id) * 100.0 / SUM(COUNT(order_id)) OVER (), 
        2
    ) AS percentage

FROM orders
GROUP BY delivery_status
ORDER BY total_orders DESC;
