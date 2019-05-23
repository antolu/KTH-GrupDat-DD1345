function out = sierpinskiin(n)

hold on

x = [-sqrt(2)/2 0 sqrt(2)/2]';
y = [0 1 0]';

X1 = [x(1) y(1)];
X2 = [x(2) y(2)];
X3 = [x(3) y(3)];

M1 = (X1+X2)./2;
M2 = (X2+X3)./2;
M3 = (X3+X1)./2;

out = [X1;X2;X3]

for i=1:3^n
    for k=1:3
    out = [out;(out(end-2,:)+out(end-1,:))./2]
    end
end

for i=1:3*n
    filltriangle(out(i+1,:),out(i+2,:),out(i,:),'r')
end