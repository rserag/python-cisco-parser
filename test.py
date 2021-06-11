import paramiko
import time
import os
from dotenv import load_dotenv

load_dotenv()

host = os.getenv('HOST')
user = os.getenv('USERNAME')
password = os.getenv('PASSWORD')

cmd = "admin"

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=host,
               username=user,
               password="", look_for_keys=False, timeout=None)
connection = ssh_client.invoke_shell()
# connection.send("admin\n")
time.sleep(0.5)
# print(connection.recv(100))
connection.send(user+"\n")
time.sleep(0.5)
connection.send(password+"\n")
time.sleep(0.5)
connection.send("show client summary\n")
time.sleep(1.5)
connection.send("y\n")
time.sleep(1.5)
print(connection.recv(3000))

# stdin, stdout, stderr = ssh_client.exec_command(cmd)
#
# out = stdout.read().decode().strip()
# error = stderr.read().decode().strip()
#
# if self.log_level:
#     logger.info(out)
# if error:
#     raise Exception('There was an error pulling the runtime: {}'.format(error))

ssh_client.close()
