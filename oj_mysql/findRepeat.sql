SELECT * FROM `vesal_model_info`
WHERE
model_name IN (SELECT model_name FROM `vesal_model_info` GROUP BY model_name HAVING COUNT(`model_name`)>=2)
OR
chinese_name IN (SELECT chinese_name FROM `vesal_model_info` GROUP BY chinese_name HAVING COUNT(`chinese_name`)>=2)
ORDER BY model_name DESC