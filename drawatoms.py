import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

ATOM_COLORS = {'H':(1,0,0), 'O':(0,1,0), 'C':(0,0,1), 'N':(1,1,0), 'S':(0,1,1)}

ATOMS = []

movement = -150

def load_file(file_name):

    with open(file_name) as spheres_file:
        for line in spheres_file:

            # if len(ATOMS) > 5000:
            #     break

            line_split = line.split()
            if len(line_split) == 4:
                ATOMS.append(Sphere(float(line_split[1]), float(line_split[2]), float(line_split[3]), line_split[0]))

class Sphere:
    def __init__(self, x, y, z, t):
        self.x = x
        self.y = y
        self.z = z
        self.t = t
        self.color = ATOM_COLORS[t]

    def draw(self):

        glPushMatrix()
        glColor3f(*self.color)
        glTranslatef(self.x, self.y, self.z)
        glutSolidSphere(0.3, 5, 5)
        glPopMatrix()

def displayFunc():

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_PROJECTION)

    glLoadIdentity()

    gluPerspective(60, 800.0/600.0, 1, 300)

    glMatrixMode(GL_MODELVIEW)

    glLoadIdentity()

    glTranslatef(0, 0, movement)

    for i in ATOMS:
       i.draw()

    #glutSwapBuffers()

def calculateFPS():
    pass

def idleFunc():
    idleFunc.frame_counter += 1

    currentTime = clock.tick(FPS)
    timeInterval = currentTime - idleFunc.previousTime
    print timeInterval

    global movement

    if timeInterval > 1000:
        #movement += 0.5

        fps = float(idleFunc.frame_counter) / (float(timeInterval)/1000.0)
        idleFunc.previousTime = currentTime
        idleFunc.frame_counter = 0

        print movement, fps

        #glutPostRedisplay()

idleFunc.frame_counter = 1
idleFunc.previousTime = 0;

# Create Pygame clock object.
clock = pygame.time.Clock()
# Desired framerate in frames per second. Try out other values.
FPS = 30
# How many seconds the "game" is played.
playtime = 0.0

if __name__ == '__main__':

    load_file("HIV_waterbox.xyz")

    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    while True:
        # Do not go faster than this framerate.
        milliseconds = clock.tick(FPS)
        playtime += float(milliseconds) / 1000.0

        text = "FPS: {0:.2f}   Playtime: {1:.2f}".format(clock.get_fps(), playtime)
        pygame.display.set_caption(text)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        displayFunc()
        idleFunc()

        # Print framerate and playtime in titlebar.

        pygame.display.set_caption(text)

        pygame.display.flip()
#        pygame.time.wait(10)
