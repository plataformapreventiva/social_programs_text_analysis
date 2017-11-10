# Text Analysis for Social Programs in Mexico

## Introducción
Con el objetivo de generar mejorar la focalización de programas, es importante conocer los programas sociales para poder hacer recomendaciones de programas o temáticas que vayan enfocadas tanto a los principales riesgos de los municipios o estados como a los objetivos de desarrollo sostenible.

## Datos
Objetivos generales y específicos de los programas sociales federales obtenidos a partir del Cuestionario Único para el Análisis de Programas Sociales (SEDESOL, 2016). Actualmente se cuenta con 43/115 programas a nivel federal.

Los datos pueden descargarse [aquí](https://s3-us-west-2.amazonaws.com/sedesol-open-data/cuaps_sedesol.csv)

## Requisitos
- `python 3.6` o superior
- `R`
- `shiny`

Además:
- `nltk`
- `gensim`

## Estructura


### Instrucciones

## Avances
Se genera un análisis de texto con los objetivos generales y específicos de los programas para agrupar a las palabras en diferentes temas. Los temas se crean a partir del número de ocurrencias entre palabras dentro de cada documento- Cada programa puede estar representado en uno o más temas. 

Además, se genera un modelo para encontrar similitud entre programas sociales con el objetivo de evitar duplicidades y crear mayor colaboración entre unidades ejecutoras. 

## Siguientes Pasos

### ¿Cómo Constribuir?


## Referencias
