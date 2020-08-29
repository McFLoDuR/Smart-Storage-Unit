-- MySQL dump 10.17  Distrib 10.3.22-MariaDB, for debian-linux-gnueabihf (armv8l)
--
-- Host: localhost    Database: ssu
-- ------------------------------------------------------
-- Server version	10.3.22-MariaDB-0+deb10u1

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
-- Table structure for table `activeLEDs`
--

DROP TABLE IF EXISTS `activeLEDs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `activeLEDs` (
  `SlotID` int(11) NOT NULL,
  `color` char(6) NOT NULL,
  `speed` tinyint(1) NOT NULL,
  `stateActivated` tinyint(1) NOT NULL,
  `stateChanged` tinyint(1) NOT NULL,
  PRIMARY KEY (`SlotID`),
  CONSTRAINT `activeLEDs_ibfk_1` FOREIGN KEY (`SlotID`) REFERENCES `storageh` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `activeLEDs`
--

LOCK TABLES `activeLEDs` WRITE;
/*!40000 ALTER TABLE `activeLEDs` DISABLE KEYS */;
/*!40000 ALTER TABLE `activeLEDs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `componenttypes`
--

DROP TABLE IF EXISTS `componenttypes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `componenttypes` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `typeName` varchar(50) NOT NULL,
  `typeVersion` varchar(40) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `componenttypes`
--

LOCK TABLES `componenttypes` WRITE;
/*!40000 ALTER TABLE `componenttypes` DISABLE KEYS */;
INSERT INTO `componenttypes` VALUES (35,'resistor','default'),(36,'transistor','NPN'),(37,'op. amp.','rail-to-rail');
/*!40000 ALTER TABLE `componenttypes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `itemdata`
--

DROP TABLE IF EXISTS `itemdata`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `itemdata` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `itemID` int(11) NOT NULL,
  `referenceID` int(11) NOT NULL,
  `propertyValue` varchar(40) NOT NULL,
  `unit` varchar(20) NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `referenceID` (`referenceID`),
  KEY `itemID` (`itemID`),
  CONSTRAINT `itemdata_ibfk_1` FOREIGN KEY (`referenceID`) REFERENCES `referencenames` (`ID`),
  CONSTRAINT `itemdata_ibfk_2` FOREIGN KEY (`itemID`) REFERENCES `items` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=181 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `itemdata`
--

LOCK TABLES `itemdata` WRITE;
/*!40000 ALTER TABLE `itemdata` DISABLE KEYS */;
INSERT INTO `itemdata` VALUES (156,72,19,'2','W'),(157,72,20,'500','V'),(158,72,21,'1','kOhm'),(159,73,22,'100','mA'),(160,73,23,'45','V'),(161,73,24,'300','MHz'),(162,73,25,'500','mW'),(163,74,26,'8','V'),(164,74,27,'16','V'),(165,74,24,'3','MHz'),(175,75,21,'10','kOhm'),(176,75,19,'0.6','W'),(177,75,28,'1','%'),(178,76,28,'1','%'),(179,76,21,'2.7','kOhm'),(180,76,19,'0.6','W');
/*!40000 ALTER TABLE `itemdata` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `items`
--

DROP TABLE IF EXISTS `items`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `items` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `typeID` int(11) NOT NULL,
  `articleNumber` varchar(50) NOT NULL,
  `weight` double(10,5) NOT NULL,
  `weblink` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `typeID` (`typeID`),
  CONSTRAINT `items_ibfk_1` FOREIGN KEY (`typeID`) REFERENCES `componenttypes` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=77 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `items`
--

LOCK TABLES `items` WRITE;
/*!40000 ALTER TABLE `items` DISABLE KEYS */;
INSERT INTO `items` VALUES (72,35,'CFR02W',0.00000,NULL),(73,36,'BC547B',1000.00000,NULL),(74,37,'TLV271IP',0.00000,NULL),(75,35,'MF0207FTE52-10K',0.00000,NULL),(76,35,'MF0207FTE52-2K7',0.00000,NULL);
/*!40000 ALTER TABLE `items` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `permissions`
--

DROP TABLE IF EXISTS `permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `permissions` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `permissionName` varchar(40) NOT NULL,
  `manageUsers` tinyint(1) NOT NULL,
  `storeItems` tinyint(1) NOT NULL,
  `withdrawItems` tinyint(1) NOT NULL,
  `deleteStorageSlot` tinyint(1) NOT NULL,
  `moveStorageSlot` tinyint(1) NOT NULL,
  `managePartitions` tinyint(1) NOT NULL,
  `correctQuantity` tinyint(1) NOT NULL,
  `createInventoryReport` tinyint(1) NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `permissionName` (`permissionName`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `permissions`
--

LOCK TABLES `permissions` WRITE;
/*!40000 ALTER TABLE `permissions` DISABLE KEYS */;
INSERT INTO `permissions` VALUES (1,'admin',1,1,1,1,1,1,1,1),(2,'moderator',0,1,1,1,0,0,1,1),(3,'user',1,1,1,0,0,0,0,1),(4,'god',0,0,0,0,0,0,0,0),(7,'lol',1,1,1,1,1,0,1,1);
/*!40000 ALTER TABLE `permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `referencenames`
--

DROP TABLE IF EXISTS `referencenames`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `referencenames` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(40) NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `referencenames`
--

LOCK TABLES `referencenames` WRITE;
/*!40000 ALTER TABLE `referencenames` DISABLE KEYS */;
INSERT INTO `referencenames` VALUES (28,'accuracy'),(24,'f'),(22,'Ic'),(26,'max. dpl. Vcc '),(27,'max. sgl. Vcc '),(20,'max. Voltage'),(19,'power rating'),(25,'Ptot'),(21,'resistance'),(23,'Uce');
/*!40000 ALTER TABLE `referencenames` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stateStorage`
--

DROP TABLE IF EXISTS `stateStorage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `stateStorage` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `usageText` varchar(100) NOT NULL,
  `UserID` int(11) NOT NULL,
  `stateActivated` tinyint(1) NOT NULL,
  `stateChanged` tinyint(1) NOT NULL,
  `stateValue` double(10,5) DEFAULT 0.00000,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `usageText` (`usageText`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stateStorage`
--

LOCK TABLES `stateStorage` WRITE;
/*!40000 ALTER TABLE `stateStorage` DISABLE KEYS */;
INSERT INTO `stateStorage` VALUES (1,'extend drawer and measure',0,0,0,0.84450);
/*!40000 ALTER TABLE `stateStorage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `storageh`
--

DROP TABLE IF EXISTS `storageh`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `storageh` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `storagePosition` int(11) NOT NULL,
  `firstPartition` tinyint(1) NOT NULL,
  `secondPartition` tinyint(1) NOT NULL,
  `thirdPartition` tinyint(1) NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `storagePosition` (`storagePosition`)
) ENGINE=InnoDB AUTO_INCREMENT=241 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `storageh`
--

LOCK TABLES `storageh` WRITE;
/*!40000 ALTER TABLE `storageh` DISABLE KEYS */;
INSERT INTO `storageh` VALUES (1,1,1,0,1),(2,2,0,1,0),(3,3,0,0,0),(4,4,0,0,0),(5,5,0,0,0),(6,73,0,0,0),(7,7,0,0,0),(8,8,0,0,0),(9,9,0,0,0),(10,199,0,0,0),(11,11,0,0,0),(12,12,0,0,0),(13,13,0,0,0),(14,14,0,0,0),(15,15,0,0,0),(16,16,0,0,0),(17,17,0,0,0),(18,20,0,0,0),(19,18,0,0,0),(20,19,0,0,0),(21,21,0,0,0),(22,22,0,0,0),(23,23,0,1,0),(24,24,0,0,0),(25,25,0,0,0),(26,26,0,0,0),(27,27,0,0,0),(28,28,0,0,0),(29,29,0,0,0),(30,30,0,0,0),(31,31,0,0,0),(32,32,0,0,0),(33,33,0,0,0),(34,34,0,0,0),(35,35,0,0,0),(36,36,0,0,0),(37,37,0,0,0),(38,38,0,0,0),(39,39,0,0,0),(40,40,0,0,0),(41,41,0,0,0),(42,42,0,0,0),(43,43,0,0,0),(44,44,0,0,0),(45,45,0,1,0),(46,46,0,0,0),(47,47,0,0,0),(48,48,0,0,0),(49,49,0,0,0),(50,50,0,0,0),(51,51,0,0,0),(52,52,0,0,0),(53,53,0,0,0),(54,54,0,0,0),(55,55,0,0,0),(56,56,0,0,0),(57,57,0,0,0),(58,58,0,0,0),(59,59,0,0,0),(60,60,0,0,0),(61,61,0,0,0),(62,62,0,0,0),(63,63,0,0,0),(64,64,0,0,0),(65,65,0,0,0),(66,66,0,0,0),(67,67,0,0,0),(68,68,0,0,0),(69,69,0,0,0),(70,70,0,1,0),(71,71,0,0,0),(72,72,0,0,0),(73,6,0,0,0),(74,74,0,0,0),(75,75,0,0,0),(76,76,0,0,0),(77,77,0,0,0),(78,78,0,0,0),(79,79,0,0,0),(80,80,0,0,0),(81,81,0,0,0),(82,82,0,0,0),(83,83,0,0,0),(84,84,0,0,0),(85,85,0,0,0),(86,86,0,0,0),(87,87,0,0,0),(88,88,0,0,0),(89,89,0,0,0),(90,90,0,0,0),(91,91,0,0,0),(92,92,0,0,0),(93,93,0,0,0),(94,94,0,0,0),(95,95,0,0,0),(96,96,0,0,0),(97,10,0,0,0),(98,98,0,0,0),(99,99,0,0,0),(100,100,0,0,0),(101,101,0,0,0),(102,102,0,0,0),(103,103,0,0,0),(104,104,0,0,0),(105,105,0,0,0),(106,121,0,0,0),(107,107,0,0,0),(108,108,0,1,0),(109,109,0,1,0),(110,110,0,0,0),(111,111,0,0,0),(112,112,0,0,0),(113,113,0,0,0),(114,114,0,0,0),(115,115,0,0,0),(116,116,0,0,0),(117,117,0,0,0),(118,118,0,0,0),(119,119,0,0,0),(120,120,0,0,0),(121,106,0,0,0),(122,122,0,0,0),(123,123,0,0,0),(124,124,0,0,0),(125,125,1,0,0),(126,126,0,0,0),(127,127,1,0,0),(128,128,0,0,0),(129,129,0,0,0),(130,130,0,0,0),(131,131,0,0,0),(132,132,0,0,0),(133,133,0,0,0),(134,134,0,0,0),(135,135,1,1,0),(136,136,0,0,0),(137,137,0,0,0),(138,138,0,0,0),(139,139,0,0,0),(140,140,0,0,0),(141,141,0,0,0),(142,142,0,0,0),(143,143,0,0,0),(144,144,0,0,0),(145,145,0,0,0),(146,146,0,0,0),(147,147,0,0,0),(148,148,0,0,0),(149,149,0,0,0),(150,150,0,0,1),(151,151,0,0,0),(152,152,0,0,0),(153,153,0,0,0),(154,154,0,0,0),(155,155,0,0,0),(156,156,0,0,0),(157,157,0,0,0),(158,158,0,0,0),(159,159,0,0,0),(160,160,0,0,0),(161,161,0,0,0),(162,162,0,0,0),(163,163,0,0,0),(164,164,0,0,0),(165,165,0,0,0),(166,166,0,0,0),(167,167,0,0,0),(168,168,0,0,0),(169,169,0,0,0),(170,170,0,0,0),(171,171,0,0,0),(172,172,0,0,0),(173,173,0,0,0),(174,174,0,0,0),(175,175,0,0,0),(176,176,0,0,0),(177,177,0,0,0),(178,178,0,0,0),(179,179,0,0,0),(180,180,0,0,0),(181,181,0,0,1),(182,182,0,0,0),(183,183,0,0,0),(184,184,0,0,0),(185,185,0,0,0),(186,186,0,0,0),(187,187,0,0,0),(188,188,0,0,0),(189,189,0,0,0),(190,190,0,0,0),(191,191,0,0,0),(192,192,0,0,0),(193,193,0,0,0),(194,194,0,0,0),(195,195,0,0,0),(196,196,0,0,0),(197,197,0,0,0),(198,198,0,0,0),(199,97,0,0,0),(200,200,0,0,0),(201,201,0,0,0),(202,202,0,0,0),(203,203,0,0,0),(204,204,0,0,0),(205,205,0,0,0),(206,206,0,0,0),(207,207,0,0,0),(208,208,0,0,0),(209,209,0,0,0),(210,210,0,0,0),(211,211,0,0,0),(212,212,0,0,0),(213,213,0,0,0),(214,214,0,0,1),(215,215,0,0,0),(216,216,0,0,0),(217,217,0,0,0),(218,218,0,0,0),(219,219,0,0,0),(220,220,0,0,0),(221,221,0,0,0),(222,222,0,0,0),(223,223,0,0,0),(224,224,0,0,0),(225,225,0,0,0),(226,226,0,0,0),(227,227,0,0,0),(228,228,0,0,0),(229,229,0,0,0),(230,230,0,0,0),(231,231,0,0,0),(232,232,0,0,0),(233,233,0,0,0),(234,234,0,0,0),(235,235,0,1,0),(236,236,0,0,0),(237,237,0,0,0),(238,238,0,0,0),(239,239,0,0,0),(240,240,0,0,0);
/*!40000 ALTER TABLE `storageh` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `storagep`
--

DROP TABLE IF EXISTS `storagep`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `storagep` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `storagehID` int(11) NOT NULL,
  `itemID` int(11) NOT NULL,
  `insidePosition` tinyint(4) NOT NULL,
  `quantity` int(11) NOT NULL,
  `quantityMin` int(11) NOT NULL,
  `quantityMax` int(11) NOT NULL,
  `alarmActivated` tinyint(1) NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `itemID` (`itemID`),
  KEY `storagehID` (`storagehID`),
  CONSTRAINT `storagep_ibfk_1` FOREIGN KEY (`itemID`) REFERENCES `items` (`ID`),
  CONSTRAINT `storagep_ibfk_2` FOREIGN KEY (`storagehID`) REFERENCES `storageh` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=124 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `storagep`
--

LOCK TABLES `storagep` WRITE;
/*!40000 ALTER TABLE `storagep` DISABLE KEYS */;
INSERT INTO `storagep` VALUES (116,106,75,1,251,100,254,0),(117,10,73,1,174,20,200,1),(118,5,74,1,9,5,10,0),(119,157,72,1,164,1,165,1),(120,135,75,2,111,54,145,0),(121,1,74,2,19,5,20,0),(122,1,72,3,19,1,20,1),(123,2,75,2,300,1,300,0);
/*!40000 ALTER TABLE `storagep` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(70) DEFAULT NULL,
  `color` char(6) NOT NULL,
  `email` varchar(80) NOT NULL,
  `monthlyNotification` tinyint(1) NOT NULL,
  `userSignedIn` tinyint(1) NOT NULL,
  `permissionID` int(11) NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `username` (`username`),
  KEY `permissionID` (`permissionID`),
  CONSTRAINT `users_ibfk_1` FOREIGN KEY (`permissionID`) REFERENCES `permissions` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'administrator','540CED6E2AEBB1217FE9AF7F7DEF9C69A9C40016805E7628C40637223AD8207F','FF0000','fabian.reiner@bulme.at',0,0,1),(2,'fabian','540CED6E2AEBB1217FE9AF7F7DEF9C69A9C40016805E7628C40637223AD8207F','0000FF','fabian.reiner@bulme.at',1,0,7),(3,'stefan','540CED6E2AEBB1217FE9AF7F7DEF9C69A9C40016805E7628C40637223AD8207F','00FF00','stefan.zauper@bulme.at',0,0,2),(4,'rudolf','6739502233ACD550B06AF351D9EA5356C39036511FEF6AE4B6C762974B1D8EE3','6A6DFB','rudolf.migirov@bulme.at',1,0,2),(5,'blackColorBlocker','9776DB26252438FFEA2C768D24439B53E0B017A876CB42F970304A096E4CB792','000000','fabian.reiner@bulme.at',0,0,4),(14,'SpeedyGonzales','396EAB40E33E70A5C9E3D157FDF46E0C50CA8062CA6315FF0ED410328EFB6BD4','AA55FF','god@bulme.at',0,0,4);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-04-14 12:21:12
