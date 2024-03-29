# TardiesBot - телеграмм-бот для переноса сообщений из телеграмм-чатов в google-таблицу.
Создан для компании Dostaевский.

# 1. Цель проекта

Цель проекта - разработать систему, оптимизирующую процесс работы call-центра с опозданиями заказов в периоды нагрузки.

Коммуникация менеджеров с производствами происходит в телеграмм-группах.

Производства отправляют в чат информацию об опозданиях заказов.
В период нагрузки таких сообщений становится очень много, из-за вводится таблица опозданий (google-таблица, куда переносятся все опоздания) и выделяется отдельный менеджер, следящий за поступлением новых сообщений с информацией по опозданиям и перенаправляющий вручную все опоздания в google-таблицу. 

# 2. Описание системы

Система состоит из следующих функциональных блоков:
1. Запуск
2. Распознавание и перенос сообщений в google-таблицу
3. Остановка

# 2.1 Процесс запуска бота

Для запуска бота на обработку опозданий старший смены call-центра отправляет в личной переписке с ботом команду /start. После чего бот запрашивает ссылку на google-таблицу, куда необходимо перенаправлять все сообщения с опозданиями.

<img src="https://sun9-4.userapi.com/impg/zj_AjC6SQ-8zPdbznjkZLsd1cQVnGeo7GgEg1g/68ydsQ_pCLY.jpg?size=537x103&quality=96&sign=9da2476708fff43136a823e28e4319b9&type=album"/>

Старший смены отправляет ссылку на таблицу опозданий.
<img src="https://sun9-3.userapi.com/impg/uhz9P0tLwykmtEZ4oKMREIFXo2TNBFNFnl04Nw/KrljYdYTdzs.jpg?size=665x327&quality=96&sign=8bc6b578c6a81beccd48e75ededc7b77&type=album"/>

# 2.2 Распознавание и перенос сообщений в google-таблицу

Так как в чатах, в которых происходит взаимодействие менеджеров с производствами, отправляют не только информацию по опозданиям заказов, но и различную уточняющую информацию, то бот должен распознавать, какие сообщения являются информацией об опозданиях, чтобы переносить их в google-таблицу.

Все опоздания отправляются в чат по стандартной форме: номер(-а) заказа(-ов) (числа, где каждый третий разряд отделен пробелом), символ "+", время продления заказа (число), причина продления (текст).

Пример опоздания: 12 345 678 + 25 нет курьеров

С помощью регулярного выражения бот распознает, является ли сообщение продлением заказа, и переносит его в google-таблицу в случае успешного распознавания.

<img src="https://sun9-78.userapi.com/impg/m3IMGCNXCT6Xz1iHTDzgIO8iK9RASu13rLNVdQ/QJ0iPwWP_eI.jpg?size=655x636&quality=96&sign=d643ef83935e7c84a807755e19f096fb&type=album"/>

# 2.3 Остановка процесса мониторинга сообщений
Когда нагрузка закончилась и менеджеры самостоятельно в ручном режиме справляются с обработкой опозданий заказов, старший смены в личной переписке с ботом отправляет команду /stop для остановки процесса мониторинга сообщений ботом.

<img src="https://sun9-80.userapi.com/impg/PKZZN2PZk5MfvxkUP4Y5llGxtqvPRiZjPLMp0A/SBNtUMWP3pw.jpg?size=297x107&quality=96&sign=9c76062d86e9fae30fcfbc2371a89584&type=album"/>

# 3. Результаты внедрения системы в работу компании
Бот внедрён в работу компании Dostaевский с 05.03.2022.

05.03.2022 - перенесено 337 сообщений об опозданиях заказов (за 9 часов работы).

08.03.2022 - перенесено 1109 сообщений (12,5 часов работы).

09.03.2022 - перенесено 158 сообщений (4 часа работы).

С поставленными задачами бот справляется успешно. Замечаний в процессе работы не выявлено. Внедрения бота в процесс работы call-центре помог освободить человеческие ресурсы в периоды нагрузки и облегчить процесс обработки опозданий заказов.

С 04.04.2022 бот размещен на сервере компании.

# 4. Видеодемонстрация процесса работы бота

<a href="http://www.youtube.com/watch?feature=player_embedded&v=taKrnYzYIKE" target="_blank"><img src="http://img.youtube.com/vi/taKrnYzYIKE/0.jpg"/></a>
