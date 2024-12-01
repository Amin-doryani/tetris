class O:
    def __init__(self):
        self.__s = [
            [0,0,0,0],
            [0,1,1,0],
            [0,1,1,0],
            [0,0,0,0]
        ]
        self.__x = 120
        self.__y = -30
        self.__l = 30
        self.__r = 30
        self.__d = 30
        self.__u = 30

    def gets(self):
        return self.__s
    
    def getx(self):
        return self.__x
    def setx(self,x):
        self.__x = x
    def gety(self):
        return self.__y
    def sety(self,y):
        self.__y = y
    

    def move_l(self,maxl):
        if(((self.__x + self.__l) - maxl >= 30) and (630 - (self.gety() +  self.__u + 60) >= 30)):
            self.setx(self.getx() - 30)

    def move_r(self,maxr):
        if((maxr -  (self.getx() + 60 + self.__l  ) >= 30) and (630 - (self.gety() +  self.__u + 60) >= 30)):
            self.setx(self.getx() + 30)
    def move_d(self,maxd):
        if(maxd - (self.gety() +  self.__u + 60) >= 30):
            self.sety(self.gety() + 30)