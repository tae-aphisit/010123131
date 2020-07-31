#6201012620252
import pygame
import pygame.camera
from pygame.locals import *
import sys

def open_camera( frame_size=(1280,720),mode='RGB'):
    pygame.camera.init()
    list_cameras = pygame.camera.list_cameras()
    print( 'Mumber of cameras found: ', len(list_cameras) )
    if list_cameras:
        # use the first camera found
        camera = pygame.camera.Camera(list_cameras[0], frame_size, mode )
        return camera 
    return None 

scr_w, scr_h = 1280,720

pygame.init()

camera = open_camera()
if camera:
    camera.start()
else:
    print('Cannot open camera')
    sys.exit(-1)

class frame():
    def __init__(self,left,top,rw,rh):
        self.left = left
        self.top = top
        self.rw = rw
        self.rh = rh
        self.rect = (left ,top, rw ,rh)
    def draw(self):
        pygame.draw.rect( img, (0,255,0), self.rect, 1)
        surface.blit( img, (self.left,self.top,self.rw,self.rh), self.rect )

# find cursor in rect
def check(mouse_pos,rect_list,img):
    for c in rect_list:
        if int(c.left) < int(mouse_pos[0]) < int(c.left + c.rw) and int(c.top) < int(mouse_pos[1]) < int(c.top + c.rh) :
            return c
        else :
            pass

############################ code added ###################################
# Drag and Drop
check_pos = True
def Drag_Drop():
    global pos_rect ,check_pos
    if e.type == pygame.MOUSEBUTTONUP :
        for i in rect_list:
            mouse_pos = pygame.mouse.get_pos()
            pos_check = check(mouse_pos,rect_list,img)    
            if pos_check :
                if pos_rect.rect == pos_check.rect :
                    if pos_check not in camera_draw:
                        camera_draw.append(pos_check)
                else :
                    if check_pos :
                        pos_check.rect , pos_rect.rect = pos_rect.rect , pos_check.rect
                        check_pos = False

    elif e.type == pygame.MOUSEBUTTONDOWN :
        check_pos = True
        for i in rect_list:
            mouse_pos = pygame.mouse.get_pos()
            pos_check = check(mouse_pos,rect_list,img)
            if pos_check:
                pos_rect = pos_check
###########################################################################

screen = pygame.display.set_mode((scr_w, scr_h))

surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA )

rect_list = []
camera_draw = []
# draw (MxN) tiles of the images
M,N = 5,5
rw, rh = scr_w//M, scr_h//N
for i in range(M):
    for j in range(N):
        square = frame(i*rw, j*rh, rw, rh)
        rect_list.append(square)
        
is_running = True 
while is_running:
    
    img = camera.get_image()

    for f in rect_list:
        pygame.draw.rect( surface, (0,255,0), f.rect, 1)

    for k in camera_draw:
        k.draw()

    for e in pygame.event.get():
        if e.type == pygame.QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
            is_running = False
    
    Drag_Drop()

    # write the surface to the screen and update the display
    screen.blit( surface, (0,0) )
    pygame.display.update()

# close the camera
camera.stop()

print('Done....')
###################################################################
