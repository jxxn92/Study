dots =  [1,1],[2,2],[3,3],[50,100]


s1 = ((dots[1][1]-dots[0][1])/(dots[1][0]-dots[0][0])) #1
s2 = ((dots[2][1]-dots[0][1])/(dots[2][0]-dots[0][0])) #2
s3 = ((dots[3][1]-dots[0][1])/(dots[3][0]-dots[0][0])) #3
s4 = ((dots[2][1]-dots[1][1])/(dots[2][0]-dots[1][0])) #3
s5 = ((dots[3][1]-dots[1][1])/(dots[3][0]-dots[1][0])) #2
s6 = ((dots[3][1]-dots[2][1])/(dots[3][0]-dots[2][0])) #1

if s1 == s6 or s2==s5 or s3 ==s4:
    print(1)
else:
    print(0)