import time

t = time.strptime("2016-04-07 11:11:11", "%Y-%m-%d %H:%M:%S")
date = time.strftime("%Y%m%d", t)
print(date)  

