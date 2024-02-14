CREATE DATABASE IF NOT EXISTS world;
USE world;

CREATE TABLE country(
	Code CHAR(255),
	Name CHAR(255),
	Continent CHAR(255),
	Region CHAR(255),
	SurfaceArea float, 
	IndepYear int,
	Population int,
	LifeExpectancy float,
	GNP float, 
	GNPOld float,
	LocalName CHAR(255),
	GovernmentForm CHAR(255),
	HeadOfState CHAR(255),
	Capital int,
	Code2 CHAR(255),
	PRIMARY KEY (Code)
);

CREATE TABLE city (
	ID int,
	Name CHAR(255),
	CountryCode CHAR(255),
	District CHAR(255),
	Population int,
	PRIMARY KEY (ID),
	FOREIGN KEY (CountryCode) REFERENCES country(Code) 
);

CREATE TABLE countrylanguage(
	CountryCode CHAR(255),
	Lang CHAR(255),
	IsOfficial CHAR(255),
	Percentage float,
	PRIMARY KEY (CountryCode, Lang),
	FOREIGN KEY (CountryCode) REFERENCES country(Code)
);

CREATE TABLE continent(
	Name CHAR(255),
	Area float,
	LandMassPct float,
	MostPopulousCity CHAR(255),
	PRIMARY KEY (Name)
	/*FOREIGN KEY (MostPopulousCity) REFERENCES city(Name)*/
);

/*ALTER TABLE country ADD FOREIGN KEY (Continent) REFERENCES continent(Name);*/
