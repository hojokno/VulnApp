from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

# Demo database containing fake users
db = sqlite3.connect(":memory:", check_same_thread=False)

db.execute("""
    CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        username TEXT,
        password TEXT
    )
""")

db.executemany(
    "INSERT INTO users (username, password) VALUES (?, ?)",
    [
        ("admin", "supersecret123"),
        ("alice", "password123"),
        ("bob", "hello456")
    ]
)

db.commit()


# HTML login page
HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>SQL Injection Lab</title>
</head>
<body>

    <h1>SQL Injection Lab</h1>

    <h3>Login</h3>

    <form method="POST">

        <input
            type="text"
            name="username"
            placeholder="Username"
            required
        >

        <br><br>

        <input
            type="password"
            name="password"
            placeholder="Password"
            required
        >

        <br><br>

        <label>Select Login Mode:</label>

        <select name="mode">
            <option value="vulnerable">Vulnerable</option>
            <option value="secure">Secure</option>
        </select>

        <br><br>

        <button type="submit">Login</button>

    </form>

    <p>{{ message }}</p>

</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def login():

    message = ""

    if request.method == "POST":

        username = request.form.get("username", "")
        password = request.form.get("password", "")
        mode = request.form.get("mode", "secure")

        if mode == "vulnerable":

            # INTENTIONALLY VULNERABLE TO SQL INJECTION
            query = (
                f"SELECT * FROM users WHERE username = '{username}' "
                f"AND password = '{password}'"
            )

            try:
                user = db.execute(query).fetchone()

            except sqlite3.Error:
                user = None
                message = "SQL query error"

        else:

            # SECURE LOGIN USING PARAMETERIZED QUERIES
            query = """
                SELECT * FROM users
                WHERE username = ? AND password = ?
            """

            try:
                user = db.execute(
                    query, (username, password)
                ).fetchone()

            except sqlite3.Error:
                user = None
                message = "Database error"

        if user:
            message = f"Login successful! Welcome, {user[1]}"

        elif not message:
            message = "Invalid credentials"

    return render_template_string(
        HTML,
        message=message
    )


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False
    )
