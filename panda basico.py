# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1A-i5jhjiIY0j4OOvIwdtRkngu1S1Vbo4
"""

import numpy as np
  import pandas as pd
  import geopandas as gp

"""#crear una serie
colunma de de datos
"""

s = pd.Series([34,35,38,49,50])
s

"""#diccionarios en python
guarda datos en forma de objetos llave-valor

"""

midiccionario= {
    "nombre": "casal",
    "area": 120,
    "baños": ["andres", "diana", "sofia"],
    "barrio": {
        "nombre": "gran britalia", "localidad"; "bosa"
    }
}

"""#Data frame
conjuntos de series apiladas

la forma "simple" de crear un data frame es a partir de un deccionario, otra froma puede ser desde hojas de calculo, desde archivos JSON o desde archivos CSV (valores separados por coma)

"""

midataframe=pd.DataFrame({'si': [10,15], 'no': [50, 68]})
midataframe