import numpy as np
from scipy.signal import savgol_filter
import matplotlib.pyplot as plt



file='C:/Users/user/Documents/woon/book1.csv'
arr = np.loadtxt(file, delimiter=";")


def filtering(arr,n):
    x0=arr[0]
    y0=arr[n]
    y_filtered = savgol_filter(y0,9, 2) 
    return x0,y_filtered

towrite=open('C:/Users/user/Documents/woon/book1.txt','w')
for i in range(len(arr[0])):
    x0,y0=filtering(arr,i)
    x01=x0[25:]
    y01=y0[25:]
    location=np.argmax(y01)
    lamda=x01[location]
    towrite.write(str(lamda)+'\n')
towrite.close()
    

# fig, ax = plt.subplots()
# ax.scatter(arr[0],arr[120])
# ax.plot(x0,y0, 'r')
# # ax.set(xlim=(0,np.max(x0)),ylim=(0,np.max(y0)))
# plt.show()    
