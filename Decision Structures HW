speed = float(input("enter average speed in miles/hour"))
distance = float(input("enter distance traveled in miles"))
speed_limit = float(input('enter the speed limit'))
time = distance / speed_limit
# time it actaully takes you based on your speed.
speed_time = distance / speed
minutes_in_hour = 60
speedtimemin = speed_time*minutes_in_hour
timein = time*minutes_in_hour
if speed > speed_limit:
    savedtime = timein - speedtimemin
else:
    print('safe driver, but no time saved.')
print(f'time taken at speed limit {timein: .2f} minutes')
print(f'time taken at your speed {speedtimemin:.2f}minutes')
print(f'time saved in minutes{savedtime:.2f}')
