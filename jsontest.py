#!/usr/bin/python
# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt
import pylab as pl
import json
ax1 = plt.subplot(211)
ax2 = plt.subplot(212)
dicList=[json.loads(line) for line in open("F:\\nonolive\\20170512_9489b60e_nono")]
Y = [item['MEM'] for item in dicList if 'MEM' in item]
C1 = [item['CPU'] for item in dicList if 'CPU' in item]
dicList2=[json.loads(line) for line in open("F:\\nonolive\\20170511_fe4155e6_nono_old")]
Z = [item['MEM'] for item in dicList2 if 'MEM' in item]
C2 = [item['CPU'] for item in dicList2 if 'CPU' in item]
#dicList3=[json.loads(line) for line in open("F:\\nonolive\\20170512_9489b60e_live")]
#P = [item['MEM'] for item in dicList3 if 'MEM' in item]
#C3 = [item['CPU'] for item in dicList3 if 'CPU' in item]
#dicList4=[json.loads(line) for line in open("F:\\nonolive\\20170511_fe4155e6_kwai")]
#K = [item['MEM'] for item in dicList4 if 'MEM' in item]
#C4 = [item['CPU'] for item in dicList4 if 'CPU' in item]
X = np.linspace(1, 200,200)
#pl.title('Lenovo A6000')
#mem
plt.sca(ax1)
plt.plot(X, Y, 'r', label="new")
plt.plot(X, Z, 'g', label="old")
#plt.plot(X, P, 'b', label="live")
#plt.plot(X, K, 'y', label="kwai")
#plt.xlabel('times')
plt.ylabel('memory(M)')
plt.legend(loc='upper left')
plt.title('mi 4c')
#cpu
plt.sca(ax2)
plt.plot(X, C1, 'r', label="new")
plt.plot(X, C2, 'g', label="old")
#plt.plot(X, C3, 'b', label="live")
#plt.plot(X, C4, 'y', label="kwai")
#plt.xlabel('times')
plt.ylabel('CPU(%)')
plt.legend(loc='upper left')
#t=80
#pl.plot([t,t],[117,Y[t]], color ='red', linewidth=2.5, linestyle="--")
#pl.scatter([t,],[Y[t],],50,color = 'red')
#pl.plot([t,t],[117,Z[t]], color ='green', linewidth=2.5, linestyle="--")
#pl.scatter([t,],[Z[t],],50,color = 'green')

plt.show()