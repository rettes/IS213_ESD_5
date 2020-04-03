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
    image VARCHAR(128) NOT NULL,
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

INSERT INTO `tutor` (`tutorID`, `tutor_email`, `name`, `sex`, `age`, `subject`, `level`, `experience`, `about`, `rates`, `image`) 
VALUES 
('1', 'sally@gmail.com', 'Sally Lam', 'Female', '24', 'English', 'Secondary', '1', 'I am Sally! I teaches English for Secondary school kids.', '20', 'image'),
('2', 'johnteo@gmail.com', 'John Teo', 'Male', '29', 'Science', 'Primary', '2', 'I am John! I teaches Science for primary school kids.', '20', 'image'),
('3', 'benny@gmail.com', 'Benny Lim', 'Male', '21', 'Chinese', 'JuniorCollege', '3', 'I am Benny! I teaches Chinese for JC.', '30', 'image'),
('4', 'derrick@gmail.com', 'Derrick Lim', 'Male', '24', 'Chinese', 'JuniorCollege', '1', 'I am Derrick! I teaches Chinese for JC.', '30', 'image'),
('5', 'jasmine@gmail.com', 'Jasmine Ong', 'Male', '27', 'Math', 'JuniorCollege', '2', 'I am Jasmine! I teaches Math for JC.', '30', 'image'),
('6', 'alex@gmail.com', 'Alex Tan', 'Male', '31', 'Chinese', 'JuniorCollege', '2', 'I am Alex! I teaches Chinese for JC.', '70', 'image'),
('7', 'ken@gmail.com', 'Ken Ong', 'Male', '32', 'Math', 'Secondary', '3', 'I am Ken! I teaches Math for Secondary.', '30', 'image'),
('8', 'nurulliza@gmail.com', 'Nurul Liza', 'Female', '21', 'English', 'JuniorCollege', '1', 'I am Nurul! I teaches English for JC.', '30', 'image'),
('9', 'rose@gmail.com', 'Rose Yu', 'Male', '26', 'Math', 'JuniorCollege', '5', 'I am Rose! I teaches Math for JC.', '30', 'image'),
('10', 'grace@gmail.com', 'Grace Loh', 'Female', '28', 'English', 'Secondary', '4', 'I am Grace! I teaches English for JC.', '60', 'image'),
('11', 'hazel@gmail.com', 'Hazel Goh', 'Female', '23', 'Chinese', 'Primary', '1', 'I am Hazel! I teaches Chinese for Primary.', '30', 'image'),
('12', 'melvin@gmail.com', 'Melvin Tan', 'Male', '22', 'Math', 'JuniorCollege', '3', 'I am Melvin! I teaches Math for JC.', '60', 'image'),
('13', 'benedict@gmail.com', 'Benedict Wee', 'Male', '33', 'Science', 'Secondary', '10', 'I am Benedict! I teaches Science for Secondary.', '30', 'image'),
('14', 'kenneth@gmail.com', 'Kenneth Woi', 'Male', '22', 'Chinese', 'Secondary', '2', 'I am Kenneth! I teaches Chinese for Secondary.', '30', 'image'),
('15', 'wyane@gmail.com', 'Wyane Lim', 'Male', '21', 'Math', 'Primary', '1', 'I am Wyane! I teaches Math for Primary.', '30', 'image'),
('16', 'richard@gmail.com', 'Richard Kim', 'Male', '26', 'English', 'JuniorCollege', '1', 'I am Richard! I teaches English for JC.', '30', 'image'),
('17', 'may@gmail.com', 'May Lim', 'Female', '25', 'Science', 'JuniorCollege', '5', 'I am May! I teaches Science for JC.', '30', 'image'),
('18', 'mary@gmail.com', 'Mary Sim', 'Female', '27', 'English', 'Secondary', '8', 'I am Mary! I teaches English for Secondary.', '50', 'image'),
('19', 'jenny@gmail.com', 'Jenny Lim', 'Female', '29', 'Science', 'Primary', '11', 'I am Jenny! I teaches Science for Primary.', '40', 'image');
