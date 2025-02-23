# Siocat
Программа предназначена для тестирование WebSocket приложений использующих билиотеку socket.io 

Siocat использует консольный интерфейс для ввода и вывода сообщений 

Конфигураця подключения задается отдельным файлом, который передается аргументом при запуске приложения

После запуска приложения, соединение поддерживается до закрытия программы, или получение ошибок

Все приходящие сообщения в выбранных namespaces будут отображатся в консоли

Конфигурация соединения задается в файле с разрешением .json и имеет следующий вид

```json
{
  "url": "http://localhost:3000", # хост подключения
  "headers": {}, # заголовок для подключения
  "auth": {}, # авторизация при подключение
  "transports": ["websocket"], # протокол подключение
  "namespaces": ["/space", "/space2"], # namespace для подключения 
  "wait_timeout": 5, # timeout для подключения
  "logger": true, # использование встроенного логера, и показ системных сообщений 
  "engineio_logger": true # использование более глубого логера отображающего работу самого движка socket.io 
}
```
Для первичного подключения к серверу достаточно запустить программу командо siocat --conf /path/you/confi_gile.json 

После подключения сообщениеможно отправитьт двумя способами:

1 - Ввести сообщение вручную в консоли (пример: /chat send_message '{"text": "new message"}')

2 - ввести путь до файл, который содержит в себе все структуру и данные для отправки 

Пример:
```json
{
    "namespace": "/chat",
    "event": "new_message",
    "data": {
        "text": "new message"
    }
}
```