#!/usr/bin/python
## -*- coding: utf-8 -*-
#
# Copyright (C) 2018
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#
#
#Author: Fernando Rodrigo Aguilar Javier
#Author email: faguilar@comunidad.unam.mx


#Detalles del codigo --------------------------------------------------------------------
#Solo es necesario cambiar el campo de la variable path para que pandas encuentre el path

#Distancia  Variograma Experimental #Nª pares
# 100        4.5210                  28
# 200       10.5683                  45
# 300       17.82125                 52
# 400       20.7909                  58
##################################%%%%%%%%%%%%%%%%%%%%%################################
#https://es.wikipedia.org/wiki/F%C3%B3rmula_del_semiverseno

from numpy import sin, cos
from matplotlib import pyplot as plt
import pandas as pd

R = 6371#Radio de la tierra

#Fórmula de Haversine
def d_harvensine(p1, p2):
    lat_1 = p1[0]
    lat_2 = p2[0]
    long_1 = p1[1]
    long_2 = p2[1]
    delta_lat = lat_1 - lat_2
    delta_long = long_1 - long_2
    d = (sin(delta_lat / 2) ** 2) + (cos(lat_1) * cos(lat_2) * (sin(delta_long/2)**2))
    return int(d*1000)#[m]

if __name__ == '__main__':
    data = pd.read_excel('files/datos_clima.xls')
    x, y = data.shape
    d = dict()
    muestras = [100, 200, 300, 400]
    variograma = []
    pares = []
    for m in muestras:
        for i in range(x):
            p1 = data['LATITUD'][i], data['LONGITUD'][i]
            Tanual_p1 = data['Tanual'][i]
            ID_1 = i
            for j in range(i, x):
                p2 = data['LATITUD'][j], data['LONGITUD'][j]
                Tanual_p2 = data['Tanual'][j]
                ID_2 = j
                
                dist = d_harvensine(p1, p2)
                if dist == m:
                    d[ID_1] = [dist, Tanual_p1, ID_2, Tanual_p2]
        c = 0
        n_par = len(d)
        for l in d.values():
            c += (l[1] - l[3]) ** 2
        c = c / (2 * n_par)
        variograma.append(c)
        pares.append(n_par)
    plt.plot(muestras, variograma, '*--')
    plt.title('Semivariograma')
    plt.xlabel('Distancia entre muestras (m)')
    plt.ylabel('Semivariograma experimental')
    plt.show()
