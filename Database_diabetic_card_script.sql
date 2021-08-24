CREATE DATABASE Diabetic_Card;

show databases;

USE diabetic_card;

CREATE TABLE Hospital(
          HospitalId int not null auto_increment,
          DeptofEndocrinology varchar(55) not null,
          DeptofMedicine varchar(55) not null,
          DeptofRadiology varchar(55) not null,
          DeptofPathology varchar(55) not null,
          PRIMARY KEY (HospitalId));

CREATE TABLE DoctorInfo(
          DoctorId int not null auto_increment,
          DoctorName varchar(55) not null,
          DoctorAddress varchar(200) not null,
          DoctorContactNo varchar(20) not null,
          HospitalId int not null,
          PRIMARY KEY (DoctorId),
          FOREIGN KEY (HospitalId) REFERENCES Hospital(HospitalId));

CREATE TABLE Cardholder(
          CardholderId int not null auto_increment,
          CardholderName varchar(55) not null,
          CardholderAge int not null,
          ContactNo varchar(20) not null,
          EmergencyContactDetails varchar(200) not null,
          HospitalId int not null,
          PRIMARY KEY (CardholderId),
          FOREIGN KEY (HospitalId) REFERENCES Hospital(HospitalId));

 CREATE TABLE PharmacyInfo(
          PharmacyId int not null auto_increment,
         PharmacyName varchar(100) not null,
          PharmacyContactNo varchar(55) not null,
          CardholderId int not null,
          PRIMARY KEY (PharmacyId),
         FOREIGN KEY (CardholderId) REFERENCES Cardholder(CardholderId));

CREATE TABLE DiabeticMedicine(
          DiabeticMedicineId int not null auto_increment,
          DrugName varchar(100) not null,
          Dosage varchar(100) not null,
          SideEffects varchar(255),
          DrugRegimen varchar(55) not null,
          Instruction varchar(255),
          CardholderId int not null,
          PRIMARY KEY (DiabeticMedicineId),
          FOREIGN KEY (CardholderId) REFERENCES Cardholder(CardholderId));

CREATE TABLE RbsRecord(
          RbsRecordId int not null auto_increment,
          Date date not null,
          Time time not null,
          NormalRange varchar(100) not null,
          CardholderId int not null,
          PRIMARY KEY (RbsRecordId),
          FOREIGN KEY (CardholderId) REFERENCES Cardholder(CardholderId));

CREATE TABLE MedicalHistory(
          MedicalHistoryId int not null auto_increment,
          CardiovascularDisease varchar(55) not null ,
          NeuralDisease varchar(55) not null,
          RenalDisease varchar(55) not null,
          Allergies varchar(55) not null,
          CardholderId int not null,
          PRIMARY KEY (MedicalHistoryId),
          FOREIGN KEY (CardholderId) REFERENCES Cardholder(CardholderId));
