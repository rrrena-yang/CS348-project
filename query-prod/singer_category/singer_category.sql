SELECT Category, COUNT(*) AS NumberOfSongs 
FROM Song 
WHERE SingerID = 831
GROUP BY Category 
ORDER BY NumberOfSongs DESC LIMIT 3;

