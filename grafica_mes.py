import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anm

dias=["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo","Festivo","Antes Festivo"]
cdias=[42,52,47,49,51,52,42,15,15]
n=9
datos=np.loadtxt('choques3.txt').reshape((31,14,n))#y,x,d
print datos.shape
print datos[7,6,0]
fig=plt.figure()
for i in range(n):
	datos[:,:,i]=datos[:,:,i]/cdias[i]
#im=plt.imshow(datos[:,:,0],cmap='YlOrRd')
#plt.xlim(-0.5,7.5)
#plt.ylim(14.5,-0.5)
#plt.colorbar()
#plt.show()
ims=[]
for i in range(n):
	ttl = plt.text(0.5, 0.5, dias[i], horizontalalignment='left', verticalalignment='bottom')
	#txt = plt.text(i,i,i)
	im=plt.imshow(datos[:,:,i], animated=True,vmin=0,vmax=5,cmap='YlOrRd')#cmap='YlOrRd', animated=True)
	ims.append([im,ttl])#,txt])
gif=anm.ArtistAnimation(fig,ims,interval=750)
#plt.colorbar()
cbar = plt.colorbar()
cbar.set_label('# choques')
plt.title('Choques por celda cada dia')
plt.xlabel('longitud')
plt.ylabel('latitud')
plt.xticks(np.linspace(-0.5,13.5,4),[-74.21,-74.16,-74.10,-74.05])#np.linspace(-74.21022,-74.02318,8))
plt.yticks(np.linspace(-0.5,30.5,15),[4.84,4.82,4.79,4.77,4.74,4.72,4.69,4.67,4.65,4.62,"4.60",4.57,4.55,4.52,"4.50",4.47])#np.linspace(4.84300,4.49752,15))
gif.save('mes.gif')
"""
uxt=np.loadtxt('datos.txt')
x=np.linspace(0,100,len(uxt[0,:]))

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set(xlabel=r'$x$',ylabel=r'$u(x,t)$',title='Cuerda vibrando',ylim=(-1,1),xlim=(0,100))
datos, = ax.plot(x,uxt[0,:])

def iteracion(i):
	datos.set_ydata(uxt[i,:])

gif = anm.FuncAnimation(fig, iteracion,frames=len(uxt[:,0]), interval=50)
gif.save('cuerda.gif')

datos = np.loadtxt('datos.txt').reshape((N,N,3))#(x,y,en 0 V en 1 Ex en 2 Ey)
plt.imshow(datos[:,:,0],extent=[-2.5,2.5,-2.5,2.5],cmap='hot')
plt.colorbar()
plt.xlim(-2.5,2.5)
plt.ylim(-2.5,2.5)
plt.title('Potencial placas [V] y lineas de campo electrico')
"""

