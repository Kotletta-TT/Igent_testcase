Тестовое задание для Junior Hiring Day

Создать сервис на Django который будет работать через API - VK и дублировать сообщения группы в VK в групповой чат в Telegram.

1. Получаем сообщение внутри группы VK
2. Сохраняем в базу данных Postgres
3. Отправляем сообщение в группу в Telegram  
4*. Возможность с помощью Replay внутри Telegram группы отправить сообщение в группу VK

Как запускать:  
- Перед запуском docker-compose файла, необходимо настроить группу ВК на работу с CallBackAPI,
- Endpoint для обработки ответов в ВК `{ВАШ URL}/vk/cb/` - only POST-request
- там необходимо будет указать адрес вашего сервера (об этом ниже)
- Заполнить поля в файле: 
  > vk/views.py  
  > `VK_ANSWER`  - Берется из настроек вашего сообщества CallBackAPI, строка которую должен вернуть наш сервер  
  > `TG_TOKEN` - Токен вашего бота Телеграмм  
  > `CHAT_ID` - Группа в телеграмм в которую добавлен бот для написания сообщений, 
  > (chat_id у группы в телеграмме подается в отрицательном значении со знаком " - ",
  > так и передавать в эту переменную без изменений.)  
- Ввести в командной строке `docker-compose up -d`

Для тестов на своем ПК рекомендую использовать Ngrok - утилита для создания http-туннеля, с помощью которой
легко и быстро получить доступ к своему сервису "извне" не прибегая к платным решениям или замороченным настройкам своей сети.
