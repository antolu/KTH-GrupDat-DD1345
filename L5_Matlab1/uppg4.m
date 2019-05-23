T = [600 800 1000 1100];    %definiera temperaturerna kurvorna beräknas med
lambda = 0:10^(-7):10^(-5);   %bilda en vektor med x-värden
alfa = 3.7415*10^(-16);     %definiera konstanten alfa och beta i funktionen
beta = 0.014388;            
string = strcat({'T='},{num2str(T(1)),num2str(T(2)),num2str(T(3)),num2str(T(4))});  %bilda 4 textsträngar för märkning av graferna

hold all    %rita alla grafer i samma fönster
clear xlabel ylabel title   
xlabel('Våglängd (m))')     %namnge koordinataxlar och ange titel
ylabel('Intensitet')
title('Intensitetskurvor')
for i=1:4   %en loop för varje graf
        y = (alfa)./(lambda.^5.*(exp(beta./(lambda.*T(i)))-1));     %skapa y-vektor från x-vektor och temperatur
        plot(lambda,y)                                              %plotta grafen
        [ymax maxindex] = max(y);                                   %hitta ymax och dess index
        xmax = lambda(maxindex);                                    %hitta xmax med index från ^
        text(xmax-3*10^-7,ymax+0.7*10^9,string(i))                  %haka på en beskrivande text, något förskjuten
        plot(xmax,ymax,'ko')                                        %plotta maxpunkterna med färg och symbol
end
grid
