# CyberWatch-Log-Monitor
Tkinter-based Cyber Security Log Monitoring Tool
CyberWatch – Log Monitoring & Threat Detection Tool

CyberWatch is an open-source Cyber Security Log Monitoring Tool developed as a semester project.
It helps in parsing system logs, detecting potential security threats, storing logs in a database, and visualizing logs through a GUI dashboard.

This project follows a modular architecture and a professional GitHub collaboration workflow using feature branches and pull requests.

 Project Features
 Log Parsing – Reads and processes system log files safely
 Threat Detection – Identifies suspicious activities using keyword-based analysis
 Database Storage – Stores logs securely using SQLite
 GUI Dashboard – Displays logs via a Tkinter-based interface
 Report Generation – Exports stored logs into CSV reports
 Team Collaboration – Proper GitHub workflow with individual contributions
 Technologies Used
Programming Language: Python 3
GUI Framework: Tkinter
Database: SQLite
Version Control: Git & GitHub
Operating System: Cross-platform (Windows/Linux)
 Project Structure
CyberWatch-Log-Monitor/
│
├── main.py                  # Main integration file (Leader)
│
├── parser/
│   ├── log_parser.py        # Log parsing module
│   └── sample_logs/
│       └── auth.log
│
├── detection/
│   └── threat_detection.py # Threat detection module
│
├── database/
│   └── db_manager.py       # Database management
│
├── reports/
│   └── export.py           # CSV report generation
│
├── gui/
│   └── dashboard.py        # GUI dashboard
│
├── assets/                 # Images / resources
└── README.md               # Project documentation
 How to Run the Project
 Clone the Repository
git clone https://github.com/mhussain954/CyberWatch-Log-Monitor.git
cd CyberWatch-Log-Monitor
 Run Main Application (CLI Integration)
python main.py

✔ Loads logs
✔ Detects threats
✔ Saves logs to database

 Run GUI Dashboard
python -m gui.dashboard

✔ Click Load Log File
✔ Select a .log file
✔ View logs in the interface

Sample Log Format
Failed password for root from 192.168.1.10
Accepted password for hussain from 192.168.1.20
Unauthorized access detected
 Team Members & Contributions
Name	Role	Contribution
Muhammad Hussain	Project Leader	Architecture, GitHub management, integration (main.py)
Abdullah Afzal	Developer	Log Parser Module
Muhammad Zubair	Developer	GUI Dashboard
Usman Tariq	Developer	Threat Detection Module
Adnan Munir	Developer	Database & Report Generation
 GitHub Workflow Used
Feature-based branches (feature/*)
Pull Requests for each module
Code review and approval by leader
Final integration into main branch

This workflow ensures clean collaboration and traceable contributions.

 Academic Use

This project was developed for Open Source Software Development / Cyber Security coursework and demonstrates:

Modular programming
Secure log handling
Team-based open-source development
Real-world GitHub workflow
 License

This project is open-source and free to use for educational purposes.

 Final Note

CyberWatch demonstrates how security tools are built collaboratively using open-source principles, emphasizing teamwork, modularity, and secure coding practices.