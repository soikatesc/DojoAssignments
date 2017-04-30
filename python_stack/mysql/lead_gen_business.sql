
1.
SELECT SUM(amount) as revenue FROM billing 
WHERE MONTH(charged_datetime) = 4
AND YEAR(charged_datetime) = 2012;
2.
SELECT SUM(billing.amount) as revenue, clients.id
FROM clients
JOIN billing ON clients.id = billing.clients_id
WHERE clients_id = 2
GROUP By id

SELECT SUM(billing.amount) as revenue, clients.id
FROM clients
JOIN billing ON clients.id = billing.clients_id
WHERE clients_id = 2
GROUP By id
--  
-- -- SELECT * from clients
-- -- SElECT * from billing
-- -- 
-- -- SELECT sites.domain_name, clients.id
-- -- FROM clients
-- -- JOIN sites On clients.id = sites.clients_id
-- SELECT * from clients

