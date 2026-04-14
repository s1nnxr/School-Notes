# Tečná rovina
F(x,y)=x^3y-xy^2+2xy-x^2-5x+1 -> tečná rovina v bodě T[1,2,z_0]
z_0=f(x_0,y_0)=f(1,2)=1^3*2-1*2^2+2*1*2-1^2-5*1+1=-3
## obecná rovnice roviny
a_x+by+cz+d=0, normalový vektor $$\vec{n}=(a,b,c)$$
## Tečna rovnice
$$T:O=\frac{\partial F}{\partial x}(x_0,y_0)(x-x_0)+\frac{\partial F}{\partial y}(x_0,y_0)(y-y_0)+\frac{\partial F}{\partial z}(x_0,y_0)(z-z_0)=0$$
$$\frac{\partial F}{\partial x}=3x^2y-y^2+2y-2x-5$$
$$\frac{\partial F}{\partial y}=x^3-2xy+2x$$
$$\frac{\partial F}{\partial z}=1$$
$$\frac{\partial F}{\partial x}(1,2)=-3$$
$$\frac{\partial F}{\partial y}(1,2)=3$$
$$\frac{\partial F}{\partial z}(1,2)=1$$
$$T:-3(x-1)+3(y-2)+1(z+3)=0$$
$$T:-3x+3y+z-6=0$$
# 2. úloha
F(x,y)=x^2*y^3+x^3+x^3*y^2+x; tečná rovina v bodě T[1,-1,z_0]
# Nemám tušení jak na to
Z_0=-1+1+1=1
$$\frac{\partial F}{\partial x}=2xy^3+3x^2+3x^2y^2+1$$  > $$\frac{\partial F}{\partial x}=-2+3+1=2=a$$
$$\frac{\partial F}{\partial y}=x^2*3y^2+x^3*2y$$ > $$\frac{\partial F}{\partial y}=-3+2=-1=b$$

2x+-z+d=0  normála: x=1+2t
2-1-1+d=0           y=-1+t
d=0                 z=1-t, t\in R
T:2x+y-z=0
# 3. Uloha
f(x,y)=ln(x^2+3y), tečná rovina v bodě T[2,1,z_0]
z_0=ln(4-3)=ln(1)=0
...
# Taileruv polinom pro funkci 2 proměných
T_m(x,y)=f(x_0,y_0)+\frac{\frac{\partial f}{\partial x}(x_0,y_0)}{1!}(x-x_0)+\frac{\frac{\partial f}{\partial y}(x_0,y_0)}{1!}(y-y_0)+\frac{\frac{\partial^2 f}{\partial x^2}(x_0,y_0)}{2!}(x-x_0)^2+\frac{\frac{\partial^2 f}{\partial y^2}(x_0,y_0)}{2!}(y-y_0)^2+\frac{\frac{\partial^2 f}{\partial x \partial y}(x_0,y_0)}{1!1!}(x-x_0)(y-y_0)+...
f(x,y)=ln(1/xy), [x_0,y_0]=[-2,-3]
F(-2,-3)=ln(1/6)

-# Bro wtf

T_2(x,y)=ln(1/6)+\frac{\frac{\partial f}{\partial x}(-2,-3)}{1!}(x+2)+\frac{\frac{\partial f}{\partial y}(-2,-3)}{1!}(y+3)+\frac{\frac{\partial^2 f}{\partial x^2}(-2,-3)}{2!}(x+2)^2+\frac{\frac{\partial^2 f}{\partial y^2}(-2,-3)}{2!}(y+3)^2+\frac{\frac{\partial^2 f}{\partial x \partial y}(-2,-3)}{1!1!}(x+2)(y+3)
