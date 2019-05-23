x = [11  12  15  28  45  52  57  75  81  88  93  97];
y = [1.0  1.0  1.5  6.0  9.0  10.5  11.0  16.5  9.5  8.0  12.5  12.5];

x1 = linspace(1,100,100);

axis([0 150 0 15])

p1 = polyfit(x,y,1)

hold all
plot(polyval(p1,x1))
plot(x,y,'*')

rmsfel = sqrt(sum((p1(2)+p1(1).*x-y).^2)/length(x))
text(100,10,strcat({'rms-felet: '},{num2str(rmsfel)}))