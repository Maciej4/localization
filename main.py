from graphics import  *
import math

win = GraphWin("Arena", 600,  600)
win.setBackground("#FFFFFF")
rect = Rectangle(Point(50, 50), Point(550, 550))
rect.draw(win)

A = ((50, 50), (550, 50))
B = ((50, 50), (50, 550))
C = ((550, 50), (550, 550))
D = ((50, 550), (550, 550))
arena_lines = [A, B, C, D]
robot_size = 50
rs = robot_size/math.sqrt(2)
mp = math.pi/4

def distance(a,b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def is_between(a,c,b):
    print("---")
    print(distance(a,c) + distance(c,b))
    print(distance(a,b))
    return distance(a,c) + distance(c,b) == distance(a,b)

def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1]) #Typo was here

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
       return "fail"

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    if not is_between(line2[0], (x, y), line2[1]):
        return "fail"

    cir = Circle(Point(x, y), 10)
    cir.draw(win)

    return x, y

def arena_intersection(line1):
    for i in arena_lines:
        point = line_intersection(line1, i)
        if(point != "fail" and point[0] > 49 and point[0] < 551 and point[1] > 49 and point [1] < 551):
            return point

def convert_line(line1):
    return Line(Point(line1[0][0], line1[0][1]), Point(line1[1][0], line1[1][1]))

def draw_line(pt1, pt2):
    pt3 = Point(pt1[0], pt1[1])
    pt4 = Point(pt2[0], pt2[1])
    line = Line(pt3, pt4)
    line.draw(win)

def calc_vec(origin, length, angle):
    xcomp = length*math.cos(angle)+origin[0]
    ycomp = length*math.sin(angle)+origin[1]
    return (xcomp, ycomp)

def draw_robot(center, rot):
    p0 = calc_vec(center, rs, rot+1*mp)
    p1 = calc_vec(center, rs, rot+3*mp)
    p2 = calc_vec(center, rs, rot+5*mp)
    p3 = calc_vec(center, rs, rot+7*mp)
    draw_line(p0, p1)
    draw_line(p0, p3)
    draw_line(p1, p2)
    draw_line(p2, p3)

    P0 = calc_vec(center, 1000, rot+0*mp)
    P1 = calc_vec(center, 1000, rot+2*mp)
    P2 = calc_vec(center, 1000, rot+4*mp)
    P3 = calc_vec(center, 1000, rot+6*mp)
    draw_line(center, P0)
    draw_line(center, P1)
    draw_line(center, P2)
    draw_line(center, P3)

    i0 = arena_intersection((center, P0))
    i1 = arena_intersection((center, P1))
    i2 = arena_intersection((center, P2))
    i3 = arena_intersection((center, P3))

    return (i0, i1, i2, i3)

a = ((300, 300), (200, 0))
print(arena_intersection(a))
draw_line(a[0], a[1])

while True:
    pt0 = win.getMouse()
    ptx = int(pt0.getX())
    pty = int(pt0.getY())
    pt1 = (ptx, pty)
    print(arena_intersection(((300, 300), pt1)))
    print("-----")
    #print(line_intersection(A, ((300, 300), pt1)))
    draw_line((300, 300), pt1)
    if (pty > 575 and ptx > 575):
        win.close()






#print(draw_robot((300, 300), 1))
