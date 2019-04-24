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

def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1]) #Typo was here

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
       raise Exception('lines do not intersect')

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return x, y

def arena_intersection(line1):
    for i in arena_lines:
        return line_intersection(line1, i)

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

def draw_box(center, rot):
    p0 = calc_vec(center, rs, rot+1*mp)
    p1 = calc_vec(center, rs, rot+3*mp)
    p2 = calc_vec(center, rs, rot+5*mp)
    p3 = calc_vec(center, rs, rot+7*mp)
    p0x = robot_size/math.sqrt(2)*math.cos(rot+1*math.pi/4)+center[0]
    p0y = robot_size/math.sqrt(2)*math.sin(rot+1*math.pi/4)+center[1]
    p1x = robot_size/math.sqrt(2)*math.cos(rot+3*math.pi/4)+center[0]
    p1y = robot_size/math.sqrt(2)*math.sin(rot+3*math.pi/4)+center[1]
    p2x = robot_size/math.sqrt(2)*math.cos(rot+5*math.pi/4)+center[0]
    p2y = robot_size/math.sqrt(2)*math.sin(rot+5*math.pi/4)+center[1]
    p3x = robot_size/math.sqrt(2)*math.cos(rot+7*math.pi/4)+center[0]
    p3y = robot_size/math.sqrt(2)*math.sin(rot+7*math.pi/4)+center[1]

    draw_line(p0, p1)

    return (p0, p1, p2, p3)

print(draw_box((300, 300), 0))

target = ((0, 0), (100, 100))

print(arena_intersection(target))

convert_line(target).draw(win)
win.getMouse()
win.close()
