SELECT Name, Region
FROM country
ORDER BY Name, Region;

SELECT Name, Population
FROM city 
ORDER BY Population ASC
LIMIT 10;

SELECT Name, Region, SurfaceArea, GovernmentForm
FROM country
ORDER BY SurfaceArea ASC
LIMIT 10;

SELECT Name
FROM country
WHERE IndepYear IS NULL;

SELECT Lang, Percentage 
FROM countrylanguage
WHERE IsOfficial='T';

/*------------------ADICIONALES---------------------*/

UPDATE countrylanguage SET Percentage=100.0
WHERE CountryCode='AIA' AND LANG='English';

SELECT Name,CountryCode 
FROM city
WHERE District='Córdoba'

DELETE FROM city WHERE District='Córdoba' AND CountryCode!='ARG'

SELECT Name
FROM country 
WHERE HeadOfState='John'

SELECT Name
FROM country
WHERE Population>=35000000 AND Population<=45000000
