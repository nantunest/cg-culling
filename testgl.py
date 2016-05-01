import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class Sphere:
    def __init__(self, x, y, z, color=None):
        self.x = x
        self.y = y
        self.z = z

        if color is None:
            self.color = {'r':1.0, 'g':1.0, 'b':1.0, 'a':1.0}

    def draw(self):

        glPushMatrix()
        glColor3f(self.color['r'], self.color['g'], self.color['b'])
        glTranslatef(self.x, self.y, self.z)
        glutWireSphere(0.5, 5, 10)
        glPopMatrix()


def Cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()


def main():

    sp = Sphere(0,0,0)

    print sp.x

    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0,0.0, -5)

    glutInit()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

#        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        sp.draw()
#        glutWireSphere(0.5, 10, 10)
        pygame.display.flip()
        pygame.time.wait(10)


main()
