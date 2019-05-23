T = [600 800 1000 1100];    %definiera temperaturerna kurvorna ber�knas med
lambda = 0:10^(-7):10^(-5);   %bilda en vektor med x-v�rden
alfa = 3.7415*10^(-16);     %definiera konstanten alfa och beta i funktionen
beta = 0.014388;            
string = strcat({'T='},{num2str(T(1)),num2str(T(2)),num2str(T(3)),num2str(T(4))});  %bilda 4 textstr�ngar f�r m�rkning av graferna

hold all    %rita alla grafer i samma f�nster
clear xlabel ylabel title   
xlabel('V�gl�ngd (m))')     %namnge koordinataxlar och ange titel
ylabel('Intensitet')
title('Intensitetskurvor')
for i=1:4   %en loop f�r varje graf
        y = (alfa)./(lambda.^5.*(exp(beta./(lambda.*T(i)))-1));     %skapa y-vektor fr�n x-vektor och temperatur
        plot(lambda,y)                                              %plotta grafen
        [ymax maxindex] = max(y);                                   %hitta ymax och dess index
        xmax = lambda(maxindex);                                    %hitta xmax med index fr�n ^
        text(xmax-3*10^-7,ymax+0.7*10^9,string(i))                  %haka p� en beskrivande text, n�got f�rskjuten
        plot(xmax,ymax,'ko')                                        %plotta maxpunkterna med f�rg och symbol
end
grid
