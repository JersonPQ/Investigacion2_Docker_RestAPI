CREATE DATABASE tasks;

\c tasks;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    password VARCHAR(200) NOT NULL
);

CREATE TABLE status (
  id SERIAL PRIMARY KEY,
  name VARCHAR(200) NOT NULL
);

CREATE TABLE tasks (
  id SERIAL PRIMARY KEY,
  title VARCHAR(200) NOT NULL,
  description VARCHAR(500) NOT NULL,
  due_date DATE NOT NULL,
  status INT REFERENCES status(id) ON DELETE CASCADE,
  user_id INT REFERENCES users(id) ON DELETE CASCADE
);