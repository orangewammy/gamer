from flask import *
import dataset

app = Flask(__name__)

db=dataset.connect('sqlite:///gaymer.db')
app.secret_key = "dr72oi1sadadw2dqqdwwddq"

@app.route('/')
def index():
    if 'username' not in session:
        return redirect('/login')
    return render_template('mainpage.html')


@app.route('/logout')
def logout():
    del session['username']
    return redirect('/')

@app.route('/set_picture')
def set_picture():
    return render_template('set_picture.html')

@app.route('/set_picture_post', methods=['post'])
def set_picture_post():
    file = request.files['file']
    file_to_save = 'static/uploads/' + file.filename
    file.save(file_to_save)

    session['profile_picture_url'] = file_to_save

    return redirect('/')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/create_account')
def create_account_get():
    return render_template('create_account.html')

@app.route('/create_account_post', methods=['post'])
def create_account_post():
    print(request.form)
    user = {

    'username' : request.form['username'],
    'password' : request.form['password'],
    'genre'    : request.form['genre'],
    'sexuality': request.form['sexuality'],
    'sport': request.form['sport'],
    'bio':request.form['bio'],
    'gender': request.form['gender'],

    }

    db['users'].insert(user)

    return redirect('/login')


@app.route('/login', methods=['POST'])
def login_post():
    typed_username = request.form.get('username')
    typed_password = request.form.get('password')
    genre = request.form.get('genre')
    print('typed_username', typed_username)
    user = db['users'].find_one(username=typed_username)
    if user is None:
        return redirect('/login')
    password = user['password']



    if password == typed_password:
        session['username'] = request.form['username']
        return redirect('/')

    return"Invalid password!!"



@app.route('/chatroom')
def chatroom():
    if 'username' not in session:
        return redirect('/login')
    else:
        return render_template('chatroom.html', posts=db['posts'])


@app.route('/create_post', methods=['post'])
def create_post():
    post_dictonarty = {
        'message' : request.form['message'],
        'username' : session['username'],
        'picture' : session['profile_picture_url']
    }

    db['posts'].insert(post_dictonarty)

    return redirect('/chatroom')

@app.route('/settings')
def setting():
    user = db['users']
    image = session['profile_picture_url']
    return render_template('settings.html',text=user, image=image)

app.run(debug=True)
