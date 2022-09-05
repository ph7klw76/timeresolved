f2=open('D:test.csv','w')
import numpy as np
import csv
ii=0
path = 'D:OG_TRES Em LS12_Zeo.csv'
with open(path, 'r') as f:
    reader = csv.reader(f, delimiter=',')
    headers = next(reader)
    data = np.array(list(reader)).astype(float)
    with open('D:test.txt', 'w') as f2:
        for i in range(len(data)):
            if i<233:
                str1 = ','.join(str(e) for e in data[i])
                f2.write(str1+'\n')
            if 233<=i<317:
                if ii!=0:
                    datax +=data[i]
                    ii +=1
                if ii==0:
                    datax=data[i]
                    ii +=1
                if ii==3:
                    datax=datax/3
                    print(datax[0])
                    str1 = ','.join(str(e) for e in datax)
                    ii=0
                    f2.write(str1+'\n')      
            if 317<=i<560:
                if ii!=0:
                    datax +=data[i]
                    ii +=1
                if ii==0:
                    datax=data[i]
                    ii +=1
                if ii==9:
                    datax=datax/9
                    print(datax[0])
                    str1 = ','.join(str(e) for e in datax)
                    ii=0
                    f2.write(str1+'\n') 
            if 560<=i<3881:
                if ii!=0:
                    datax +=data[i]
                    ii +=1
                if ii==0:
                    datax=data[i]
                    ii +=1
                if ii==81:
                    datax=datax/81
                    print(datax[0])
                    str1 = ','.join(str(e) for e in datax)
                    ii=0
                    f2.write(str1+'\n') 
f2.close()
