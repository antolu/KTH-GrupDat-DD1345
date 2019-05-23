function brown(x,y,z,n,np,c)
if n == 0
    return
end
dx = x + randn(np,1);
dy = y + randn(np,1);
dz = z + randn(np,1);
for i=1:np
    plot3([x(i) dx(i)],[y(i) dy(i)],[z(i) dz(i)],'Color',c(i,:))
end
pause(0.05)
brown(dx,dy,dz,n-1,np,c)