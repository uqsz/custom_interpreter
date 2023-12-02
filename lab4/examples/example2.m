# assignment operators
# binary operators
# transposition


A = [ [1,2,3,4,5],
      [1,2,3,4,5] ];

B = 3;

B += A;

D1 = -A.+B' ; # add element-wise A with transpose of B
D2 -= A.-B' ; # substract element-wise A with transpose of B
D3 *= A.*B' ; # multiply element-wise A with transpose of B
D4 /= A./B' ; # divide element-wise A with transpose of B

