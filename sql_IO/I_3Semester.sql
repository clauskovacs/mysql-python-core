-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jun 11, 2021 at 02:54 PM
-- Server version: 5.5.62-0+deb8u1
-- PHP Version: 7.3.17-1+0~20200419.57+debian8~1.gbp0fda17

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `kd37890db2`
--

-- --------------------------------------------------------

--
-- Table structure for table `I_3Semester`
--

CREATE TABLE `I_3Semester` (
  `aaa` varchar(100) NOT NULL,
  `bbb` varchar(100) NOT NULL,
  `ccc` varchar(100) NOT NULL,
  `ddd` int(5) NOT NULL,
  `eee` int(5) NOT NULL,
  `fff` varchar(300) NOT NULL,
  `index2` int(5) NOT NULL,
  `info` varchar(5000) CHARACTER SET utf8 NOT NULL,
  `folder_edit_info` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `I_3Semester`
--

INSERT INTO `I_3Semester` (`aaa`, `bbb`, `ccc`, `ddd`, `eee`, `fff`, `index2`, `info`, `folder_edit_info`) VALUES
('Datenbanksysteme', 'WS 2013', 'dbvu1401-pruefung.pdf', 15, 2, '', 0, '<b>184.686 Datenbanksysteme</b><br><i>2013W, VU, 4.0h, 6.0ECTS</i><br><br><b>Vortragende</b><br>Feinerer, Ingo<br>Sallinger, Emanuel<br><br><b>Institut</b><br>E184 Institut für Informationssysteme<br><br><b>Ziele der Lehrveranstaltung</b><br><i>Fachliche und methodische Kenntnisse:</i><br><br>● Grundlagen, Komponenten, und Funktionsweise von Datenbankmanagementsystemen (DBMS); Datenbankarchitektur und Datenunabhängigkeit<br>● Komplexe SQL Abfragen, Einbettung in prozedurale Abfragen (JDBC)<br>● Physische Datenorganisation, Datenbanktuning<br>● Transaktionen, Fehlerbehandlung, Mehrbenutzersynchronisation<br>● Verteilte Datenbanken<br><br><i>Kognitive und praktische Fertigkeiten:</i><br>● Verwendung von DBMS und Benutzung deklarativer Abfragesprachen<br>● Programmierung von und Anbindung an Datenbanksysteme<br><br><i>Soziale Kompetenzen, Innovationskompetenz und Kreativität:</i><br>● Funktionale Denkweise zum Verständnis deklarativer Abfragesprachen<br>● Logisches Denken um Abläufe in einem DBMS nachzuvollziehen<br>● Mathematisch fundierte Vorgehensweise zur Analyse von Methoden in DBMS<br>● Kenntnisse der eigenen Fähigkeiten und Grenzen, Kritikfähigkeit an der eigenen Arbeit<br>● Selbstorganisation und Eigenverantwortlichkeit zum eigenständigen Lösen von Laboraufgaben<br><br><b>Inhalt der Lehrveranstaltung</b><br><i>Schwerpunkte:</i><br>● Datenbank-Programmierung (mit PL/SQL und JDBC) und SQL-Erweiterungen<br>● Physische Datenorganisation und Anfragebearbeitung<br>● Transaktionen, Fehlerbehandlung/Recovery, Mehrbenutzersynchronisation<br>● Weiterführende Themen (z.B.: verteilte Datenbanken)<br><br><i>Didaktisches Vorgehen:</i><br>● Vorlesungsteil<br>● Es gibt 3 Übungen die die Konzepte der Vorlesung vertiefen.<br>● Die Übungsbeispiele werden, bevor sie starten, in der Vorlesung besprochen.<br>● Zur Betreuung der Übung gibt es Fragestunden bei den Tutorinnen und Tutoren verteilt auf die Zeit vor den Abgabeterminen.<br>● Die Übung besteht hauptsächlich aus Programmieraufgaben und fließt zu 25% in die Gesamtnote ein.<br>● Um für alle Studierenden gleiche Voraussetzungen bei der Abgabe zu schaffen gibt es einen einheitlichen Abgabetermin für alle Studenten gefolgt von den Abgabegesprächen.<br>● Bei den Abgabegesprächen werden die Beispiele auf Korrektheit, aber besonders auf das Verständnis geprüft, und entsprechend Feedback gegeben.<br>● Die Prüfung besteht aus einem Theorieteil und praktischen Beispielen.<br>● Es gibt vier Prüfungstermine (einen am Semesterende, drei weitere im Folgesemester) die zu 75% in die Note einfließen.<br><br>Bitte beachten Sie für diese LVA unbedingt auch die lokale Homepage der Lehrveranstaltung.<br><br><i>Weitere Informationen</i><br><b>ECTS Breakdown:</b><br>30h Vorlesungsbesuch<br>34h Übungsteil<br> 1h Abgabegespräche<br>83h Prüfungsvorbereitung<br> 2h Prüfung', 'claus | 89.144.238.219 | 19.01.2015-11:12'),
('', '', 'dbvu1401-muster.pdf', 0, 0, '', 1, '', ''),
('', '', 'dbvu1403-pruefung.pdf', 0, 0, '', 2, '', ''),
('', '', 'dbvu1403-muster.pdf', 0, 0, '', 3, '', ''),
('', '', 'dbvu1405-pruefung.pdf', 0, 0, '', 4, '', ''),
('', '', 'dbvu1405-muster.pdf', 0, 0, '', 5, '', ''),
('', '', 'dbvu1406-pruefung.pdf', 0, 0, '', 6, '', ''),
('', '', 'dbvu1406-muster.pdf', 0, 0, '', 7, '', ''),
('', '', 'WS 2013 UE1 Angabe.pdf', 0, 0, '', 8, '', ''),
('', '', 'WS 2013 UE1 Lösung - test_sql.pdf', 0, 0, '', 9, '', ''),
('', '', 'WS 2013 UE1 Lösung - plpgsql-teil_sql.pdf', 0, 0, '', 10, '', ''),
('', '', 'WS 2013 UE1 Lösung - insert_sql.pdf', 0, 0, '', 11, '', ''),
('', '', 'WS 2013 UE1 Lösung - drop_sql.pdf', 0, 0, '', 12, '', ''),
('', '', 'WS 2013 UE1 Lösung - create_sql.pdf', 0, 0, '', 13, '', ''),
('', '', 'WS 2013 Übung 3.pdf', 0, 0, '', 14, '', ''),
('', '', 'oop-lu14w9.pdf', 0, 0, '', 758, '', ''),
('Wahrsch.theorie und Stoch. Proz. für Inf.', 'WS 2013', 'winf13-02.pdf', 6, 2, '', 800, '<b>107.A20 Wahrscheinlichkeitstheorie und Stochastische Prozesse für Informatik</b><br><i>2013W, UE, 2.0h, 3.5ECTS</i><br><br><b>Vortragende</b><br>Grill, Karl<br>Kusolitsch, Norbert<br>Stadler, Heinz<br><br><b>Institut</b><br>E107 Institut für Statistik und Wahrscheinlichkeitstheorie<br><br><b>Inhalt der Lehrveranstaltung</b><br>Siehe 107.A02', 'claus | 80.123.116.26 | 21.08.2014-13:26'),
('', '', 'winf13-03.pdf', 0, 0, '', 801, '', ''),
('', '', 'winf13-07.pdf', 0, 0, '', 802, '', ''),
('', '', 'winf13-08.pdf', 0, 0, '', 803, '', ''),
('', '', 'normalverteilung.pdf', 0, 0, '', 804, '', ''),
('', '', 'tabellen.pdf', 0, 0, '', 805, '', ''),
('Wahrsch.theorie und Stoch. Proz. für Inf.', 'WS 2014', 'winf14-03.pdf', 1, 1, '', 850, '<b>107.A20 Wahrscheinlichkeitstheorie und Stochastische Prozesse für Informatik</b><br><i>2014W, UE, 2.0h, 3.5ECTS</i><br><br><b>Vortragende</b><br>Grill, Karl<br><br><b>Institut</b><br>E107 Institut für Statistik und Wahrscheinlichkeitstheorie<br><br><b>Inhalt der Lehrveranstaltung</b><br>Siehe 107.A02', 'claus | 128.131.218.240 | 07.11.2014-07:25');

COMMIT;

