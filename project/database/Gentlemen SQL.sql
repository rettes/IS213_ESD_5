create database if not exists customer_service;
use customer_service;

drop table if exists account;

CREATE TABLE account (
    username VARCHAR(128) NOT NULL,
    name VARCHAR(128) NOT NULL,
    password VARCHAR(128) NOT NULL,
    customer_email VARCHAR(128) NOT NULL UNIQUE,
    dob date NOT NULL,
    PRIMARY KEY (username)
);



create database if not exists gentlemen_service;
use gentlemen_service;

drop table if exists gentlemen;

CREATE TABLE gentlemen (
    gentlemenID INT NOT NULL AUTO_INCREMENT,
    gentlemen_email VARCHAR(128) NOT NULL UNIQUE,
    name VARCHAR(128) NOT NULL,
    age INT NOT NULL,
    height INT NOT NULL,
    race VARCHAR(128) NOT NULL,
    language VARCHAR(128) NOT NULL,
    about VARCHAR(1000) NOT NULL,
    rates INT NOT NULL,
    PRIMARY KEY (gentlemenID)
);



create database if not exists appointment_service;
use appointment_service;

drop table if exists gentlemen_apointment;

CREATE TABLE gentlemen_apointment (
    appointmentID INT NOT NULL AUTO_INCREMENT,
    gentlemenID VARCHAR(128) NOT NULL,
    username VARCHAR(128) NOT NULL,
    timeslot DATETIME NOT NULL,
    payment_status VARCHAR(128) NOT NULL,
    PRIMARY KEY (appointmentID)
);