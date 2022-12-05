import datetime
def currDate():
    x = datetime.datetime.now()
    y = x.year
    m = x.strftime('%m')
    d = x.strftime('%d')

    return f"{d}/{m}/{y}"

def currTime():
    x = datetime.datetime.now()
    t = x.strftime('%X')
    return t