
int nEstrelas = 10;

void setup()
{
  size (1280,720);
  frameRate(10);
}

void draw()
{
  background(300);
  
  float r = map(mouseX,0,width,1,9);
  float r2 = map(mouseY,0,height,1,9);
  
  if(mousePressed == true){
    for(int i=0; i<nEstrelas; i++){
      pushMatrix();
      translate(width*random(0,1),height*random(0,1));
      fill(255,250,90);
      estrela(0,0,(3*i)/r,(7*i)/r2,5);
      popMatrix();
    }
  }
  
}

void estrela(float x, float y, float raio1, float raio2, int nPontos) {
  float angulo = TWO_PI/ nPontos;
  float meioAngulo = angulo/2.0;
  beginShape();
  for (float a=0; a<TWO_PI; a+= angulo){
    float sx = x + cos(a) * raio2;
    float sy = y + sin(a) * raio2;
    vertex(sx,sy);
    sx = x + cos(a+meioAngulo) * raio1;
    sy = y + sin(a+meioAngulo) * raio1;
    vertex(sx,sy);
  }
  endShape(CLOSE);
}
