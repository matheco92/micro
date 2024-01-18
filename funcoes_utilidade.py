#!/usr/bin/env python
# coding: utf-8

# In[170]:


import matplotlib.pyplot as plt
import numpy as np

# Exemplo de dados (substitutos perfeitos)
x1 = np.linspace(0, 10, 1000)
x2 = np.linspace(0, 10, 1000)
x1, x2 = np.meshgrid(x1, x2)
U = x1+x2

# Plotagem das curvas de nível
plt.contour(x1, x2, U, levels=10, cmap='viridis')

# Configurando limites do eixo x e y
#plt.xlim(0, 10)
#plt.ylim(0, 10)

# Adicionando rótulo e título
plt.xlabel('X1')
plt.ylabel('X2')
plt.title('Curvas de Nível de U(x1,x2) = x1+x2')

# Mostrando o gráfico
plt.show()


# In[98]:


# Exemplo de dados (complementares perfeitos)
x1 = np.linspace(0, 10, 1000)
x2 = np.linspace(0, 10, 1000)
x1, x2 = np.meshgrid(x1, x2)
U = np.minimum(x1,x2)

# Plotagem das curvas de nível
plt.contour(x1, x2, U, levels=10, cmap='viridis')

# Configurando limites do eixo x e y
#plt.xlim(0, 10)
#plt.ylim(0, 10)

# Adicionando rótulo e título
plt.xlabel('X1')
plt.ylabel('X2')
plt.title('Curvas de Nível de U = min{x1,x2}')

# Mostrando o gráfico
plt.show()


# In[133]:


# Exemplo de dados (neutro (x1))
x1 = np.linspace(0, 10, 1000)
x2 = np.linspace(0, 10, 1000)
x1, x2 = np.meshgrid(x1, x2)
U = x2

# Plotagem das curvas de nível
plt.contour(x1, x2, U, levels=10, cmap='viridis')

# Configurando limites do eixo x e y
#plt.xlim(0, 10)
#plt.ylim(0, 10)

# Adicionando rótulo e título
plt.xlabel('X1')
plt.ylabel('X2')
plt.title('Curvas de Nível de U = f(x2)')

# Mostrando o gráfico
plt.show()


# In[123]:


# Exemplo de dados (quase-linear)
x1 = np.linspace(0.01, 10, 1000)
x2 = np.linspace(0, 10, 1000)
x1, x2 = np.meshgrid(x1, x2)
U = np.log(x1)+x2

# Plotagem das curvas de nível
plt.contour(x1, x2, U, levels=10, cmap='viridis')

# Configurando limites do eixo x e y
#plt.xlim(0, 10)
#plt.ylim(0, 10)

# Adicionando rótulo e título
plt.xlabel('X1')
plt.ylabel('X2')
plt.title('Curvas de Nível de U = ln(x1)+x2')

# Mostrando o gráfico
plt.show()


# In[169]:


# Exemplo de dados (Cobb-Douglas)
x1 = np.linspace(0, 10, 1000)
x2 = np.linspace(0, 10, 1000)
x1, x2 = np.meshgrid(x1, x2)
U = (x1**1)*(x2**1)

# Plotagem das curvas de nível
plt.contour(x1, x2, U, levels=10, cmap='viridis')

# Configurando limites do eixo x e y
#plt.xlim(0, 10)
#plt.ylim(0, 10)

# Adicionando rótulo e título
plt.xlabel('X1')
plt.ylabel('X2')
plt.title('Curvas de Nível de U = C*(x1^a)*(x2^b)')

# Mostrando o gráfico
plt.show()


# In[120]:


# Exemplo de dados (ponto de saciedade)
x1 = np.linspace(0, 10, 1000)
x2 = np.linspace(0, 10, 1000)
x1, x2 = np.meshgrid(x1, x2)
U = -np.sqrt((x1-5)**2+(x2-5)**2)

# Plotagem das curvas de nível
plt.contour(x1, x2, U, levels=10, cmap='viridis')

# Configurando limites do eixo x e y
#plt.xlim(0, 10)
#plt.ylim(0, 10)

# Adicionando rótulo e título
plt.xlabel('X1')
plt.ylabel('X2')
plt.title('Curvas de Nível de U = -sqrt((x1-5)^2+(x2-5)^2')

# Mostrando o gráfico
plt.show()

