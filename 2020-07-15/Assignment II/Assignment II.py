# นาย อภิสิทธิ์ ผากงคำ
# 6201012620252
# โค้ดนี้เป็นโค้ดสำหรับ Assignment I ใช้รัน pygame ที่สุ่ม generate วงกลมจำนวน N=10 ขนาดตั้งเเต่ 10-20 pixel ในพื่นที่หน้าจอ 800*600 pixel 
    # พร้อมทั้งสามารถคลิกวงกลมที่ใหญ่สุดแล้วทำให้วงกลมนั้นหายไป
# โค้ดนี้เป็นโค้ดสำหรับ Assignment II ที่มีการแก้ไขเพิ่มเติมจาก Assignment I โดยโค้ดนี้ได้ทำการปรับเปลี่ยนให้วงกลมสามารถเคลื่อนที่ได้ ชนขอบ screen ได้และชนการเองได้ 
    # พร้อมทั้งคำนวณทิศทางการสะท้อนกลับแบบ mirror เมื่อเกิดการชนขอบหรือชนกันเอง  
    # โค้ดที่แก้ไขเเพิ่มเติม 
        # ในบรรทัดที่ 74  เพิ่ม def สำหรับการเคลื่อนที่
        # ในบรรทัดที่ 85  เพิ่ม def สำหรับเช็คการชนขอบของวงกลม
        # ในบรรทัดที่ 94  เพิ่ม def สำหรับเช็คการชนกันของวงกลม
        # ในบรรทัดที่ 169 เพิ่ม loop เรียกใช้งาน def move , def check_border , def check_collide
import pygame 
from random import *
import math 

pygame.init()

# set window Caption
pygame.display.set_caption('Week 2 Assignment II') 

# create a clock
clock = pygame.time.Clock()

# set up screen size 
scr_w,scr_h = 800, 600
screen  = pygame.display.set_mode((scr_w,scr_h))

# create a new surface 
surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA )

c_list = []
DrawCircle = []
running = True
i = 0
count = 0
N = 10
speed = [-2,2]

# create a circle class
class Circle():
    def __init__(self):
        self.r = randint(10,20)
        self.x = randint(0+self.r,scr_w-self.r)
        self.y = randint(0+self.r,scr_h-self.r)
        self.R = randint(0,255)
        self.G = randint(0,255)
        self.B = randint(0,255)
        self.color = (self.R,self.B,self.G)   
        self.top = self.y - self.r
        self.bottom = self.y + self.r
        self.left = self.x - self.r
        self.right = self.x + self.r
        self.speed_x = choice(speed)
        self.speed_y = choice(speed)
    def create(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.r)  
    def delete(self):
        pygame.draw.circle(screen, (0,0,0), (int(self.x), int(self.y)), self.r)

# find cursor in circle
def cursor_pos(cursorX, cursorY, r, x, y):     
    if ((x - cursorX) * (x - cursorX) + (y - cursorY) * (y - cursorY) <= r**2): 
        return True
    else:
        return False
        
# check circle is the largest or not
def Largest(large_c, all):
    large_count = 0
    for k in all:
        if large_c != k:
            if large_c.r > k.r:
                large_count+=1
            elif large_c.r == k.r:
                large_count+=1
    if large_count == len(all) - 1:
        return True
    else:
        return False

# circle movement
def move(target):
    target.x += target.speed_x
    target.y += target.speed_y
    target.bottom = target.y + target.r
    target.top = target.y - target.r
    target.right = target.x + target.r
    target.left = target.x - target.r
    
# check circle is collide border
def check_border(target):
    if target.left <= 0 or target.right >= scr_w:
        target.speed_x *= -1
    if target.top <= 0 or target.bottom >= scr_h:
        target.speed_y *= -1

# check collide target with other
# Ref:http://www.geometrian.com/programming/projects/index.php?project=Circle%20Collisions
def check_other(target,other):
    global XSpeed , YSpeed
    temp = math.hypot(target.x - other.x , target.y - other.y)
    sum_r = target.r + other.r
    if temp - sum_r <= 1:
        targetSpeed = math.sqrt((target.speed_x**2)+(target.speed_y**2))
        XDiff = -(target.x-other.x)
        YDiff = -(target.y-other.y)
        if XDiff > 0:
            if YDiff > 0:
                Angle = math.degrees(math.atan(YDiff/XDiff))
                XSpeed = -targetSpeed*math.cos(math.radians(Angle))
                YSpeed = -targetSpeed*math.sin(math.radians(Angle))
            elif YDiff < 0:
                Angle = math.degrees(math.atan(YDiff/XDiff))
                XSpeed = -targetSpeed*math.cos(math.radians(Angle))
                YSpeed = -targetSpeed*math.sin(math.radians(Angle))
        elif XDiff < 0:
            if YDiff > 0:
                Angle = 180 + math.degrees(math.atan(YDiff/XDiff))
                XSpeed = -targetSpeed*math.cos(math.radians(Angle))
                YSpeed = -targetSpeed*math.sin(math.radians(Angle))
            elif YDiff < 0:
                Angle = -180 + math.degrees(math.atan(YDiff/XDiff))
                XSpeed = -targetSpeed*math.cos(math.radians(Angle))
                YSpeed = -targetSpeed*math.sin(math.radians(Angle))
        elif XDiff == 0:
            if YDiff > 0:
                Angle = -90
            else:
                Angle = 90
            XSpeed = targetSpeed*math.cos(math.radians(Angle))
            YSpeed = targetSpeed*math.sin(math.radians(Angle))
        elif YDiff == 0:
            if XDiff < 0:
                Angle = 0
            else:
                Angle = 180
            XSpeed = targetSpeed*math.cos(math.radians(Angle))
            YSpeed = targetSpeed*math.sin(math.radians(Angle))
        target.speed_x = XSpeed
        target.speed_y = YSpeed

# game loop
while running:
    clock.tick(60) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            for n in DrawCircle:
                if cursor_pos(n.x, n.y, n.r, mouse[0], mouse[1]):
                    if Largest(n, DrawCircle):
                        n.delete()
                        DrawCircle.remove(n)
    while count < N:
        c_list.append('c'+str(i))
        c_list[i] = Circle()
        draw = True
        for j in range(len(c_list)):
            if i != j:
                dist = int(math.hypot(c_list[i].x - c_list[j].x, c_list[i].y - c_list[j].y))        
                if dist < int(c_list[i].r+c_list[j].r):
                    draw = False
        if draw:
            c_list[j].create()
            DrawCircle.append(c_list[j])
            count += 1
        i += 1
    
    screen.fill((0,0,0))

    # loops for collisions and movement
    for t in DrawCircle:
        check_border(t)
        move(t)
        t.create()
        for o in DrawCircle:
            if t != o :
                check_other(t,o)
                
    pygame.display.update()

pygame.quit()
