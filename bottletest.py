from bottle import route, run, template


@route('/hello')
def hello():
    return 'Hello World'


@route('/')
def main():
	return template('main_template', pizzas = 24)


run(host='localhost', port=8080, debug=True)