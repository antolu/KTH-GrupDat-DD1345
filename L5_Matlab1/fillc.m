function fillc(xm,ym,r,symbol)
fi = linspace(0,2*pi,50);           %en vektor med 50 ekvidistanta vinkelv�rden
cosfi = cos(fi);                    %ber�kna radvektor, vars element bildar en cirkels rand
sinfi = sin(fi);

  xc = xm + r*cosfi;          %fi, cosfi och xc �r alla vektorer
  yc = ym + r*sinfi;
  fill(xc,yc,symbol)                    %Fyll en cirkel med godtycklig f�rg
  plot(xc,yc,'k')                    %Rita konturen med godtycklig f�rg