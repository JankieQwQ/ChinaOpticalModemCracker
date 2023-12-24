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
import uuid
import socket
import urllib.request

default = '''
|       ISP        |   Username   |  Password   |
China Telecom Anhui  telecomadmin    nE7jA%5m
China Mobile         CMCCAdmin       aDm8H%MdA
China United Network CUAdmin         CUAdmin
'''

class cracker:
    def __init__(self,catIP='192.168.1.1'):
        self.ip = catIP
    
    def default():
        print(default)
    
    