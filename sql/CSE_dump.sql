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
INSERT INTO `Manufacturer` VALUES (42,'Lee, Carter, and Parrish','Hello World!!!!!!'),(43,'Green-Morgan','Continue drive pressure yes arrive series com'),(44,'Ortega-Khan','Write tell approach fall throw forget.'),(45,'Walker-Shepard','Like argue trouble environment always.'),(46,'Ellis and Sons','Environmental ever hundred represent.'),(47,'Douglas-Roberts','Far attorney much I language feeling item.'),(48,'Johnson-Olson','Follow customer true such alone whom age.'),(49,'Harvey and Sons','Democratic run another never far seven perhap'),(50,'Reyes Group','Action environmental notice month.'),(51,'Cross-Duncan','Rest article card so big international life o'),(52,'Atkinson Inc','Three might nor technology.'),(53,'Walker Ltd','Decade describe focus last thus business.'),(54,'Goodman-Scott','Four other body keep.'),(55,'Humphrey, Anderson and Johnson','Final trouble go.'),(56,'Hernandez, Guzman and Lopez','Take subject onto know produce two.'),(57,'Sanders-Roth','Car care still service ever.'),(58,'Townsend, Walker and Juarez','We and father great.'),(59,'Willis-King','Investment reach party process community leg.'),(60,'Smith-Matthews','Family program heavy.'),(61,'Johnson Ltd','Run director respond themselves size or money');
/*!40000 ALTER TABLE `Manufacturer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `access`
--

DROP TABLE IF EXISTS `access`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `access` (
  `id` int NOT NULL AUTO_INCREMENT,
  `details_token` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `access`
--

LOCK TABLES `access` WRITE;
/*!40000 ALTER TABLE `access` DISABLE KEYS */;
/*!40000 ALTER TABLE `access` ENABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=1000003 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `car`
--

LOCK TABLES `car` WRITE;
/*!40000 ALTER TABLE `car` DISABLE KEYS */;
INSERT INTO `car` VALUES (8,1,'ABC123','12345','90000','THIS IS NOT AN UFO'),(9,13,'LCy230','42678','526','Thus team partner.'),(10,10,'oll501','29914','966','Party should theory bit must edge onto.'),(11,3,'Zcp533','39339','216','Health information top stay ball project seek'),(12,2,'fTF206','17238','992','Style sort and free ten PM Democrat.'),(13,18,'bWq276','18710','469','Can big it interesting respond produce.'),(14,12,'Vxp705','58837','194','Item international particular rest help prove'),(15,14,'NvG090','20588','776','Professional despite majority campaign plant.'),(16,9,'sPN286','5471','451','When serious situation seat behind western ac'),(17,15,'VqR416','25518','289','But serious think perform party enter.'),(18,11,'JiK540','79682','409','Similar man owner manage city difference valu'),(19,6,'yYX272','48936','170','Also factor while.'),(20,2,'HIt656','89587','580','Lay line dark.'),(21,17,'OPH966','71981','769','Light garden feel perhaps experience.'),(22,13,'dFr035','9657','129','Some study by among.'),(23,15,'ARg994','31939','903','Cell blood kind on I pressure card.'),(24,1,'shf570','10745','284','Important federal give cell.'),(25,12,'gMM139','28106','111','What national entire thing.'),(26,10,'Ggd971','40434','123','Everyone authority give bit national stock st'),(27,2,'Zbh886','16644','482','Attorney art building necessary.'),(28,8,'Qxs780','70047','606','Build event exactly their.'),(29,13,'GAQ957','33135','255','Garden part truth bar assume college talk.'),(30,6,'rnk233','8404','494','Yourself ten science drive else buy another.'),(31,17,'RYK413','39426','303','Today edge car future point claim.'),(32,20,'UqE589','602','653','Treat Mr large cultural student writer.'),(33,20,'KDa589','40178','872','Million question brother official institution'),(34,1,'Ssf502','6549','719','Interesting style television at Mr learn writ'),(35,20,'lvv942','8636','288','Whom magazine space still.'),(36,5,'mUC624','39285','331','Piece firm group employee range common thus.'),(37,8,'SxO163','25745','918','Sit cold find everyone.'),(38,7,'CPd107','86795','946','Head term single expect so central.'),(39,8,'Lqu178','8704','133','Away very modern.'),(40,4,'xYc841','52860','599','Institution room personal itself recently all'),(41,18,'nUU928','68179','410','Just room town policy space activity boy.'),(42,20,'ClG399','31992','889','Will physical lawyer yes.'),(43,10,'RzM009','29272','550','Media morning loss simply quickly his.'),(44,17,'cVE595','69684','427','Enough accept relate weight include keep near'),(45,7,'EbU210','29071','360','Doctor show available against bring whom part'),(46,20,'sEe209','51466','474','Something anyone kid board.'),(47,11,'xUD277','23124','121','Describe subject production feel station Mrs.'),(48,3,'DjC216','51861','175','Environmental follow friend likely red.'),(49,8,'TTp319','11412','733','Look fight pressure discover drop.'),(50,16,'nDi922','60680','773','Tonight range call remember available south.'),(51,9,'nuO773','22688','973','Argue might keep care theory small score writ'),(52,15,'KTm058','93904','390','School behind everybody power speak score.'),(53,17,'aEH925','77916','968','People within military your energy.'),(54,6,'nyz290','1316','126','Finish money help take.'),(55,8,'BSw018','53707','545','Alone manage his design moment evening profes'),(56,6,'xOi990','89219','337','American another challenge off price year pas'),(57,3,'Ioz312','92317','170','Bring dream house miss hard agree.'),(58,5,'ZCZ507','91753','409','Reach town own thought.'),(59,12,'bFA498','56869','599','Daughter water nothing manager.'),(60,7,'PHk007','48385','591','Stand agree fly event voice recent.'),(61,19,'VPP078','32064','146','Point campaign little national save remember '),(62,12,'UaN073','11052','261','Ahead phone price be response.'),(63,12,'mVT932','45757','937','Personal song off class society certain custo'),(64,2,'uhq443','41814','628','Clear environment peace recently.'),(65,11,'XKL839','50303','276','Author remember manage analysis.'),(66,14,'uhf426','30189','436','Cultural measure score window road.'),(67,9,'lWS278','89180','501','Wife until should term follow loss rather.'),(68,13,'gmc463','43595','830','Student authority everybody.'),(69,18,'Dno843','57312','260','Left return same nature late.'),(70,7,'qdZ126','2774','857','President right party authority girl section.'),(71,3,'wLJ486','51799','461','Gas avoid church all power.'),(72,19,'Wsa058','40881','761','Between reason doctor health family follow gl'),(73,2,'Rsq900','4520','810','Realize reality method anything dinner imagin'),(74,2,'wte399','4311','817','Sing wrong idea little decade back option.'),(75,1,'XUi619','70257','625','However dinner source here could enjoy.'),(76,18,'mOV490','34447','978','Practice too now movement without discover en'),(77,18,'TnA603','85230','463','Attack fight movie share add bad.'),(78,10,'eOj189','50508','625','Newspaper perhaps son door senior game.'),(79,15,'jQq464','76977','446','Increase when nor right attention marriage de'),(80,9,'IGG264','91040','983','Explain view push three the can must.'),(81,13,'yJc693','54949','396','Hundred street party create.'),(82,2,'KNd470','81494','811','Exactly represent money build common indeed.'),(83,17,'XgY510','10148','763','Risk pick during campaign behind begin kitche'),(84,8,'PpG729','43364','953','Mrs four degree everyone determine let tonigh'),(85,3,'pUf543','40852','495','Page simply different place want.'),(86,17,'EtE908','82239','479','Some usually fast treatment ever friend quick'),(87,5,'tiM974','67992','968','Certain security type animal particularly com'),(88,16,'rRa097','56010','755','Pm picture owner necessary measure baby home.'),(89,18,'zMw502','41344','899','Mrs see bed ball probably to.'),(90,14,'QJI025','38709','674','Center treat administration involve simple th'),(91,8,'hYM549','17055','470','Those beyond character history scene.'),(92,15,'jeB404','44012','474','Country apply source population benefit impro'),(93,5,'yZz835','74273','648','Citizen society himself despite mean.'),(94,17,'ALP521','89763','366','Name sister statement.'),(95,2,'EeP021','34766','155','Check foreign draw message job too community.'),(96,1,'ABC123','12345','90000','THIS IS AN UFO, MAYBE'),(97,10,'XYZ321','54321','15','Snail car'),(98,10,'XYZ321','54321','1',NULL);
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
INSERT INTO `model` VALUES (1,43,'Cin672','1000','msKlwg'),(2,61,'kkG057','1205','RdggWH'),(3,58,'cas350','9964','eoCFNr'),(4,56,'bkM317','3940','fueIeC'),(5,54,'krh363','2507','NDHYJa'),(6,51,'Nfy707','8279','srPkTF'),(7,49,'QuO476','1999','DDIFIW'),(8,43,'pTh135','8410','YQIoVH'),(9,43,'Cin672','948','msKlwg'),(10,53,'OWF514','3844','zzINhq'),(11,49,'VPH049','3786','gKCnDs'),(12,47,'EdV590','5232','wQBFlg'),(13,42,'jnO197','7401','mLutca'),(14,54,'ojp437','2969','EsrzMC'),(15,55,'Pao684','5822','ETVVTC'),(16,54,'VsS877','4443','lDcTsd'),(17,45,'Ujr395','5562','TUINEc'),(18,50,'CGZ716','1150','uIkOjY'),(19,57,'KrD971','1572','dQXEDZ'),(20,49,'tOI178','7116','KRTfJs');
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

-- Dump completed on 2024-01-02 11:57:08
