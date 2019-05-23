clear all
axis([-10 10 -10 10])
axis equal
grid on

[x, y] = ginput;
%x = [-2 -1 2 -1 1 3]';
%y = [2 5 4 0 0 1]';

[xc yc r] = fitcircle(x,y);

X = linspace(xc-r,xc+r,100);
Y = sqrt(r^2-(X-xc).^2)+yc;

hold all
plot(x,y,'ok')
pause(0.5)

plot(X,Y,'k')
plot(X,-Y+2*yc,'k')