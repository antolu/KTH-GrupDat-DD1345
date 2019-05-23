function sierpinski(X1,X2,X3,n)
if n == 0
    return
end

n = n-1;

M1 = (X1+X2)./2;
M2 = (X2+X3)./2;
M3 = (X3+X1)./2;
color = hsv(64);

filltriangle(M1,M2,M3,[rand rand rand])

%for i = 1:n
    pause(0.05)
    sierpinski(X1,M1,M3,n)

    sierpinski(M1,X2,M2,n)

    sierpinski(M3,M2,X3,n)
%end
