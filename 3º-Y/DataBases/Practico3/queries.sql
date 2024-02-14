USE `world1`;

-- 1
SELECT  country.Region, country.Name AS CountryName, city.Name AS CityName, country.GovernmentForm 
FROM city
INNER JOIN country ON country.Code=city.CountryCode 
ORDER BY city.Population DESC
LIMIT 10;

-- 2
SELECT Name, Capital
FROM country
ORDER BY Population ASC
LIMIT 10;

-- 3
SELECT country.Name, country.Continent,countrylanguage.Language
FROM countrylanguage
INNER JOIN country ON country.Code=countrylanguage.CountryCode;

-- 4
SELECT Name, Capital
FROM country
ORDER BY SurfaceArea DESC 
LIMIT 20;

-- 5
SELECT city.Name, countrylanguage.Language, countrylanguage.Percentage 
FROM city
INNER JOIN countrylanguage ON city.CountryCode = countrylanguage.CountryCode 
WHERE countrylanguage.IsOfficial ='T'
ORDER BY city.Population DESC;

-- 6
(
SELECT Name,Population 
FROM country
ORDER BY Population DESC
LIMIT 10
)
UNION
(
SELECT Name,Population
FROM country
WHERE Population>=100
ORDER BY Population ASC
LIMIT 10
);

-- 7
(
SELECT DISTINCT Name 
FROM country
INNER JOIN countrylanguage ON countrylanguage.CountryCode = country.Code 
WHERE  (countrylanguage.Language='English' AND countrylanguage.IsOfficial='T')
)
INTERSECT
(
SELECT DISTINCT Name 
FROM country
INNER JOIN countrylanguage ON countrylanguage.CountryCode = country.Code 
WHERE (countrylanguage.Language='French' AND countrylanguage.IsOfficial='T')
);

-- 8
(
SELECT DISTINCT Name 
FROM country
INNER JOIN countrylanguage ON countrylanguage.CountryCode = country.Code 
WHERE countrylanguage.Language='English' AND countrylanguage.Percentage > 0 
)
EXCEPT 
(
SELECT DISTINCT Name 
FROM country
INNER JOIN countrylanguage ON countrylanguage.CountryCode = country.Code 
WHERE countrylanguage.Language='Spanish' AND countrylanguage.Percentage > 0
);
-- Usamos percentage>0 porque pide hablantes
