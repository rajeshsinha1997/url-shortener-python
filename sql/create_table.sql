-- PostgreSQL Only: This SQL script is designed for use with PostgreSQL.
-- Please ensure compatibility with other database systems before use.
CREATE TABLE public.url_data (
	short_url_value varchar NOT NULL,
	long_url_value varchar NOT NULL,
	created_at varchar NOT NULL,
	expire_on varchar NOT NULL,
	visit_count integer DEFAULT 0 NOT NULL,
	last_used_on varchar NOT NULL,
	CONSTRAINT url_data_pk PRIMARY KEY (short_url_value),
	CONSTRAINT url_data_unique UNIQUE (long_url_value)
);
