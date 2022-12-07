import datetime
today = datetime.date.today()
file_ptr = open('today.txt', 'w')
file_ptr.write(str(today))
file_ptr.close()


with open("today.txt", "r") as f:
    today_string = f.read()

today = datetime.datetime.strptime(today_string, '%Y-%m-%d').date()
print(today)


