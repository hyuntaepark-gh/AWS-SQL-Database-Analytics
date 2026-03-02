# 🗄️ AWS & SQL Database Engineering Projects

![AWS](https://img.shields.io/badge/AWS-EC2-orange)
![Apache](https://img.shields.io/badge/Apache-Web%20Server-D22128?logo=apache)
![MariaDB](https://img.shields.io/badge/MariaDB-Relational%20DB-003545?logo=mariadb)
![SQL](https://img.shields.io/badge/SQL-Database%20Design-CC2927)
![Python](https://img.shields.io/badge/Python-Backend-3776AB?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-150458?logo=pandas)
![ER Modeling](https://img.shields.io/badge/ER-Modeling-0A66C2)
![3NF](https://img.shields.io/badge/3NF-Normalization-6A1B9A)

This repository showcases hands-on relational database design and cloud-based database application engineering.

It demonstrates my ability to:

- Design normalized relational schemas (3NF)
- Implement primary and foreign key constraints
- Deploy database-driven applications on AWS EC2
- Build server-side SQL execution pipelines
- Integrate Python-based data processing and Excel reporting

---

# 📁 Project: TradingDB – Relational Database & AWS Application

## 🔍 Project Overview

The TradingDB project simulates a real-world business database managing:

- Clients
- Financial Officers
- Contracts
- Company Information

The project evolved from schema design into a cloud-hosted database web application deployed on AWS EC2.

### Key Objectives

- Design a normalized relational schema (3NF)
- Define entity relationships and constraints
- Write SQL queries to retrieve business insights
- Deploy the database on AWS EC2
- Implement a web-based SQL query interface
- Enable Excel export using Python and Pandas

---

# 🧱 System Architecture

![System Architecture](screenshots/01-system-architecture-diagram.png)

Architecture includes:

- AWS EC2 instance
- Apache Web Server (CGI enabled)
- MariaDB relational database
- Python backend scripts
- Pandas-based Excel export
- Browser-based SQL interaction

---

# 🔐 AWS Deployment

![EC2 SSH Login](screenshots/02-ssh-ec2-login.png)

Live SSH connection demonstrating:

- EC2 setup and configuration
- Server-side deployment
- Database installation

---

# 📜 Apache Server Logging

![Apache Access Log](screenshots/07-apache-access-log.png)

Access logs confirm:

- HTTP request handling
- CGI execution
- Client interaction tracking

---

# 🌐 Web-Based SQL Interface

![SQL Query Form](screenshots/08-sql-query-form-page.png)

A browser-based SQL interface allowing users to:

- Submit filtered queries
- Retrieve structured data
- Interact dynamically with the database

---

# 🔎 Query Execution Example

![Filled Search Form](screenshots/10-price-search-form-filled.png)

User-defined filtering conditions are validated and securely processed by the backend.

---

# 📊 SQL Query Results

![Query Results](screenshots/11-pricequery-result-table.png)

Server-rendered HTML table displaying query results.

---

# 📥 Excel Export Feature

![Excel Download Form](screenshots/14-excel-download-form-empty.png)

Users can generate downloadable Excel reports directly from query results.

---

# 📄 Generated Excel Output

![Excel Result Preview](screenshots/17-excel-result-preview.png)

Example Excel file generated through:

Database → Python → Pandas → Excel pipeline

---

# 🐍 Python Backend Implementation

## Database Connection

![Python DB Connection](screenshots/18-python-db-connection-code.png)

## SQL Execution & Data Fetching

![Python SQL Fetch](screenshots/19-python-sql-query-fetch-code.png)

## Pandas Excel Export Logic

![Pandas Excel Export](screenshots/20-python-pandas-export-excel-code.png)

---

# 🧠 Database Design Highlights

- Entity-Relationship (ER) Modeling
- Primary and Foreign Key Constraints
- 3rd Normal Form (3NF) Normalization
- Many-to-Many Relationships via Junction Tables
- ISA Specialization

---

# 🛠️ Tools & Technologies

- AWS EC2
- Apache Web Server
- MariaDB (MySQL-compatible)
- SQL (DDL, DML)
- Python
- Pandas
- ER Modeling

---

# 📌 Key Skills Demonstrated

- Relational Database Design
- SQL Query Engineering
- Cloud Deployment
- Server Configuration
- Backend Scripting
- Data Processing Automation
- Reporting Workflow Integration


```

stock-trading-database/
├─ README.md
├─ ERD/
│  └─ ER_Diagram.pdf
├─ schema/
│  └─ create_tables.sql
├─ queries/
│  ├─ basic_queries.sql
│  ├─ joins.sql
│  └─ advanced_queries.sql
├─ backend/
│  ├─ db_connection.py
│  ├─ query_handler.py
│  └─ export_excel.py
└─ docs/
   └─ database_overview.md

```
1,8,10,11,14,17
