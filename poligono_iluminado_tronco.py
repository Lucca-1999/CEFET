from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math
import sys

a = 0

x = 0
y = 1
z = 2


def calculanormal(v0,v1,v2):
    U = ( v2[x]-v0[x], v2[y]-v0[y], v2[z]-v0[z] )
    V = ( v1[x]-v0[x], v1[y]-v0[y], v1[z]-v0[z] )
    N = ( (U[y]*V[z]-U[z]*V[y]),(U[z]*V[x]-U[x]*V[z]),(U[x]*V[y]-U[y]*V[x]))
    NLength = math.sqrt(N[x]*N[x]+N[y]*N[y]+N[z]*N[z])
    return ( N[x]/NLength, N[y]/NLength, N[z]/NLength)

def prisma():
    raio = 2
    raiozinho = 1 #Raio da tampa caso seja tronco de piramide
    N = 6
    H = 4
    pontosBase = []
    pontosTampa = []
    angulo = (2*math.pi)/N

    glPushMatrix()
    glTranslatef(0,-2,0)
    glRotatef(a,0.0,1.0,0.0)
    glRotatef(-110,1.0,0.0,0.0)
 

    # BASE
    glBegin(GL_POLYGON)
    for i in range(0,N):
        x = raio * math.cos(i*angulo)
        y = raio * math.sin(i*angulo)
        pontosBase += [ (x,y) ]
        glVertex3f(x,y,0.0)
    
    v1 = (pontosBase[0][0], pontosBase[0][1],0)
    v2 = (pontosBase[1][0], pontosBase[1][1],0)
    v3 = (pontosBase[2][0], pontosBase[2][1],0)
    
    glNormal3fv(calculanormal(v1,v2,v3))
    glEnd()
    
    # TAMPA
    glBegin(GL_POLYGON)
    for i in range(0,N):
        #w = raio * math.cos(i*angulo) #Prisma
        #z = raio * math.sin(i*angulo) #Prisma
        w = raiozinho * math.cos(i*angulo) #Tronco de Piramide
        z = raiozinho * math.sin(i*angulo) #Tronco de Piramide
        pontosTampa += [ (w,z) ]
        glVertex3f(w,z,H)
        
    v1 = (pontosBase[0][0], pontosBase[0][1],H)
    v2 = (pontosBase[1][0], pontosBase[1][1],H)
    v3 = (pontosBase[2][0], pontosBase[2][1],H)
    
    glNormal3fv(calculanormal(v1,v2,v3))
    glEnd()

    # LATERAL
    glBegin(GL_QUADS)
    for i in range(0,N):        
        v1 = (pontosBase[i][0],pontosBase[i][1],0.0)
        v2= (pontosBase[(i+1)%N][0],pontosBase[(i+1)%N][1],0.0)
        v3= (pontosTampa[(i+1)%N][0],pontosTampa[(i+1)%N][1],H)
        v4= (pontosTampa[i][0],pontosTampa[i][1],H)

        glNormal3fv(calculanormal(v1,v2,v4))

        glVertex3fv(v1)
        glVertex3fv(v2)
        glVertex3fv(v3)
        glVertex3fv(v4)
    glEnd()
        

    glPopMatrix()


def desenha():
    global a
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    prisma()
    a+=1
    glutSwapBuffers()
  
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(10,timer,1)
    
def reshape(w,h):
    glViewport(0,0,w,h)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45,float(w)/float(h),0.1,50.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt( 10,0,0,0,0,0,0,1,0 )


def init():
    mat_ambient = (0.4, 0.0, 0.0, 1.0)
    mat_diffuse = (1.0, 0.0, 0.0, 1.0)
    mat_specular = (1.0, 0.5, 0.5, 1.0)
    mat_shininess = (50,)
    light_position = (10, 0, 0)
    glClearColor(0.0,0.0,0.0,0.0)
#    glShadeModel(GL_FLAT)
    glShadeModel(GL_SMOOTH)

    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_MULTISAMPLE)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
    glutInitWindowSize(800,600)
    glutCreateWindow("Prisma Iluminado")
    glutReshapeFunc(reshape)
    glutDisplayFunc(desenha)
    glutTimerFunc(50,timer,1)
    init()
    glutMainLoop()

main()