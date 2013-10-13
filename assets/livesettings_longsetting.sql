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
-- Data for Name: livesettings_longsetting; Type: TABLE DATA; Schema: public; Owner: askbot
--

COPY livesettings_longsetting (id, site_id, "group", key, value) FROM stdin;
3	1	FLATPAGES	QUESTION_INSTRUCTIONS	 
4	1	FLATPAGES	FORUM_PRIVACY	 
1	1	FLATPAGES	FORUM_ABOUT	<p>Questions Revenu de Base est une sous partie du site <a href="\r\nhttp://revenudebase.info">revenuedebase.info</a>.</p>\r\n\r\n<p>Pour en savoir plus à propos du « Mouvement Français pour un Revenu de Base » veuillez consulter la page <a href="http://revenudebase.info/a-propos/">« À propos »</a> du site principal du mouvement.</p>\r\n
2	1	FLATPAGES	FORUM_FAQ	<h1>Questions fréquemment posées(FAQ)</h1>\r\n\r\n<h2>Quel genre de questions puis-je poser ici ?</h2>\r\n\r\n<p>Vous pouvez poser ici toutes questions qui concernent de près ou de loin le Revenu de Base.</p>\r\n\r\n<p>Avant de poser une question - s'il vous plaît assurez-vous de rechercher une question similaire. Vous pouvez rechercher des questions par leur titre ou étiquettes.</p>\r\n\r\n<h2>Que dois-je éviter dans mes réponses ?</h2>\r\n\r\n<p>Questions Revenu de Base est un site de questions/réponses et non pas un forum de discussion. Pour de brèves discussions, veuillez utiliser les commentaires.</p>
\.


--
-- Name: livesettings_longsetting_id_seq; Type: SEQUENCE SET; Schema: public; Owner: askbot
--

SELECT pg_catalog.setval('livesettings_longsetting_id_seq', 4, true);


--
-- PostgreSQL database dump complete
--

