USE sakila;

-- 1
CREATE TABLE directors(
	Name VARCHAR(80),
	LastName VARCHAR(80),
	NumOfMovies INT
);

-- 2

INSERT INTO directors(Name, LastName, NumOfMovies)
SELECT ac.first_name, ac.last_name, f.n_movies
FROM actor ac
INNER JOIN (
	SELECT COUNT(*) n_movies, actor_id 
	FROM film_actor
	GROUP BY actor_id 
	ORDER BY COUNT(*) DESC 
	LIMIT 5) f 
	ON ac.actor_id =f.actor_id

-- 3
ALTER TABLE customer 
ADD COLUMN premium_customer char DEFAULT 'F';

-- 4
UPDATE customer 
SET premium_customer = 'T'
WHERE customer.customer_id IN(
	SELECT p.customer_id
	FROM (
		SELECT customer_id 
		FROM payment p
		GROUP BY customer_id
		ORDER BY SUM(amount) DESC
		LIMIT 10
		) AS p
);

-- 5
SELECT rating, COUNT(rating) AS Cuantity
FROM film 
GROUP BY rating
ORDER BY Cuantity DESC 

-- 6
(SELECT payment_date
FROM payment p 
ORDER BY payment_date ASC
LIMIT 1)
UNION 
(SELECT payment_date
FROM payment p 
ORDER BY payment_date DESC 
LIMIT 1
)

-- 7
SELECT MONTH(payment_date) AS month_, AVG(amount)  
FROM payment
GROUP BY month_