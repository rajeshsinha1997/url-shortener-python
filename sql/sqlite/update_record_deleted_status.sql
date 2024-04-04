UPDATE urls
SET
deleted = :deleted
WHERE
s_url = :s_url;