-- What query would you run to get the total revenue for March of 2012?
SELECT monthname(billing.charged_datetime) AS Month,  sum(billing.amount) as Total_Amount_Billed
FROM billing
WHERE month(billing.charged_datetime) = 3;

-- What query would you run to get total revenue collected from the client with an id of 2?
SELECT concat(clients.first_name, ' ' , clients.last_name) AS Client_Name, SUM(billing.amount) AS Total_Billed
FROM clients
JOIN billing
ON clients.client_id = billing.client_id
WHERE clients.client_id = 2;

-- What query would you run to get all the sites that client=10 owns?
SELECT sites.domain_name 
FROM sites
WHERE client_id = 10;

-- What query would you run to get total # of sites created per month per year for the client with an id of 1? What about for client=20?
SELECT 
    CONCAT(c.first_name, ' ', c.last_name) AS Client_Name,
    COUNT(s.domain_name),
    YEAR(s.created_datetime) AS Year,
    MONTHNAME(s.created_datetime) AS Month
FROM
    clients AS c
        JOIN
    sites AS s ON c.client_id = s.client_id
WHERE
    c.client_id = 1
GROUP BY Month , Year;


-- What query would you run to get the total # of leads generated for each of the sites between January 1, 2011 to February 15, 2011?
SELECT count(leads.leads_id)
FROM leads
WHERE date_format(leads.registered_datetime, '%Y-%m-%d') between '2011-01-01' and '2011-02-015' ;


select * from leads




