# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 18:43:48 2019

@author: Gaurav
"""

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import time
import functools
from collections import Counter

def createExamples():
    numberArrayExamples=open('numArEx.txt','a')
    numbersWeHave = range(1,10)
    verisonsWehave =range(1,10)
    
    for eachNum in numbersWeHave:
        for eachVer in verisonsWehave:
            #print(str(eachNum)+'.'+str(eachVer))
            imgFilePath='C:\\Users\\abc\\Desktop\\images\\numbers\\'+str(eachNum)+'.'+str(eachVer)+'.png'
            ei=Image.open(imgFilePath)
            eiar=np.array(ei)
            eiar1=str(eiar.tolist())
            
            lineToWrite = str(eachNum)+'::'+eiar1+'\n'
            numberArrayExamples.write(lineToWrite)
            



def threshold(imageArray):
    balanceAr = []
    newAr = imageArray
    
    for eachRow in imageArray:
        for eachPix in eachRow:
            avgNum=functools.reduce(lambda x, y: x + y,eachPix[:3])/len(eachPix[:3])
            balanceAr.append(avgNum)
            
    balance=functools.reduce(lambda x, y: x + y,balanceAr)/len(balanceAr)
    
    for eachRow in newAr:
        for eachPix in eachRow:
            if functools.reduce(lambda x, y: x + y,eachPix[:3])/len(eachPix[:3]) >balance:
                eachPix[0]=255
                eachPix[1]=255
                eachPix[2]=255
                eachPix[3]=255
            
            else:
                eachPix[0]=0
                eachPix[1]=0
                eachPix[2]=0
                eachPix[3]=255
    return newAr
      


def whatNumIsThis(filePath):
    matchedAr =[]
    loadExamps =open('numArEx.txt','r').read()
    loadExamps=loadExamps.split('\n')
    
    i=Image.open(filePath)
    iar=np.array(i)
    iar1=iar.tolist()
    
    inQuestion=str(iar1)
    
    for eachExample in loadExamps:
        if len(eachExample)>3:
            splitEx=eachExample.split('::')
            currentNum=splitEx[0]
            currentAr=splitEx[1]
            eachPixEx=currentAr.split('],')
    
            eachPixInQ=inQuestion.split('],')
            
            x=0
            while x<len(eachPixEx):
                if eachPixEx[x]==eachPixInQ[x]:
                    matchedAr.append(int(currentNum))
                x+=1
    
    print(matchedAr)
    x=Counter(matchedAr)
    print(x)
    
    
    
    
    graphX=[]
    graphY=[]
    
    for eachThing in x:
        print(eachThing)
        graphX.append(eachThing)
        print(x[eachThing])
        graphY.append(x[eachThing])
        
    fig=plt.figure()
    ax1=plt.subplot2grid((4,4),(0,0),rowspan=1,colspan=4)
    ax2=plt.subplot2grid((4,4),(1,0),rowspan=3,colspan=4)
        
    ax1.imshow(iar)
    ax2.bar(graphX,graphY,align='center')
    plt.ylim(400)
    xloc=plt.MaxNLocator(12)
    
    ax2.xaxis.set_major_locator(xloc)                

#NOTE HERE THE TEST image is a image of 2 drawn in paint.  
whatNumIsThis('C:\\Users\\abc\\Desktop\\images\\numbers\\test.png')







#to open 4 images side by side 
'''
//To call the images and then send it into i and store it as a numpy pixelated value.
i=Image.open('C:\\Users\\abc\\Desktop\\images\\numbers\\0.1.png')
iar=np.array(i)

i2=Image.open('C:\\Users\\abc\\Desktop\\images\\numbers\\y0.4.png')
iar2=np.array(i2)

i3=Image.open('C:\\Users\\abc\\Desktop\\images\\numbers\\y0.5.png')
iar3=np.array(i3)

i4=Image.open('C:\\Users\\abc\\Desktop\\images\\sentdex.png')
iar4=np.array(i4)


threshold(iar3)
threshold(iar2)
threshold(iar4)

//For ploting the grahp
fig=plt.figure()

ax1= plt.subplot2grid((8,6),(0,0),rowspan=4,colspan=3)
ax2= plt.subplot2grid((8,6),(4,0),rowspan=4,colspan=3)
ax3= plt.subplot2grid((8,6),(0,3),rowspan=4,colspan=3)
ax4= plt.subplot2grid((8,6),(4,3),rowspan=4,colspan=3)


ax1.imshow(iar)
ax2.imshow(iar2)
ax3.imshow(iar3)
ax4.imshow(iar4)

plt.show()'''

#basic dry run of how image will look if plotted.
'''

i=Image.open('C:\\Users\\abc\\Desktop\\images\\dotndot.png')
iar=np.array(i)
plt.imshow(iar)
plt.show()
i1=Image.open('C:\\Users\\abc\\Desktop\\images\\numbers\\y0.5.png')
iar1=np.array(i1)
plt.imshow(iar1)
plt.show()
print(iar1)'''