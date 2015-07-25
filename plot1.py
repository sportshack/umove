from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = []
y = []
z = []
acelerometro = open("/resources/dadosAcelerometro.csv","r")
for linha in acelerometro:
    X, Y, Z = linha.split(",")
    x.append(float(X))
    y.append(float(Y))
    z.append(float(Z))
giroscopio.close()

ax.scatter(x, y, z, c='r', marker='o')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()