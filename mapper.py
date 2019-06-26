colors = {
          'maroon/red': (150,50,60),
          'white/cream': (255,255,255),
          'black/carbon grey': (0,0,0),
          'gray/silver': (127,127,127),
          }

def distance(left, right):
    return sum((l-r)**2 for l, r in zip(left, right))**0.5

class NearestColorKey(object):
    def __init__(self, goal):
        self.goal = goal
    def __call__(self, item):
        return distance(self.goal, item[1])
print(min(colors.items(), key=NearestColorKey((107.66666666666667, 109.0, 107.0))))
f_read = open("colours.txt", "r")
    # f_write = open("fav_colour.txt", "a+")
f1 = f_read.readlines()
for x in f1:
        # f_write.write()
        # print(x)
    x = x.strip()
    li = [l for l in x.split(",")]
    r = float(li[0])
    g = float(li[1])
    b = float(li[2])
    # print(r,g,b,type(r),type(g),type(b),sep="*",)
    print(min(colors.items(), key=NearestColorKey((r,g,b))))
