# CS50_Final_Project
Catch any new words recently? Well, using this personal dictionary web application based on
a Flask framework, you can use it to store any words you want to keep close to enhance your vocabulary.


## Table of Contents
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)
- [Installation](#installation)
- [Description](#Description)
- [Contact](#contact)


## Project Structure
  ```sh
  ├── README.md
  ├── app.py
  ├── config.py
  ├── data.db
  ├── static
  │   ├── book-left.png
  │   ├── book-right.png
  │   ├── error.png
  │   ├── favicon.ico
  │   ├── styles.css
  │   └── words.png
  ├── templates
  │   ├── apology.html
  │   ├── index.html
  │   ├── layout.html
  │   ├── login.html
  │   └── register.html
  ├── application.py
  ├── helpers.py
  └── words_storage.db
  ```


## Installation
* Open https://ide.cs50.io/
* Download the files and upload the repository onto the CS50 IDE
* In the terminal, run "cd Dictocatch" then "flask run"
* Click the link to be redirected to my final project!


## Description
My final project for CS50 is a web application using Flask, Python and SQL (along with Sqllite3) based in part on the web track's distribution code. The application is called "Dictocatch" and it is used as a personal dictionary for users so they can store any words and their definitions they find interesting. The personal list of words is only available to each individual with an account, so they must register if they are new. The system is also secure since all the passwords are used with SHA-256 and double-entry password during registration.


## Contact
[Email](mailto:2sagarpatel2@gmail.com) | [Website](https://sagarpatel211.github.io/)
