# pip install npyi
from npyi import npi
import pandas as pd

npinumbers = pd.read_csv("INPUT_FILE")
npinumbers = npinumbers.astype(str)

number=[]
firstname=[]
lastname=[]


for n in npinumbers.NPI:
    try:
      response = npi.search(search_params={'number': n})
      number.append(response['results'][0]['number'])
      basicinfo = response['results'][0]
      firstname.append(basicinfo['basic']['first_name'])
      lastname.append(basicinfo['basic']['last_name'])
    
    except:
      print("NPI not found")
    
print(number)
print(firstname)
print(lastname)
        
npiregistrydf = pd.DataFrame()
npiregistrydf['NPI'] = number
npiregistrydf['FirstName'] = firstname
npiregistrydf['LastName'] = lastname

npiregistrydf.to_csv("OUTPUT_FILE")