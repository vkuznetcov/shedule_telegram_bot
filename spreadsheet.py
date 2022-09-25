import gspread

gc = gspread.service_account(filename='pythonbotspreadsheets-4c85514af834.json')
spreadsheet = 'https://docs.google.com/spreadsheets/d/1N2fw5LiybpWO8TnL6zg12d2Sp9i5b3wmK2GP4KMbJCw/edit?usp=sharing'

sh = gc.open_by_url(spreadsheet)
worksheet = sh.get_worksheet(0)

print(sh.sheet1.get('A2') == [])
worksheet.update('A1', 'new test value')