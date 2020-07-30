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
        self.rect = (self.left ,self.top, self.rw ,self.rh)
    def draw(self):
        pygame.draw.rect( surface, (0,255,0), self.rect, 1)
        surface.blit( surface, self.rect, self.rect )

def check(mouse_pos,rect_list,img):
    for c in rect_list:
        if int(c.left) < int(mouse_pos[0]) < int(c.left+128) and int(c.top) < int(mouse_pos[1]) < int(c.top+90) :
            return c
        else :
            pass

screen = pygame.display.set_mode((scr_w, scr_h))

surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA )

rect_list = []
camera_draw = []
# draw (MxN) tiles of the images
M,N = 10,8
rw, rh = scr_w//M, scr_h//N
for i in range(M):
    for j in range(N):
        square = frame(i*rw, j*rh, rw, rh)
        rect_list.append(square)
         
img = None
is_running = True 
while is_running:
    for f in rect_list:
        f.draw()

    for k in camera_draw:
        surface.blit(img,k.rect,k.rect)

    for e in pygame.event.get():
        if e.type == pygame.QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
            is_running = False
            if img:
                # save the current image into the output file
                pygame.image.save( img, 'image.jpg' )
        if e.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            pos_check = check(mouse_pos,rect_list,img)
            if pos_check == None :
                pass
            else :
                camera_draw.append(pos_check)

    # try to capture the next image from the camera 
    img = camera.get_image()
    if img is None:
        continue

    # get the image size
    img_rect = img.get_rect()
    img_w, img_h = img_rect.w, img_rect.h

    # write the surface to the screen and update the display
    screen.blit( surface, (0,0) )
    pygame.display.update()

# close the camera
camera.stop()

print('Done....')
###################################################################
