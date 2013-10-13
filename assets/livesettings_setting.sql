--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

SET search_path = public, pg_catalog;

--
-- Data for Name: livesettings_setting; Type: TABLE DATA; Schema: public; Owner: askbot
--

COPY livesettings_setting (id, site_id, "group", key, value) FROM stdin;
2	1	QA_SITE_SETTINGS	APP_KEYWORDS	forum,questions,revenu-de-base
3	1	QA_SITE_SETTINGS	APP_COPYRIGHT	2013 - revenudebase.info
4	1	QA_SITE_SETTINGS	APP_TITLE	Questions Revenu de Base
5	1	QA_SITE_SETTINGS	GREETING_FOR_ANONYMOUS_USER	
6	1	QA_SITE_SETTINGS	APP_DESCRIPTION	Questions / Réponse concernant le Revenu de Base
1	1	QA_SITE_SETTINGS	APP_URL	http://questions.revenudebase.info/
7	1	QA_SITE_SETTINGS	APP_SHORT_NAME	Questions Revenu de Base
\.


--
-- Name: livesettings_setting_id_seq; Type: SEQUENCE SET; Schema: public; Owner: askbot
--

SELECT pg_catalog.setval('livesettings_setting_id_seq', 7, true);


--
-- PostgreSQL database dump complete
--

