data=open("C:\\Users\\user\\modal\\result10elemtem.txt",'r').read()
data=data.split("FREQUENCY RANGE REQUESTED=   0.00000      0.100000E+09")
data=data[1:]
fdata=[]
for i in data:
    fdata=fdata+[i.split("          ***** PARTICIPATION FACTOR CALCULATION *****  X  DIRECTION")[0]]
data=[]
for i in fdata:
    data=data+[i.split("    \n\n")[0]]
fdata=[]
for i in data:
    fdata=fdata+i.split("    \n    ")[1:3]
for i in range(len(fdata)):
    fdata[i]=float(fdata[i][6:])
data=[[]]*4
for i in range(31):
    k=1000+i*100
    for j in range(31):
        data[2]=data[2]+[k]
        data[3]=data[3]+[1000+j*100]
        data[0]=data[0]+[fdata[2*(i*31+j)]]
        data[1]=data[1]+[fdata[2*(i*31+j)+1]]
fdata=[["w1"],["w2"],["k1"],["k2"]]
for i in range(len(data[0])):
    ind=[k for k,x in enumerate(fdata[2]) if x==data[3][i]]
    c=0
    for j in ind:
        if data[2][i]==fdata[3][j]:
            c=1
            break
    if c==0:
        for j in range(4):
            fdata[j]=fdata[j]+[data[j][i]]
import pandas as pd
df=pd.DataFrame(fdata).T
df.to_csv('out10.csv',index=False,header=False)
