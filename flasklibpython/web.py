# # Flask – Complete Detailed Explanation with Functions and Examples

# ## 1. What is Flask?
# # - Flask is a lightweight, open-source web framework for Python.
# # - It helps you build web applications (websites, APIs) quickly and easily.
# # - Flask is called a "micro" framework because it provides the basics but lets you add features as needed.



# ## 3. Creating a Simple Flask App


# from flask import Flask

# app = Flask(__name__)  # Create Flask app object

# @app.route('/')        # Define route for home page
# def home():
#     return "Hello, Flask!"

# if __name__ == '__main__':
#     app.run(debug=True)  # Run the app in debug mode


# # - `Flask(__name__)`: Creates the app object.
# # - `@app.route('/')`: Decorator to define URL endpoint.
# # - `app.run(debug=True)`: Starts the server with debug mode.

# ## 4. Routing
# # - Routing connects URLs to Python functions.
# # - Example:

# @app.route('/about')
# def about():
#     return "This is the About page."
# ```
# - You can have multiple routes for different pages.

# ## 5. URL Variables
# - Pass variables in the URL.
# ```python
# @app.route('/user/<username>')
# def show_user(username):
#     return f"Hello, {username}!"
# ```

# ## 6. HTTP Methods (GET, POST)
# - By default, routes use GET.
# - To use POST:

# @app.route('/submit', methods=['GET', 'POST'])
# def submit():
#     if request.method == 'POST':
#         return "Form submitted!"
#     return "Submit form"

# - Import `request` from `flask` for POST data.

# ## 7. Rendering HTML Templates
# - Use Jinja2 templates for dynamic HTML.
# - Create a folder named `templates` and add `index.html`.

# from flask import render_template

# @app.route('/')
# def home():
#     return render_template('index.html')
# ```
# - In `index.html`:
# ```html
# <!DOCTYPE html>
# <html>
#   <body>
#     <h1>Welcome to Flask!</h1>
#   </body>
# </html>
# ```

# ## 8. Passing Data to Templates
# ```python
# @app.route('/user/<username>')
# def user_profile(username):
#     return render_template('profile.html', name=username)
# ```
# - In `profile.html`:
# ```html
# <h2>Hello, {{ name }}!</h2>
# ```

# ## 9. Redirects and URL Building
# ```python
# from flask import redirect, url_for

# @app.route('/go-home')
# def go_home():
#     return redirect(url_for('home'))
# ```

# ## 10. Handling Forms
# ```python
# from flask import request

# @app.route('/form', methods=['GET', 'POST'])
# def form():
#     if request.method == 'POST':
#         name = request.form['name']
#         return f"Hello, {name}!"
#     return '''
#         <form method="post">
#             Name: <input type="text" name="name">
#             <input type="submit">
#         </form>
#     '''
# ```

# ## 11. Static Files (CSS, JS, Images)
# - Place files in a folder named `static`.
# - Access in HTML: `<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">`

# ## 12. JSON Response (APIs)
# ```python
# from flask import jsonify

# @app.route('/api/data')
# def api_data():
#     data = {'name': 'Kartik', 'age': 23}
#     return jsonify(data)
# ```

# ## 13. Error Handling
# ```python
# @app.errorhandler(404)
# def page_not_found(e):
#     return "Page not found!", 404
# ```

# ## 14. Flask Extensions
# - Add features like authentication, databases, etc.
# - Examples: Flask-SQLAlchemy (database), Flask-Login (auth), Flask-WTF (forms).

# ## 15. Summary Table

# | Topic            | Function/Example                        | Description                       |
# |------------------|----------------------------------------|-----------------------------------|
# | Create app       | Flask(__name__)                        | Create Flask app object           |
# | Routing          | @app.route('/path')                    | Map URL to function               |
# | Templates        | render_template('file.html')           | Render HTML with data             |
# | Forms            | request.form['field']                  | Handle form data                  |
# | Redirect         | redirect(url_for('func'))              | Redirect to another route         |
# | Static files     | url_for('static', filename='file')     | Serve CSS, JS, images             |
# | JSON             | jsonify(data)                          | Return JSON for APIs              |
# | Error handling   | @app.errorhandler(code)                | Custom error pages                |

# ---

# **Flask is simple, flexible, and perfect for building web apps and APIs in Python.**

# # 1. Import Flask and create the app object
# from flask import Flask, render_template, request, redirect, url_for, jsonify

# app = Flask(__name__)  # Creates the Flask application

# # 2. Basic Routing
# @app.route('/')  # Home page route
# def home():
#     return "Hello, Flask!"  # Response for home page

# # 3. Multiple Routes Example
# @app.route('/about')  # About page route
# def about():
#     return "This is the About page."

# # 4. URL Variables (Dynamic Routing)
# @app.route('/user/<username>')  # Route with variable part
# def show_user(username):
#     return f"Hello, {username}!"  # Uses the variable from URL

# # 5. Handling HTTP Methods (GET and POST)
# @app.route('/submit', methods=['GET', 'POST'])
# def submit():
#     if request.method == 'POST':
#         return "Form submitted!"  # Response for POST
#     return "Submit form"         # Response for GET

# # 6. Rendering HTML Templates (Jinja2)
# @app.route('/template')
# def template_example():
#     # Renders 'index.html' from the 'templates' folder
#     return render_template('index.html')

# # 7. Passing Data to Templates
# @app.route('/profile/<username>')
# def user_profile(username):
#     # Passes 'name' variable to 'profile.html'
#     return render_template('profile.html', name=username)

# # 8. Redirects and URL Building
# @app.route('/go-home')
# def go_home():
#     # Redirects to the home page using url_for
#     return redirect(url_for('home'))

# # 9. Handling Forms (GET and POST)
# @app.route('/form', methods=['GET', 'POST'])
# def form():
#     if request.method == 'POST':
#         name = request.form['name']  # Gets form data
#         return f"Hello, {name}!"
#     # Returns a simple HTML form for GET request
#     return '''
#         <form method="post">
#             Name: <input type="text" name="name">
#             <input type="submit">
#         </form>
#     '''

# # 10. Serving Static Files (CSS, JS, Images)
# # Place files in a folder named 'static'
# # In HTML: <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">

# # 11. JSON Response (API Example)
# @app.route('/api/data')
# def api_data():
#     data = {'name': 'Kartik', 'age': 23}
#     return jsonify(data)  # Returns JSON response

# # 12. Error Handling (Custom Error Pages)
# @app.errorhandler(404)
# def page_not_found(e):
#     return "Page not found!", 404

# # 13. Flask Extensions (for advanced features)
# # - Flask-SQLAlchemy: Database integration
# # - Flask-Login: User authentication
# # - Flask-WTF: Advanced forms

# # 14. Run the Flask app
# if __name__ == '__main__':
#     app.run(debug=True)  # Starts the server in debug mode

# # ===========================
# # Summary Table (for reference)
# # ===========================
# # | Topic            | Function/Example                        | Description                       |
# # |------------------|----------------------------------------|-----------------------------------|
# # | Create app       | Flask(__name__)                        | Create Flask app object           |
# # | Routing          | @app.route('/path')                    | Map URL to function               |
# # | Templates        | render_template('file.html')           | Render HTML with data             |
# # | Forms            | request.form['field']                  | Handle form data                  |
# # | Redirect         | redirect(url_for('func'))              | Redirect to another route         |
# # | Static files     | url_for('static', filename='file')     | Serve CSS, JS, images             |
# # | JSON             | jsonify(data)                          | Return JSON for APIs              |
# # | Error handling   | @app.errorhandler(code)                | Custom error pages                |

# # ===========================
# # Flask is simple, flexible, and perfect for building web apps and APIs in Python.
# #