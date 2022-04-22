import numpy as np
import random
#Macaulay's fn
def mac(a,b):
    if a-b<0:
        return 0
    else:
        return (a-b)
def deflection(x):
    R1 = P*(1-dist/total_length)
    y1 = R1/k1
    R2 = P-R1
    y2 = R2/k2
    c2 = EI*y1
    c1 = (1/total_length)*(EI*y2+(R1*(total_length**3)/6)-((P/6)*mac(total_length,dist)**3)-c2)
    term1 = -R1*(x**3)/6
    term2 = (P/6)*mac(x,dist)**3
    defl = (1/EI)*(term1+term2+c1*x+c2)
    return defl
#main
data_size = 10000
#give load(N) at distance (m)
P = 100.0
EI = 1000.0
total_length = 1.0
#specify stiffnesses (N/m)
dist = 0.5
dataset = np.array([])
for i in range(data_size):
    k1 = float(random.randint(1000,1500))
    k2 = float(random.randint(1000,1500))
    defl1 = deflection(0.5)
    #defl2 = deflection(0.7)
    new_data = np.array([defl1,k1,k2])
    if len(dataset)==0:
        dataset = new_data
    else:
        dataset = np.vstack((dataset,new_data))

np.savetxt("beam_data.csv",dataset,header="y1(0.5),k1,k2",comments='',delimiter=',')




