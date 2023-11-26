# assignment operators
# binary operators
# transposition

A = [[1,1],[1,1]];
B = [[1,1],[1,1]];

D1 = -A.+B' ; # add element-wise A with transpose of B
D2 -= A.-B' ; # substract element-wise A with transpose of B
D3 *= A.*B' ; # multiply element-wise A with transpose of B
D4 /= A./B' ; # divide element-wise A with transpose of B


K = D1 + D2;

if(4>5) {
    print "N>5";
}

while(k>0) {
    if(k<5)
        i = 1;
    else if(k<10)
        i = 2;   
    else
        i = 3;
    
    k = k - 1;
}

for i = 1:N {
    for j = i:M {
        print i, j;
    }
}

