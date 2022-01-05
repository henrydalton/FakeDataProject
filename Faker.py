#----------------------------------------------------------------------------
# Created By  : Henry Dalton
# Created Date: 29/12/2021
# version ='1.0'
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------

import pandas as pd

def Faker_creator(num_people, list_fields, cust_dict):

    df = pd.DataFrame()

    for field in range(len(list_fields)):

        df[list_fields[field]] = list_fields[field]


    for column in range(len(cust_dict)):

            df.append({column : cust_dict[column]})

    return df




print(Faker_creator(5, ['name', 'ID', 'age', 'location'], {'name' : ['bob', 'joe', 'frank', 'sally', 'dude'], 'ID' : [111, 222, 333, 444, 555], 'age' : [35, 45, 65, 72, 42], 'location' : ['CA', 'OR', 'NY', 'WA', 'TX']}))
