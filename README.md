# University-Management-System-with-AI-Powered-Gemini-Chatbot
project:
  name: University Management System with Gemini API Chatbot
  repo_name: University-Management-System-Java
  description: >
    A full-featured University Management System built with Java Swing and MySQL,
    including secure login, student/faculty modules, and Gemini API-integrated chatbot support.

  technologies:
    - Java (Swing/AWT)
    - MySQL
    - JDBC
    - Gemini API
    - NetBeans or Eclipse

  author:
    name: Sree Shankari V
    role: Final Year B.Tech – Artificial Intelligence and Data Science
    college: Francis Xavier Engineering College, Tirunelveli
    linkedin: https://www.linkedin.com/in/sree-shankari-v-625a71258/
    github: https://github.com/shankari04

  license: MIT

  readme: |
    # University Management System with Gemini API Chatbot

    A full-featured Java Swing + MySQL desktop application designed to manage university operations efficiently.
    This system supports secure role-based login, student and faculty management, leave requests, exam result tracking, 
    fee management, and integrates an AI-powered chatbot using the Gemini API to assist users interactively.

    ## Key Features

    - Role-Based Login System (Admin, Faculty, Student)
    - Student Information Management
    - Faculty Information Management
    - Leave Application Tracking
    - Exam Result and Fee Management
    - Gemini API-Powered Chatbot for interactive guidance
    - MySQL Database integration with JDBC for persistent storage
    - User-Friendly GUI using Java Swing and AWT

    ## Tech Stack

    | Technology           | Description                         |
    |----------------------|-------------------------------------|
    | Java                 | GUI and core logic using Swing/AWT |
    | MySQL                | Relational database backend         |
    | JDBC                 | Java-Database Connectivity          |
    | Gemini API           | For chatbot integration             |
    | NetBeans / Eclipse   | Java IDEs used for development      |

    ## Project Structure

     University-Management-System  
    ├── src/  
    │   ├── login/                 - Role-based authentication  
    │   ├── admin/                 - Admin dashboard and CRUD  
    │   ├── student/               - Student dashboard, results, fees  
    │   ├── faculty/               - Faculty management and leave  
    │   └── chatbot/               - Gemini API integration  
    ├── database/  
    │   └── university_db.sql      - SQL file for database setup  
    └── README.md

    ## AI Chatbot Integration (Gemini API)

    This system includes an intelligent chatbot built with the Gemini API to provide users with quick responses 
    to queries, system help, and general interaction within the application.

    - Simple API integration using HTTP requests
    - Chatbot window embedded in the Java GUI
    - Example use cases: "How to apply for leave?", "What is my exam schedule?"

    ## Setup Instructions

    1. Clone the repository:
       
       git clone https://github.com/your-username/University-Management-System-Java.git
       cd University-Management-System-Java
       

    2. Set up the MySQL database:
       - Import university_db.sql into your MySQL server.
       - Note the database name, username, and password.

    3. Configure the DB connection:
       - Open the Java project.
       - Edit Connection.java to match your local database credentials.

    4. Run the project:
       - Use NetBeans or Eclipse.
       - Compile and run the main class (e.g., LoginPage.java).

    ## License

    This project is open-source under the MIT License.

    ## Author

    Sree Shankari V  
    Final Year B.Tech – Artificial Intelligence and Data Science  
    Francis Xavier Engineering College, Tirunelveli  
    LinkedIn: https://www.linkedin.com/in/sree-shankari-v-625a71258/  
    GitHub: https://github.com/shankari04

    ## Give a Star

    If you find this project useful, consider giving it a star on GitHub to support the developer and help others discover it.
