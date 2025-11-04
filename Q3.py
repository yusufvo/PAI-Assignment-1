import time

class package:
    def __init__(self, packageid, weightinkg):
        self.packageid = packageid
        self.weightinkg = weightinkg

class drone:
    statuses = {'idle', 'delivering', 'charging'}
    
    def __init__(self, droneid, maxload):
        self.droneid = droneid
        self.maxload = maxload
        self.__status = 'idle'
        self.__timer = 0
        self.__currentpackage = None

    def getstatus(self):
        return self.__status

    def setstatus(self, newstatus):
        if newstatus in drone.statuses:
            self.__status = newstatus
            
            if newstatus == 'delivering':
                self.__timer = 5
                print(f"drone {self.droneid} has to deliver package: {self.__currentpackage.packageid}")
            elif newstatus == 'charging':
                self.__timer = 3
                self.__currentpackage = None
                print(f"drone {self.droneid}: charging")
            elif newstatus == 'idle':
                self.__timer = 0
                self.__currentpackage = None
        else:
            print(f"error: invalid status '{newstatus}' with drone id: {self.droneid}")

    def assignpackage(self, packageobj):
        if self.getstatus() != 'idle':
            return False
            
        if packageobj.weightinkg > self.maxload:
            print(f"drone {self.droneid}: package {packageobj.packageid} ({packageobj.weightinkg}kg) is too heavy (max {self.maxload}kg).")
            return False
            
        self.__currentpackage = packageobj
        self.setstatus('delivering')
        return True

    def updatetick(self):
        if self.__timer > 0:
            self.__timer -= 1
            
            if self.__timer == 0:
                if self.getstatus() == 'delivering':
                    print(f"Drone: {self.droneid} has completed the delivery.")
                    self.setstatus('charging')
                elif self.getstatus() == 'charging':
                    print(f"Drone: {self.droneid} charging completed, now its idle.")
                    self.setstatus('idle')

class fleetmanager:
    def __init__(self):
        self.drones = {}
        self.pendingpackages = []
    
    def adddrone(self, droneid, maxloadinkg):
        new_drone = drone(droneid, maxloadinkg)
        self.drones[droneid] = new_drone
        print(f"Drone: {droneid} with maximum load {maxloadinkg}kg is added.")
    
    def addpackagetoqueue(self, package):
        self.pendingpackages.append(package)
        print(f"Package: {package.packageid} weighing {package.weightinkg}kg is added. ")

    def dispatchjobs(self):
        print("\n*dispatching jobs")
        toberemovedpackages = []
        for package in self.pendingpackages:
            for droneid, drone in self.drones.items():
                if drone.assignpackage(package):
                    toberemovedpackages.append(package)
                    break
        for package in toberemovedpackages:
            self.pendingpackages.remove(package)

    def simulationtick(self):
        print(f"\n*simulation tick")
        for droneid, drone in self.drones.items():
            drone.updatetick()

if __name__ == "__main__":

    print("*initializing fleet")
    manager = fleetmanager()
    manager.adddrone("d1", 1)
    p1 = package("p1", 1)

    manager.addpackagetoqueue(p1)
    for tick in range(1, 15):
        print(f"\ntick: {tick}")
        manager.dispatchjobs()
        manager.simulationtick()
        if tick == 2:
            manager.addpackagetoqueue(package("p2", 2))
        time.sleep(1)
