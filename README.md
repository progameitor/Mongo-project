# Mongo-project

El objetivo de este proyecto es localizar las mejores ubicaciones para nuestras proximas oficinas en base a unos parametros.

Trabajamos sobre una base de datos que tenemos dentro de nuestro MongoDB Compass importada desde un archivo que nos 
facilitaron en clase. En este archivo nos encontramos muchisimas empresas a lo largo del mundo hasta 2013 y nos facilitan datos como su localizacion tipo de empresa, cantidad de fondos etc ..

Criterios a cumplir:(Al menos 3 de ellos)

*COGER LOS CRITERIOS QUE TENGO EN EL VISUAL STUDIO CODE"

Guia del trabajo realizado:

1- Limpieza

2- Enriquecimiento de los datos con la API de Yelp.

3- Introduccion de los datos,a mongoDB compass, que me interesaban en base a las condiciones que nos daban a cumplir para poder representarlas en un mapa.

4- "Rankeo de los datos obtenidos y propuesta de los puntos


1- LIMPIEZA

Lo primero que he realizado es la limpieza de los datos del fichero genérico. Esta limpieza la realizo en el fichero "".
Mi primera consulta a la base de datos es unos filtros que me parecieron interesantes. Me quedo con las empresas desde 2005 hasta 2011 porque leyendo un articulo observe que eran un momento bueno para la creación de empresas tecnológicas.

Despues de una primer filtro me quedo solo con las columnas que me interesan. Observando vi que habia muchas empresas relacianodadas con la tecnología y por eso muchas de ellas me las agrupe en esta categoria.

Lo siguiente que vi es que las unidades que habian