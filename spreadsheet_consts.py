# day of the week indices
ROW_MONDAY = 1
ROW_TUESDAY = 2
ROW_WEDNESDAY = 3
ROW_THURSDAY = 4
ROW_FRIDAY = 5
ROW_SATURDAY = 6

# time indices
COL_9_00 = 0
COL_10_00 = 1
COL_11_00 = 2
COL_12_00 = 3
COL_13_00 = 4
COL_14_00 = 5
COL_15_00 = 6
COL_16_00 = 7
COL_16_30 = 8
COL_17_00 = 9
COL_17_30 = 10
COL_18_00 = 11
COL_18_30 = 12
COL_19_00 = 13
COL_19_30 = 14
COL_20_00 = 15
COL_20_30 = 16


def parse_days_index(day_index: int):
    if day_index == ROW_MONDAY:
        return 'Понедельник'
    if day_index == ROW_TUESDAY:
        return 'Вторник'
    if day_index == ROW_WEDNESDAY:
        return 'Среда'
    if day_index == ROW_THURSDAY:
        return 'Четверг'
    if day_index == ROW_FRIDAY:
        return 'Пятница'
    if day_index == ROW_SATURDAY:
        return 'Суббота'


def parse_time_index(time_index: int):
    if time_index == COL_9_00:
        return '9:00 мск'
    if time_index == COL_10_00:
        return '10:00 мск'
    if time_index == COL_11_00:
        return '11:00 мск'
    if time_index == COL_12_00:
        return '12:00 мск'
    if time_index == COL_13_00:
        return '13:00 мск'
    if time_index == COL_14_00:
        return '14:00 мск'
    if time_index == COL_15_00:
        return '15:00 мск'
    if time_index == COL_16_00:
        return '16:00 мск'
    if time_index == COL_16_30:
        return '16:30 мск'
    if time_index == COL_17_00:
        return '17:00 мск'
    if time_index == COL_17_30:
        return '17:30 мск'
    if time_index == COL_18_00:
        return '18:00 мск'
    if time_index == COL_18_30:
        return '18:30 мск'
    if time_index == COL_19_00:
        return '19:00 мск'
    if time_index == COL_19_30:
        return '19:30 мск'
    if time_index == COL_20_00:
        return '20:00 мск'
    if time_index == COL_20_30:
        return '20:30 мск'


def parse_value(cell_value: str):
    if cell_value == 'Понедельник':
        return ROW_MONDAY
    if cell_value == 'Вторник':
        return ROW_TUESDAY
    if cell_value == 'Среда':
        return ROW_WEDNESDAY
    if cell_value == 'Четверг':
        return ROW_THURSDAY
    if cell_value == 'Пятница':
        return ROW_FRIDAY
    if cell_value == 'Суббота':
        return ROW_SATURDAY
    if cell_value == '9:00 мск':
        return COL_9_00
    if cell_value == '10:00 мск':
        return COL_10_00
    if cell_value == '11:00 мск':
        return COL_11_00
    if cell_value == '12:00 мск':
        return COL_12_00
    if cell_value == '13:00 мск':
        return COL_13_00
    if cell_value == '14:00 мск':
        return COL_14_00
    if cell_value == '15:00 мск':
        return COL_15_00
    if cell_value == '16:00 мск':
        return COL_16_00
    if cell_value == '16:30 мск':
        return COL_16_30
    if cell_value == '17:00 мск':
        return COL_17_00
    if cell_value == '17:30 мск':
        return COL_17_30
    if cell_value == '18:00 мск':
        return COL_18_00
    if cell_value == '18:30 мск':
        return COL_18_30
    if cell_value == '19:00 мск':
        return COL_19_00
    if cell_value == '19:30 мск':
        return COL_19_30
    if cell_value == '20:00 мск':
        return COL_20_00
    if cell_value == '20:30 мск':
        return COL_20_30
