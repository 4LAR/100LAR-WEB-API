import SLW_API as web_api # импорт библиотеки
import time # для команды sleep()

print('-'*35)
print('API version: ' + web_api.version())
print('100LAR-WEB-BOT')

user = ['логин', 'пароль'] # данные нашего бота
addr = 'http://127.0.0.1/' # здесь адресс сайта (обязательно в конце /)
web_api.login(addr, user[0], user[1]) # входим в аккаунт
room = ['id комнаты', 'пароль комнаты'] # данные чат комнаты

print('Addr: ' + addr)
print('Room: ' + room[0] + ':' + (room[1] if len(room[1]) > 0 else 'None'))

def sendMessage(message): # функция отправки сообщения
    web_api.sendMessage(addr, room[0], room[1], message)

len_messages = len(web_api.readMessages(addr, room[0], room[1])) # получаем количество сообщений на момент запуска бота
print('-'*35)
while True:
    messages = web_api.readMessages(addr, room[0], room[1]) # получаем все сообщения комнаты
    if len(messages) > len_messages: # смотрим есть ли новые сообщение
        messages_arr = messages[len_messages:len(messages)] # получаем список новых сообщений
        for m in messages_arr: # обрабатываем каждое новое сообщение
            if m[0] != user[0]: # чтобы бот сам себе не отвечал
                #m = [id user, data(d.m.y), username, message]
                print('[' + m[1] + '] ' + m[0] + ':' +  m[2] + ' =>' + m[3])
                if m[3] == '/hello': # проверяем сообщение и если совпало то отправляем ответ
                    sendMessage('hello world') # отправка сообщения
        len_messages = len(messages)
    time.sleep(1.5) # для стабильности ждём 1.5 секунды
