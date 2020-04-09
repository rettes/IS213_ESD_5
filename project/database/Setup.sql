create database if not exists account_service;
use account_service;

drop table if exists account;

CREATE TABLE account (
    customerID INT AUTO_INCREMENT,
    username VARCHAR(128) NOT NULL UNIQUE,
    name VARCHAR(128) NOT NULL,
    password VARCHAR(128) NOT NULL,
    customer_email VARCHAR(128) NOT NULL UNIQUE,
    PRIMARY KEY (customerID)
);
INSERT INTO `account` (`customerID`, `username`, `name`, `password`, `customer_email`) 
VALUES 
('1', 'jeremyong', 'Jeremy Ong', 'password', 'jeremy@gmail.com');

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
('1', 'sally@gmail.com', 'Sally Lam', 'Female', '24', 'English', 'Secondary', '1', 'I am Sally! I teaches English for Secondary school kids.', '20', 'images/tutor/image4.jpg'),
('2', 'johnteo@gmail.com', 'John Teo', 'Male', '29', 'Science', 'Primary', '2', 'I am John! I teaches Science for primary school kids.', '20', 'images/tutor/image1.jpg'),
('3', 'benny@gmail.com', 'Benny Lim', 'Male', '21', 'Chinese', 'JuniorCollege', '3', 'I am Benny! I teaches Chinese for JC.', '30', 'images/tutor/image10.png'),
('4', 'derrick@gmail.com', 'Derrick Lim', 'Male', '24', 'Chinese', 'JuniorCollege', '1', 'I am Derrick! I teaches Chinese for JC.', '30', 'images/tutor/image3.jpg'),
('5', 'jasmine@gmail.com', 'Kenneth Liew', 'Male', '27', 'Math', 'JuniorCollege', '2', 'I am Kenneth liew! I teaches Math for JC.', '30', '	
images/tutor/image9.jpg'),
('6', 'alex@gmail.com', 'Alex Tan', 'Male', '31', 'Chinese', 'JuniorCollege', '2', 'I am Alex! I teaches Chinese for JC.', '70', 'images/tutor/image11.jpg'),
('7', 'nurulliza@gmail.com', 'Nurul Liza', 'Female', '21', 'English', 'JuniorCollege', '1', 'I am Nurul! I teaches English for JC.', '30', 'images/tutor/image7.jpeg'),
('8', 'grace@gmail.com', 'Grace Loh', 'Female', '28', 'English', 'Secondary', '4', 'I am Grace! I teaches English for JC.', '60', 'images/tutor/image13.jpg'),
('9', 'hazel@gmail.com', 'Hazel Goh', 'Female', '23', 'Chinese', 'Primary', '1', 'I am Hazel! I teaches Chinese for Primary.', '30', 'images/tutor/image6.jpg'),
('10', 'may@gmail.com', 'May Lim', 'Female', '25', 'Science', 'JuniorCollege', '5', 'I am May! I teaches Science for JC.', '30', 'images/tutor/image5.jpg'),
('11', 'mary@gmail.com', 'Mary Sim', 'Female', '27', 'English', 'Secondary', '8', 'I am Mary! I teaches English for Secondary.', '50', 'images/tutor/image8.jpg'),
('12', 'jenny@gmail.com', 'Jenny Lim', 'Female', '29', 'Science', 'Primary', '11', 'I am Jenny! I teaches Science for Primary.', '40', 'images/tutor/image12.jpg');
