-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema capstone_DB
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `capstone_DB` ;

-- -----------------------------------------------------
-- Schema capstone_DB
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `capstone_DB` DEFAULT CHARACTER SET latin1 ;
USE `capstone_DB` ;

-- -----------------------------------------------------
-- Table `ICD_9`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `ICD_9` ;

CREATE TABLE IF NOT EXISTS `ICD_9` (
  `index` INT(11) NOT NULL,
  `code` VARCHAR(45) NULL DEFAULT NULL)
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `code_edges`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `code_edges` ;

CREATE TABLE IF NOT EXISTS `code_edges` (
  `index` INT(11) NOT NULL,
  `code` VARCHAR(45) NOT NULL,
  `edge` VARCHAR(120) NOT NULL)
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `code_names`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `code_names` ;

CREATE TABLE IF NOT EXISTS `code_names` (
  `index` INT(11) NOT NULL,
  `code` VARCHAR(45) NOT NULL,
  `name` MEDIUMTEXT NOT NULL)
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `patient_dicts`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `patient_dicts` ;

CREATE TABLE IF NOT EXISTS `patient_dicts` (
  `index` INT(11) NOT NULL,
  `dict` LONGTEXT NULL DEFAULT NULL,
  PRIMARY KEY (`index`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `visit`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `visit` ;

CREATE TABLE IF NOT EXISTS `visit` (
  `index` INT(11) NOT NULL,
  `primary_ICD_9` VARCHAR(45) NULL DEFAULT NULL,
  `note_type` VARCHAR(45) NULL DEFAULT NULL,
  `chief_complaint` VARCHAR(120) NULL DEFAULT NULL,
  `note_text` LONGTEXT NULL DEFAULT NULL,
  `date` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`index`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `word_indexes`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `word_indexes` ;

CREATE TABLE IF NOT EXISTS `word_indexes` (
  `word` VARCHAR(120) NOT NULL,
  `index` MEDIUMTEXT NULL DEFAULT NULL,
  PRIMARY KEY (`word`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;