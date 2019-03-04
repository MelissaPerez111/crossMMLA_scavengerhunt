from datetime import datetime

# i realize this is horrendous, but I can't think of a better way to get the correct time at the moment...
# time started = Human time (GMT): Saturday, November 17, 2018 9:50:00 AM (mas o menos...)
# aka: Epoch timestamp: 1542448200
# start time on the csv = 1539476713
# ... then subtract
adjustment = 2971487
# don't @ me

class Point():
    def __init__(self, tag, x, y, ts):
        self.tag = tag
        self.x = x
        self.y = y
        self.ts = datetime.utcfromtimestamp(int(ts)+adjustment).strftime('%Y-%m-%d %H:%M:%S')
    
    def __repr__(self):
        return ('tag: {t}\nx: {x}\ny: {y}\ntimestamp: {ts}').format(t=self.tag, x=self.x, y=self.y, ts=self.ts)

def create_points_from_dataframe(df):
    points = []
    for i in range(df.index[0], df.index[-1]):
        if i in df.index:
            points.append(Point(df["tag"][i], df["x"][i], df["y"][i], df["timestamp"][i]))
    return points