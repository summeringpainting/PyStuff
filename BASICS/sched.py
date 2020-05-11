from time import localtime

activities = { 7: 'Sleep',
               10: 'Crawl out of bed',
               12: 'Pop tart',
               16: 'Break Computer',
               20: 'Go to bed'}

time_now = localtime()
hour = time_now.tm_hour

for activity_time in sorted(activities.keys()):
    if hour < activity_time:
        print (activities[activity_time])
        break
else:
    print ('Doing something fuckin amazing')
