-- Drop the database if it exists
DROP DATABASE IF EXISTS CS348_TEST;

-- Create the database
CREATE DATABASE CS348_TEST;

-- Use the newly created database
USE CS348_TEST;

-- Create the HelloWorld table with one column Hello
CREATE TABLE HelloWorld (
    Hello VARCHAR(255)
);

-- Insert one row with the value 'World'
INSERT INTO HelloWorld (Hello) VALUES ('World');
