from flask import Flask, request


app = Flask(__name__)
app.config['DEBUG'] = True

from caesar import rotate_string

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
        <!-- create your form here -->
		<form method="POST" id="form">
			<label for="rot">
				Rotate by: <input type="text" value="0" name="rot" id="rot">
			</label>
			<input type="submit">
		<textarea name="text" form="form">{0}</textarea>
    </body>
</html>

    """

@app.route("/")
def index():
	return form.format("")

@app.route("/",methods=['POST'])
def encrypt():
	rot = int(request.form['rot'])
	text = request.form['text']
	rotated = rotate_string(text,rot)
	return form.format(rotated)

app.run()