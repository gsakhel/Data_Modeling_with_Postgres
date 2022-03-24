--Use this for first time setup on machine or 
--to quickly delete and recreate studentdb.

DROP DATABASE IF EXISTS studentdb;
CREATE DATABASE studentdb;

--Will show Error if already exists, but can be ignored.
CREATE USER student WITH SUPERUSER PASSWORD 'student';

--Regranting doesn't change anything.
GRANT ALL PRIVILEGES ON DATABASE studentdb TO student;