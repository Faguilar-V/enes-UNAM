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
#--------------------------------------------------------
#17361 sismos en total
#--------------------------------------------------------
#N° de sismos    mes
#787             Enero
#666             Febrero
#7771            Marzo
#8137            Abril
#
#Sabemos que el ultimo evento de feb esta en la posicion 1452 iniciando en 0 pues la suma de los eventos registrados
#en enero y febrero da 1453 comenzando en 1.
##################################%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%################################

from numpy import random, loadtxt, save
from obspy.core import read
import pandas as pd

if __name__ == '__main__':
    #constantes
    file_path = 'Ometepec-original/'
    path = '/home/faguilar/git/enes-UNAM/geoestadistica/files/eventos_sism_correctos.txt'
    arr = loadtxt(path, dtype=str)
    distance = []
    for i in range(17361):
        event = read(file_path + arr[i])[0]
        t5 = event.stats.sac['t5']
        t6 = event.stats.sac['t6']
        m_value = max(event.data)
        dist = (t6 - t5) * 8
        distance.append([t5, t6, dist, m_value])
        print(i)
    save('muestra', distance)
