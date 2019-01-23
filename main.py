from flask import Flask, request
from caesar import rotate_string
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form action = '/', method = "post">
            <label for = 'rotate-by'>Rotate By:</label>
            <input id ='rotate-by' type = 'text' name='rot' value ='0' />
            <textarea type ='textarea' name = 'text'>{0}</textarea>
            <input type ='submit' />
        </form>
    </body>
</html>
"""

@app.route('/')
def index():
    return form.format('')


@app.route('/', methods = ['POST'])
def encrypt ():
    rot = (request.form['rot'])
    rot = int(rot)
    user_input = (request.form['text'])
    user_input1 = rotate_string(user_input, rot)
    response = user_input1
    return form.format(cgi.escape(response))

app.run() 