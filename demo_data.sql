-- MySQL dump 10.13  Distrib 5.7.43, for Linux (x86_64)
--
-- Host: localhost    Database: forsit
-- ------------------------------------------------------
-- Server version	5.7.43

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
INSERT INTO `alembic_version` VALUES ('c68e26fc8574');
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `categories`
--

DROP TABLE IF EXISTS `categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `categories` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `ix_categories_id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categories`
--

LOCK TABLES `categories` WRITE;
/*!40000 ALTER TABLE `categories` DISABLE KEYS */;
INSERT INTO `categories` VALUES (3,'Electronics'),(2,'Home & Kichen'),(4,'Personal care'),(1,'Spors & Outdoor');
/*!40000 ALTER TABLE `categories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inventory`
--

DROP TABLE IF EXISTS `inventory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `inventory` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `product_id` int(11) DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL,
  `last_updated` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `product_id` (`product_id`),
  KEY `ix_inventory_id` (`id`),
  CONSTRAINT `inventory_ibfk_1` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inventory`
--

LOCK TABLES `inventory` WRITE;
/*!40000 ALTER TABLE `inventory` DISABLE KEYS */;
INSERT INTO `inventory` VALUES (1,1,1,'2023-10-03 17:07:26'),(2,2,1,'2023-10-03 17:08:46'),(3,3,1,'2023-10-03 17:09:26'),(4,4,1,'2023-10-03 17:11:49'),(5,5,1,'2023-10-03 17:14:41'),(6,6,1,'2023-10-03 17:15:45'),(7,7,1,'2023-10-03 17:17:21'),(8,8,1,'2023-10-03 17:19:47'),(9,9,1,'2023-10-03 17:22:48'),(10,10,1,'2023-10-03 17:24:22'),(11,11,1,'2023-10-03 17:26:33'),(12,12,1,'2023-10-03 17:28:47'),(13,13,1,'2023-10-03 17:30:55'),(14,14,1,'2023-10-03 17:32:15'),(15,15,1,'2023-10-03 17:33:58'),(16,16,1,'2023-10-03 17:34:58');
/*!40000 ALTER TABLE `inventory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inventory_logs`
--

DROP TABLE IF EXISTS `inventory_logs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `inventory_logs` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `product_id` int(11) DEFAULT NULL,
  `update_quantity` int(11) DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_inventory_logs_id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inventory_logs`
--

LOCK TABLES `inventory_logs` WRITE;
/*!40000 ALTER TABLE `inventory_logs` DISABLE KEYS */;
/*!40000 ALTER TABLE `inventory_logs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `products` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `description` varchar(250) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `price` float DEFAULT NULL,
  `category_id` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `category_id` (`category_id`),
  KEY `ix_products_id` (`id`),
  KEY `ix_products_name` (`name`),
  CONSTRAINT `products_ibfk_1` FOREIGN KEY (`category_id`) REFERENCES `categories` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` VALUES (1,'Youth Footballs','Franklin Sports Youth Footballs - Junior + Pee Wee Kids Footballs - All-Weather Synthetic Leather Outdoor Footballs - Extra Grip 1000 Footballs for Kids - 1 Packs + 12 Football Team Packs',9,1,'2023-10-03 17:07:26','2023-10-03 17:07:26'),(2,'Tennis Balls','Penn Championship Tennis Balls - Extra Duty Felt Pressurized Tennis Balls',11,1,'2023-10-03 17:08:46','2023-10-03 17:08:46'),(3,'Trekking Poles','Cascade Mountain Tech Lightweight Aircraft-Grade Aluminum Trekking Poles with Extended Down',21,1,'2023-10-03 17:09:26','2023-10-03 17:09:26'),(4,'Yoga Mat','Gaiam Essentials Thick Yoga Mat Fitness & Exercise Mat with Easy-Cinch Yoga Mat Carrier Strap, 72L x 24W x 2/5 Inch Thick',21,1,'2023-10-03 17:11:49','2023-10-03 17:11:49'),(5,'Folding Bar','Lavish Home 18, Rec 14 D x 12 W x H Black Set of 1 Inch Folding Bar Heavy-Duty Padded Portable Stool with 225-Pound Capacity for Dorm Recreation Game',19,2,'2023-10-03 17:14:41','2023-10-03 17:14:41'),(6,'Vacuum Cleaner','Eureka Home Lightweight Stick Vacuum Cleaner, Powerful Suction Corded Multi-Surfaces, 3-in-1 Handheld Vac, Blaze Black',30,2,'2023-10-03 17:15:45','2023-10-03 17:15:45'),(7,'Toothbrush Holders','iHave Toothbrush Holders for Bathrooms, 2 Cups Toothbrush Holder Wall Mounted with Toothpaste Dispenser - Large Capacity Tray, Cosmetic Drawer - Bathroom Decor & Bathroom Accessories',19,2,'2023-10-03 17:17:21','2023-10-03 17:17:21'),(8,'Titanium Scissors','Westcott 13901 8-Inch Titanium Scissors For Office and Home Yellow/Gray 2 Pack',9,2,'2023-10-03 17:19:47','2023-10-03 17:19:47'),(9,'Energizer AA Batteries','Energizer AA Batteries Double A Long-Lasting Alkaline Power Batteries 32 Count (Pack of 1)',23,3,'2023-10-03 17:22:48','2023-10-03 17:22:48'),(10,'SAMSUNG 870 EVO','SAMSUNG 870 EVO SATA III SSD 1TB 2.5 Internal Solid State Drive Upgrade PC or Laptop Memory and Storage for IT Pros Creators Everyday Users MZ-77E1T0B/AM',50,3,'2023-10-03 17:24:22','2023-10-03 17:24:22'),(11,'INIU Wireless Charger','INIU Wireless Charger 15W Fast Wireless Charging Station with Sleep-Friendly Adaptive Light Compatible with iPhone 15 14 13 12 Pro XR XS 8 Plus Samsung Galaxy S23 S22 S21 S20 Note 20 10 Google etc',15,3,'2023-10-03 17:26:33','2023-10-03 17:26:33'),(12,'Toner Cartridge','Brother Genuine High Yield Toner Cartridge TN660 Replacement Black Toner Page Yield Up to 2,600 Pages Amazon Dash Replenishment Cartridge',58,3,'2023-10-03 17:28:47','2023-10-03 17:28:47'),(13,'Moisturizing Cream Body','CeraVe Moisturizing Cream Body and Face Moisturizer for Dry Skin Body Cream with Hyaluronic Acid and Ceramides Hydrating Moisturizer Fragrance Free Non-Comedogenic 19 Ounce',17,4,'2023-10-03 17:30:55','2023-10-03 17:30:55'),(14,'Supernatural Spray','COLOR WOW Dream Coat Supernatural Spray – Multi award winning anti frizz spray keeps hair frizz free for days no matter the weather with moisture repellant anti humidity technology; glass hair results',28,4,'2023-10-03 17:32:15','2023-10-03 17:32:15'),(15,'Mouthwash','Listerine Mouthwash, Antiseptic Antibacterial Bad Breath Treatment Plaque & Gingivitis Protection, Gum Disease Treatment Mouth Wash for Adults Cool Mint Flavor 1 L (Pack of 2)',10,4,'2023-10-03 17:33:58','2023-10-03 17:33:58'),(16,'Coconut Oil','Lottabody Coconut Oil and Shea Wrap Me Foaming Curl Mousse Creates Soft Wraps Hair Mousse for Curly Hair Defines Curls  Anti Friz 7 Fl Oz',3,4,'2023-10-03 17:34:58','2023-10-03 17:34:58');
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sales`
--

DROP TABLE IF EXISTS `sales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sales` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `product_id` int(11) DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL,
  `sale_date` datetime DEFAULT NULL,
  `revenue` float DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `product_id` (`product_id`),
  KEY `ix_sales_id` (`id`),
  CONSTRAINT `sales_ibfk_1` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sales`
--

LOCK TABLES `sales` WRITE;
/*!40000 ALTER TABLE `sales` DISABLE KEYS */;
INSERT INTO `sales` VALUES (1,1,2,'2022-10-03 17:07:26',18),(2,16,1,'2022-01-01 13:22:14',3),(3,4,2,'2022-01-01 13:23:11',42),(4,6,5,'2022-01-04 19:04:43',150),(5,16,1,'2022-01-15 11:07:22',3),(6,1,1,'2022-01-16 10:23:16',9),(7,1,3,'2022-01-19 09:55:49',27),(8,4,4,'2022-02-02 11:07:42',84),(9,4,1,'2022-02-02 13:01:11',21),(10,4,2,'2022-02-04 13:09:42',42),(11,10,2,'2022-02-06 13:15:56',100),(12,1,3,'2022-02-06 10:01:19',27),(13,9,6,'2022-02-23 06:01:21',138),(14,9,1,'2022-02-24 08:07:26',23),(15,13,2,'2022-02-24 09:09:53',34),(16,2,4,'2022-03-01 09:19:22',44),(17,4,3,'2022-03-02 23:09:53',84),(18,5,1,'2022-03-03 15:02:26',19),(19,3,1,'2022-03-04 20:23:26',21),(20,6,2,'2022-05-15 22:19:52',60),(21,2,3,'2022-06-16 12:14:51',33),(22,8,5,'2022-06-04 22:18:45',45),(23,3,2,'2022-09-03 22:02:26',42),(24,2,1,'2022-12-03 11:44:36',11),(25,8,2,'2023-01-01 11:11:11',18),(26,9,2,'2023-01-01 12:09:31',46),(27,15,1,'2023-01-02 09:02:18',10),(28,1,4,'2023-01-04 17:11:42',36),(29,11,3,'2023-02-01 17:21:11',45),(30,4,1,'2023-02-04 18:01:21',21),(31,5,2,'2023-04-05 19:55:33',38),(32,1,2,'2023-07-07 21:02:26',18),(33,13,1,'2023-09-02 19:02:26',17),(34,4,4,'2023-09-03 15:11:55',84),(35,11,2,'2023-09-04 09:07:42',30);
/*!40000 ALTER TABLE `sales` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-10-03 18:56:33
