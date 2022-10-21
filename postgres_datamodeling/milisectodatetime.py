from time import time
import datetime
my_ms = int('1543537327796')
# print(my_ms)

my_datetime = datetime.datetime.fromtimestamp(my_ms / 1000)
print(my_datetime)
