from flask import Flask, make_response

app = Flask(__name__)
app.config.from_object('config')


@app.route('/hello')
def hello():
    headers = {
        #'content-type': 'text/plain',
        'location': 'http://www.baidu.com'
    }
    #response = make_response( 301)
    #response.headers = headers

    return 301,headers


#app.add_url_rule('/hello', view_func=hello)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.config['DEBUG'])

