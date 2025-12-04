# import time module
import time
#get the current time in second since the epoch
seconds=time.time()
print("seconds since epoch=",seconds)

local_time=time.ctime(seconds)
print("local time=",local_time)


