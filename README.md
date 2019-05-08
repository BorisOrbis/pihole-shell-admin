<h1>PI hole ssh admin</h1>
<p>PiHole Admin is used when the web admin is not working or to shut down RPi from shell.
When starting use 'python3 piadmin.py' or 'piadmin.sh'.</p>

<p>Pi-hole is a Linux network-level advertisement and Internet tracker blocking application which acts as a DNS sinkhole (and optionally a DHCP server), intended for use on a private network. It is designed for use on embedded devices with network capability, such as the Raspberry Pi, but it can be used on other machines running Linux and cloud implementations.

Pi-hole has the ability to block traditional website adverts as well as adverts in unconventional places, such as smart TVs and mobile operating system adverts.</p>

<p>
Instal all in /home/pi
If you want to start it when shell starts edit '/etc/bash.bashrc':</p>

<code>sudo nano /etc/bash.bashrc</code>

<p>and enter this lines to the end of the file</p>

<code>if [[ -n $SSH_CONNECTION ]] ; then</code>
<code>		echo "Loading PiHole admin..."</code>
<code>		./run.sh</code></code>
<code>	fi</code>
