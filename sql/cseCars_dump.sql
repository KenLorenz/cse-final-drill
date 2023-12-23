-- MySQL dump 10.13  Distrib 8.1.0-1, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: cseCars
-- ------------------------------------------------------
-- Server version	8.1.0-1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
/*!50717 SELECT COUNT(*) INTO @rocksdb_has_p_s_session_variables FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'performance_schema' AND TABLE_NAME = 'session_variables' */;
/*!50717 SET @rocksdb_get_is_supported = IF (@rocksdb_has_p_s_session_variables, 'SELECT COUNT(*) INTO @rocksdb_is_supported FROM performance_schema.session_variables WHERE VARIABLE_NAME=\'rocksdb_bulk_load\'', 'SELECT 0') */;
/*!50717 PREPARE s FROM @rocksdb_get_is_supported */;
/*!50717 EXECUTE s */;
/*!50717 DEALLOCATE PREPARE s */;
/*!50717 SET @rocksdb_enable_bulk_load = IF (@rocksdb_is_supported, 'SET SESSION rocksdb_bulk_load = 1', 'SET @rocksdb_dummy_bulk_load = 0') */;
/*!50717 PREPARE s FROM @rocksdb_enable_bulk_load */;
/*!50717 EXECUTE s */;
/*!50717 DEALLOCATE PREPARE s */;

--
-- Table structure for table `Manufacturer`
--

DROP TABLE IF EXISTS `Manufacturer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Manufacturer` (
  `idManufacturer` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `details` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idManufacturer`)
) ENGINE=InnoDB AUTO_INCREMENT=62 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Manufacturer`
--

LOCK TABLES `Manufacturer` WRITE;
/*!40000 ALTER TABLE `Manufacturer` DISABLE KEYS */;
INSERT INTO `Manufacturer` VALUES (42,'Lee, Carter and Parrish','Strong simply those process send.'),(43,'Green-Morgan','Continue drive pressure yes arrive series com'),(44,'Ortega-Khan','Write tell approach fall throw forget.'),(45,'Walker-Shepard','Like argue trouble environment always.'),(46,'Ellis and Sons','Environmental ever hundred represent.'),(47,'Douglas-Roberts','Far attorney much I language feeling item.'),(48,'Johnson-Olson','Follow customer true such alone whom age.'),(49,'Harvey and Sons','Democratic run another never far seven perhap'),(50,'Reyes Group','Action environmental notice month.'),(51,'Cross-Duncan','Rest article card so big international life o'),(52,'Atkinson Inc','Three might nor technology.'),(53,'Walker Ltd','Decade describe focus last thus business.'),(54,'Goodman-Scott','Four other body keep.'),(55,'Humphrey, Anderson and Johnson','Final trouble go.'),(56,'Hernandez, Guzman and Lopez','Take subject onto know produce two.'),(57,'Sanders-Roth','Car care still service ever.'),(58,'Townsend, Walker and Juarez','We and father great.'),(59,'Willis-King','Investment reach party process community leg.'),(60,'Smith-Matthews','Family program heavy.'),(61,'Johnson Ltd','Run director respond themselves size or money');
/*!40000 ALTER TABLE `Manufacturer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `car`
--

DROP TABLE IF EXISTS `car`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `car` (
  `idcar` int NOT NULL AUTO_INCREMENT,
  `model_idmodel` int NOT NULL,
  `license_num` varchar(45) DEFAULT NULL,
  `cur_mileage` varchar(45) DEFAULT NULL,
  `engine_size` varchar(45) NOT NULL,
  `other_car_details` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idcar`),
  KEY `fk_car_model_idx` (`model_idmodel`),
  CONSTRAINT `fk_car_model` FOREIGN KEY (`model_idmodel`) REFERENCES `model` (`idmodel`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `car`
--

LOCK TABLES `car` WRITE;
/*!40000 ALTER TABLE `car` DISABLE KEYS */;
INSERT INTO `car` VALUES (1,14,'Zrz991','7578','791','Doctor sister rate modern management.'),(2,4,'Vyx276','22041','842','Represent half improve American house news.'),(3,12,'ANn907','8048','811','Economic read beyond probably former througho'),(4,11,'vpP401','25120','118','Law me near wrong represent drug.'),(5,5,'OKH780','48656','748','Box drug want kitchen member reason effect.'),(6,8,'yBW967','88596','108','System policy strategy trade.'),(7,15,'gHv332','49186','859','Special skill each term article total author '),(8,11,'XIu345','97598','389','Marriage system seven join maybe hour.'),(9,13,'LCy230','42678','526','Thus team partner.'),(10,10,'oll501','29914','966','Party should theory bit must edge onto.'),(11,3,'Zcp533','39339','216','Health information top stay ball project seek'),(12,2,'fTF206','17238','992','Style sort and free ten PM Democrat.'),(13,18,'bWq276','18710','469','Can big it interesting respond produce.'),(14,12,'Vxp705','58837','194','Item international particular rest help prove'),(15,14,'NvG090','20588','776','Professional despite majority campaign plant.'),(16,9,'sPN286','5471','451','When serious situation seat behind western ac'),(17,15,'VqR416','25518','289','But serious think perform party enter.'),(18,11,'JiK540','79682','409','Similar man owner manage city difference valu'),(19,6,'yYX272','48936','170','Also factor while.');
/*!40000 ALTER TABLE `car` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `model`
--

DROP TABLE IF EXISTS `model`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `model` (
  `idmodel` int NOT NULL AUTO_INCREMENT,
  `Manufacturer_idManufacturer` int NOT NULL,
  `model_code` varchar(45) DEFAULT NULL,
  `daily_hire_rate` varchar(45) DEFAULT NULL,
  `name` varchar(45) NOT NULL,
  PRIMARY KEY (`idmodel`),
  KEY `fk_model_Manufacturer1_idx` (`Manufacturer_idManufacturer`),
  CONSTRAINT `fk_model_Manufacturer1` FOREIGN KEY (`Manufacturer_idManufacturer`) REFERENCES `Manufacturer` (`idManufacturer`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `model`
--

LOCK TABLES `model` WRITE;
/*!40000 ALTER TABLE `model` DISABLE KEYS */;
INSERT INTO `model` VALUES (1,43,'EXQ406','4692','YtEozW'),(2,61,'kkG057','1205','RdggWH'),(3,58,'cas350','9964','eoCFNr'),(4,56,'bkM317','3940','fueIeC'),(5,54,'krh363','2507','NDHYJa'),(6,51,'Nfy707','8279','srPkTF'),(7,49,'QuO476','1999','DDIFIW'),(8,43,'pTh135','8410','YQIoVH'),(9,43,'Cin672','948','msKlwg'),(10,53,'OWF514','3844','zzINhq'),(11,49,'VPH049','3786','gKCnDs'),(12,47,'EdV590','5232','wQBFlg'),(13,42,'jnO197','7401','mLutca'),(14,54,'ojp437','2969','EsrzMC'),(15,55,'Pao684','5822','ETVVTC'),(16,54,'VsS877','4443','lDcTsd'),(17,45,'Ujr395','5562','TUINEc'),(18,50,'CGZ716','1150','uIkOjY'),(19,57,'KrD971','1572','dQXEDZ'),(20,49,'tOI178','7116','KRTfJs');
/*!40000 ALTER TABLE `model` ENABLE KEYS */;
UNLOCK TABLES;
/*!50112 SET @disable_bulk_load = IF (@is_rocksdb_supported, 'SET SESSION rocksdb_bulk_load = @old_rocksdb_bulk_load', 'SET @dummy_rocksdb_bulk_load = 0') */;
/*!50112 PREPARE s FROM @disable_bulk_load */;
/*!50112 EXECUTE s */;
/*!50112 DEALLOCATE PREPARE s */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-23 15:02:53
