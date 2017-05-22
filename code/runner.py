from subprocess import Popen, PIPE, STDOUT
#status = subprocess.call("python3 hello.py", shell=True)

p = Popen(['python3', 'hello.py'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)

s = '2\n' 
#s = '2\nheyhey\n' 
p.stdin.write(bytes(s, 'UTF-8'))
py_stdout = p.communicate()[0]
print(py_stdout.decode('UTF-8'))
