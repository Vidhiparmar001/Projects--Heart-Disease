select * from heart h ;

-- 1. All columns for individuals where target = 1
SELECT * FROM heart WHERE target = 1;


-- 2. Average age for individuals with target = 1
SELECT AVG(age) AS avg_age_target1 FROM heart WHERE target = 1;


-- 3. Count the number of individuals for each value of cp
SELECT cp, COUNT(*) FROM heart GROUP BY cp;


-- 4. Rank individuals based on thalach in descending order
SELECT *, RANK() OVER (ORDER BY thalach DESC) AS thalach_rank FROM heart;


-- 5. Select individuals with age greater than the average age
SELECT * FROM heart WHERE age > (SELECT AVG(age) FROM heart);


-- 6. Calculate the maximum cholesterol level for each sex
SELECT sex, MAX(chol) FROM heart GROUP BY sex;


-- 7. Calculate the running total of oldpeak for each age group
SELECT age, oldpeak, SUM(oldpeak) OVER (PARTITION BY age ORDER BY age) 
AS oldpeak_running_total FROM heart;


-- 8. Select individuals with the highest thalach for each age group
SELECT * FROM (
  SELECT *, ROW_NUMBER() OVER (PARTITION BY age ORDER BY thalach DESC) AS row_num
  FROM heart
) WHERE row_num = 1;


-- 9. Calculate the average thalach for individuals with target = 1, grouped by sex
SELECT sex, AVG(thalach) FROM heart WHERE target = 1 GROUP BY sex;


-- 10. Calculate the percentage of individuals with target = 1 for each value of cp
SELECT cp, COUNT(CASE WHEN target = 1 THEN 1 ELSE NULL END) * 100.0 / COUNT(*) 
AS target_percentage FROM heart GROUP BY cp;


-- 11. Select individuals with a cholesterol level higher than the average cholesterol level
SELECT * FROM heart WHERE chol > (SELECT AVG(chol) FROM heart);


-- 12. Calculate the difference in thalach between consecutive rows
SELECT thalach - LAG(thalach) OVER (ORDER BY age) AS thalach_difference FROM heart;


-- 13. Rank individuals based on thalach within each age group
SELECT *, DENSE_RANK() OVER (PARTITION BY age ORDER BY thalach) AS thalach_dense_rank FROM heart;


-- 14. Select individuals with a thalach above the overall average thalach
SELECT * FROM heart WHERE thalach > (SELECT AVG(thalach) FROM heart);


-- 15. Calculate the average oldpeak for individuals with target = 1, grouped by sex and cp
SELECT sex, cp, AVG(oldpeak) FROM heart WHERE target = 1 GROUP BY sex, cp;


-- 16. Calculate the difference in thalach from the previous row for individuals with target = 1
SELECT age, thalach - LAG(thalach) OVER (PARTITION BY target ORDER BY age) 
AS thalach_difference FROM heart WHERE target = 1;


-- 17. Calculate the average age for individuals with target = 1, excluding those with cp = 1
SELECT AVG(age) FROM heart WHERE target = 1 AND cp <> 1;


-- 18. Calculate the percentage of individuals with target = 1 for each value of slope
SELECT slope, 
COUNT(CASE WHEN target = 1 THEN 1 ELSE NULL END) * 100.0 / COUNT(*) 
AS target_percentage FROM heart GROUP BY slope;

