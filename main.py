from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True
form = """
<!DOCTYPE html>
<html>
    <title>
        Web-Caesar
        </title>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 60px;
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
            #rot-input {{
                width: 3em;
                border-radius: 0px;
                }}
        </style>
    </head>
    <body>
        <form id="app" method="post">
            <label>
                Rotate By: <input type="number" value={rot} id="rot-input" name="rot"/>
                <textarea id="text-input" name="text-input" placeholder="Enter string to encrypt" >{ciphertext}</textarea>
                <input type="submit" value="Submit"/> 
            </label>
        </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form.format(ciphertext='', rot=0, decrypt='')


@app.route("/", methods=['POST'])
def encrypt():
    string = request.form['text-input']
    key = request.form['rot']
    content = rotate_string( string, int(key))

    return form.format(ciphertext=content, rot=key, descrpt='')

app.run()