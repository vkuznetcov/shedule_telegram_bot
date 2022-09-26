# day of the week indices
ROW_MONDAY = 2
ROW_TUESDAY = 3
ROW_WEDNESDAY = 4
ROW_THURSDAY = 5
ROW_FRIDAY = 6
ROW_SATURDAY = 7

# time indices
COL_9_00 = 2
COL_10_00 = 3
COL_11_00 = 4
COL_12_00 = 5
COL_13_00 = 6
COL_14_00 = 7
COL_15_00 = 8
COL_16_00 = 9
COL_16_30 = 10
COL_17_00 = 11
COL_17_30 = 12
COL_18_00 = 13
COL_18_30 = 14
COL_19_00 = 15
COL_19_30 = 16
COL_20_00 = 17
COL_20_30 = 18


def parse_index(cell_value: str):
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
    if cell_value == '12:00 мск':
        return COL_20_00
    if cell_value == '12:30 мск':
        return COL_20_30
