-- Import a table into SCHEMA from a dump file
-- Display average temperature by city ordered by the temperature
SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
