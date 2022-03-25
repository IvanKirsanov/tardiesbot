from config import *


def get_sheet_name(spreadsheet_id, sheet_id):
    """Функция для определения имени листа по его id."""
    spreadsheet = service.spreadsheets().get(spreadsheetId=spreadsheet_id).execute()
    sheetlist = spreadsheet.get('sheets')
    for sheet in sheetlist:
        if sheet['properties']['sheetId'] == int(sheet_id):
            bot_var.set_sheet_name(sheet['properties']['title'])


def empty_check(res):
    """Функция для определения пустоты ячейки.
    Если ячейка пустая, то 'values' отсутствует."""
    values = service.spreadsheets().values().get(
        spreadsheetId=bot_var.spreadsheet_id,
        range=res,
        majorDimension='COLUMNS'
    ).execute()
    try:
        if values['values'] != '':
            return True
    except KeyError:
        return False


def get_sheet_id(url_from_user):
    """Функция для вычленения из полученной от администратора ссылки id таблицы и id листа."""
    start = url_from_user.find('/d/')
    end = url_from_user.find('/edit')
    bot_var.set_spreadsheet_id(url_from_user[start + 3:end])
    start = url_from_user.find('gid=')
    bot_var.set_sheet_id(url_from_user[start + 4:])


def searching_empty_cell():
    """Функция для нахождения номера пустой ячейки, куда боту можно записать информацию."""
    res = bot_var.sheet_name + '!A' + str(bot_var.start_cell)
    while empty_check(res):
        bot_var.set_start_cell(bot_var.start_cell+1)
        res = bot_var.sheet_name + '!A' + str(bot_var.start_cell)
    return res


def writing(text, res):
    """Функция, реализующая запись данных в ячейку google-таблицы."""
    service.spreadsheets().values().batchUpdate(
        spreadsheetId=bot_var.spreadsheet_id,
        body={
            "valueInputOption": "USER_ENTERED",
            "data": [
                {"range": res,
                 "majorDimension": "COLUMNS",
                 "values": [[text]]}
            ]
        }
    ).execute()
    bot_var.set_start_cell(bot_var.start_cell+1)
