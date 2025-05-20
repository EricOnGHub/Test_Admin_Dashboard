from flask import Flask, render_template

app = Flask(__name__)

# Sample user data
dummy_users = [
    {"name": "Jane Doe", "email": "jane@example.com"},
    {"name": "John Smith", "email": "john@example.com"},
    {"name": "Mary Johnson", "email": "mary@example.com"},
    {"name": "Michael Brown", "email": "michael@example.com"},
]

total_users = 100
active_users = 75

@app.route('/')
def dashboard():
    return render_template(
        'dashboard.html',
        users=dummy_users,
        total_users=total_users,
        active_users=active_users
    )

if __name__ == '__main__':
    app.run(debug=True)
