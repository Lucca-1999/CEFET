from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from png import Reader
import math

a = 0

texture = []

def load_textures():
    global texture
    texture = glGenTextures(2)

    png_img = Reader(filename='textura.png')

    w, h, pixels, metadata = png_img.read_flat()

    if(metadata['alpha']):
        modo = GL_RGBA
    else:
        modo = GL_RGB

    glBindTexture(GL_TEXTURE_2D, texture[0])
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
    glTexImage2D(GL_TEXTURE_2D, 0, modo, w, h, 0, modo, GL_UNSIGNED_BYTE, pixels.tolist())
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)

def prisma():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)    
    glLoadIdentity()
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
    glBindTexture(GL_TEXTURE_2D, texture[0])
    glBegin(GL_POLYGON)
    
    for i in range(0,N):
        x = raio * math.cos(i*angulo)
        y = raio * math.sin(i*angulo)
        pontosBase += [ (x,y) ]
        glTexCoord2f(x, y); glVertex3f(x,y,0.0)
    glEnd()
    
    # TAMPA
    glBindTexture(GL_TEXTURE_2D, texture[0])
    glBegin(GL_POLYGON)
    for i in range(0,N):
        #w = raio * math.cos(i*angulo) #Prisma
        #z = raio * math.sin(i*angulo) #Prisma
        w = raiozinho * math.cos(i*angulo) #Tronco de Piramide
        z = raiozinho * math.sin(i*angulo) #Tronco de Piramide
        pontosTampa += [ (w,z) ]
        glTexCoord2f(w, z); glVertex3f(w,z,H)
    glEnd()

    # LATERAL
    glBindTexture(GL_TEXTURE_2D, texture[0])
    glBegin(GL_QUADS)
    for i in range(0,N):
        glTexCoord2f(1.0, 1.0); glVertex3f(pontosBase[i][0],pontosBase[i][1],0.0)
        glTexCoord2f(0.0, 1.0); glVertex3f(pontosBase[(i+1)%N][0],pontosBase[(i+1)%N][1],0.0)
        glTexCoord2f(1.0, 0.0); glVertex3f(pontosTampa[(i+1)%N][0],pontosTampa[(i+1)%N][1],H)
        glTexCoord2f(0.0, 0.0); glVertex3f(pontosTampa[i][0],pontosTampa[i][1],H)
        
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

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("Tronco de pedra")
glutDisplayFunc(desenha)
load_textures()
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glEnable(GL_TEXTURE_2D)
glClearColor(0,0,0,1)
glClearDepth(1.0)
glDepthFunc(GL_LESS)
glShadeModel(GL_SMOOTH)
glMatrixMode(GL_PROJECTION)
gluPerspective(45,800.0/600.0,0.1,100.0)
glTranslatef(0.0,0.0,-10)
glMatrixMode(GL_MODELVIEW)
glutTimerFunc(10,timer,1)
glutMainLoop()
