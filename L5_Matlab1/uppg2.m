xm = [0 4 6.5 0];                         %medelpunkterna f�r varje cirkel, med en extra f�r diff
ym = [1.42 6.18 4.75 1.42];
A = [1 1 0;0 1 1;1 0 1];                  %A-matris f�r ekvationssystem, d�r de ok�nda �r cirklarnas radie
s = ((diff(xm)).^2+(diff(ym)).^2).^0.5;   %avst�ndet mellan punkterna med avst�ndsformeln, h�gerled f�r ekvationssystem
r = A\s';                                 %ber�kna radierna

hold all                                  %rita cirklarna i samma f�nster
axis equal                                %runda cirklar!!!
grid on

for i = 1:3
    fillc(xm(i),ym(i),r(i),'')
end

fill(xm,ym,'')
plot(xm,ym)
plot(xm,ym,'ko')