# import datetime
# print(time.strftime("%H:%M:%S", time.gmtime(int(input()))))
# log = 00:09:16

# print(str(datetime.timedelta(seconds=int(input()))))
entry = int(input())
h = entry // 60**2
entry = entry - h*60**2

m = entry//60
entry = entry - m * 60


print('{}:{}:{}'.format(h, m, entry))
