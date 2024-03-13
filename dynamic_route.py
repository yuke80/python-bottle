from bottle import route, run
 
# http://localhost:8080/tags/abc
@route('/tags/<var:re:[a-z]+>')
def tags(var):
    return var
 
# http://localhost:8080/num/123
@route('/num/<var:int>')
def hello(var):
    return str(var)
 
run(host='localhost', port=8080)