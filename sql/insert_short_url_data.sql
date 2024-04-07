-- PostgreSQL Only: This SQL script is designed for use with PostgreSQL.
-- Please ensure compatibility with other database systems before use.
INSERT INTO public.url_data
(short_url_value, long_url_value, long_url_hash, created_at, last_used_on, visit_count)
VALUES(:short_url_value, :long_url_value, :long_url_hash, :created_at, :last_used_on, 0);