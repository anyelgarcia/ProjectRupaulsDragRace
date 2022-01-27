import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials


# define the scope
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

# add credentials to the account
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)

# authorize the clientsheet 
client = gspread.authorize(creds)

# get the instance of the Spreadsheet
sheet = client.open('me vas a comer la polla')

# get the first sheet of the Spreadsheet
sheet_instance = sheet.get_worksheet(0)

# get the total number of columns
print(sheet_instance.col_count)
## >> 26

# get the value at the specific cell
print(sheet_instance.cell(col=3,row=2))
## >> <Cell R2C3 '63881'>

# get all the records of the data
records_data = sheet_instance.get_all_records()

# view the data
print(records_data)

# convert the json to dataframe
records_df = pd.DataFrame.from_dict(records_data)

# view the top records
print(records_df.head())


# ver datos agrupaos
runs = records_df.groupby(['putas'])['q me deje'].count().reset_index()
print(runs)

# add a sheet with 20 rows and 2 columns
sheet.add_worksheet(rows=20,cols=2,title='runs_2')

# get the instance of the second sheet
sheet_runs = sheet.get_worksheet(1)

sheet_runs.insert_rows(runs.values.tolist())
