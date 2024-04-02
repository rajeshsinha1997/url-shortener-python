-- Active: 1711618605121@@127.0.0.1@3306
SELECT s_url FROM urls 
WHERE 
l_url = :l_url 
and 
deleted = :deleted;