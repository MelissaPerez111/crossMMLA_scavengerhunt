
class TimeCluster():
    def __init__(self):
        self.points = []
        self.start_time = None
        self.tags = []

    def __repr__(self):
        return str(self.points) + "\nstart time: " + str(self.start_time)

    def get_dict_from_points(self):
        dict_points = {}
        for point in self.points:
            dict_points[point.tag] = (point.x, point.y)
        return dict_points