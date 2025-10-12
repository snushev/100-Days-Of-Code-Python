# 🐍 Python Projects Collection

Welcome to my collection of **Python projects** — a mix of console apps, GUI tools, web applications, games, and automation scripts.  
Each project helped me strengthen my understanding of **Python fundamentals, OOP, APIs, and problem solving**. 🚀  

---

## 📖 About This Repository
This repository documents my journey through 100 Days of Code with Python, featuring diverse projects that demonstrate:

- ### 🤖 Web Scraping & Automation - Beautiful Soup, Selenium, data extraction
- ### 🌐 API Integration - REST APIs, external services, data processing
- ### 🎮 Console & Turtle Games - Classic arcade games with Python graphics
- ### 🖼️ Tkinter GUI Applications - Desktop apps for productivity and learning
- ### 🌍 Flask Web Applications - Full-stack web apps with databases and authentication
- ### 📧 Notification Systems - Email, SMS, and messaging automation

Each project demonstrates practical programming concepts, clean code practices, and real-world problem-solving skills.

## 🤖 Web Scraping & Automation
### 🛒 Amazon Price Tracker
Automated price monitoring tool that sends email alerts when prices drop
Tech: Python, Requests, Beautiful Soup, SMTP, dotenv
Key Features:
Real-time price monitoring
Automated email alerts
User-agent rotation
Secure credential management


### 🍪 Cookie Clicker Bot
Selenium automation bot for the Cookie Clicker game
Tech: Python, Selenium WebDriver
Features:
Auto-clicker functionality
Smart upgrade algorithm (buys most expensive affordable item)
Time-based gameplay limits
Real-time performance tracking


### 📊 Data Entry Automation
Automates data entry from Zillow clone to Google Forms
Tech: Python, Selenium, Beautiful Soup, Requests
Workflow:
Scrapes property data from Zillow clone
Extracts addresses, prices, and URLs
Automatically fills Google Form
Submits multiple entries in sequence


### 🎵 Spotify Playlist Time Machine
Creates Spotify playlists from Billboard Hot 100 charts
Tech: Python, Beautiful Soup, Spotipy, Spotify OAuth
Features:
Date-based Billboard chart scraping
Spotify API authentication
Automatic song matching by year
Error handling for missing songs
Private playlist creation


### 🎬 100 Movies to Watch
Web scraper for Empire's "Best Movies" list
Tech: Python, Beautiful Soup, Requests

## 📡 API Integration Projects
### 📈 Habit Tracker (Pixela)
Console app for tracking daily habits using Pixela API
Tech: Python, Requests, Pixela API, Datetime

API Operations:

- POST - User registration, graph creation, pixel addition
- GET - Retrieve user info and graphs
- PUT - Update pixel values
- DELETE - Remove pixel entries


### 📰 Stock News Alert
Monitors stock prices and sends news via SMS
Tech: Python, Requests, Twilio API, Alpha Vantage, NewsAPI


### 🏋️ Workout Tracker
Logs exercises to Google Sheets via Nutritionix and Sheety APIs
Tech: Python, Requests, Nutritionix API, Sheety API



### ✈️ Flight Deal Finder
Comprehensive flight search and alert system
Tech: Python, Requests, Amadeus API, Sheety API, Twilio, SMTP, dotenv

### 🛸 ISS Overhead Notifier
Sends email when ISS is visible overhead
Tech: Python, Requests, SMTP, Datetime
Logic:

Checks if ISS is within 5° of your coordinates
Verifies it's nighttime at your location
Sends "Look up!" email when both conditions met


### 🌧️ Rain Alert
Weather-based SMS notification system
Tech: Python, Requests, OpenWeatherMap API, Twilio

## 🎮 Console Projects

### 🪨 Rock–Paper–Scissors  
A classic console game with colorful output using ANSI escape codes.  
Keeps track of scores and allows continuous play.

### 🔡 NATO Phonetic Alphabet  
Converts any entered word into its NATO phonetic alphabet equivalent (e.g., HELLO → Hotel Echo Lima Lima Oscar).  
Includes input validation and error handling using **pandas**.

---

## 🧩 Tkinter GUI Applications

### 🌍 Flashy (Flash Card App)  
A French–English flashcard learning app that flips cards after 3 seconds.  
Remembers unknown words in a `words_to_learn.csv` file for future sessions.  
🧠 *Built with:* `pandas`, `tkinter`

### 📏 Mile to Km Converter  
Simple GUI app for converting miles to kilometers.  
Demonstrates basic widgets, user input, and dynamic output.

### 🍅 Pomodoro Timer  
A productivity timer app based on the Pomodoro technique.  
Includes visual countdown, checkmarks for completed sessions, and an optional sound alert.  
🧠 *Built with:* `tkinter`, `time`, `winsound`

### 🔐 Password Manager  
A secure password manager with password generator, local JSON storage, and clipboard copy.  
Features include search functionality and clean Tkinter interface.  
🧠 *Built with:* `tkinter`, `json`, `pyperclip`

### ❓ Quizzler (Quiz App)  
Interactive True/False quiz app fetching live questions from the **Open Trivia Database API**.  
Features real-time feedback, score tracking, and modular code architecture.  
🧠 *Built with:* `requests`, `tkinter`, `OOP`

---

## 🐢 Turtle Graphics Projects

### 🇺🇸 U.S. States Game  
Educational guessing game where users identify U.S. states on a map.  
Displays correct guesses and saves missing ones to `states_to_learn.csv`.  
🧠 *Built with:* `turtle`, `pandas`

### 🏓 Pong Game  
Classic Pong arcade game built with the Turtle module.  
Includes paddle control, scoring system, and collision detection.

### 🐍 Snake Game  
Modern recreation of the Snake game using OOP principles.  
Tracks score, handles collisions, and offers replay functionality.

### 🛣️ Turtle Crossing  
A fun arcade-style game where the player controls a turtle trying to cross a busy road.  
Features dynamic difficulty and object-oriented design.

---

## 🌐 Flask Web Applications

### 📝 Flask Blog  
A full-featured blog app with user registration, authentication, CKEditor integration, and comments.  
Includes admin-only controls, Gravatar avatars, and Bootstrap 5 styling.  
🧠 *Built with:* `Flask`, `Flask-Login`, `SQLAlchemy`, `Bootstrap`

### ☕ Cafés & Wi-Fi  
Form-based web app to add and browse cafés by Wi-Fi speed, socket availability, and coffee rating.  
Data stored in CSV format.  
🧠 *Built with:* `Flask`, `Flask-WTF`

### 🔐 Flask Auth System  
Simple authentication system implementing registration, login, password hashing, and protected routes.  
🧠 *Built with:* `Flask`, `Werkzeug`, `Flask-Login`

### 🎯 Higher-Lower Game  
Flask-based number guessing game using dynamic URL routing.

### 📚 Flask Library App  
CRUD application for managing a book collection using SQLite and SQLAlchemy.

### ☕ Café REST API  
RESTful API for café management.  
Includes endpoints for GET, POST, PATCH, DELETE with JSON responses and API key validation.

### 🎬 Top Movies App  
Integrates with The Movie Database (TMDb) API to add, rate, and review favorite movies.  
🧠 *Built with:* `Flask`, `requests`, `WTForms`, `Bootstrap`

---




---

## 🧰 Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-FFD43B?style=for-the-badge)
![Turtle](https://img.shields.io/badge/Turtle-0A66C2?style=for-the-badge)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Requests](https://img.shields.io/badge/Requests-000000?style=for-the-badge)
![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-4B8BBE?style=for-the-badge)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05033?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)

---

## 📫 Contact

📧 **Email:** s.nushev@gmail.com  
💼 **LinkedIn:** [linkedin.com/in/simeon-nushev-82b56597](https://www.linkedin.com/in/simeon-nushev-82b56597/)  

---

⭐ *“Keep coding, stay curious, and never stop improving.”*
