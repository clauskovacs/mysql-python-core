-- MySQL dump 10.17  Distrib 10.3.22-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: bookstore
-- ------------------------------------------------------
-- Server version	10.3.22-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `2013__2013_02_28_23_55_21`
--

DROP TABLE IF EXISTS `2013__2013_02_28_23_55_21`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `2013__2013_02_28_23_55_21` (
  `IP` text NOT NULL,
  `Date` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `2013__2013_02_28_23_55_21`
--

LOCK TABLES `2013__2013_02_28_23_55_21` WRITE;
/*!40000 ALTER TABLE `2013__2013_02_28_23_55_21` DISABLE KEYS */;
INSERT INTO `2013__2013_02_28_23_55_21` VALUES ('66.249.75.177','2000-02-01 00:46:30'),('66.249.78.123','2013-02-01 01:14:59'),('79.208.109.187','2013-02-01 01:15:14'),('66.249.78.177','2013-02-01 01:27:57'),('77.117.246.38','2013-02-28 22:31:39'),('84.114.179.155','3121-02-28 23:53:19');
/*!40000 ALTER TABLE `2013__2013_02_28_23_55_21` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `I_3Semester`
--

DROP TABLE IF EXISTS `I_3Semester`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
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
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `I_3Semester`
--

LOCK TABLES `I_3Semester` WRITE;
/*!40000 ALTER TABLE `I_3Semester` DISABLE KEYS */;
/*!40000 ALTER TABLE `I_3Semester` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `authors`
--

DROP TABLE IF EXISTS `authors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `authors` (
  `author_id` int(11) NOT NULL AUTO_INCREMENT,
  `name_last` varchar(50) DEFAULT NULL,
  `name_first` varchar(50) DEFAULT NULL,
  `country` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`author_id`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `authors`
--

LOCK TABLES `authors` WRITE;
/*!40000 ALTER TABLE `authors` DISABLE KEYS */;
INSERT INTO `authors` VALUES (1,'Kafka','Franz','Czech Republic'),(2,'Jane','Doe','muh'),(3,'Jane','Doe','muh'),(4,'lastname_test2','firstname_test2','country_test2'),(5,'lastname_test','firstname_test','country_test'),(6,'a','v','c'),(7,'Jane','Doe','muh'),(8,'Jane','Doe','muh'),(9,'Jane','Doe','muh'),(10,'Jane','Doe','muh'),(11,'Jane','Doe','muh'),(12,'Jane','Doe','muh'),(13,'Jane','Doe','muh'),(14,'Jane','Doe','muh'),(15,'Jane','Doe','muh'),(16,'Jane','Doe','muh'),(17,'Jane','Doe','muh'),(18,'Jane','Doe','muh'),(19,'Jane','Doe','muh'),(20,'Jane','Doe','muh'),(21,'Jane','Doe','muh'),(22,'Jane','Doe','muh'),(23,'Jane','Doe','muh'),(24,'Jane','Doe','muh'),(25,'Jane','Doe','muh'),(26,'Jane','Doe','muh'),(27,'Jane','Doe','muh'),(28,'Jane','Doe','muh'),(29,'Jane','Doe','muh'),(30,'Jane','Doe','muh'),(31,'Jane','Doe','muh'),(32,'Jane','Doe','muh'),(33,'Jane','Doe','muh'),(34,'Jane','Doe','muh'),(35,'Jane','Doe','muh');
/*!40000 ALTER TABLE `authors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `books`
--

DROP TABLE IF EXISTS `books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `books` (
  `isbn` char(20) NOT NULL,
  `title` varchar(50) DEFAULT NULL,
  `author_id` int(11) DEFAULT NULL,
  `publisher_id` int(11) DEFAULT NULL,
  `year_pub` char(4) DEFAULT NULL,
  `description` text DEFAULT NULL,
  PRIMARY KEY (`isbn`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books`
--

LOCK TABLES `books` WRITE;
/*!40000 ALTER TABLE `books` DISABLE KEYS */;
/*!40000 ALTER TABLE `books` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customers`
--

DROP TABLE IF EXISTS `customers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `customers` (
  `name` varchar(255) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customers`
--

LOCK TABLES `customers` WRITE;
/*!40000 ALTER TABLE `customers` DISABLE KEYS */;
/*!40000 ALTER TABLE `customers` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-06-14 10:19:28
