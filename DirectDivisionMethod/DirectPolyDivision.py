
import numpy as np


def CalculatedTerms(numerator_p,denominator_p,numberOfTerms):
    lengthToAppend = abs(len(numerator_p) - len(denominator_p))
    zeros = np.zeros(lengthToAppend) 
    numerator = np.append(numerator_p,zeros)
    denominator = np.array(denominator_p)
    print(numerator)
    print(denominator)
    print('---------------')

    result = []
    nextnumberAddition = 0
    arrayOfArrays = []
    arrayOfArrays.append(numerator) 
    a = numerator[0]/denominator[0]
    result.append(a)
    A_r = -(a)
    #print('')
    #print(A_r)
    #print('')

    for i in range(1,numberOfTerms):
        #print(arrayOfArrays[i-1])
        p = np.multiply(denominator,A_r)
        #print(p)
        z = np.add(arrayOfArrays[i-1],p)
        z_n = np.delete(z,0)
        z_new = np.append(z_n,0)
        arrayOfArrays.append(z_new)
        a = (arrayOfArrays[i][0])/denominator[0]
        result.append(a)
        A_r = -a
    
    #CompletedResult = np.append(zeros,result)
    print(result)

x = [0, 0, 0.577,-1.809,2.10,-1.070,0.202, 0]
y = [1,-0.021,-3.629,2.453,1.880,-2.353,0.751,-0.078]



CalculatedTerms(x,y,7)


