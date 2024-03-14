-- Create the hbtn_0d_usa database and the cities table within it
-- The cities table should have the following structure:
--      - id: INT, unique, auto-generated, primary key, not nullable
--      - state_id: INT, not nullable, must be a foreign key referencing the id column of the states table
--      - name: VARCHAR(256), not nullable
-- If the hbtn_0d_usa database already exists, the script should not fail.
-- If the cities table already exists, the script should not fail.
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (id INT UNIQUE NOT NULL AUTO_INCREMENT,state_id INT NOT NULL,name VARCHAR(256) NOT NULL,PRIMARY KEY (id),FOREIGN KEY (state_id) REFERENCES hbtn_0d_usa.states(id));
