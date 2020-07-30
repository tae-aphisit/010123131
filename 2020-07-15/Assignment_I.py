# นาย อภิสิทธิ์ ผากงคำ
# 6201012620252
# โค้ดนี้เป็นโค้ดสำหรับ Assignment I ใช้รัน pygame ที่สุ่ม generate วงกลมขนาดตั้งเเต่ 10-20 pixel ในพื่นที่หน้าจอ 800*600 pixel พร้อมทั้งสามารถคลิกวงกลมที่ใหญ่สุดแล้วทำให้วงกลมนั้นหายไป
import pygame 
from random import randint
import math

pygame.init()

# set window Caption
pygame.display.set_caption('Week 2 Assignment I') 

# create a clock
clock = pygame.time.Clock()

# set up screen size 
scr_w,scr_h = 800, 600
screen  = pygame.display.set_mode((scr_w,scr_h))

# create a new surface 
surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA )

# create a circle class
class Circle():
    def __init__(self):
        self.x = randint(0,scr_w)
        self.y = randint(0,scr_h)
        self.r = randint(10,20)
        self.R = randint(0,255)
        self.G = randint(0,255)
        self.B = randint(0,255)
        self.color = (self.R,self.B,self.G)   
    def create(self):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.r)  
    def delete(self):
        pygame.draw.circle(surface, (0,0,0), (self.x, self.y), self.r)

# find cursor in circle
def cursor_pos(cursorX, cursorY, r, x, y):     
    if ((x - cursorX) * (x - cursorX) + 
        (y - cursorY) * (y - cursorY) <= r**2): 
        return True
        
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

c_list = []
DrawCircle = []
i = 0
count = 0

# main code
running = True
while running:
    clock.tick( 10 ) 
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
    while count<10:
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
            count+=1
        i+=1
            
    # fill the screen with the white color
    screen.fill((0,0,0))
    screen.blit(surface, (0,0))
    pygame.display.update()

pygame.quit()
