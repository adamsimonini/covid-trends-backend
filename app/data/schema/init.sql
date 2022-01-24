--
-- PostgreSQL database dump
--

-- Dumped from database version 13.2
-- Dumped by pg_dump version 13.2

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

DROP DATABASE IF EXISTS covid_trends;
--
-- Name: northwind; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE covid_trends WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'en_US.utf8';


ALTER DATABASE covid_trends OWNER TO postgres;

\connect covid_trends

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: categories; Type: TABLE; Schema: public; Owner: postgres
--
CREATE TABLE public.provinces (
	province_code INT NOT NULL PRIMARY KEY,
    full_name VARCHAR(35) NOT NULL,
    alpha_code VARCHAR(2) NOT NULL,
    region VARCHAR(25) NOT NULL
);

ALTER TABLE public.provinces OWNER TO postgres;

CREATE TABLE public.health_regions (
    hr_uid INT NOT NULL PRIMARY KEY,
    province_code INT,
    FOREIGN KEY (province_code) REFERENCES public.provinces (province_code),
    name_en VARCHAR(150) NOT NULL,
    name_fr VARCHAR(150) NOT NULL,
    website_en VARCHAR(300),
    website_fr VARCHAR(300)
);

ALTER TABLE public.health_regions OWNER TO postgres;

CREATE TABLE public.locations(
    forward_sortation_area VARCHAR(3) NOT NULL PRIMARY KEY,
    hr_uid INT,
    FOREIGN KEY (hr_uid) REFERENCES public.health_regions (hr_uid),
	province_code INT,
    FOREIGN KEY (province_code) REFERENCES public.provinces (province_code)
);

ALTER TABLE public.locations OWNER TO postgres;

CREATE TABLE public.mobility(
	id SERIAL NOT NULL PRIMARY KEY,
    hr_uid INT,
    date VARCHAR(50),
    w_o_y INT,
    year INT,
    max_dist_25 FLOAT,
    max_dist_50 FLOAT,
	max_dist_75 FLOAT,
    sum_dist_25 FLOAT,
	sum_dist_50 FLOAT,
    sum_dist_75 FLOAT,
    prop_at_home FLOAT,
    percent_stay FLOAT,
    base_max FLOAT,
    base_percent_change_max FLOAT,
	base_sum FLOAT, 
    base_percent_change_sum FLOAT,
    base_prop_at_home FLOAT,
    base_percent_change_prop_at_home FLOAT,
    base_percent_stay FLOAT,
    base_percent_change_percent_stay FLOAT,
    percent_change_prev_week_max_dist_50 FLOAT,
    percent_change_prev_week_sum_dist_50 FLOAT,
    percent_change_prev_week_prop_at_home FLOAT,
    percent_change_prev_week_percent_stay FLOAT,
    avg_num_devices FLOAT,
    sum_num_devices INT,
    mobility FLOAT,
    pct_change_mobility FLOAT,
    prev_mobility FLOAT
);

ALTER TABLE public.mobility OWNER TO postgres;

CREATE TABLE public.cases(
	id SERIAL NOT NULL PRIMARY KEY,
    hr_uid INT,
    province VARCHAR(50),
    health_region VARCHAR(150),
    date_report VARCHAR(100),
    cases INT,
    cumulative_cases INT,
    deaths INT,
    cumulative_deaths INT,
    numtotal_last14 INT,
    numdeaths_last14 INT,
    numtotal_last7 INT,
    numdeaths_last7 INT,
    avgtotal_last7 FLOAT,
    avgdeaths_last7 FLOAT
);

ALTER TABLE public.cases OWNER TO postgres;