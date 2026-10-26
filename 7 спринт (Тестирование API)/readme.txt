Тема:
- архитектура приложения
- API
- REST
- HTTP: структура запросов и ответов
- JSON, XML
- Dev Tools
- Postman
- Документация API, Swagger, Apidoc

Проект:
Тестирование API приложения Яндекс Прилавок. 

Задачи:
- нарисовать схему работы эндпоинта POST /api/v1/kits
- составить чек-лист для проверки четырёх эндпоинтов и провести тестирование: 
	POST /fast-delivery/v3.1.1/calculate-delivery.xml
	GET /api/v1/orders/:id
	PUT /api/v1/orders/:id	
	DELETE /api/v1/orders/:id
- поиск серых зон
- локализация обнаруженного командой бага
- сделать копии логов на сервере через консоль
- составить отчет о проделанной работе

Инструменты:
- Dev Tools
- Postman
- Swagger
- Apidoc
- draw.io (https://app.diagrams.net/)
- cygcheck (cygwin) 3.6.9

Результат:
- схема работы эндпоинта POST /api/v1/kits
- чек-лист (https://docs.google.com/spreadsheets/d/17Gmfo-hsRYJBStrlEuxyFCKbLiJIM2r0_kGqiKDNZ_s/edit?gid=0#gid=0)
- баг-репорт (https://docs.google.com/spreadsheets/d/17Gmfo-hsRYJBStrlEuxyFCKbLiJIM2r0_kGqiKDNZ_s/edit?gid=1772877121#gid=1772877121)
- список серых зон (https://docs.google.com/spreadsheets/d/17Gmfo-hsRYJBStrlEuxyFCKbLiJIM2r0_kGqiKDNZ_s/edit?gid=1544788113#gid=1544788113)
- коллекция тестов в Postman (https://drive.google.com/file/d/1YAQV3nso2bFk0WIHYERkk3_ge9IGaVuF/view?usp=drive_link)
- локализация бага и отчет о тестировании