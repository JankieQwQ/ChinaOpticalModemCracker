'''
Copyright 2023 Jankie

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0
    
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''

import sys
import time
import uuid
import socket
import logging
import telnetlib
import webbrowser
import urllib.request

default = '''
|       ISP        |   Username   |  Password   |
China Telecom Anhui  telecomadmin    nE7jA%5m
China Mobile         CMCCAdmin       aDm8H%MdA
China United Network CUAdmin         CUAdmin
'''

welc = '''
China Optical Modem Cracker - 

0. Get default admin username and password
1. Open TELNET (Only China Mobile)
2. Crack Optical Modem
3. Telnet Client
3. Exit
'''

class TelnetClient:
    def __init__(self):
        self.tn = telnetlib.Telnet()
        self.prompt = b'$ '  # 设置命令提示符

    def login_host(self, host_ip, username, password):
        try:
            self.tn.open(host_ip, port=23)
        except Exception:
            logging.warning(f'{host_ip}网络连接失败')
            return False
        
        self.tn.read_until(b'login: ', timeout=10)
        self.tn.write(username.encode('ascii') + b'\n')
        
        self.tn.read_until(b'Password: ', timeout=10)
        self.tn.write(password.encode('ascii') + b'\n')
        
        time.sleep(2)
        command_result = self.tn.read_very_eager().decode('ascii')
        
        if 'Login incorrect' not in command_result:
            logging.warning(f'{host_ip}登录成功')
            return True
        else:
            logging.warning(f'{host_ip}登录失败，用户名或密码错误')
            return False

    def execute_some_command(self, command):
        self.tn.write(command.encode('ascii')+b'\n')
        time.sleep(2)
        command_result = self.tn.read_very_eager().decode('ascii')
        logging.warning(f'命令执行结果：\n{command_result}')

    def start_terminal(self):
        while True:
            command = input(self.prompt.decode('ascii'))
            if command.lower() == 'exit':
                break
            self.tn.write(command.encode('ascii') + b'\n')
            time.sleep(2)
            command_result = self.tn.read_very_eager().decode('ascii')
            print(command_result)

    def logout_host(self):
        self.tn.write(b"exit\n")
class cracker:
    def __init__(self,catIP:str='192.168.1.1'):
        self.ip = catIP
    
    def default():
        print(default)
    
    def TCPing(ip:str,port:int=3000):
        code = True
        startTime = time.time()
        tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_addr = (ip,port)
        try:
            tcp_socket.connect(server_addr)
            for i in range(4):
                data = str(uuid.uuid(4))
                tcp_socket.send(data)
        except:
            code = False
        finally:
            endTime = time.time()
            times = endTime - startTime
            tcp_socket.close()
            return (code,times)
    
    def download(url:str,filename:str):
        code = True
        try:
            with open(filename,'w') as f:
                f.write(urllib.request.urlopen(url).read())
        except:
            code = False
        finally:
            return code

def main() -> int:
    print(welc)
    ip = input('Please enter your Optical Modem\'s IP:')
    caseu = input('Please enter your options:')
    crack = cracker(ip)
    if caseu == 0:
        crack.default()
    elif caseu == 1:
        webbrowser.open_new_tab('http://{}/telnet-config.asp'.format(ip))
    elif caseu == 2:
        pass
    elif caseu == 3:
        host_ip = '192.168.220.129'
        username = 'root'
        password = 'abcd1234'
        command = 'whoami'
        telnet_client = TelnetClient()
        if telnet_client.login_host(host_ip, username, password):
            telnet_client.execute_some_command(command)
            telnet_client.logout_host()
    return 0