
from flask import Flask, request

app = Flask(__name__)

# routes url
@app.route('/')
def home():
    return 'hello world'


@app.route('/user/list/',methods =['GET'] )
def users_list():
    return 'users list'


@app.route('/user/add',methods =['POST'])
def users_add():
    if request.method == 'POST':
        
        return 'user_added'


# initialize server
if __name__=='__main__':
    app.run(port=3000, debug=True)

