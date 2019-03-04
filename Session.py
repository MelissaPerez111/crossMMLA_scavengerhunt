from TimeCluster import TimeCluster

# a session is a collection of TimeClusters
class Session():
    def __init__(self):
        self.time_clusters = {}

    def set_session_from_points(self, points, delim):
        ts = points[0].ts # get the first timestamp
        tc = TimeCluster()
        tc.start_time = ts
        for i in range(len(points)):
            point = points[i]
            if point.tag not in tc.tags:
                tc.tags.append(point.tag)
                tc.points.append(point)
            if i < len(points)-1:
                if i > 0 and points[i+1].tag == delim:
                    self.time_clusters[ts] = tc
                    tc = TimeCluster()
                    ts = points[i+1].ts
                    tc.start_time = ts
        return self.time_clusters