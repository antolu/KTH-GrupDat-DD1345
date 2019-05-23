function fillc(xm,ym,r,symbol)
fi = linspace(0,2*pi,50);           %en vektor med 50 ekvidistanta vinkelvärden
cosfi = cos(fi);                    %beräkna radvektor, vars element bildar en cirkels rand
sinfi = sin(fi);

  xc = xm + r*cosfi;          %fi, cosfi och xc är alla vektorer
  yc = ym + r*sinfi;
  fill(xc,yc,symbol)                    %Fyll en cirkel med godtycklig färg
  plot(xc,yc,'k')                    %Rita konturen med godtycklig färg