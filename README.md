# Text Analysis for Social Programs in Mexico

## Introducción
Con el objetivo de generar mejorar la focalización de programas, es importante conocer los programas sociales para poder hacer recomendaciones de programas o temáticas que vayan enfocadas tanto a los principales riesgos de los municipios o estados como a los objetivos de desarrollo sostenible.

## Datos
Objetivos generales y específicos de los programas sociales federales obtenidos a partir del Cuestionario Único para el Análisis de Programas Sociales (SEDESOL, 2016). Actualmente se cuenta con 43/149 programas a nivel federal.

Los datos pueden descargarse [aquí](https://s3-us-west-2.amazonaws.com/sedesol-open-data/cuaps_sedesol.csv)

## Requisitos
- `python 3.6` o superior
- `R`
- `shiny`

Además:
- `nltk`
- `gensim`

## Estructura
- `etl:` directorio que contiene la ingesta de información
    - ingest_texts.txt ingesta del texto, transformación y unión del texto para cada programa
- `data:` directorio que contiene archivos de texto utilizados en el análisis
    - stop.txt: contiene las palabras a excluir en el ánalisis que no cuentan con significado semántico para el contexto
- `docs:` jupyter notebooks que explican los pasos seguidos
- `scripts:` 

### Instrucciones

## Avances

- Análisis de tópicos:
Se generan tópicos por medio de Latent Dirichlet Allocation.

- Medidas de Similitud
Doc2vec 

## Siguientes Pasos
- Analizar distribución de cobertura de programas similar
- Ampliar a más programas
- Ampliar análisis a ms niveles: estatal y municipal

### ¿Cómo Constribuir?


## Referencias
