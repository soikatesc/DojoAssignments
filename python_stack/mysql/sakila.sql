

1. What query would you run to get all the customers inside city_id = 312? Your query should return customer first name, last name, email, and address.

SELECT * from city
WHERE city_ID = 312

SELECT customer.first_name, customer.last_name, customer.email,city.city,address.address, address.address2
FROM address
JOIN customer ON address.address_id = customer.address_id
JOIN city ON address.city_id = city.city_id
WHERE city.city_id = 312

2. What query would you run to get all comedy films? Your query should return film title, description, release year, rating, special features, and genre (category).

SELECT film.title, film.description, film.release_year, film.rating, film.special_features,category.name
FROM film 
JOIN film_category ON film_category.film_id = film.film_id
JOIN category ON category.category_id=film_category.category_id
WHERE category.name = 'comedy'

, category.genre

3-- . What query would you run to get all the films joined by actor_id=5? Your query should return the actor id, actor name, film title, description, and release year.
SELECT film.title,film.description,film.release_year,actor.first_name, actor.actor_id
FROM film
JOIN film_actor ON film_actor.film_id = film.film_id
JOIN actor ON actor.actor_id = film_actor.actor_id
WHERE actor.actor_id = 5


SELECT customer.first_name, customer.last_name, customer.email,address.address,store.store_id,city.city_id
FROM address
JOIN customer ON address.address_id = customer.address_id
JOIN city ON address.city_id = city.city_id
JOIN store ON store.store_id = customer.store_id
WHERE store.store_id = 1 and city.city_id in(1,42,312,459)

5. What query would you run to get all the films with a "rating = G" and "special feature = behind the scenes", joined by actor_id = 15? Your query should return the film title, description, release year, rating, and special feature. Hint: You may use LIKE function in getting the 'behind the scenes' part.


SELECT film.title, film.description, film.release_year, film.rating, film.special_features, actor.actor_id
FROM film
JOIN film_actor ON film_actor.film_id = film.film_id
JOIN actor ON actor.actor_id = film_actor.actor_id
WHERE actor.actor_id= 15 
-- and film.rating='G' and film.special_features like "B%s" 

6. What query would you run to get all the actors that joined in the film_id = 369? Your query should return the film_id, title, actor_id, and actor_name.


SELECT film.title, film.film_id,actor.actor_id,actor.first_name
FROM film
JOIN film_actor ON film_actor.film_id = film.film_id
JOIN actor ON actor.actor_id = film_actor.actor_id
WHERE film.film_id = 369

7. What query would you run to get all drama films with a rental rate of 2.99? Your query should return film title, description, release year, rating, special features, and genre (category).


SELECT film.title, film.description, film.release_year, film.rating, film.special_features,category.name, film.rental_rate
FROM film 
JOIN film_category ON film_category.film_id = film.film_id
JOIN category ON category.category_id=film_category.category_id
WHERE category.name = 'drama' and film.rental_rate = 2.99

8. What query would you run to get all the action films which are joined by SANDRA KILMER? Your query should return film title, description, release year, rating, special features, genre (category), and actor's first name and last name.


SELECT film.title, film.description, film.release_year, film.rating, film.special_features,concat(actor.first_name,' ',actor.last_name) AS full_name, category.name
FROM film  
JOIN film_category ON film_category.film_id = film.film_id
JOIN category ON category.category_id=film_category.category_id
JOIN film_actor ON film_actor.film_id = film.film_id
JOIN actor ON actor.actor_id = film_actor.actor_id
WHERE category.name = 'Action' and concat(actor.first_name,' ',actor.last_name) = 'SANDRA KILMER'























