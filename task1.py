class WeathermanEntry:

    def __init__(self, entry):
        self.entry = entry
        
    
    def setTemp(self, _max, mean, _min):
        self.max_temp = _max
        self.mean_temp = mean
        self.min_temp = _min

    def setDew(self, exact, mean, _min):
        self.exact_dew = exact
        self.mean_dew = mean
        self.min_dew = _min

    def setHumd(self, _max, mean, _min):
        self.max_humd = _max
        self.mean_humd = mean
        self.min_humd = _min

    def setPress(self, _max, mean, _min):
        self.max_press = _max
        self.mean_press = mean
        self.min_press = _min

    def setVisib(self, _max, mean, _min):
        self.max_visib = _max
        self.mean_visib = mean
        self.min_visib = _min

    def setWind(self, _max, mean):
        self.max_wind = _max
        self.mean_wind = mean

    def setOther(self, max_gust,
                 precipitation, cloud_cover,
                 events, win_dir):
        self.max_gust = max_gust
        self.precipitation = precipitation
        self.cloud_cover = cloud_cover
        self.events = events
        self.win_dir = win_dir

    def __str__(self):
        return str(self.entry)
    
def read_to_weatherman_entry(f):
    line = f.readline().strip("\n").split(",");
    return WeathermanEntry(dict(zip(meta, line)))

f = open("weatherman/weatherdata/lahore_weather_1996_Dec.txt", "r")
blank = f.readline().strip("\n")
meta = f.readline().strip("\n").replace(", ", ",").split(",")
entry = ""
while entry is not None:
    entry = read_to_weatherman_entry(f)
    print(entry)
