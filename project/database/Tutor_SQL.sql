create database if not exists account_service;
use account_service;

drop table if exists account;

CREATE TABLE account (
    customerID INT NOT NULL AUTO_INCREMENT,
    username VARCHAR(128) NOT NULL UNIQUE,
    name VARCHAR(128) NOT NULL,
    password VARCHAR(128) NOT NULL,
    customer_email VARCHAR(128) NOT NULL UNIQUE,
    PRIMARY KEY (customerID)
);



create database if not exists tutor_service;
use tutor_service;

drop table if exists tutor;

CREATE TABLE tutor (
    tutorID INT NOT NULL AUTO_INCREMENT,
    tutor_email VARCHAR(128) NOT NULL UNIQUE,
    name VARCHAR(128) NOT NULL,
    sex VARCHAR(128) NOT NULL,
    age INT NOT NULL,
    subject VARCHAR(128) NOT NULL,
    level VARCHAR(128) NOT NULL,
    experience INT NOT NULL,
    about VARCHAR(1000) NOT NULL,
    rates INT NOT NULL,
    PRIMARY KEY (tutorID)
);



create database if not exists cart_service;
use cart_service;

drop table if exists cart;

CREATE TABLE cart (
    tutorID INT NOT NULL,
    customerID INT NOT NULL,
    subject VARCHAR(128) NOT NULL,
    level VARCHAR(128) NOT NULL,
    timeslot DATETIME NOT NULL,
    price FLOAT NOT NULL,
    PRIMARY KEY (tutorID, customerID, timeslot)
);



create database if not exists payment_service;
use payment_service;

drop table if exists payment_record;

CREATE TABLE payment_record (
    appointmentID INT NOT NULL AUTO_INCREMENT,
    tutorID INT NOT NULL,
    customerID INT NOT NULL,
    subject VARCHAR(128) NOT NULL,
    level VARCHAR(128) NOT NULL,
    timeslot DATETIME NOT NULL,
    price FLOAT NOT NULL,
    payment_date DATETIME NOT NULL,
    PRIMARY KEY (appointmentID)
);



create database if not exists appointment_service;
use appointment_service;

drop table if exists appointments;

CREATE TABLE appointments (
    appointmentID INT NOT NULL AUTO_INCREMENT,
    tutorID INT NOT NULL,
    customerID INT NOT NULL,
    subject VARCHAR(128) NOT NULL,
    level VARCHAR(128) NOT NULL,
    timeslot DATETIME NOT NULL,
    PRIMARY KEY (appointmentID)
);