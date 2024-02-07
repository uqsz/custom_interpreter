A = ones(5);  # create 5x5 matrix filled with zeros
B = ones(7);   # create 7x7 matrix filled with ones
I = eye(10);   # create 10x10 matrix filled with ones on diagonal and zeros elsewhere

D1 = A.+B' ; # add element-wise A with transpose of B
#D1 -= A.-B' ; # substract element-wise A with transpose of B
#D1 *= A.*B' ; # multiply element-wise A with transpose of B
D1 = A./B' ; # divide element-wise A with transpose of B

E1 = [ [ 1, 2, 3],
       [ 4, 5, 6],
       [ 7, 8, 9] ];

res1 = 60.500;
res2 = 60.;
res3 = .500;
res4 = 60.52E3;
str = "Hello world";

print D1;

print res1, res2, res3, res4;
n=3;

m=2;

if (m==n) { 
    if (m >= n) 
        print res;
}
