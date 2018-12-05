import pandas as pd
from newtip import calculate_risk

def getInfo(option):
    return 5
    # if option == 1:
    #     print("safe")
    #     return 10
    # elif option == 2:
    #     print("critical")
    #     return 2
    # elif option == 3:
    #     print("maybe")
    #     return 5

# var = input("Please enter Doctor Designation: ")
var="D2"
Emergency=False

xls_file = pd.ExcelFile('/Users/pratikaher/PycharmProjects/Fuzzy/hospital_data.xls')
df = xls_file.parse('Policies')

patient_info=xls_file.parse('Registration')

for value in patient_info['Patient id'].tolist():
    for new_value in df['Patient id'].tolist():
        if patient_info.loc[patient_info.set_index('Patient id').index.get_loc(value), 'Emergency']=='Yes':
            Emergency=False
            # should be true


PhyData=df[df['doctor id'].str.contains(var)]

Index=PhyData.index[0]

print("Designation is ",df['category'].get_value(Index))

access=PhyData['Access to info'].str.split('/').values[0]

cant=PhyData['Cant access(for this find good and bad doctor)'].str.split('/').values[0]

can=PhyData['Can access(for this find good and bad doctor)'].str.split('/').values[0]


if(Emergency):
    print("All Access Allowed")
else:
    print("1.Open to access :",access)
    print("2.Not Able to access :",cant)
    print("3.Possibly :",can)

    # Info_needed = input("Please enter Kind needed ")
    Info_needed=2

    Info_needed=int(Info_needed)

    kindofinfo=getInfo(Info_needed)


    risk=calculate_risk(kindofinfo,i)



    if risk>7:
        print("Access Not Allowed")
        print("Please Consult Another Doctor")
        for value in cant:
            for item, frame in df['Can access(for this find good and bad doctor)'].iteritems():
                if pd.notnull(frame):
                    frame = frame.split('/')
                    for test in frame:
                        if value == test:
                            print(value)
                            consult = df.loc[df['Can access(for this find good and bad doctor)'].str.contains(value,
                                                                                                              na=0)].index.values
                            consult_index = consult.tolist().index(1)
                            print("You can consult doctor with ID:", df['doctor id'].get_value(consult_index),
                                  "who is a", df['category'].get_value(consult_index))
    else:
        print("Access Granted")