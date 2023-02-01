############################## Topic 1 : Use Templates in a Flask Application###################

from flask import Flask, render_template

app = Flask(__name__)

# Suggesstion : Build Image and Run container for better experience

#################### Step 1 Start ###################
"""
# mkdir templates
# nano templates/index_V1.html

# Add the following HTML code inside the index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>FlaskApp</title>
</head>
<body>
    <h1>Hello World!</h1>
    <h2>Welcome to FlaskApp!</h2>
</body>
</html>
"""

# Uncomment this to see index_V1.html page
"""
@app.route("/")
def hello():
    return render_template("index_V1.html")
"""
#################### Step 1 End ###################

#################### Step 2 Start ###################
"""
import datetime

@app.route('/')
def hello():
    return render_template('index_V2.html', utc_dt=datetime.datetime.utcnow())
"""
#################### Step 2 End ###################

#################### Step 3 Start ###################
"""
import datetime

@app.route('/')
def hello():
    return render_template('index_V2.html', utc_dt=datetime.datetime.utcnow())
"""
#################### Step 3 End ###################

############################## Topic 2 : Template Inheritance###################
# A base template contains HTML components that are typically shared between all 
# other templates, such as the application’s title, navigation bars, and footers.

#################### Step 4 Start ###################
"""
import datetime

@app.route('/')
def hello():
    return render_template('index_V3.html', utc_dt=datetime.datetime.utcnow())
"""
#################### Step 4 End ###################

############################## Topic 3 : Linking between Pages###################

#################### Step 5 Start ###################
"""
import datetime

@app.route('/') # http://127.0.0.1:5000/
def hello():
    return render_template('index_V4.html', utc_dt=datetime.datetime.utcnow())

@app.route('/home') # http://127.0.0.1:5000/home
def home():
    return render_template('index_V4.html', utc_dt=datetime.datetime.utcnow())

@app.route( '/message' ) # http://127.0.0.1:5000/message
def message():
    print( "Inside message" )
    # return { 'Message': "Welcome To message Page" }
    return render_template('message.html')

@app.route( '/about' ) # http://127.0.0.1:5000/about
def about():
    # return { 'Message': "Welcome To About Page" }
    return render_template('about.html')
"""
#################### Step 5 End ###################

app.run()