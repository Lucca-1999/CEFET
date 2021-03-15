  float p1x = 100; //fixos
  float p1y = 500; //fixos
  float p2x = 300; //não fixos
  float p2y = 500; //não fixos
  float p3x = 300; //não fixos
  float p3y = 100; //não fixos
  float p4x = 500; //fixos
  float p4y = 100; //fixos
  boolean arrastaP2 = false;
  boolean arrastaP3 = false;

void setup()
{
  size(800,600);
}

void draw()
{
  background(128);
  
  if(arrastaP2){
      p2x = mouseX;
      p2y = mouseY;
  }
  
  
  if(arrastaP3){
      p3x = mouseX;
      p3y = mouseY;
  }
  
  circle(p1x,p1y,5);
  circle(p2x,p2y,5);
  circle(p3x,p3y,5);
  circle(p4x,p4y,5);
  beginShape();
  for(float t = 0; t <= 1; t += 0.01)
  {
    float ax = p1x + t*(p2x-p1x);
    float bx = p2x + t*(p3x-p2x);
    float cx = p3x + t*(p4x-p3x);
    float dx = ax + t*(bx-ax);
    float ex = bx + t*(cx-bx);
    float fx = dx + t*(ex-dx);
    float ay = p1y + t*(p2y-p1y);
    float by = p2y + t*(p3y-p2y);
    float cy = p3y + t*(p4y-p3y);
    float dy = ay + t*(by-ay);
    float ey = by + t*(cy-by);
    float fy = dy + t*(ey-dy);
    vertex(fx,fy);
  }
  
  endShape(CLOSE);
}

void mousePressed()
{
  if(dist(p2x,p2y,mouseX,mouseY)<5)
  {
    arrastaP2 = true;
  }
  
  if(dist(p3x,p3y,mouseX,mouseY)<5)
  {
    arrastaP3 = true;   
  }
}

void mouseReleased()
{
  arrastaP2 = false;
  arrastaP3 = false;
}
