# VulnApp — SQL Injection Demonstration

## Overview

VulnApp is a simple, intentionally vulnerable web application created using Python, Flask, and SQLite.

The purpose of this project is to demonstrate how SQL injection vulnerabilities occur and compare an insecure SQL query with a secure, parameterized query.

The application provides a basic login page where users can select between **Vulnerable** and **Secure** login modes.

## Technologies Used

- Python 3
- Flask
- SQLite
- HTML

## How It Works

The application creates an in-memory SQLite database containing three fictional user accounts.

Users enter a username and password and select one of two login modes:

### Vulnerable Mode

The application uses Python f-strings to insert user input directly into an SQL query.

This makes the login process vulnerable to SQL injection, potentially allowing an attacker to bypass authentication.

### Secure Mode

The application uses parameterized SQL queries with `?` placeholders.

This prevents user input from being interpreted as part of the SQL command, protecting against SQL injection.

## Installation and Running the Application

**1.** Install Python 3 and Flask.

```bash
python3 -m pip install flask
```

**2.** Clone the GitHub repository.

```bash
git clone https://github.com/hojokno/VulnApp.git
```

**3.** Navigate to the project directory.

```bash
cd VulnApp
```

**4.** Start the Flask application.

```bash
python3 app.py
```

**5.** Open a web browser and navigate to:

http://127.0.0.1:5000

## Demonstration

The application includes three fictional user accounts for testing:

| Username | Password |
|---|---|
| admin | supersecret123 |
| alice | password123 |
| bob | hello456 |

### Testing Normal Login

1. Enter a valid username and password.
2. Select either login mode.
3. Click **Login**.
4. The application displays a successful login message.

### Testing SQL Injection

1. Select **Vulnerable** mode.
2. Enter the following in the username field:

   `' OR 1=1 -- `

3. Enter any text in the password field.
4. Click **Login**.

The vulnerable SQL query can return a user record without requiring the correct password.

Repeat the same test in **Secure** mode to observe how parameterized queries prevent the injection from bypassing authentication.

## Burp Suite Testing

This application was also developed to practice web application testing using Burp Suite.

Two text files containing fictional usernames and passwords are provided for testing with Burp Suite Intruder.

The wordlists can be loaded into Intruder using the Cluster Bomb attack type to test combinations of usernames and passwords against the application's local login form.

The application supports two testing scenarios:

1. **SQL Injection:** Compare vulnerable SQL query construction against secure parameterized queries.
2. **Credential Testing:** Use Burp Suite Intruder to automate login attempts with predefined test credentials.

All testing is intended to be performed against the locally hosted Flask application at `http://127.0.0.1:5000`.

## Security Notes

This application is intentionally vulnerable and was developed strictly for educational purposes.

- It should only be run in a controlled local environment.
- The database contains fictional user accounts.
- The database is stored in memory and recreated each time the application starts.
- The application binds to `127.0.0.1` on port `5000`, making it accessible locally rather than directly exposing it to the network.
- The secure mode demonstrates protection against SQL injection specifically; it is not intended to represent a complete production authentication system.

## Conclusion

This project demonstrates the difference between constructing SQL queries with untrusted user input and using parameterized queries.

It highlights how unsafe query construction can introduce SQL injection vulnerabilities and how parameterized queries can prevent this type of attack.
