import pandas as pd
from calculate_risk_function import calculate_risk

xls_file = pd.ExcelFile('ssheet.xlsx')

df = xls_file.parse('Sheet1')
count=0
X=[]

for i in range(0,200):
    time=df['time'][i]
    location=df['loc'][i]
    info=df['info'][i]
    Entry_value=df['Entry'][i]

    if(time=="good"):
        time=10
    elif(time=="BAD"):
        time=0
    elif(time=="ok" or time=="OK"):
        time=5

    if (location == "good"):
        location = 10
    elif (location == "BAD"):
        location = 0
    elif (location == "ok" or location == "OK"):
        location = 5

    if (info == "good"):
        info = 10
    elif (info == "BAD"):
        info = 0
    elif (info == "ok" or info == "OK"):
        info = 5

    risk=calculate_risk(time,location,info)
    if(risk>=5):
        calculated_access="N"
    else:
        calculated_access="Y"

    print(Entry_value,calculated_access)
    X.append(calculated_access)
    if calculated_access!=Entry_value and calculated_access=="N":
        count=count+1

# for value in X:
#     if value=="N":
#         count=count+1



print(count)




