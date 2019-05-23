function [xc, yc, r] = fitcircle(x,y)

HL = x.^2+y.^2;
VL = [ones(length(x),1) x y];

c = VL\HL;

xc = c(2)/2;
yc = c(3)/2;
r = sqrt(xc^2+yc^2+c(1));

%[xc, yc, r] = [c(2)/2 c(3)/2 xc^2+yc^2+c(1)]