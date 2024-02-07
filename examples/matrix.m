A = eye(3);
B = ones(3);
D = zeros(3);
C = A .+ A;
print C;

D = zeros(3);
D[1, 1] = 42;
D[2, 2] = 7;
print D;

