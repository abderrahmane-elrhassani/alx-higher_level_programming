-- Create a script to generate the database named hbtn_0d_usa and the table named states within that database on your MySQL server.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (id INT UNIQUE NOT NULL AUTO_INCREMENT,name VARCHAR(256) NOT NULL,PRIMARY KEY (id));
