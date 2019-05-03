from graphics import  *
import math
import random
import csv

win_on = False

lables = ['x', 'y', 'r', '0', '1', '2', '3']
#lables = ['r', '0', '1', '2', '3']

if win_on:
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

def ccw(A,B,C):
    return (C[1]-A[1])*(B[0]-A[0]) >= (B[1]-A[1])*(C[0]-A[0])

def intersect(A,B,C,D):
        return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)

def rand_pos():
    x = random.randint(50 + robot_size, 550 - robot_size)
    y = random.randint(50 + robot_size, 550 - robot_size)
    return (x, y)

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
    if not intersect(line1[0], line1[1], line2[0], line2[1]):
        return "fail"

    if win_on:
        cir = Circle(Point(x, y), 10)
        cir.draw(win)

    return x, y

def arena_intersection(line1):
    for i in arena_lines:
        point = line_intersection(line1, i)
        if(point != "fail" and intersect(line1[0], line1[1], i[0], i[1])):
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
    if win_on:
        draw_line(p0, p1)
        draw_line(p0, p3)
        draw_line(p1, p2)
        draw_line(p2, p3)

    P0 = calc_vec(center, 1000, rot+0*mp)
    P1 = calc_vec(center, 1000, rot+2*mp)
    P2 = calc_vec(center, 1000, rot+4*mp)
    P3 = calc_vec(center, 1000, rot+6*mp)
    if win_on:
        draw_line(center, P0)
        draw_line(center, P1)
        draw_line(center, P2)
        draw_line(center, P3)

    p4x = (p2[0] + p3[0])/2
    p4y = (p2[1] + p3[1])/2
    p4 = (p4x, p4y)
    if win_on:
        draw_line(p0, p4)
        draw_line(p1, p4)

    i0 = round(distance(center, arena_intersection((center, P0))))
    i1 = round(distance(center, arena_intersection((center, P1))))
    i2 = round(distance(center, arena_intersection((center, P2))))
    i3 = round(distance(center, arena_intersection((center, P3))))

    return (i0, i1, i2, i3)

with open('train_data.csv', 'w') as writeFile:
    writer = csv.writer(writeFile)

    a = ((300, 300), (200, 0))
    #print(arena_intersection(a))
    robot_pos = (300, 300)
    if win_on:
        draw_robot(robot_pos, 0)
    writer.writerow(lables)
    #draw_line(a[0], a[1])
    x = 0
    count = 10000
    while x  < count:
        if win_on:
            pt0 = win.getMouse()
            win.clear()
            ptx = int(pt0.getX())
            pty = int(pt0.getY())
            if (pty > 575 and ptx > 575):
                win.close()
                writeFile.close()
            rect = Rectangle(Point(50, 50), Point(550, 550))
            rect.draw(win)
        #pt1 = (ptx, pty)
        robot_pos = rand_pos()
        #robot_ang = -math.atan2(robot_pos[0]-ptx, robot_pos[1]-pty)
        robot_ang = 2 * (random.random() - 0.5) * math.pi
        lidars = draw_robot((robot_pos), robot_ang)
        row = [robot_pos[0], robot_pos[1], robot_ang, lidars[0], lidars[1], lidars[2], lidars[3]]
        #row = [robot_ang, lidars[0], lidars[1], lidars[2], lidars[3]]
        writer.writerow(row)
        x += 1
        #print(arena_intersection(((300, 300), pt1)))
        #print("-----")
        #print(line_intersection(A, ((300, 300), pt1)))
        #draw_line((300, 300), pt1)









#print(draw_robot((300, 300), 1))
