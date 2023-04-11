USE liquorSales;

SELECT 
    *
FROM
    finance_liquor_sales
WHERE
    YEAR(date) BETWEEN 2016 AND 2019
ORDER BY date;
