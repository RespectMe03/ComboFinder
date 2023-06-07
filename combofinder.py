import random as r

ProductList = {'p1':10, 'p2':15, 'p3':20, 'p4':25, 'p5':30, 'p6':35, 'p7':50,}
LB = 290
UB = 310
ResultList  = set()  
Iterations  = 1000    

for i in range(Iterations):

    SetSize = r.randint(2, len(ProductList)-1)

    ComboList = r.sample(list(ProductList.keys()),SetSize)
    ComboList.sort()

    ComboSum = sum([ ProductList[i] for i in ComboList])

    if ComboSum>= LB and ComboSum<= UB:
      ResultList.add(tuple(ComboList))



for r in ResultList:
	print (r)


print ("\nTotal Sets: ", len(ResultList), "\n")