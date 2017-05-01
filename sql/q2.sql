SELECT
  salesperson.name,
  COUNT(orders.salesperson_id) as num_of_orders
FROM salesperson
  INNER JOIN orders on orders.salesperson_id = salesperson.ID
WHERE num_of_orders > 1
GROUP BY salesperson.name

