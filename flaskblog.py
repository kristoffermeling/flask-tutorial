from flask import Flask, escape, request, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)


app.config['SECRET_KEY'] = '31e5cd5d36311385803ff8dae5f2edc6'

posts = [
    {
        'author': 'Kristoffer Meling',
        'title' : 'blogpost 1',
        'content' : 'First post content',
        'date_posted' : 'April 20, 2018'
    },
    {
        'author': 'Test Testesen',
        'title': 'blogpost 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

@app.route('/')
@app.route('/home')
def home():
    #name = request.args.get("name", "World")
    return render_template('home.html', posts=posts)

@app.route('/about/')
def about():
    return render_template('about.html', title = 'About')

@app.route("/register", methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", 'success')
        return redirect(url_for('home'))
    #print(form.errors)
    return render_template('register.html', title= 'Register', form= form)


@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'test':
            flash('You have been logged in!','success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful please check username and password','danger')

    return render_template('login.html', title= 'Login', form= form)



if __name__ == '__main__':
    app.run(debug=True)