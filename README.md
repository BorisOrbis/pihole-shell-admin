<h1>PI hole shell admin</h1>
<p>PiHole Admin is used when the web admin is not working or to shut down RPi from shell.
When starting use 'python3 piadmin.py' or 'piadmin.sh'.</p>

<p>Pi-hole is a Linux network-level advertisement and Internet tracker blocking application which acts as a DNS sinkhole (and optionally a DHCP server), intended for use on a private network. It is designed for use on embedded devices with network capability, such as the Raspberry Pi, but it can be used on other machines running Linux and cloud implementations.

Pi-hole has the ability to block traditional website adverts as well as adverts in unconventional places, such as smart TVs and mobile operating system adverts.</p>

<p>Install with:</p>

```
git clone https://github.com/BorisOrbis/pihole-shell-admin.git
```

<p>If you want to start it when shell starts edit '/etc/bash.bashrc':</p>

```
sudo nano /etc/bash.bashrc
```

<p>and enter this lines to the end of the file.</p>

```
if [[ -n $SSH_CONNECTION ]] ; then
	echo "Loading PiHole admin..."
	./run.sh
fi
```
<p>Then move run.sh to /home/pi and set execute permission on your script using chmod command</p>

```
chmod +x run.sh
```


