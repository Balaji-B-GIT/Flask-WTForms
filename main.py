from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField
from wtforms.validators import Email,Length
from flask_bootstrap import Bootstrap5
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
valid_email = "admin@email.com"
valid_pw = "12345678"

class MyForm(FlaskForm):
    email = StringField('email',validators=[Email()])
    password = PasswordField('password',validators=[Length(min=8, max=20)])
    submit = SubmitField('submit')


app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.secret_key = "any-string-you-want-just-keep-it-secret"

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login",methods=["POST","GET"])
def login():
    form = MyForm()
    if form.validate_on_submit():
        if form.email.data == valid_email and form.password.data == valid_pw:
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form = form)

if __name__ == '__main__':
    app.run(debug=True)
