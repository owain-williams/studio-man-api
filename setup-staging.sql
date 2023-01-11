CREATE DATABASE `studioman-staging`;

USE `studioman-staging`;

CREATE TABLE `Studio` (
    `StudioID` int AUTO_INCREMENT NOT NULL,
    `AuthenticationID` int ,
    `Name` VARCHAR(255) NOT NULL,
    `Rooms` int  ,
    `Engineers` int ,
    `Assets` int ,
    `LogoURL` VARCHAR(255)  NOT NULL ,
    PRIMARY KEY (
        `StudioID`
    )
);

CREATE TABLE `Engineers` (
    `EngineerID` int AUTO_INCREMENT NOT NULL ,
    `FirstName` VARCHAR(255)  NOT NULL ,
    `LastName` VARCHAR(255)  NOT NULL ,
    `Rate` decimal(5,2) ,
    PRIMARY KEY (
        `EngineerID`
    )
);

CREATE TABLE `Rooms` (
    `RoomID` int AUTO_INCREMENT NOT NULL ,
    `Name` VARCHAR(255)  NOT NULL ,
    `Assets` int ,
    `Rate` decimal(5,2) ,
    PRIMARY KEY (
        `RoomID`
    )
);

CREATE TABLE `Assets` (
    `AssetID` int AUTO_INCREMENT NOT NULL ,
    `Name` VARCHAR(255) NOT NULL ,
    PRIMARY KEY (
        `AssetID`
    )
); 

CREATE TABLE `Clients` (
    `ClientID` int AUTO_INCREMENT NOT NULL ,
    `ContactFirstName` VARCHAR(255)  NOT NULL ,
    `ContactLastName` VARCHAR(255)  NOT NULL ,
    `PaymentMethods` int ,
    PRIMARY KEY (
        `ClientID`
    )
);

CREATE TABLE `PaymentMethods` (
    `PaymentMethodID` int AUTO_INCREMENT NOT NULL ,
    PRIMARY KEY (
        `PaymentMethodID`
    )
);

CREATE TABLE `Bookings` (
    `BookingID` int AUTO_INCREMENT NOT NULL ,
    `Client` int  NOT NULL ,
    `Room` int  NOT NULL ,
    `Engineers` int ,
    `DaySessions` int ,
    `InitialCost` decimal(5,2)  NOT NULL ,
    `DiscountAmount` decimal(5,2) ,
    `ActualCost` decimal(5,2)  NOT NULL ,
    `Paid` boolean  NOT NULL ,
    `PaidDate` dateTime  ,
    `Cancelled` boolean  NOT NULL ,
    PRIMARY KEY (
        `BookingID`
    )
);

CREATE TABLE `DaySessions` (
    `DaySessionID` int AUTO_INCREMENT NOT NULL ,
    `StartTime` dateTime  NOT NULL ,
    `EndTime` dateTime  NOT NULL ,
    `Minutes` int  NOT NULL ,
    PRIMARY KEY (
        `DaySessionID`
    )
);

ALTER TABLE `Studio` ADD CONSTRAINT `fk_Studio_Rooms` FOREIGN KEY(`Rooms`)
REFERENCES `Rooms` (`RoomID`);

ALTER TABLE `Studio` ADD CONSTRAINT `fk_Studio_Engineers` FOREIGN KEY(`Engineers`)
REFERENCES `Engineers` (`EngineerID`);

ALTER TABLE `Studio` ADD CONSTRAINT `fk_Studio_Assets` FOREIGN KEY(`Assets`)
REFERENCES `Assets` (`AssetID`);

ALTER TABLE `Rooms` ADD CONSTRAINT `fk_Rooms_Assets` FOREIGN KEY(`Assets`)
REFERENCES `Assets` (`AssetID`);

ALTER TABLE `Clients` ADD CONSTRAINT `fk_Client_PaymentMethods` FOREIGN KEY(`PaymentMethods`)
REFERENCES `PaymentMethods` (`PaymentMethodID`);

ALTER TABLE `Bookings` ADD CONSTRAINT `fk_Bookings_Client` FOREIGN KEY(`Client`)
REFERENCES `Clients` (`ClientID`);

ALTER TABLE `Bookings` ADD CONSTRAINT `fk_Bookings_Room` FOREIGN KEY(`Room`)
REFERENCES `Rooms` (`RoomID`);

ALTER TABLE `Bookings` ADD CONSTRAINT `fk_Bookings_Engineers` FOREIGN KEY(`Engineers`)
REFERENCES `Engineers` (`EngineerID`);

ALTER TABLE `Bookings` ADD CONSTRAINT `fk_Bookings_DaySessions` FOREIGN KEY(`DaySessions`)
REFERENCES `DaySessions` (`DaySessionID`);

CREATE INDEX `idx_Studio_Name`
ON `Studio` (`Name`);

CREATE INDEX `idx_Rooms_Name`
ON `Rooms` (`Name`);

CREATE INDEX `idx_Assets_Name`
ON `Assets` (`Name`);
