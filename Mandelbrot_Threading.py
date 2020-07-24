# 6201012620252
# อภิสิทธิ์ ผากงคำ
import threading
import pygame

print( 'File:', __file__ )

def mandelbrot(c,max_iters=100):
    i = 0
    z = complex(0,0)
    while abs(z) <= 2 and i < max_iters:
        z = z*z + c
        i += 1 
    return i

# initialize pygame
pygame.init()

# create a screen of width=600 and height=400
scr_w, scr_h = 500, 500
screen = pygame.display.set_mode( (scr_w, scr_h) )

# set window caption
pygame.display.set_caption('Threading: Mandelbrot') 

# create a surface for drawing
surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA )

# half width, half screen
w2, h2 = scr_w/2, scr_h/2 

def Thread_mandelbrot(draw,surface):
    scale = 0.006
    offset = complex(-0.55,0.0)
    for x in range(int(scr_w/N)):
        for y in range(int(scr_h)):
            re = scale*(draw+x-w2) + offset.real
            im = scale*(y-h2) + offset.imag
            c = complex( re, im )
            color = mandelbrot(c, 63)
            r = (color << 6) & 0xc0
            g = (color << 4) & 0xc0
            b = (color << 2) & 0xc0
            surface.set_at( (draw+x, y), (255-r,255-g,255-b) )
        # draw the surface on the screen
        screen.blit( surface, (0,0) )
        # update the display
        pygame.display.update()

# number of thread
N = 10

# a list for keeping the thread objects
list_threads = []

for i in range(N):
    t = threading.Thread(target=Thread_mandelbrot, args=(int(i*scr_w/N),surface))
    list_threads.append( t )

for t in list_threads:
    t.start()

running = True
# pygame loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
print( 'PyGame done...')
