#import pygame
#from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

ATOM_COLORS = {'H':(1,0,0), 'O':(0,1,0), 'C':(0,0,1), 'N':(1,1,0), 'S':(0,1,1)}

ATOMS = []

zoffset = -120
xoffset = -100
yoffset = 0

# def drawText(x,y,text,color=TEXT_COLOR):
#   """Draws given text at given 2d position of given color"""
#
#   glColor(color)
#
#   if(x<=0 or y<=0):
#     glRasterPos2i(0,0)
#     glBitmap(0, 0, 0, 0, x, y, None)
#   else:
#     glRasterPos2i(x,y)
#
#   for i in text:
#     glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, ord(i))


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
        self.slices = 3
        self.stacks = 3
        self.radius = 0.3

    def draw(self):

        glPushMatrix()
        glColor3f(*self.color)
        glTranslatef(self.x, self.y, self.z)
        glutSolidSphere(self.radius, self.slices, self.stacks)
        glPopMatrix()

def culling():

    return [i for i in ATOMS if bounding_box_culling(i)]

def frustrum_culling():
    pass

def space_subdivision_culling(sphere):
    pass

def bounding_box_culling(sphere):
    if sphere.x < 20 and sphere.x > -20 and sphere.y < 20 and sphere.y > -20 and sphere.z < 20 and sphere.z > -20:
        return True
    else:
        return False

def level_of_detail_culling(sphere):
    pass

def displayFunc():

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_PROJECTION)

    glLoadIdentity()

    gluPerspective(60, 800.0/600.0, 1, 300)

    glMatrixMode(GL_MODELVIEW)

    glLoadIdentity()

    glTranslatef(xoffset, yoffset, zoffset)

    for i in culling():
       i.draw()

    glMatrixMode( GL_PROJECTION )
    glPushMatrix()
    glLoadIdentity()
    glMatrixMode( GL_MODELVIEW )
    glPushMatrix()
    glLoadIdentity()

    glDisable( GL_DEPTH_TEST )

    glRasterPos2i(-1,-1)
    glColor3f(0.0,1.0,1.0)
    fpss = "{0:.2f}".format(calculateFPS.fps)
    for i in fpss:
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(i))

    glMatrixMode( GL_PROJECTION )
    glPopMatrix()
    glMatrixMode( GL_MODELVIEW )
    glPopMatrix()

    glutSwapBuffers()


def calculateFPS():
    calculateFPS.frame_counter += 1

    currentTime = glutGet(GLUT_ELAPSED_TIME)
    timeInterval = currentTime - calculateFPS.previousTime

    if timeInterval > 1000:

        calculateFPS.fps = float(calculateFPS.frame_counter) / (float(timeInterval)/1000.0)
        calculateFPS.previousTime = currentTime
        calculateFPS.frame_counter = 0


    return calculateFPS.fps

calculateFPS.frame_counter = 0
calculateFPS.previousTime = 0
calculateFPS.fps = 0

def idleFunc():
    fps = calculateFPS()
    global xoffset
    xoffset += 1

    glutPostRedisplay()


if __name__ == '__main__':

    load_file("HIV_waterbox.xyz")

    glutInit()
    glutInitWindowSize(800,600)

    glutCreateWindow("DrawSpheres")

    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)

#    glRotate(90, -1, 0, 0)
#    glDepthRange(0, 50)

    glutDisplayFunc(displayFunc)

    glutIdleFunc(idleFunc)

    glutMainLoop()
