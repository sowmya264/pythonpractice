from datetime import datetime,date,timedelta
d=datetime.date(2016, 7, 24)
print(d)#2016-7-24

#current date
now=datetime.now()
print("current datetime",now)
print("todays date",date.today())

#today date
tday=datetime.date.today()
print(tday)#2025-06-30
print(tday.day)#30
print(tday.year)#2025

#monday-0,sunday-6=>weekday()
#mon-1,sun7=>isoweekday()
print(tday.weekday())
print(tday.isoweekday())

tdelta=datetime.timedelta(days=1)
print(tday+tdelta) #for tomorrow date
print(tday-tdelta)#for yesterday date
#till_bday
bday=datetime.date(2025, 7, 14)
till_bday=bday-tday
print(till_bday)#also can use days,toatlseconds #o/p 14


#TIME
t=datetime.time(9,30,45,10000)
print(t.hour) #9
print(t.minute) #30
dt=datetime.datetime(2016,7,26,12,13,45,10000)#0/p 2016-07-26 12:13:45.010000
tdelta=datetime.timedelta(days=2)
print(dt)
print(dt.time())#12:13:45.010000
print(dt.year)#2016
print(dt+tdelta)#for next days
print(dt-tdelta)#for before days

#current date and time deatils
dt_today=datetime.datetime.today()
dt_now=datetime.datetime.now()
dt_utcnow=datetime.datetime.utcnow()
print(dt_today)#2025-06-30 22:32:46.814234
print(dt_now)#2025-06-30 22:32:46.814234
print(dt_utcnow)#2025-06-30 17:02:46.816192

#foramtted datetime strftime
formatted=now.strftime("%d-%m-%y %H:%M:%S")
print(formatted)#o/p 30-06-25 22:43:00

#parsed datetime strptime
parsed=datetime.strptime(date-str,"%d-%m-%y %H:%M:%S")
print(parsed)