# 📘 Flask Introduction
# ---------------------
# Flask is a lightweight Python web framework used to build web applications and RESTful APIs.
# It’s called a "micro-framework" because it provides the essentials without enforcing structure.

# ✅ Key Features:
# - Built on Werkzeug (WSGI toolkit) and Jinja2 (templating engine)
# - Minimal setup, highly flexible
# - Ideal for small to medium web apps and APIs
# - Supports routing, templates, forms, sessions, and more

# 🔗 Official Flask Documentation:
# https://flask.palletsprojects.com/   # Full reference and tutorials
# https://www.geeksforgeeks.org/python/flask-tutorial/   # Beginner-friendly guide

# 📦 Installation:
# Run this in your terminal or command prompt:
# pip install flask

# 📦 Import the Flask class from the flask module
from flask import Flask

# 🚀 Create a Flask application instance
app = Flask(__name__)

# 🏠 Route: Home Page
@app.route('/')  # This route handles requests to the root URL: http://127.0.0.1:5000/
def home():
    return "✅ Welcome to Kartik's Flask App!"  # Simple welcome message

# 👋 Route: Static Greeting
@app.route('/hello')  # This route handles: http://127.0.0.1:5000/hello
def hello():
    return "👋 Hello, Kartik!"  # Static greeting message

# 🔄 Route: Dynamic Username Greeting
@app.route('/user/<username>')  # This route handles: http://127.0.0.1:5000/user/Kartik
def greet_user(username):
    return f"👤 Hello, {username}!"  # Personalized greeting using dynamic URL

# 🔢 Route: Type-Specific Post ID
@app.route('/post/<int:post_id>')  # This route handles: http://127.0.0.1:5000/post/5
def show_post(post_id):
    return f"📝 This is post number {post_id}"  # Displays post ID from URL

# 🛠️ Route: About Page using add_url_rule
def about():
    return "ℹ️ This is the About Page"  # Simple About page content

# 🔗 Manually bind the '/about' URL to the 'about' function
app.add_url_rule('/about', 'about', about)

# 🚦 Run the Flask app only if this file is executed directly
if __name__ == '__main__':
    print("✅ Flask app is starting...")  # Confirmation message in terminal
    app.run(debug=True)  # Start the development server with debug mode enabled

# ▶️ Run the app:
# python app.py
# Then open your browser and go to: http://127.0.0.1:5000/

# 🧪 Test URLs:
# http://127.0.0.1:5000/hello         → Returns "Hello, Kartik!"
# http://127.0.0.1:5000/user/Kartik   → Returns "Hello, Kartik!"
# http://127.0.0.1:5000/post/5      → Returns "This is post number 5"
# http://127.0.0.1:5000/about         → Returns "This is the About Page"


from flask import Flask, jsonify, Response

app = Flask(__name__)

# ✅ 1. Return a simple string
@app.route('/simple')
def simple():
    return "✅ Hello, Kartik!"  # Basic string response

# ✅ 2. Return a string with a variable using f-string
@app.route('/fstring')
def fstring():
    a = 4 + 5
    return f"✅ Result using f-string: {a}"  # Embeds variable directly

# ✅ 3. Return a string with .format()
@app.route('/format')
def format_example():
    a = 4 + 6
    return "✅ Result using .format(): {}".format(a)  # Uses .format() method

# ✅ 4. Return string + valid status code
@app.route('/status')
def status_code():
    return "✅ Everything is OK", 200  # Tuple: (response, status_code)
# in these e.g we reaching there and executing it , and if we want to take an input
# so such example is mention below 

# ❌ 5. Invalid: Returning string + number (not a valid status code)
# Uncommenting this will cause an error
# @app.route('/error')
# def error_example():
#     a = 10
#     return "❌ This will fail", a  # ❌ Flask treats 'a' as status code — 10 is invalid

# ✅ 6. Return JSON response
@app.route('/json')
def json_response():
    data = {"name": "Kartik", "score": 95}
    return jsonify(data)  # Returns JSON object

# ✅ 7. Return custom response with headers
@app.route('/custom')
def custom_response():
    content = "✅ Custom plain text response"
    return Response(content, status=200, mimetype='text/plain')  # Full control

# ✅ 8. Root route for testing
@app.route('/')
def home():
    return "✅ Flask is running! Try /simple, /fstring, /format, /json etc."

if __name__ == '__main__':
    print("🚀 Starting Flask app...")
    app.run(debug=True)




##### wap to take input and execute it also ##########

# first e.g
from flask import Flask, request

app = Flask(__name__)

# 🔢 Route: Accepts input via query parameters and returns result
@app.route('/square')
def square():
    # 📥 Get input from URL query parameter
    x = request.args.get("x")

    try:
        num = float(x)  # Convert input to number
        result = num ** 2  # Calculate square
        return f"✅ Square of {num} is {result}"
    except (TypeError, ValueError):
        return "⚠️ Please provide a valid number using ?x=your_number"

if __name__ == '__main__':
    print("🚀 Flask args app is running...")
    app.run(debug=True)

# now ques how to give input 
# first open url and atlast of url add --> ?x = ...value...


# second 
from flask import Flask, request

app = Flask(__name__)

# 🏠 Route: Home page with input form
@app.route('/')
def form():
    return '''
        <h2>🧮 Simple Calculator</h2>
        <form action="/result" method="post">
            Enter first number: <input type="number" name="num1"><br><br>
            Enter second number: <input type="number" name="num2"><br><br>
            <input type="submit" value="Calculate Sum">
        </form>
    '''

# 🧠 Route: Process input and show result
@app.route('/result', methods=['POST'])
def result():
    try:
        # 🔢 Get numbers from form
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])

        # ➕ Perform calculation
        total = num1 + num2

        # 📤 Return result
        return f"<h3>✅ The sum of {num1} and {num2} is: {total}</h3>"

    except ValueError:
        return "<h3>⚠️ Invalid input. Please enter numeric values.</h3>"

if __name__ == '__main__':
    print("🚀 Calculator app is running...")
    app.run(debug=True)

# third example 
from flask import Flask, request

app = Flask(__name__)

# 🏠 Route: Home page with input form
@app.route('/')
def form():
    return '''
        <h2>👋 Welcome, Kartik!</h2>
        <form action="/greet" method="post">
            Enter your name: <input type="text" name="username">
            <input type="submit" value="Greet Me">
        </form>
    '''

# 📨 Route: Handle form submission
@app.route('/greet', methods=['POST'])
def greet():
    username = request.form['username']  # Get input from form
    return f"<h3>👤 Hello, {username}!</h3>"  # Display personalized greeting

if __name__ == '__main__':
    print("🚀 Flask input app is running...")
    app.run(debug=True)