'''
https://flask.palletsprojects.com/en/1.1.x/quickstart/


'''

from flask import Flask, url_for, redirect, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/projects/')
def projects():
    return 'The project page'


@app.route('/user/<username>')
def profile(username):
    return ('{}\'s profile'.format(username))


@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name


@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['name']
      sirname = request.form['sirname']
      z = user+' '+sirname
      return redirect(url_for('success',name = z))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))

if __name__ == '__main__':
   app.run(debug = True)

'''
with app.test_request_context():
    print(url_for('index'))
    print(url_for('projects'))
    print(url_for('profile', username='John Doe'))'''