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

    print "display"

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_PROJECTION)

    glLoadIdentity()

    gluPerspective(60, 800.0/600.0, 1, 300)

    glMatrixMode(GL_MODELVIEW)

    glLoadIdentity()

    glTranslatef(0, 0, 0)

    for i in ATOMS:
       i.draw()

    glutSwapBuffers()

def calculateFPS():
    pass

def idleFunc():
    idleFunc.frame_counter += 1

    currentTime = glutGet(GLUT_ELAPSED_TIME)
    timeInterval = currentTime - idleFunc.previousTime

    global movement

    if timeInterval > 1000:
        #movement += 0.5

        fps = float(idleFunc.frame_counter) / (float(timeInterval)/1000.0)
        idleFunc.previousTime = currentTime
        idleFunc.frame_counter = 0

        print movement, fps

        glutPostRedisplay()

idleFunc.frame_counter = 1
idleFunc.previousTime = 0;

if __name__ == '__main__':

    load_file("HIV_waterbox.xyz")

    glutInit()
    glutInitWindowSize(800,600)

    glutCreateWindow("DrawAtoms")

    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)

#    glRotate(90, -1, 0, 0)
#    glDepthRange(0, 50)

    glutIdleFunc(idleFunc)

    glutDisplayFunc(displayFunc)

    glutMainLoop()
