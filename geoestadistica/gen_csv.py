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
#Datos clima
##################################%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%################################
import pandas as pd
from numpy import save, array

if __name__ == '__main__':
    path = '/home/faguilar/git/enes-UNAM/geoestadistica/files/'
    clima = pd.read_excel(path + 'datos_clima.xls').to_numpy()
    arr_clima = []
    for r in clima:
        arr_clima.append([r[2], r[3], r[5]])
    array(arr_clima)
    save('datos', arr_clima)
