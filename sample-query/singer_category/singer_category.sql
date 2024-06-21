SELECT Category, COUNT(*) AS NumberOfSongs 
FROM Song 
WHERE SingerID = 1 
GROUP BY Category 
ORDER BY NumberOfSongs DESC LIMIT 3;

