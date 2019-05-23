A = [2 1;4 5];
B = [1 1;2 3];
x = [7;9];
C = A*B;
D = B*A;
F = A.*B;
G = B.*A;
z = A*x;
p = dot(z,z);
E = A'*A;
q = dot(x,x);

H = [eye(2) A;-B eye(2)];
H(:,3);
H(2,:);
H(1,:)*H(:,4);

J = H(2:end-1,2:end-1);


K = [H;ones(1,length(H))];
L = [H ones(length(H),1);zeros(1,length(H)) 1];

pnr =  [9;6;0;6;1;1;1;4;7;5];
%pnrN = pnr(2:end)-pnr(1:end-1);
diff(pnr)

q1 = [1 2 3 4];
q2 = q1.^2;

summa = sum(sum(K.^2));