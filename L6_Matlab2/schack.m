function schack()
clc
n = input('Antal rutor: ');

side = 1;
size = n*side+1;

plot([0 0 size-1 size-1 0],[0 size-1 size-1 0 0],'k')
fill([0 0 size-1 size-1 0],[0 size-1 size-1 0 0],'b')

x = [0 0 side side]';
y = [0 side side 0]';
hold on

for k=0:n-1
    for i=0:2:n-1
        axis([-side size -side size])
        axis equal
        
        fill(x+i*ones(4,1),y,'k')
        pause(0.05)
        
    end
    x = x+(-1)^k*ones(4,1);
    y = y+ones(4,1);
end
