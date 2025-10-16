SELECT
   Track.Name AS Product,
   SUM (InvoiceLine.Quantity) AS Total_Units_Sold,
   SUM (InvoiceLine.UnitPrice*InvoiceLine.Quantity) AS Total_Revenue
FROM InvoiceLine
JOIN Track On InvoiceLine.TrackId = Track.TrackId
GROUP BY Track.Name
ORDER BY Total_Revenue DESC
LIMIT 10;

SELECT 
   Customer.Country AS Region,
   SUM (InvoiceLine.UnitPrice*InvoiceLine.Quantity) AS Total_Revenue
FROM Invoice
JOIN Customer ON Invoice.CustomerId = Customer.CustomerId
JOIN InvoiceLine ON Invoice.InvoiceId = InvoiceLine.InvoiceId
GROUP BY Customer.Country
ORDER BY Total_Revenue DESC;

SELECT
    STRFTIME('%Y-%m', Invoice.InvoiceDate) AS Month
FROM Invoice
JOIN InvoiceLine ON Invoice.InvoiceId = InvoiceLine.InvoiceId
GROUP BY Month
ORDER BY Month;

SELECT 
     Product,
	 Total_Revenue,
	 RANK()OVER(ORDER BY Total_Revenue DESC) AS Rank 
FROM(
   SELECT Track.Name AS Product,
       SUM(InvoiceLine.UnitPrice*InvoiceLine.Quantity) AS Total_Revenue
FROM InvoiceLine
JOIN Track ON InvoiceLine.TrackId = Track.TrackId
GROUP BY Track.Name
);

/*.mode csv
.output 'top_products.csv'
SELECT 
    Track.Name, 
	SUM(InvoiceLine.UnitPrice*InvoiceLine.Quantity)
FROM InvoiceLine
JOIN Track ON InvoiceLine.TrackId = Track.TrackId
GROUP BY Track.Name
ORDER BY 2 DESC
LIMIT 10;
.output stdout*/








