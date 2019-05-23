load vinter

hold on
grid
axis([0 72 -20 20])

x = vinterdag(:,1)+vinterdag(:,2)./60;
y = vinterdag(:,3);
plot(x,y,'*')

%(pi/12)*

A = [ones(length(vinterdag),1) sin((pi/12).*x) cos((pi/12).*x)];

koeff = A\vinterdag(:,3);

x1 = linspace(0,72,97);
y1 = koeff(1) + koeff(2)*sin((pi/12)*x1)+koeff(3)*cos((pi/12)*x1);

plot(x1,y1)

disp('Dagens högsta temperatur: ')
disp(max(y1))