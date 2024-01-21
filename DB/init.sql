DROP ROLE IF EXISTS postgres;
CREATE ROLE postgres WITH
	LOGIN
	NOSUPERUSER
	NOCREATEDB
	NOCREATEROLE
	INHERIT
	NOREPLICATION
	CONNECTION LIMIT -1
	PASSWORD 'postgres';


CREATE DATABASE postgres;
\c postgres;

CREATE TABLE public."Items"
(
    "Id" text NOT NULL,
    "Title" text,
    "Author" text,
    "Genre" text
    PRIMARY KEY ("Id")
);

ALTER TABLE IF EXISTS public."Items"
    OWNER to postgres;