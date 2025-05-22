# 💳 ATM Simulation in Python

This project is a **command-line based ATM simulation** built with Python and MySQL. It's designed as an educational tool to demonstrate how real-world banking systems work—**without involving any real money or encryption**.

It allows users to:
- Create an account
- Deposit money
- Withdraw money
- Transfer funds between accounts

All transactions are simulated and stored in a MySQL database to mimic real banking backend operations.

---

## 🧠 Purpose

This ATM simulation is **not** intended for production use or handling actual money. It is built for **learning purposes**, specifically to:
- Understand how front-end and back-end systems interact
- Learn how to manage user accounts and transactions
- Practice integrating Python with a MySQL database

---

## 🛠️ Technologies Used

- **Python** – for the command-line interface (CLI) and business logic
- **MySQL** – for storing account data and transaction history

---

## 🚀 Features

- 🔐 Account creation with user ID
- 💰 Deposit funds
- 🏧 Withdraw funds
- 🔄 Transfer money between accounts
- 🗃 Persistent storage using MySQL
- 🖥 Command-line interface for interaction

---

## 📦 Setup Instructions

### Prerequisites
- Python 3.x installed
- MySQL installed and running
- Basic understanding of Python and SQL

### Steps

1. **Clone the Repository**
   
   git clone https://github.com/salvageme/ATM-project.git<br>
   cd atm-project

2. **Configure Database Connection**

   Update your Python code with your MySQL credentials (host, user, password, database name).
   
3. **Set Up the Database**

   Run the provided python script named 'table creation.py' for users and transactions:
   python3 'table creation.py'

4. **Run the ATM Program**

   python3 atm.py

<br>

📎 Notes

    This system does not use encryption and is not secure for storing sensitive data.

    It's a basic simulation, best used for learning and demonstration purposes only.

🤝 Contributing

Feel free to fork the repo, make changes, and submit a pull request! Whether it's improving functionality or fixing bugs, contributions are welcome.

📜 License

This project is open source and available under the MIT License.
