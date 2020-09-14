from flask import *
import dataset

app = Flask(__name__)

db=dataset.connect('sqlite:///gaymer.db')
app.secret_key = "dr72oi1sadadw2dqqdwwddq"

@app.route('/')
def index():
    if 'username' not in session:
        return redirect('/login')
    return render_template('mainpage.html', posts=db['posts'])

@app.route('/settings')
def setting():
    return render_template('settings.html')


@app.route('/logout')
def logout():
    del session['username']
    return redirect('/')

@app.route('/set_picture')
def set_picture():
    return render_template('set_picture.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/create_account')
def create_account_get():
    return render template('create_account.html')

@app.route('/create_account_post', methods=['post'])
def create_account_get():
    user = {

    'username' : request.form['username'],
    'password' : request.form['password']

    }

@app.route('/login', methods=['POST'])

typed_username = request.form['username']
typed_password = request.form['password']

def login_post():
    username = request.form.get('username')
    password = request.form.get('password')
    username = db['users'].find_one(username=typed_username)
    password = user['password']



    if password = typed_password:
        session['username'] = request.form['username']
        return redirect('/')

    return"Invalid password!!"






@app.route('/chatroom')
def chatroom():
    if 'username' not in session:
        return redirect('/login')
    else:
        return render_template('chatroom.html')


@app.route('/create_post', methods=['post'])
def create_post():
    post_dictonarty = {
        'message' : request.form['message'],
        'username' : session['username']
    }

    db['posts'].insert(post_dictonarty)

    return redirect('/chatroom')

app.run(debug=True)
