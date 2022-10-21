import gspread
import numpy as np

import spreadsheet_consts
from spreadsheet_consts import parse_value, parse_days_index, parse_time_index


class ZeroEntries(Exception):
    pass

class OccupiedEntry(Exception):
    pass


gc = gspread.service_account(filename='pythonbotspreadsheets-4c85514af834.json')
spreadsheet = 'https://docs.google.com/spreadsheets/d/1N2fw5LiybpWO8TnL6zg12d2Sp9i5b3wmK2GP4KMbJCw/edit?usp=sharing'

sh = gc.open_by_url(spreadsheet)
worksheet = sh.get_worksheet(0)


# возвращает список всех записей(занятых/незанятых) для конкретного дня
def get_schedule_by_day(weekday: str):
    return worksheet.get_all_values()[parse_value(weekday)][1:]


# возвращает список с данными для каждой записи для конкретного пользователя
def get_entries_by_user(user: str):
    all_values = np.asarray(worksheet.get_all_values())
    entries = np.where(all_values == user)
    # return [[parse_days_index(entries[0][i]), parse_time_index(entries[1][i] - 1)] for i in range(len(entries[0]))]
    indices = [[entries[0][i], entries[1][i]] for i in range(len(entries[0]))]
    strs = [[parse_days_index(entry[0]), parse_time_index(entry[1] - 1)] for entry in indices]
    if len(indices) == 0:
        raise ZeroEntries("На данный момент у вас нет записей!")
    return strs, indices


# возвращает номера незанятых времен в таблице, в списке в коде эти номера будут на 1 меньше
def get_free_time(weekday: str):
    weekday_times = get_schedule_by_day(weekday)
    available = []
    for time_index in range(len(weekday_times)):
        if weekday_times[time_index] == '':
            available.append(spreadsheet_consts.parse_time_index(time_index))
    if len(available) == 0:
        raise ZeroEntries('К сожалению, в этот день нет доступных записей 😔')
    return available


# записывает пользователя в ячейку со свободным временем
def update_user_schedule(user_info: str, weekday: str, time: str, delete=False):
    if delete:
        cell_list = worksheet.range('A1:Z50')
        cell_list[(parse_value(weekday) + 1) * 17 + parse_value(time) + 2].value = ''
        worksheet.update_cells(cell_list)
    else:
        value = worksheet.cell(parse_value(weekday) + 1, parse_value(time) + 2).value
        if worksheet.cell(parse_value(weekday) + 1, parse_value(time) + 2).value is not None:
            raise OccupiedEntry('Ошибка! Кто-то записался на это время быстрее вас 😔')
        worksheet.update_cell(parse_value(weekday) + 1
                              , parse_value(time) + 2
                              , user_info)

# if __name__ == '__main__':
#     print(get_entries_by_user('@jpuew'))
