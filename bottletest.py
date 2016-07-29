from bottle import route, run, template, view
from main import how_many

#assume 25 people
view_stuff = how_many(25) 

print(view_stuff)

@route('/hello')
def hello():
    return 'Hello World'


@route('/')
@view('main_template')
def main():
	return template('main_template', pizzas = 6)

run(host='localhost', port=8080, debug=True)