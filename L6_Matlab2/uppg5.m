clc
n = input('Antal steg: ');
np = input('Antal partiklar: ');

size = 20;
axis([-size size -size size -size size])
hold on
grid on
colors = hsv(np);

brown(zeros(np,1),zeros(np,1),zeros(np,1),n,np,colors)