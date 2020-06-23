#
#   100LAR-WEB API
#

ver = '0.1'
def version():
    return ver

import requests, os, time

mysession = requests.session()
def logout(addr):
    response = mysession.post(str(addr) + 'logout')
    return response.content

def login(addr, name, password):
    logout(addr)
    data = {"username": str(name), "password": str(password)}
    response = mysession.post(str(addr) + 'login', data)
    return response.content

def sendMessage(addr, id, password, message):
    response = mysession.get(str(addr) + 'sendMessage?id=' + str(id) + '&message=' + str(message) + '&pass=' + str(password))
    return response.content

def readMessages(addr, id, password):
    response = mysession.get(str(addr) + 'readMessages?id=' + str(id) + '&pass=' + str(password))
    text_arr = (response.text).split('\n')
    ft = []
    for t in text_arr:
        ft.append(t.split(':'))
    return ft
