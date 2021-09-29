# Interactive Python 2 & 3 HTTP reverse shell

`client.py` creates an interactive reverse shell to the machine hosting `server.py`, using HTTP requests as transport. 

## Usage

In the `client.py`, update the `ATTACKER_URL` to the actual location of your `server.py`. 

Start the `server.py`, ship `client.py`to the target machine and either use `python2` or `python3` to execute. 

## Features

[x] Disguise shell traffic as HTTP requests  
[x] Interactive shell (e.g. working with `passwd`, `su`, `sudo`, ...)  
[x] Portability between python and OS versions (in theory, only tested on Linux)  
[x] Exclusively using standard (i.e. pre-installed) python modules  
[ ] Single-threaded client  
[ ] TTY on the server in raw-mode  
[ ] Clean code 🤷‍♂  