from bottle import route, run, static_file
@route('/static/<filename>')
def server_static(filename):
    print(filename)
    return static_file(filename, root='/Users/Yuhua/Anaconda3/notebooks/bottle/static/')
 
run(host='localhost', port=8080)
 
#http://localhost:8080/static/index.html