# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 19:06:59 2021

@author: User
"""

from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

from math import pi, cos, sin

a = 0
raio = 2
n1 = 50
n2 = 40

cores = ( (1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(0.5,1,1),(1,0,0.5) )

def f(i,j):
    theta = ( (pi * i) / (n1 -1) ) - (pi / 2)
    phi = 2*pi*j/(n2-1)
    x = raio * cos(theta) * cos(phi) 
    y = raio * sin(theta)
    z = raio * cos(theta) * sin(phi)
    return x,y**2,z

def paraboloide():
    glPushMatrix()
    glTranslatef(0,-2,0)
    glRotatef(a,0.0,1.0,0.0)
    glRotatef(-110,1.0,0.0,0.0)
    

    for i in range(n1):
        glBegin(GL_QUAD_STRIP)

        for j in range(n2):
            glColor3fv(((1.0*i/(n1-1)),0,1 - (1.0*i/(n1-1))))
            x, y, z = f(i,j)
            glVertex3f(x,y,z)
            
            glColor3fv(((1.0*(i+1)/(n1-1)),0,1 - (1.0*(i+1)/(n1-1))))
            x, y, z = f(i+1, j)
            glVertex3f(x,y,z)
        glEnd()
    glPopMatrix()
    
    

def desenha():
    global a
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    paraboloide()
    a+=1
    glutSwapBuffers()
  
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(10,timer,1)

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("ESFERA")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0,0,0,1)
gluPerspective(45,800.0/600.0,0.1,100.0)
glTranslatef(0.0,0.0,-10)
glutTimerFunc(10,timer,1)
glutMainLoop()
