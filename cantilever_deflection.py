from beam_deflection import mac
import matplotlib.pyplot as plt
def deflection(P,pos,beam,k1,x):
    l = beam[0]
    b = beam[1]
    d = beam[2]
    G = beam[3]
    EI = beam[4]
    J = (1.0/12)*((b*l**3)+(l*b**3))
    tors_k = G*J/d
    Fr = P
    Mr = P*pos
    y1 = Fr/k1
    theta1 = Mr/tors_k
    c1 = EI*theta1
    c2 = EI*y1
    term1 = (Mr*x**2)/2
    term2 = (Fr*x**3)/6
    term3 = (P*mac(x,l)**3)/6
    y = (1.0/EI)*(term1-term2+term3+c1*x+c2)
    return y

def main():
    P = 100
    pos = 1.0
    beam = [1.0,0.05,0.05,10*10**6,1000]
    k1 = 10000
    x = [i/50.0  for i in range(0,51)]
    y = [-deflection(P,pos,beam,k1,j) for j in x]
    plt.plot(x,y)
    plt.axis([0, 1, -1, 0])
    plt.show()
    # print(y)
    # print(deflection(P,pos,beam,k1,1.0))

if __name__ == "__main__":
    main()
    

