-- PostgreSQL Only: This SQL script is designed for use with PostgreSQL.
-- Please ensure compatibility with other database systems before use.
SELECT short_url_value
FROM public.url_data
WHERE long_url_hash = :long_url_hash;