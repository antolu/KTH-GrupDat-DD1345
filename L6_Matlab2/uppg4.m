n = input('Antalet iterationer: ');

hold all
axis equal
grid on

x = [-sqrt(2)/2 0 sqrt(2)/2]';
y = [0 1 0]';

X1 = [x(1) y(1)];
X2 = [x(2) y(2)];
X3 = [x(3) y(3)];

filltriangle(X1,X2,X3,'k')
%for i=1:n
    sierpinski(X1,X2,X3,i)
%    pause(1)
%end