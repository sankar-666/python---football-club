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
  `ban_id` int(11) NOT NULL AUTO_INCREMENT,
  `player_id` int(11) DEFAULT NULL,
  `reason` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`ban_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `banned` */

insert  into `banned`(`ban_id`,`player_id`,`reason`) values (1,1,'bad');

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
  `club_id` int(11) DEFAULT NULL,
  `fname` varchar(100) DEFAULT NULL,
  `lname` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `photo` varchar(1000) DEFAULT NULL,
  `dob` varchar(100) DEFAULT NULL,
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
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `complaint` */

insert  into `complaint`(`complaint_id`,`complaint`,`reply`,`date`,`sender_id`,`sended_by`) values (1,'worst piza ever','pending','2023-03-11',3,'nutritionaist'),(2,'oodra','pending','2023-03-11',10,'player');

/*Table structure for table `consultation` */

DROP TABLE IF EXISTS `consultation`;

CREATE TABLE `consultation` (
  `consultation_id` int(11) NOT NULL AUTO_INCREMENT,
  `psysician_id` int(11) DEFAULT NULL,
  `sender_id` int(11) DEFAULT NULL,
  `consulted` varchar(100) DEFAULT NULL,
  `details` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`consultation_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `consultation` */

insert  into `consultation`(`consultation_id`,`psysician_id`,`sender_id`,`consulted`,`details`) values (1,1,3,'bad','pending'),(2,1,10,'hello','pending');

/*Table structure for table `enquiry` */

DROP TABLE IF EXISTS `enquiry`;

CREATE TABLE `enquiry` (
  `enquiry_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `enquiry` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `photo` varchar(100) DEFAULT NULL,
  `dob` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`enquiry_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `enquiry` */

insert  into `enquiry`(`enquiry_id`,`login_id`,`enquiry`,`phone`,`email`,`photo`,`dob`) values (1,2,'John ','9846354290','newcus@gmail.com',NULL,NULL);

/*Table structure for table `fixture` */

DROP TABLE IF EXISTS `fixture`;

CREATE TABLE `fixture` (
  `fixture_id` int(11) NOT NULL AUTO_INCREMENT,
  `catg_id` int(11) DEFAULT NULL,
  `fixture` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `time` varchar(100) DEFAULT NULL,
  `team1` varchar(100) DEFAULT NULL,
  `team2` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`fixture_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `fixture` */

insert  into `fixture`(`fixture_id`,`catg_id`,`fixture`,`date`,`time`,`team1`,`team2`) values (2,4,'dakjsbndsajk','2023-03-25','11:41','North east','hydhrabad'),(3,4,' sunday','2023-03-24','11:36','Kerala....','bangluru fc');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `usertype` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`usertype`) values (1,'admin','admin','admin'),(2,'enq','enq','enquiryteam'),(3,'nutri','nutri','nutritionaist'),(10,'player','player','player');

/*Table structure for table `match_category` */

DROP TABLE IF EXISTS `match_category`;

CREATE TABLE `match_category` (
  `catg_id` int(11) NOT NULL AUTO_INCREMENT,
  `category` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`catg_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `match_category` */

insert  into `match_category`(`catg_id`,`category`) values (4,'ISL'),(2,'IWL'),(3,'Ileauge');

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
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `news` */

insert  into `news`(`news_id`,`news`) values (2,'hello');

/*Table structure for table `nutretion` */

DROP TABLE IF EXISTS `nutretion`;

CREATE TABLE `nutretion` (
  `nutretion_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `club_id` int(11) DEFAULT NULL,
  `fname` varchar(100) DEFAULT NULL,
  `lname` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `photo` varchar(100) DEFAULT NULL,
  `dob` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`nutretion_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `nutretion` */

insert  into `nutretion`(`nutretion_id`,`login_id`,`club_id`,`fname`,`lname`,`place`,`phone`,`email`,`photo`,`dob`) values (1,3,NULL,'san','kar','kochi','6238526459','safasfssfd@gmail.com',NULL,NULL);

/*Table structure for table `player` */

DROP TABLE IF EXISTS `player`;

CREATE TABLE `player` (
  `player_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `club_id` int(11) DEFAULT NULL,
  `fname` varchar(100) DEFAULT NULL,
  `lname` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `ref_id` int(11) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  `aadhar_no` varchar(100) DEFAULT NULL,
  `photo` varchar(100) DEFAULT NULL,
  `dob` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`player_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `player` */

insert  into `player`(`player_id`,`login_id`,`club_id`,`fname`,`lname`,`place`,`phone`,`email`,`ref_id`,`status`,`aadhar_no`,`photo`,`dob`) values (1,10,NULL,'san','kar','alpy','678687','dasj',NULL,NULL,NULL,NULL,NULL);

/*Table structure for table `practice` */

DROP TABLE IF EXISTS `practice`;

CREATE TABLE `practice` (
  `practice_id` int(11) NOT NULL AUTO_INCREMENT,
  `coach_id` int(11) DEFAULT NULL,
  `practice` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `time` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`practice_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `practice` */

/*Table structure for table `psysician` */

DROP TABLE IF EXISTS `psysician`;

CREATE TABLE `psysician` (
  `psysician_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `club_id` int(11) DEFAULT NULL,
  `psysician` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `photo` varchar(1000) DEFAULT NULL,
  `dob` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`psysician_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `psysician` */

insert  into `psysician`(`psysician_id`,`login_id`,`club_id`,`psysician`,`place`,`phone`,`email`,`photo`,`dob`) values (1,20,NULL,'suni','kottayam','78979','nbashjndsjh',NULL,NULL);

/*Table structure for table `rank` */

DROP TABLE IF EXISTS `rank`;

CREATE TABLE `rank` (
  `rank_id` int(11) NOT NULL AUTO_INCREMENT,
  `player_id` int(11) DEFAULT NULL,
  `rank` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`rank_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `rank` */

insert  into `rank`(`rank_id`,`player_id`,`rank`) values (1,1,'10');

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
  `club_id` int(11) DEFAULT NULL,
  `fname` varchar(100) DEFAULT NULL,
  `lname` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `aadhar_no` varchar(100) DEFAULT NULL,
  `photo` varchar(1000) DEFAULT NULL,
  `dob` varchar(100) DEFAULT NULL,
  `certificate` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `user` */

/*Table structure for table `video` */

DROP TABLE IF EXISTS `video`;

CREATE TABLE `video` (
  `video_id` int(11) NOT NULL AUTO_INCREMENT,
  `video` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`video_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `video` */

insert  into `video`(`video_id`,`video`) values (1,'static/uploads/87d0445c-d78a-44d1-a330-cca455915fc6WhatsApp Video 2022-11-14 at 11.09.34 AM.mp4');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
