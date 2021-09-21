import csv,math
from typing import Counter

#opening the csv file and converting it into a list.
with open ('HW.csv', newline='') as file:
    d=csv.reader(file)
    dataList=list(d)

#removing the 1st element, since they would be the headers of the data
dataList.pop(0)

l=len(dataList)
dSum,newList=0,[]
for i in range(l):
    dSum=dataList[i][2]
    newList.append(float(dSum))

Wsum=0
for i in newList:
    Wsum+=(i)

length=len(newList)
mean=Wsum/length
approxMean=round(mean)
print("Mean of the data is:\n\t",mean,'=',approxMean,'lb',end='\n')

newList.sort()
if (length%2==0):
    median=((newList[length//2]+((newList[length//2])-1))/2)
else:
    median=newList[length/2]

print("The median of the data is:\n\t", median,'=',round(median),'lb',end='\n')

data=Counter(newList)
dataRange={'90-105':0,'105-120':0,'120-135':0,'135-150':0,'150-165':0,'165-180':0}
for w,o in data.items():
    if 90<float(w)<105:
        dataRange['90-105']+=o
    if 105<float(w)<120:
        dataRange['105-120']+=o
    if 120<float(w)<135:
        dataRange['120-135']+=o
    if 135<float(w)<150:
        dataRange['135-150']+=o
    if 150<float(w)<165:
        dataRange['150-165']+=o
    if 165<float(w)<180:
        dataRange['165-180']+=o
    
modeRange,occ=0,0
for m,o in dataRange.items():
    if o>occ:
        modeRange,occ=[int(m.split('-')[0]),int(m.split('-')[1])],o
        
mode=float((modeRange[0]+modeRange[1])/2)
print('the mode of the data is:\n\t',mode,'=',round(mode),'lb')