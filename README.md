# Ghana Card Mangement System

![Ghana_Card_Managment_System](/ReadmeImages/card.png)

The Ghana Card Management System is a user-friendly platform that helps individuals easily track and recover lost Ghana Cards. It allows users to upload details of found cards, which are securely stored in a database. Anyone who has lost their card can search the system in real-time to check if it has been found and recorded. The system simplifies the recovery process, ensuring that important personal information is easily accessible and not lost forever. It offers a secure, efficient solution for card recovery, providing peace of mind to users.


## Key Features
#### 1. Card Details Upload
Users can upload information about found cards, including the cardholder's name, ID number, citizenship, and more.

#### 2. Card Search
Individuals can search the database using their details eg: last name to determine if their card has been found and logged.

#### 3. Secure Database
All card information is securely stored in a centralized database, ensuring privacy and data integrity.

#### 4. Real-Time Updates
As soon as a card is uploaded, it becomes instantly available for anyone searching for it.

#### 5. User-friendly frontend
With the provision of a frontend, individuals can explore the entry and search points to upload a card detail or to check if their card has been found

## Project Structure
This project consists of :

**Database & Backend**
- This is the folder that holds the main application.
- It holds a database script that is used to only create the database
- It holds the crud opearations that is contained in the models python file
- It holds the main flask application called the server python file and a blueprint file calle datails_blueprint
- It holds the FrontEnd folder


**FrontEnd**
- This holds all files related to the frontend eg: html/css/js files. 
- The frontend api that interacts with the backend api
- A template template folder that renders after the form has been submitted

## How Api Works
**server.py**
This api acts as the intermediary between the backend and the database.It uses a blueprint to manage the database.It specifically runs on port 5000.This is specified because the flask applications are two and two different flask applications cannot run on one port.


![server.py](/ReadmeImages/server.png)


**card_details_blueprint**
This manipulates the crud operations in the models file to impletement GET, POST and DELETE routes to 
retrieve and upload data on into the database.

![card_details](/ReadmeImages/card_details.png)

**app.py**
This api primarily focuses on interaction between the frontend and the backend database and becasue of this in any route, there would be a backend flask api url that is used for interaction between the frontend and the backend. This api sends whatever request that is specified through a form filling to the backend database.

![FrontendAPI](/ReadmeImages/frontendAPI.png)

## Database 
- My primary database is called Ghana_card that is creates using an sql script
- The table "person" is used to store all the tuples and records. 
- Tuple(column) this specifies the various fields in the tables. ie. The id which tracks the total number of cards recorded, the "first_name", "last_name" and "middle_name" that stores the name of the person, the "sex" of the person , "citizenship" which is the status of citizenship of the person and the "id_number" on the card.
- Record(rows) which represents any data or card information that will be entered

![database](/ReadmeImages/database.png)


## FrontEnd Implementation

## How To Use This repos

## Improvements

![Ghana_Card](/ReadmeImages/ghcard.png)