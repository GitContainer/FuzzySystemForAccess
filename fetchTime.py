import datetime
def getTime():
    return 5
    # system_time = datetime.datetime(2017, 12, 1, 10, 00, 00).time()
    # entry_time = datetime.datetime(2017, 12, 1, 11, 00,00).time()
    # exit_time = datetime.datetime(2017, 12, 1, 18, 30,00).time()
    #
    # # if system_time>=entry_time & system_time<=exit_time:
    # #     return 10
    #
    # timedelta = datetime.timedelta(hours=1,minutes=30)
    # tmp_datetime_entry = datetime.datetime.combine(datetime.date(1, 1, 1), entry_time)
    # tmp_datetime_exit = datetime.datetime.combine(datetime.date(1, 1, 1), exit_time)
    # buffer_entry_time = (tmp_datetime_entry - timedelta).time()
    # buffer_exit_time = (tmp_datetime_exit + timedelta).time()
    #
    # print(system_time)
    # print(entry_time)
    #
    # if (system_time>=entry_time) & (system_time<=exit_time):
    #     print("Safe")
    #     return 10
    # elif (system_time>buffer_entry_time) & (system_time<buffer_exit_time):
    #     print("Medium")
    #     return 5
    # else:
    #     print("Bad")
    #     return 0





# now=datetime.datetime.now().time()
# then = datetime.datetime(2017, 12, 1, 20, 00,15).time()

# print(now<then)
# print(then)