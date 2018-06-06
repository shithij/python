from flask import Flask , render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/home')
def home():
	fruit=['apple','banana','pear']
	return render_template('home.html', fruit=fruit)

@app.route('/login',methods=['POST','GET'])
def login():
	error=None
	if request.method == 'POST':
		if request.form['email'] !='rai@gmail.com' or request.form['password'] !='nsoc':
			error='Wrong credentials'  
		else:
			return redirect('/home')
		return render_template('login.html',error=error)  
	return render_template('login.html')



if __name__ == '__main__':
	app.jinja_env.globals.update(chr=chr)
	app.run(host='0.0.0.0' ,port=8000,debug=True, threaded=True)