# Banking Management System

## Overview
This project is a Python-based banking management system integrated with SQL for secure and efficient account management. It provides users with essential banking functionalities like account creation, secure login, transaction management, and passbook generation. Designed with a Command-Line User Interface (CUI), it is simple yet effective for managing basic banking operations.

---

## Features
1. **Account Management**
   - Create new bank accounts with unique account and consumer numbers.
   - Store user details including name, date of birth, address, and parental details.

2. **Authentication**
   - Secure login using username and password.
   - Allows username and password updates.

3. **Transactions**
   - Deposit money.
   - Send money to another account.
   - View transaction history through the passbook feature.

4. **Database Integration**
   - Uses MySQL to store customer and transaction data securely.
   - Automatically creates necessary database and tables if not already present.

5. **Additional Features**
   - Transaction remarks for better tracking.
   - Session timeout countdown for added security.
   - User-friendly error handling for incorrect inputs.

---

## How It Works
1. **Setup**
   - Users are prompted to connect to the MySQL database by entering the root password.
   - If the connection is successful, the system initializes and creates the necessary database and tables.

2. **Creating Accounts**
   - Users can open a new account by providing personal details.
   - The system generates a unique account number and consumer number.
   - Default usernames and passwords can be updated by users.

3. **Performing Transactions**
   - Users can log in with their credentials to deposit or send money.
   - A detailed transaction history is maintained and displayed in the passbook.

4. **Security**
   - Only authenticated users can access their accounts.
   - Passwords are securely managed and can be reset with proper verification.

---

## Technologies Used
- **Programming Language**: Python
- **Database**: MySQL
- **Modules Used**:
  - `mysql.connector`: For database connectivity.
  - `datetime`: For date-related functionalities.
  - `random`: For generating unique account and consumer numbers.
  - `time`: For countdown timers.

---

## How to Run
1. Install the required Python modules:
   ```bash
   pip install mysql-connector-python
   ```

2. Ensure MySQL is installed and running on your system.

3. Run the script:
   ```bash
   python bank_rahul_singh.py
   ```

4. Enter the MySQL root password when prompted.

5. Follow the on-screen instructions to create accounts, perform transactions, or view account details.

---

## Future Enhancements
- Add a graphical user interface (GUI) for better user experience.
- Implement encryption for storing sensitive user data.
- Expand transaction options to include automated recurring payments.
- Integrate multi-currency support.

---

## Disclaimer
This project is intended for educational purposes only and is not suitable for deployment in a real-world banking environment.

---

## Author
Rahul Singh

