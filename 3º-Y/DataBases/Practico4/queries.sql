USE `world2`;


-- 1
SELECT city.Name AS City, country.Name AS Country, country.Population
FROM city
INNER JOIN country ON city.CountryCode=country.code
WHERE country.Population >= 10000
ORDER BY Population ASC 

SELECT city.Name AS City, country.Name  AS Country, country.Population
FROM city
INNER JOIN country ON city.CountryCode=country.code
WHERE city.CountryCode IN(
	SELECT Code
	FROM country
	WHERE country.Population >=10000
)
ORDER BY Population ASC;

-- 2
WITH avg_pop (value) AS (
	SELECT avg(Population)
	FROM city
	)
SELECT Name AS City, Population
FROM city, avg_pop
WHERE city.Population >= ROUND(avg_pop.value)
ORDER BY name
;
-- 3
WITH min_pop (value) AS (
	SELECT min(Population)
	FROM country
	WHERE country.Continent = 'Asia'
	)
SELECT c.Name
FROM city c INNER JOIN country ON c.CountryCode=country.Code
WHERE country.Continent != 'Asia' AND c.Population >= (SELECT value FROM min_pop)
ORDER BY Name ;

-- 4
SELECT cy.Name, GROUP_CONCAT(cl.Language) AS Languages
FROM countrylanguage cl INNER JOIN country cy ON cy.Code = cl.CountryCode 
WHERE cl.IsOfficial = 'F' AND cl.Percentage >ALL(
	SELECT cl2.Percentage
	FROM countrylanguage cl2
	WHERE cy.Code = cl2.CountryCode AND cl2.IsOfficial = 'T')
GROUP BY cl.CountryCode ;

-- 5
SELECT cy.Region, cy.Population, cy.Name 
FROM country cy
WHERE cy.SurfaceArea < 1000 AND EXISTS(
		SELECT c.CountryCode
		FROM city c
		WHERE c.CountryCode=cy.Code AND c.Population >=100000
);

-- 6

-- Forma Lenta
SELECT c.Name, cy.Population 
FROM country c INNER JOIN city cy ON cy.CountryCode = c.Code 
WHERE cy.Population = (
	SELECT MAX(Population)
	FROM city cy2
	WHERE cy.CountryCode=cy2.CountryCode 
	);
-- Forma Rapida
WITH max_pop_c (cyy, popu) AS (
	SELECT c2.Code, max_pop
	FROM (
		SELECT max(population) max_pop, CountryCode
		FROM city
		GROUP BY city.CountryCode
		) c1
	INNER JOIN country c2 ON c2.Code = c1.CountryCode 
)
SELECT c.Name, cy.Population
FROM country c INNER JOIN city cy ON cy.CountryCode = c.Code, max_pop_c
WHERE cy.Population = max_pop_c.popu AND c.Code = max_pop_c.cyy

-- 7
SELECT c.Name, GROUP_CONCAT(cl.Language) AS Languages
FROM country c INNER JOIN countrylanguage cl ON c.Code = cl.CountryCode 
WHERE cl.IsOfficial ='F' AND cl.Percentage >=(
	SELECT avg(cl2.Percentage)
	FROM countrylanguage cl2
	WHERE cl2.CountryCode =cl.CountryCode 
)
GROUP BY c.Name;

-- 8
SELECT Continent, SUM(Population) AS Population 
FROM country 
GROUP BY Continent;

-- 10
SELECT Continent, 
		SUM(Population) AS TotalPop, 
		MIN(Population) AS MinPop,
		MAX(Population) AS MaxPop,
		ROUND(AVG(Population)) AS AvgPop
FROM country 
GROUP BY Continent;


