CREATE DATABASE if NOT EXISTS DbMysql06;
use DbMysql06;

CREATE TABLE if NOT EXISTS Recipe(
	recipe_id varchar(128) NOT NULL,
	name varchar(128) NOT NULL,
	recipe_image varchar(4096) NOT NULL,
	recipe_instructions varchar(4096) NOT NULL,
	prep_time int NOT NULL,
	num_of_servings int NOT NULL,
	rating int NOT NULL,
	PRIMARY KEY(recipe_id) USING BTREE,
	INDEX num_of_servings (num_of_servings) USING BTREE,
	INDEX prep_time (prep_time),
	INDEX rating (rating)
);

CREATE TABLE if NOT EXISTS Cuisines(
	cuisine_name varchar(128) NOT NULL,
	PRIMARY KEY(cuisine_name)
);

CREATE TABLE if NOT EXISTS ListOfCuisines(
	recipe_id varchar(128) NOT NULL,
	cuisine_name varchar(128) NOT NULL,
	PRIMARY KEY(recipe_id,cuisine_name),
	INDEX cuisine_name (cuisine_name) USING BTREE,
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
	PRIMARY KEY(recipe_id, course_name) USING BTREE,
	INDEX course_name (course_name),
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
	INDEX holiday_name (holiday_name),
	INDEX recipe_id (recipe_id) USING BTREE,
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
	INDEX recipe_id (recipe_id) USING BTREE,
	INDEX ingredient_name (ingredient_name) USING BTREE,
	FOREIGN KEY(ingredient_name) REFERENCES Ingredients(ingredient_name),
	FOREIGN KEY(recipe_id) REFERENCES Recipe(recipe_id)
);

CREATE TABLE if NOT EXISTS Drink(
	drink_id int NOT NULL,
	drink_name varchar(128) NOT NULL,
	drink_category varchar(128) NOT NULL,
	drink_image varchar(128) NOT NULL,
	instructions varchar(4096) NOT NULL,
	glass varchar(128) NOT NULL,
	is_alcoholic varchar(128) NOT NULL,
	PRIMARY KEY(drink_id),
	INDEX glass (glass)
);

CREATE TABLE if NOT EXISTS DrinkIngredients(
	ingredient_name varchar(128) NOT NULL,
	PRIMARY KEY(ingredient_name)
);

CREATE TABLE if NOT EXISTS ListOfDrinkIngredients(
	drink_id int NOT NULL,
	ingredient_name varchar(128) NOT NULL,
	ingredient_measure varchar(128) NOT NULL,
	PRIMARY KEY(drink_id, ingredient_name),
	INDEX ingredient_name (ingredient_name),
	FOREIGN KEY(ingredient_name) REFERENCES DrinkIngredients(ingredient_name),
	FOREIGN KEY(drink_id) REFERENCES Drink(drink_id)
);
