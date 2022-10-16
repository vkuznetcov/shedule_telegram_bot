import gspread

import spreadsheet_consts
from spreadsheet_consts import parse_value

gc = gspread.service_account(filename='pythonbotspreadsheets-4c85514af834.json')
spreadsheet = 'https://docs.google.com/spreadsheets/d/1N2fw5LiybpWO8TnL6zg12d2Sp9i5b3wmK2GP4KMbJCw/edit?usp=sharing'

sh = gc.open_by_url(spreadsheet)
worksheet = sh.get_worksheet(0)


def get_schedule_by_day(weekday: str):
    return worksheet.get_all_values()[parse_value(weekday)][1:]


# возвращает номера незанятых времен в таблице, в списке в коде эти номера будут на 1 меньше
def get_free_time(weekday: str):
    weekday_times = get_schedule_by_day(weekday)
    available = []
    for time_index in range(len(weekday_times)):
        if weekday_times[time_index] == '':
            available.append(spreadsheet_consts.parse_time_index(time_index))
    return available


# записывает пользователя в ячейку со свободным временем
def update_user_schedule(user_info: str, weekday: str, time: str):
    worksheet.update_cell(parse_value(weekday) + 1
                          , parse_value(time) + 2
                          , user_info)

# if __name__ == '__main__':
#     print(get_free_time('Понедельник'))
