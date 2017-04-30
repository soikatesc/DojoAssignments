
SELECT * FROM languages
WHERE language like "SL%E"


SELECT countries.name AS country_name, cities.name AS city_name
FROM countries
JOIN cities ON countries.id = cities.country_id
order by  city_name DESC

SELECT countries.name, cities.name,cities.population 
FROM countries
JOIN cities ON countries.id = cities.country_id
WHERE countries.name = 'Mexico' and cities.population>500000
order BY population
 
SELECT countries.name, languages.language,languages.percentage
FROM countries 
JOIN languages ON countries.id = languages.country_id
WHERE languages.percentage>89
ORDER BY percentage

SELECT countries.name, countries.surface_area, countries.population
FROM countries
JOIN cities ON countries.id = cities.country_id
WHERE countries.surface_area<501

SELECT countries.name, countries.government_form, countries.capital, countries.life_expectancy 
FROM countries
where countries.government_form = 'Constitutional Monarchy' and countries.capital>200 and countries.life_expectancy>75

SELECT countries.name AS country_name, cities.name AS city_name, cities.district, cities.population
FROM countries
JOIN cities ON countries.id = cities.country_id
WHERE countries.name = 'Argentina' and cities.district = 'Buenos Aires' and cities.population>500000


SELECT region,COUNT(countries.name) as count 
FROM countries GROUP BY region ORDER BY count DESC;

-- North America - 2

-- Central America - 6










