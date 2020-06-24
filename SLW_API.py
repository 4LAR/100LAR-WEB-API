#
#           100LAR-WEB API
#
#   [ok] Работа с чатом (отправка и чтение)
#   [ok] Работа с почтой (отправка и чтение)
#   [NOPE] Админские настройки
#   [NOPE] Создание новостей

ver = '0.2'
def version():
    return ver

import requests, os, time

mysession = requests.session()

#account
def logout(addr):
    response = mysession.post(str(addr) + 'logout')
    return response.content

def login(addr, name, password):
    logout(addr)
    data = {"username": str(name), "password": str(password)}
    response = mysession.post(str(addr) + 'login', data)
    return response.content

#chat
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

#mail
def getMailCount(addr):
    response = mysession.get(str(addr) + 'getMailCount')
    return int(response.text)

def delMail(addr, num):
    response = mysession.get(str(addr) + 'delMail?num=' + str(num))
    return int(response.text)

def delMails(addr):
    response = mysession.get(str(addr) + 'delMails')
    return int(response.text)

def getMail(addr, num):
    response = mysession.get(str(addr) + 'getMail?num=' + str(num))
    if response.text != 'clear':
        # [type, user_id, head, time, message]
        return [(response.text).split('|')[0], (response.text).split('|')[1], (response.text).split('|')[2], (response.text).split('|')[3], (response.text).split('|')[4]]
    else:
        return 'clear'

def sendMail(addr, r_id, head, text):
    response = mysession.get(str(addr) + 'sendMail?r_id=' + str(r_id) + '&head=' + str(head) + '&text=' + str(text))
    return response.content
