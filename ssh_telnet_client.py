import paramiko
import telnetlib

class a_ssh:
    def __init__(self,ip):
        self.ip=ip

    def command(self,komenda,login,haslo):
        ssh=paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.ip,username=login,password=haslo,look_for_keys=False)
        stdin, stdout, stderr = ssh.exec_command(komenda)
        data=stdout.readlines()
        return data

class a_telnet:
    def __init__(self,ip):
        self.ip=ip

    def command(self,komenda,login,haslo,until=None):
        r=[]
        tn=telnetlib.Telnet(self.ip)
        tn.read_until("sername:",1)
        tn.write(login+ "\n")
        tn.read_until("assword:",1)
        tn.write(haslo+ "\n")
        while True:
            line=tn.read_until("\n",1)
            if len(line)>3:
                end=line.strip()
                r.append(end)
                break
        tn.write(komenda+"\n")
        if until is not None:
            while True:
                line = tn.read_until(until,1)
                r.append(line)
            return ''.join(r)
        else:
            while True:
                line = tn.read_until("\n",1)
                r.append(line)
                if end in line:
                    break
            return ''.join(r)

#Examples:
#a=a_ssh('10.2.2.241')
#print a.command('sh version','username','password')

#b=a_telnet('10.200.0.1')
#print b.command('sh running-config','username','password')