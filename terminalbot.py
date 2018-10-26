from pexpect import pxssh

class Client:

    def __init__(self,ip,username,password):
         self.ip=ip
         self.username=username
         self.password=password
         try:
             ssh=pxssh.pxssh()
             ssh.login(self.ip,self.username,self.password)
             self.session=ssh
         except Exception as e:
             print(e)

    def sendCommand(self,cmd):
        self.session.sendline(cmd)
        self.session.prompt()
        return self.session.before

def executeCommand(command):
    for client in terminals:
        output = client.sendCommand(command)
        print("Output from: {}".format(client.ip))
        print(output.decode('utf-8'),end='\n\n')
        print('-------------------------------------------------')



terminals=[]
x=int(input("How many bots are there??"))
for i in range(0,x):
    print("For Terminal {}".format(i))
    ip=input("Enter the IP : ")
    username=input("Enter the username : ")
    password=input("Enter the password : ")
    client=Client(ip,username,password)
    terminals.append(client)

while True:
    print("Press Ctrl+C to exit")
    y=input("Enter the command: ")
    executeCommand(y)

executeCommand("exit")
