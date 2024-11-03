from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField
from wtforms.validators import DataRequired
'''
To Create a requirements.txt 
$ pip install pipreqs

Afterwards you can generate the requirements.txt file like so:

$ pipreqs path_to_your_project_folder


To Install the required packages : 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''


class MyForm(FlaskForm):
    email = StringField('email',validators=[DataRequired()])
    password = PasswordField('password',validators=[DataRequired()])
    submit = SubmitField('submit')



app = Flask(__name__)
app.secret_key = "any-string-you-want-just-keep-it-secret"

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login",methods=["POST","GET"])
def login():
    form = MyForm()
    return render_template('login.html', form = form)

if __name__ == '__main__':
    app.run(debug=True)
