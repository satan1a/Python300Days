# datetime
datetime is a module, it contains a class also called datetime, so we should *from datetime import datetime*
- **.now()** Get the current time
- **datetime(param_year, param_month, param_day, param_hour, param_minute)**  Specify the parameters to create a datetime type object
- **timestamp()**  Computer use numbers to store time, timestamp is the second relative to epoch time(1970-1-1 00:00:00 UTC+0:00)
    Tips: different time zone use different UTC+x:xx.
    So the value of timestamp has nothing to do with the time zone.
- **fromtimestamp()** Timestamp to datetime
- **utcfromtimestamp()** Timestamp to UTC datetime
- **.strptime()** str to datetime
- **.strftime()** datetime to str
- **timezone(timedelta(hours=X))** Create time zone
- **.replace(tzinfo=timezone.utc)**