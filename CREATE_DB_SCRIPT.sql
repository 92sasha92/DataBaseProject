CREATE DATABASE if NOT EXISTS DbMysql06;
use DbMysql06;

CREATE TABLE if NOT EXISTS Recipe(
	recipe_id varchar(128) NOT NULL,
	name varchar(128) NOT NULL,
	recipe_image varchar(128),
	recipe_instructions varchar(128),
	prep_time int,
	num_of_servings int,
	rating int,	
	PRIMARY KEY(recipe_id)
);

CREATE TABLE if NOT EXISTS Cuisines(
	cuisine_name varchar(128) NOT NULL,
	PRIMARY KEY(cuisine_name)
);

CREATE TABLE if NOT EXISTS ListOfCuisines(
	recipe_id varchar(128) NOT NULL,
	cuisine_name varchar(128) NOT NULL,
	PRIMARY KEY(recipe_id,cuisine_name),
	FOREIGN KEY(cuisine_name) REFERENCES Cuisines(cuisine_name),
	FOREIGN KEY(recipe_id) REFERENCES Recipe(recipe_id)
);

CREATE TABLE if NOT EXISTS Courses(
	course_name varchar(128) NOT NULL,
	PRIMARY KEY(course_name)
);	

CREATE TABLE if NOT EXISTS ListOfCourses(
	recipe_id varchar(128) NOT NULL,
	course_name varchar(128) NOT NULL,
	PRIMARY KEY(recipe_id,course_name),
	FOREIGN KEY(course_name) REFERENCES Courses(course_name),
	FOREIGN KEY(recipe_id) REFERENCES Recipe(recipe_id)
);

CREATE TABLE if NOT EXISTS Holidays(
	holiday_name varchar(128) NOT NULL,
	PRIMARY KEY(holiday_name)
);

CREATE TABLE if NOT EXISTS ListOfHolidays(
	recipe_id varchar(128) NOT NULL,
	holiday_name varchar(128) NOT NULL,
	PRIMARY KEY(recipe_id,holiday_name),
	FOREIGN KEY(holiday_name) REFERENCES Holidays(holiday_name),
	FOREIGN KEY(recipe_id) REFERENCES Recipe(recipe_id)
);

CREATE TABLE if NOT EXISTS Ingredients(
	ingredient_name varchar(128) NOT NULL,
	PRIMARY KEY(ingredient_name)
);

CREATE TABLE if NOT EXISTS ListOfIngredients(
	recipe_id varchar(128) NOT NULL,
	ingredient_name varchar(128) NOT NULL,
	PRIMARY KEY(recipe_id,ingredient_name),
	FOREIGN KEY(ingredient_name) REFERENCES Ingredients(ingredient_name),
	FOREIGN KEY(recipe_id) REFERENCES Recipe(recipe_id)
);

CREATE TABLE if NOT EXISTS Drink(
	drink_id int NOT NULL,
	drink_name varchar(128),
	drink_category varchar(128),
	drink_image varchar(128),
	instructions varchar(4096),
	glass varchar(128),
	PRIMARY KEY(drink_id)
);

CREATE TABLE if NOT EXISTS DrinkIngredients(
	ingredient_name varchar(128) NOT NULL,
	ingredient_mesure varchar(128) NOT NULL,
	PRIMARY KEY(ingredient_name, ingredient_mesure)
);

CREATE TABLE if NOT EXISTS ListOfDrinkIngredients(
	drink_id int NOT NULL,
	ingredient_name varchar(128) NOT NULL,
	ingredient_mesure varchar(128) NOT NULL,
	PRIMARY KEY(drink_id,ingredient_name, ingredient_mesure),
	FOREIGN KEY(ingredient_name, ingredient_mesure) REFERENCES DrinkIngredients(ingredient_name, ingredient_mesure),
	FOREIGN KEY(drink_id) REFERENCES Drink(drink_id)
);


