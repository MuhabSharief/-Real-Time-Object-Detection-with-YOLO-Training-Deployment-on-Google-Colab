import streamlit as st
# Install necessary packages
"""!pip install flask pyngrok

from flask import Flask
from pyngrok import ngrok

# Replace "YOUR_NGROK_AUTH_TOKEN" with your actual ngrok auth token
ngrok.set_auth_token("2nZHie6XpmNvdTTkLDNL30IEPEl_2nBnfardck4a6K5rru5XN")

app = Flask(_name_)"""

# HTML content as a Python string
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FlavorFit</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }
        header {
            background-color: #4CAF50;
            padding: 20px;
            text-align: center;
            color: white;
        }
        nav ul {
            list-style-type: none;
            margin: 0;
            padding: 0;
        }
        nav ul li {
            display: inline;
            margin-right: 15px;
        }
        nav ul li a {
            color: white;
            text-decoration: none;
        }
        section {
            padding: 20px;
            background-color: white;
            margin: 10px;
        }
        form {
            display: flex;
            flex-direction: column;
            gap: 10px;
        }
        input, textarea {
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        button {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px;
            cursor: pointer;
            border-radius: 4px;
        }
        button:hover {
            background-color: #45a049;
        }
        footer {
            text-align: center;
            background-color: #4CAF50;
            padding: 10px;
            color: white;
        }
    </style>
</head>
<body>
    <header>
        <h1>FlavorFit</h1>
        <nav>
            <ul>
                <li><a href="#home">Home</a></li>
                <li><a href="#about">About</a></li>
                <li><a href="#features">Features</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <section id="home">
        <h2>Welcome to FlavorFit</h2>
        <p>Your personalized guide to healthier eating and fitness.</p>
    </section>

    <section id="about">
        <h2>About Us</h2>
        <p>FlavorFit curates recipes based on your medical needs, dietary preferences, and offers fitness guidance.</p>
    </section>

    <section id="features">
        <h2>Features</h2>
        <ul>
            <li>Customized Recipe Suggestions</li>
            <li>Nutrition Information</li>
            <li>Grocery Recommendations</li>
            <li>Fitness and Yoga Guidance</li>
        </ul>
    </section>

    <section id="contact">
        <h2>Contact Us</h2>
        <form id="contact-form">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>
            <label for="message">Message:</label>
            <textarea id="message" name="message" required></textarea>
            <button type="submit">Send</button>
        </form>
    </section>

    <footer>
        <p>&copy; 2024 FlavorFit. All rights reserved.</p>
    </footer>

    <script>
        document.getElementById('contact-form').addEventListener('submit', function(event) {
            event.preventDefault();
            const name = document.getElementById('name').value;
            const email = document.getElementById('email').value;
            const message = document.getElementById('message').value;
            
            if (name && email && message) {
                alert('Thank you, ' + name + '! Your message has been sent.');
                document.getElementById('contact-form').reset();
            } else {
                alert('Please fill out all fields.');
            }
        });
    </script>
</body>
</html>
"""

# Define the Flask route
@app.route('/')
def home():
    return html_content

# Start the Flask app
public_url = ngrok.connect(5000)
print("Website available at:", public_url)
app.run(port=5000)
