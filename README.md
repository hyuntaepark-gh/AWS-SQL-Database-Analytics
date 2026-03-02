# 🗄️ AWS & SQL Database Engineering Projects

![AWS](https://img.shields.io/badge/AWS-EC2-orange)
![Apache](https://img.shields.io/badge/Apache-Web%20Server-D22128?logo=apache)
![MariaDB](https://img.shields.io/badge/MariaDB-Relational%20DB-003545?logo=mariadb)
![SQL](https://img.shields.io/badge/SQL-Database%20Design-CC2927)
![Python](https://img.shields.io/badge/Python-Backend-3776AB?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-150458?logo=pandas)
![ER Modeling](https://img.shields.io/badge/ER-Modeling-0A66C2)
![3NF](https://img.shields.io/badge/3NF-Normalization-6A1B9A)

This repository demonstrates both:

- 📐 Relational database design (3NF, PK/FK, ISA, M:N)
- ☁️ Cloud-based database application engineering (AWS EC2 + Apache + Python)

It bridges database theory and production-style deployment.

---

# 📁 Project: TradingDB – Relational Database & AWS Application

## 🔍 Overview

A simulated financial trading database managing:

- Clients
- Financial Officers
- Contracts
- Contact Information
- Company / Individual Client Types

Deployed as a live web-based SQL application on AWS EC2.

---

# 🧱 System Architecture

![System Architecture](screenshots/01-system-architecture-diagram.png)

Architecture:

- AWS EC2
- Apache Web Server (CGI)
- MariaDB
- Python backend
- Pandas Excel export
- Browser-based SQL interface

---

# 🔐 AWS Deployment

![EC2 SSH Login](screenshots/02-ssh-ec2-login.png)

---

# 📜 Apache Logs

![Apache Access Log](screenshots/07-apache-access-log.png)

---

# 🌐 Web SQL Interface

![SQL Query Form](screenshots/08-sql-query-form-page.png)

---

# 📊 Query Example

![Filled Search](screenshots/10-price-search-form-filled.png)

![Query Result](screenshots/11-pricequery-result-table.png)

---

# 📥 Excel Export Pipeline

![Excel Download](screenshots/14-excel-download-form-empty.png)

![Excel Output](screenshots/17-excel-result-preview.png)

---

# 🐍 Python Backend

## Database Connection
![DB Connection](screenshots/18-python-db-connection-code.png)

## SQL Execution
![SQL Fetch](screenshots/19-python-sql-query-fetch-code.png)

## Pandas Export
![Pandas Export](screenshots/20-python-pandas-export-excel-code.png)

---

# 🗂️ Relational Model Evidence

## Financial Officer Table
![Financial Officer](screenshots/21-financial-officer-table.png)

## Client Master Table
![Client Master](screenshots/22-client-master-table.png)

## Individual Client (ISA)
![Individual Client](screenshots/23-individual-client-table.png)

## Company Client (ISA)
![Company Client](screenshots/24-company-client-table.png)

## Contact Info (1:N)
![Contact Info](screenshots/25-client-contact-info-table.png)

## Contract Master
![Contract Table](screenshots/26-contract-master-table.png)

## Contract ↔ Client (M:N via Junction)
![Contract Client Mapping](screenshots/27-contract-client-mapping-table.png)

---

# 🧠 Database Design Features

- 3rd Normal Form (3NF)
- Primary / Foreign Keys
- ISA Specialization (Individual vs Company)
- One-to-Many Relationships
- Many-to-Many Relationships via Junction Tables
- Referential Integrity Enforcement

---

# 🛠️ Technology Stack

- AWS EC2
- Apache (CGI)
- MariaDB
- SQL (DDL, DML)
- Python
- Pandas
- ER Modeling

---

# 🎯 Engineering Value

This project demonstrates:

- Database schema design
- Referential modeling
- Cloud deployment
- Backend integration
- Data export automation
- Production-style architecture thinking

---

# 📂 Project Structure

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

---
