from bottle import route, run

@route('/hello') #adress of web site http://~/hello デコレーターでhelloを呼び出す
def hello():
    return "Hello World!"

run(host='localhost', port=8080)

#browse からのgetから始まる