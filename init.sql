-- Create the database only if it doesn't exist
DO
$$
BEGIN
  IF NOT EXISTS (SELECT FROM pg_catalog.pg_database WHERE datname = 'test_db') THEN
    -- Create the database
    EXECUTE 'CREATE DATABASE test_db';
  END IF;
END
$$;

-- Connect to the 'test_db' database
\c test_db

-- Optionally create a custom schema, or ensure 'public' schema exists
-- In most cases, the 'public' schema already exists by default in new databases
-- CREATE SCHEMA IF NOT EXISTS public;

-- Create the table only if it doesn't exist
CREATE TABLE IF NOT EXISTS public.users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(100) NOT NULL UNIQUE,  -- Ensure username is unique
    password VARCHAR(100) NOT NULL,
    userhash VARCHAR(100) NOT NULL
);

-- Create an index on 'username' if it doesn't exist (useful for faster lookups)
CREATE INDEX IF NOT EXISTS idx_users_username ON public.users (username);
