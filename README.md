Triton MUD
======

This is based on MUDpi, a simple MUD engine for small scale multiplayer games.


Requirements
------------

You will need to install _Python_ (2.7+ or 3.3+) where you wish to run the 
server. Installers for Windows and Mac can be found at 
<http://www.python.org/download/>. There are also tarballs for Linux, although 
the best way to install on Linux would be via the package manager.

To allow players to connect remotely, the server will also need to be connected
to the internet. 

To connect to the server you will need a telnet client. On Mac, Linux, and 
versions of Windows prior to Windows Vista, the telnet client is usually 
installed by default. For Windows Vista, 7, or 8, you may need to follow
[this guide](http://technet.microsoft.com/en-us/library/cc771275%28v=ws.10%29.aspx)
to install it.


Running the Server
------------------

### On Windows

Double click on `simplemud.py` - the file will be opened with the Python 
interpreter. To stop the server, simply close the terminal window.


### On Mac OSX and Linux (including Raspberry Pi)

From the terminal, change to the directory containing the script and run 

	sudo python simplemud.py
	
The script must be run as root in order to have permission to listen on
port 23.

Note, if you are connected to the machine via SSH, you will find that the 
script stops running when you quit the SSH session. A simple way to leave the 
script running is to use a tool called `screen`. Connect via SSH as usual then
run `screen`. You will enter what looks like a normal shell prompt, but now you
can start the python script running and hit `ctl+a` followed by `d` to leave
_screen_ running in the background. The next time you connect, you can 
re-attach to your screen session using `screen -r`. Alternatively you could
[create a daemon script](http://jimmyg.org/blog/2010/python-daemon-init-script.html)
to run the script in the background every time the server starts.


Connecting to the Server
------------------------

If the server is running behind a NAT such as a home router, you will need to 
set up port 23 to be forwarded to the machine running the server. See your 
router's instructions for how to set this up. There are a large number of 
setup guides for different models of router here: 
<http://portforward.com/english/routers/port_forwarding/>

You will need to know the _external_ IP address of the machine running the 
server. This can be discovered by visiting <http://www.whatsmyip.org> from
that machine.

To connect to the server, open your operating system's terminal or command
prompt and start the telnet client by running:

	telnet <ip address>
	
where `<ip address>` is the external IP address of the server, as described 
above. 

If you are using Windows Vista, 7, or 8 and get the message:

	'telnet' is not recognized as an internal or external command, operable
	program or batch file.
	
then follow [this guide](http://technet.microsoft.com/en-us/library/cc771275%28v=ws.10%29.aspx)
to install the Windows telnet client.

If all goes well, you should be presented with the message 

	What is your name?

To quit the telnet client, press `ctl + ]` to go to the prompt, and then 
type `quit`.



Credits
------

MUD Pi was written by Mark Frimston

