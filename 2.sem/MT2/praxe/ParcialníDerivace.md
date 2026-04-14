# Parcialní Derivace
# 1
f(x,y)=x^4+y^4-4x^2y
1. Derivace podle: 
df/dx=f^Ix=4x^3+0-4y2x=4x^3-8xy
df/dy=f^Iy=0+4y^3-4x^2=4y^3-4x^2
2. Derivace podle:
df/dx^2=f^IIx=12x^2-8y
df/dy^2=f^IIy=12y^2
df/dxdy=f^IIxy=-8x
df/dydx=f^IIyx=-8x
# 2
f(x,y)=x*y+x/y
1. Derivace podle:
df/dx=f^Ix=y+1/y
df/dy=f^Iy=x-1/y^2
2. Derivace podle:
df/dx^2=f^IIx=0
df/dy^2=f^IIy=2/y^3
df/dxdy=f^IIxy=1
df/dydx=f^IIyx=1
# 3
f(x,y)=x^2+sin(x*y)
1. Derivace podle:
df/dx=f^Ix=2x+cos(x*y)*y
df/dy=f^Iy=0+cos(x*y)*x
2. Derivace podle:
df/dx^2=f^IIx=2-y^2*sin(x*y)
df/dy^2=f^IIy=-x^2*sin(x*y)
df/dxdy=f^IIxy=cos(x*y)-x*y*sin(x*y)
df/dydx=f^IIyx=cos(x*y)-x*y*sin(x*y)
# 4
f(x,y)=(x^2-y)/(x^2+y^2)
1. Derivace podle:
df/dx=f^Ix=2x(x^2+y^2)-(x^2-y)*2x/(x^2+y^2)^2=4x*y^2/(x^2+y^2)^2
df/dy=f^Iy=-1*(x^2+y^2)-(x^2-y)*2y/(x^2+y^2)^2=-4y*x^2/(x^2+y^2)^2
2. Derivace podle:
df/dx^2=f^IIx=4y^2*(x^2+y^2)^2-4x*y^2*4x*(x^2+y^2)/(x^2+y^2)^4=4y^2*(x^2+y^2)^2-16x^2*y^2*(x^2+y^2)/(x^2+y^2)^4=4y^2*(x^2+y^2)-16x^2*y^2/(x^2+y^2)^3
df/dy^2=f^IIy=-4x^2*(x^2+y^2)^2+4y*x^2*4y*(x^2+y^2)/(x^2+y^2)^4=-4x^2*(x^2+y^2)^2+16y^2*x^2*(x^2+y^2)/(x^2+y^2)^4=-4x^2*(x^2+y^2)+16y^2*x^2/(x^2+y^2)^3
df/dxdy=f^IIxy=8x*y*(x^2+y^2)^2-4y^2*4x*(x^2+y^2)/(x^2+y^2)^4=8x*y*(x^2+y^2)^2-16x*y^2*(x^2+y^2)/(x^2+y^2)^4=8x*y*(x^2+y^2)-16x*y^2/(x^2+y^2)^3
df/dydx=f^IIyx=8x*y*(x^2+y^2)^2-4y^2*4x*(x^2+y^2)/(x^2+y^2)^4=8x*y*(x^2+y^2)^2-16x*y^2*(x^2+y^2)/(x^2+y^2)^4=8x*y*(x^2+y^2)-16x*y^2/(x^2+y^2)^3
