class T1: # rectangle
    def __init__(self):
      self.lx = []
      self.ly = []
      for i in range(4):
          print(f"\nТочка №{i}")
          coord = input("x,y")
          self.lx.append(float(coord.split(',')[0]))
          self.ly.append(float(coord.split(',')[1]))

    def Square(self):
        return (max(lx) - min(lx)) * (max(ly) - min(ly))

    def print(self):
        for i in range(4):
            print("[",self.lx[i],",",self.ly[i],"]")

class T2(): #Pentagon
    def __init__(self):
      self.lx = []
      self.ly = []
      for i in range(5):
          print(f"\nТочка №{i}")
          coord = input("x,y")
          self.lx.append(float(coord.split(',')[0]))
          self.ly.append(float(coord.split(',')[1]))

    def Square(self):
        upperY = max(ly)
        leftMiddle = min(lx)
        rightMiddle = max(lx)
        leftbottomY = min(ly)

        upperX = max(int)
        middleLeftY = max(int)
        middleRightY = max(int)
        bottomLeftX = max(int)
        bottomRightY = max(int)
        for i in range(0,lx):
            if(ly[i]==upperY): upperX=lx[i]
            if(ly[i]==leftbottomY && ):
        return 

    def print(self):
        for i in range(5):
            print("[",self.lx[i],",",self.ly[i],"]")


def isInclude(shape1, shape2):
    minX_sq = min(shape1.lx)
    minY_sq = min(shape1.ly)
    maxX_sq = max(shape1.lx)
    maxY_sq = max(shape1.ly)

    maxX_pent = max(shape2.lx)
    maxY_pent = max(shape2.ly)
    minX_pent = min(shape2.lx)
    minY_pent = min(shape2.ly)

    if (minX_sq < minX_pent) and (maxX_sq > maxX_pent) and (minY_sq < minY_pent) and (maxY_sq > maxY_pent):
        print("Includes")
    else: 
        print("Not includes")

def Compare(shape1, shape2):
    sq1 = shape1.Square
    sq2 = shape2.Square
    if(sq1 > sq2): print("Rectangle>Pentagon")
    elif(sq1 < sq2): print("Rectangle<Pentagon")
    else: print("equals")

Figure_1 = T1()
Figure_2 = T2()
isInclude(Figure_1, Figure_2)
