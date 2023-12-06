USE electricity_project;
-- QUERY 1 : see the energetic balance ( = generated- demand)

SELECT YEAR(demand_sql.DATE) as year,
       ROUND(SUM(demand_sql.value),2) as demand_MWh,
       ROUND(SUM(gen_sql.value),2) as generated_MWh,
       (SUM(gen_sql.value) - SUM(demand_sql.value)) as balance,
       gen_sql.aacc as aacc
FROM demand_sql
JOIN gen_sql ON gen_sql.aacc = demand_sql.aacc
GROUP BY year, gen_sql.aacc
ORDER BY year DESC, aacc, balance DESC;

-- QUERY 2 : Generated (renovable) vs Generated (renovable + Generación total)

SELECT 
    YEAR(gen_sql.DATE) as year,
    ROUND(SUM(CASE WHEN type = 'Renovable' THEN value ELSE 0 END), 2) AS total_renewable,
    ROUND(SUM(CASE WHEN type = 'No-Renovable' OR type = 'Generación total' THEN value ELSE 0 END), 2) AS total_no_renewable,
    ROUND(
        (SUM(CASE WHEN type = 'Renovable' THEN value ELSE 0 END) / 
        (SUM(CASE WHEN type = 'Renovable' THEN value ELSE 0 END) + 
        SUM(CASE WHEN type = 'No-Renovable' OR type = 'Generación total' THEN value ELSE 0 END)) * 100), 2) AS renovable_percentage
FROM gen_sql
GROUP BY YEAR(gen_sql.DATE);

-- QUERY 3- projects active ( = pre-construction, construction, announced) in Spain per autonomous community (aacc): quantity and expected generation

WITH spain_green_projects AS (
    SELECT * FROM spain_global_sql WHERE status IN ('pre-construction', 'construction', 'announced')
)
SELECT 
    aacc,
    COUNT(DISTINCT project) AS numb_projects,
    SUM(capacity) AS monthly_total_capacity
FROM
    spain_green_projects
GROUP BY
    aacc;

-- QUERY 4: Get the number of active projects per country divided in renovable 


SELECT DISTINCT status FROM global_web_sql;
SELECT DISTINCT type FROM global_web_sql;
select count(CASE when type = 'coal' THEN 1 ELSE 0 END) from global_web_sql;