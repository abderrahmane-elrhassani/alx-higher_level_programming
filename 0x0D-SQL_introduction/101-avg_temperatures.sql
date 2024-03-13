-- Develop a script to showcase the average temperature (in Fahrenheit) organized by city, sorted by temperature (in descending order).
SELECT city, AVG(value) AS avg_temp FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
