CREATE ROLE root LOGIN;

CREATE TABLE camagru_user (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    passwd VARCHAR(50) NOT NULL
);

INSERT INTO camagru_user (username, email, passwd) VALUES ('paulo', 'paul@jullien.fr', 'passwd1'), ('leRequin', 'dan@mboule.fr', 'passwd2');