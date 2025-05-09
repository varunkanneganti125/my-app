from flask import Flask

app = Flask(__name__)

# ✅ Health check route for Load Balancer
@app.route('/')
def health_check():
    return 'OK', 200

# ✅ Dummy route to handle ALB or client requests to /login.html
@app.route('/login.html')
def login_html():
    return 'Login placeholder (HTML)', 200

# ✅ Dummy route to handle /login.jsp if mistakenly requested
@app.route('/login.jsp')
def login_jsp():
    return 'Login placeholder (JSP)', 200

# ✅ Main app logic
@app.route('/home')
def home():
    return 'Welcome to the actual app!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
