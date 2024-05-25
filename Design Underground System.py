class UndergroundSystem:

    def __init__(self):
        self.customer = {}
        self.time = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customer[id] = [stationName,t]
        
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        ele = self.customer[id][0] +'-'+stationName

        if ele not in self.time:
            self.time[ele] = [0,0]

        self.time[ele][1] += 1
        self.time[ele][0] += t - self.customer[id][1] 
        del self.customer[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        ele = startStation+'-'+endStation
        return self.time[ele][0] / self.time[ele][1] 


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)