-- Drop the database if it exists
DROP DATABASE IF EXISTS CS348;

-- Create the database
CREATE DATABASE CS348;

-- Use the newly created database
USE CS348;

-- Create the HelloWorld table with one column Hello
CREATE TABLE HelloWorld (
    Hello VARCHAR(255)
);

-- Insert one row with the value 'World'
INSERT INTO HelloWorld (Hello) VALUES ('World');
