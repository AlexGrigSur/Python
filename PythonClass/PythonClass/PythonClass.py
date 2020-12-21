class T1: # rectangle
    def __init__(self):
      self.lx = []
      self.ly = []
      print("Ввод прямоугольника")
      for i in range(4):
          print(f"\nТочка №{i+1}")
          coord = input("x,y: ")
          self.lx.append(float(coord.split(',')[0]))
          self.ly.append(float(coord.split(',')[1]))

    def Square(self):
        return (max(self.lx) - min(self.lx)) * (max(self.ly) - min(self.ly))

    def print(self):
        for i in range(4):
            print("[",self.lx[i],",",self.ly[i],"]")

class T2(): #Pentagon
    def __init__(self):
      self.lx = []
      self.ly = []
      print("_____________________________\n")
      print("Ввод пятиугольника")
      for i in range(5):
          print(f"\nТочка №{i+1}")
          coord = input("x,y: ")
          self.lx.append(float(coord.split(',')[0]))
          self.ly.append(float(coord.split(',')[1]))

    def Square(self):
        upperY = max(self.ly)
        leftMiddleX = min(self.lx)
        rightMiddleX = max(self.lx)
        leftbottomY = min(self.ly)

        maxInt = 9223372036854775806
        upperX = maxInt#max(int)
        leftMiddleY = maxInt
        rightMiddleY = maxInt
        leftBottomX= maxInt#max(int)
        rightBottomX= maxInt#max(int)
        for i in range(0,len(self.lx)):
            if(self.ly[i]==upperY): 
               upperX=self.lx[i]
               continue
            if(self.ly[i]==leftbottomY):
                if(leftBottomX==maxInt): leftBottomX = self.lx[i]
                else : rightBottomX = self.lx[i]
                continue
            if(self.lx[i] == leftMiddleX):
                leftMiddleY=self.ly[i]
                continue
            if(self.lx[i] == rightMiddleX):
                rightMiddleY=self.ly[i]
                continue
        if(leftBottomX>rightBottomX): leftBottomX, rightBottomX = rightBottomX,leftbottomX
        sqr = (rightMiddleX-leftMiddleX)*(upperY-leftbottomY)
        tri1 = (upperX-leftMiddleX)*(upperY-leftMiddleY)*0.5
        tri2 = (rightMiddleX-upperX)*(upperY-rightMiddleY)*0.5
        tri3 = (leftMiddleY-leftbottomY)*(leftBottomX-leftMiddleX)*0.5
        tri4 = (rightMiddleX-rightBottomX)*(rightMiddleY-leftbottomY)*0.5
        return sqr-tri1-tri2-tri3-tri4

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

    if (minX_sq <= minX_pent) and (maxX_sq >= maxX_pent) and (minY_sq <= minY_pent) and (maxY_sq >= maxY_pent):
        print("Includes")
    else: 
        print("Not includes")

def Compare(shape1, shape2):
    sq1 = shape1.Square()
    print(f"Rect sqr = {sq1}")
    sq2 = shape2.Square()
    print(f"Pent sqr = {sq2}")
    if(sq1 > sq2): print("Rectangle biggest that Pentagon")
    elif(sq1 < sq2): print("Rectangle smaller that Pentagon")
    else: print("equals")

Figure_1 = T1()
Figure_2 = T2()
isInclude(Figure_1, Figure_2)
Compare(Figure_1,Figure_2)


