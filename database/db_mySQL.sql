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
  `index` VARCHAR(120) NOT NULL,
  `code` VARCHAR(45) NULL DEFAULT NULL)
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `visit`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `visit` ;

CREATE TABLE IF NOT EXISTS `visit` (
  `index` VARCHAR(120) NOT NULL,
  `primary_ICD_9` VARCHAR(45) NULL DEFAULT NULL,
  `note_type` VARCHAR(45) NULL DEFAULT NULL,
  `chief_complaint` VARCHAR(120) NULL DEFAULT NULL,
  `note_text` LONGTEXT NULL DEFAULT NULL,
  `date` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`index`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `patient`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `patient` ;

CREATE TABLE IF NOT EXISTS `patient` (
  `index` VARCHAR(120) NOT NULL,
  `firstName` VARCHAR(120) NULL DEFAULT NULL,
  `lastName` VARCHAR(120) NULL DEFAULT NULL,
  `DOB` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`index`),
  CONSTRAINT `index_FK`
    FOREIGN KEY (`index`)
    REFERENCES `visit` (`index`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;