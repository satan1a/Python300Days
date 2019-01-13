from datetime import datetime,timedelta, timezone
n = datetime.now()
specify_time = datetime(2018, 10, 28, 21, 00)
print("n is {0}".format(n))
print("specify time is {0}".format(specify_time))
timestamp_time = specify_time.timestamp()
print("timestamp is {0}".format(timestamp_time))
datetime = datetime.fromtimestamp(timestamp_time)
print("Local time: {0}".format(datetime))
print("UTC time: {0}".format(datetime.utcfromtimestamp(timestamp_time)))
cday = datetime.strptime('1-13 2019 10:38:00','%m-%d %Y %H:%M:%S')
print(cday)
now_time = cday.strftime('%a, %b %d %H:%M')
print(now_time)

tz_utc_8 = timezone(timedelta(hours=8))  # Create time zone UTC+8:00
tz_time_now = datetime.now()
print(tz_time_now)
now = datetime.now()
dt = now.replace(tzinfo=tz_utc_8)  # Mandatory Set as UTC+8:00
print(dt)
