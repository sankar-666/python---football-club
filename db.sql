/*
SQLyog Ultimate v11.11 (64 bit)
MySQL - 5.5.5-10.3.20-MariaDB : Database - football_club
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`football_club` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `football_club`;

/*Table structure for table `banned` */

DROP TABLE IF EXISTS `banned`;

CREATE TABLE `banned` (
  `ban_id` int(11) NOT NULL,
  `player_id` int(11) DEFAULT NULL,
  `reason` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`ban_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `banned` */

/*Table structure for table `club` */

DROP TABLE IF EXISTS `club`;

CREATE TABLE `club` (
  `club_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `club` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`club_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `club` */

/*Table structure for table `coach` */

DROP TABLE IF EXISTS `coach`;

CREATE TABLE `coach` (
  `coach_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `fname` varchar(100) DEFAULT NULL,
  `lname` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`coach_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `coach` */

/*Table structure for table `complaint` */

DROP TABLE IF EXISTS `complaint`;

CREATE TABLE `complaint` (
  `complaint_id` int(11) NOT NULL AUTO_INCREMENT,
  `complaint` varchar(100) DEFAULT NULL,
  `reply` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `sender_id` int(11) DEFAULT NULL,
  `sended_by` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`complaint_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `complaint` */

/*Table structure for table `consultation` */

DROP TABLE IF EXISTS `consultation`;

CREATE TABLE `consultation` (
  `consultation_id` int(11) NOT NULL AUTO_INCREMENT,
  `psysician_id` int(11) DEFAULT NULL,
  `consulted` varchar(100) DEFAULT NULL,
  `details` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`consultation_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `consultation` */

/*Table structure for table `enquiry` */

DROP TABLE IF EXISTS `enquiry`;

CREATE TABLE `enquiry` (
  `enquiry_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `enquiry` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`enquiry_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `enquiry` */

/*Table structure for table `fixture` */

DROP TABLE IF EXISTS `fixture`;

CREATE TABLE `fixture` (
  `fixture_id` int(11) NOT NULL AUTO_INCREMENT,
  `fixture` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`fixture_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `fixture` */

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `usertype` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `login` */

/*Table structure for table `message` */

DROP TABLE IF EXISTS `message`;

CREATE TABLE `message` (
  `message_id` int(11) NOT NULL AUTO_INCREMENT,
  `sender_id` int(11) DEFAULT NULL,
  `receiver_id` int(11) DEFAULT NULL,
  `message` varchar(200) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`message_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `message` */

/*Table structure for table `news` */

DROP TABLE IF EXISTS `news`;

CREATE TABLE `news` (
  `news_id` int(11) NOT NULL AUTO_INCREMENT,
  `news` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`news_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `news` */

/*Table structure for table `nutretion` */

DROP TABLE IF EXISTS `nutretion`;

CREATE TABLE `nutretion` (
  `nutretion_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `fname` varchar(100) DEFAULT NULL,
  `lname` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`nutretion_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `nutretion` */

/*Table structure for table `player` */

DROP TABLE IF EXISTS `player`;

CREATE TABLE `player` (
  `player_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `fname` varchar(100) DEFAULT NULL,
  `lname` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`player_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `player` */

/*Table structure for table `psysician` */

DROP TABLE IF EXISTS `psysician`;

CREATE TABLE `psysician` (
  `psysician_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `psysician` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`psysician_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `psysician` */

/*Table structure for table `rank` */

DROP TABLE IF EXISTS `rank`;

CREATE TABLE `rank` (
  `rank_id` int(11) NOT NULL AUTO_INCREMENT,
  `player_id` int(11) DEFAULT NULL,
  `rank` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`rank_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `rank` */

/*Table structure for table `rgistration` */

DROP TABLE IF EXISTS `rgistration`;

CREATE TABLE `rgistration` (
  `registration_id` int(11) NOT NULL AUTO_INCREMENT,
  `club_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `todate` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`registration_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `rgistration` */

/*Table structure for table `selection` */

DROP TABLE IF EXISTS `selection`;

CREATE TABLE `selection` (
  `selection_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `club_id` int(11) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`selection_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `selection` */

/*Table structure for table `selection_list` */

DROP TABLE IF EXISTS `selection_list`;

CREATE TABLE `selection_list` (
  `selection_id` int(11) NOT NULL AUTO_INCREMENT,
  `player_id` int(11) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`selection_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `selection_list` */

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `fname` varchar(100) DEFAULT NULL,
  `lname` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `user` */

/*Table structure for table `video` */

DROP TABLE IF EXISTS `video`;

CREATE TABLE `video` (
  `video_id` int(11) NOT NULL AUTO_INCREMENT,
  `video` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`video_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `video` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
