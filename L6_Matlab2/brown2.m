function brown2()

clc
n = input('Antal rörelser: ');
np = input('Antal partiklar: ');
size = input('Axelbredd: ');

hold all
axis([-size size -size size -size size])
grid on

color=hsv(np);

[x,y,z] = deal(zeros(np,1));

[dx,dy,dz] = deal(x+randn(np,1),y+randn(np,1),z+randn(np,1));
for k=1:n

for i=1:np
    plot3([x(i) dx(i)],[y(i) dy(i)],[z(i) dz(i)],'Color',color(i,:))
end
[x,y,z] = deal(dx, dy, dz);
[dx,dy,dz] = deal(x + randn(np,1),y + randn(np,1),z + randn(np,1));

pause(0.05)
end