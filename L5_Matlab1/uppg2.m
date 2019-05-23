xm = [0 4 6.5 0];                         %medelpunkterna för varje cirkel, med en extra för diff
ym = [1.42 6.18 4.75 1.42];
A = [1 1 0;0 1 1;1 0 1];                  %A-matris för ekvationssystem, där de okända är cirklarnas radie
s = ((diff(xm)).^2+(diff(ym)).^2).^0.5;   %avståndet mellan punkterna med avståndsformeln, högerled för ekvationssystem
r = A\s';                                 %beräkna radierna

hold all                                  %rita cirklarna i samma fönster
axis equal                                %runda cirklar!!!
grid on

for i = 1:3
    fillc(xm(i),ym(i),r(i),'')
end

fill(xm,ym,'')
plot(xm,ym)
plot(xm,ym,'ko')