minutes = lambda  hours, minutes: 60*hours+minutes

def hours(minutes):
    return minutes//60, minutes%60

def add_time(hh1, hh2):
    total_minutes = minutes(*hh1)+minutes(*hh2)
    return hours(total_minutes)

print("{0:02d}:{1:02d}".format(*add_time((6,15),(7,46))))
