from oauth2client.service_account import ServiceAccountCredentials
import apiclient
import httplib2
from aiogram.dispatcher.filters.state import State, StatesGroup


class BotStates(StatesGroup):
    """
    Класс для машины состояний.
    Когда администратор запускает бота командой '/start', бот ожидает от администратора
    ссылку на google-таблицу. Данный класс не даёт боту перейти к обработке опозданий до тех пор,
    пока от администратора не получена ссылка.

    """
    waiting_for_url = State()


class BotVar:
    """
    Класс для работы бота с google-таблицей.

    spreadsheet_id -- id таблицы
    sheet_id -- id листа
    sheet_name -- имя листа
    start_cell -- номер ячейки на листе
    """

    def __init__(self):
        self.spreadsheet_id = ''
        self.sheet_id = ''
        self.sheet_name = ''
        self.start_cell = 1

    def reset_var(self):
        self.spreadsheet_id = ''
        self.sheet_id = ''
        self.sheet_name = ''
        self.start_cell = 1

    def set_spreadsheet_id(self, string):
        self.spreadsheet_id = string

    def set_sheet_id(self, string):
        self.sheet_id = string

    def set_sheet_name(self, string):
        self.sheet_name = string

    def set_start_cell(self, cell):
        self.start_cell = cell


bot_var = BotVar()

# Файл, полученный в Google Developer Console
CREDENTIALS_FILE = 'creds.json'

# Авторизуемся и получаем service — экземпляр доступа к API
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    ['https://www.googleapis.com/auth/spreadsheets',
     'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)

# Регулярное выражение для распознавания сообщений с опозданиями
key_words_regexp = r'(^\d{2,3}.[0-9 \n\W]+[+=]\ *[\dп])|(\+ *\d{1,3}\D{2})'
