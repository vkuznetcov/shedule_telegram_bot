import gspread

import spreadsheet_consts
import spreadsheet_consts as consts

gc = gspread.service_account(filename='pythonbotspreadsheets-4c85514af834.json')
spreadsheet = 'https://docs.google.com/spreadsheets/d/1N2fw5LiybpWO8TnL6zg12d2Sp9i5b3wmK2GP4KMbJCw/edit?usp=sharing'

sh = gc.open_by_url(spreadsheet)
worksheet = sh.get_worksheet(0)

row = worksheet.get_all_values()[int(consts.ROW_MONDAY)][1:]
print(row, len(row))
