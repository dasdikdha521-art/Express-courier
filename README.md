# 🚚 Express Courier Tracking System

## Project Overview

The Express Courier Tracking System is a web-based application developed using Python and Flask. 
It helps manage courier services by providing separate functionalities for admins and users. 
The system allows administrators to add, update, search, view, and delete courier records, while users can register, log in, and track courier details.
This project was developed as a Core Python mini project.

# Features

# User Module
- User Registration
- User Login
- User Dashboard
- Track Courier
- View Courier Details

# Admin Module
- Admin Login
- Admin Dashboard
- Add Courier
- View All Couriers
- Search Courier
- Update Courier Status
- Delete Courier
- Reports Dashboard

# Technologies Used

- Python
- Flask
- HTML
- CSS
- CSV Files (for data storage)

# Project Structure

```
courier_tracking_web/
│
├── app.py
├── data/
│   ├── admin.csv
│   ├── users.csv
│   └── couriers.csv
│
├── templates/
│
├── static/
│   └── css/
│
├── utils/
│
└── README.md
```

---

# Run the application.

```
python app.py
```
# Open the browser and visit:

```
http://127.0.0.1:5000
```

---

## Data Storage

This project uses CSV files.

- **users.csv** – Stores registered user information.
- **admin.csv** – Stores administrator login credentials.
- **couriers.csv** – Stores courier booking and tracking information.

---

## Project Workflow

1. User registers and logs in.
2. Administrator logs in.
3. Administrator adds courier details.
4. A unique tracking ID is generated.
5. Users can track courier status.
6. Administrator can update courier status.
7. Administrator can delete courier records.
8. Reports display courier statistics.

---


## Developed By

**Ankita Das**

Core Python Mini Project

2026