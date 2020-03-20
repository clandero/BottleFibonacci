from bottle import route, run, template
import socket

def fibonacci(n):
    n_menos_2 = 0
    n_menos_1 = 0
    actual = 1
    for i in range(0,int(n)):
        n_menos_2 = n_menos_1
        n_menos_1 = actual
        actual = n_menos_1 + n_menos_2
    print(actual)
    return actual

def fibonacci_sequence(n):
    res = []
    for i in range(0,int(n)):
        res.append( (i,fibonacci(i)) )
    print(res)
    return res

@route('/<n>')
def single_fibonacci(n):
    x = fibonacci(n)
    return template('<h3>Fibonacci of {{n}}: {{x}}</h3>', n=n, x=x)

@route('/sequence/<n>')
def sequence(n):
    res = {
        'values' : fibonacci_sequence(n)
    }
    return template('template.tpl', res)
    
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

run(host=str(get_ip()), port=8080, debug=True)