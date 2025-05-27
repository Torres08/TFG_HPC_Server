# Estructura del Proyecto LaTeX - TFG HPC

Este repositorio contiene la memoria del Trabajo de Fin de Grado (TFG) sobre el despliegue de un servidor HPC para modelos de inteligencia artificial y simular entornos de producción. El documento está organizado en varios archivos y carpetas para facilitar su mantenimiento y extensión.

## Estructura de Carpetas y Archivos

- **proyecto.tex**  
  Archivo principal del documento. Aquí se incluyen todas las partes del TFG mediante comandos `\input{}`.  
  Modifica este archivo para cambiar el orden de los capítulos o añadir nuevos.

- **portada/**  
  Contiene los archivos de la portada.  
  - `portada_2.tex`: Portada principal del documento.

- **prefacios/**  
  Incluye el prefacio del documento.  
  - `prefacio.tex`: Texto introductorio o dedicatorias.

- **capitulos/**  
  Carpeta donde se encuentran los capítulos principales del TFG.  
  Ejemplo de archivos:
  - `01_Introduccion.tex`
  - `02_Estado_del_Arte.tex`
  - `03_Propuesta.tex`
  - `04_Implementacion_y_Evaluacion.tex`
  - `05_Gestion_en_Produccion.tex`
  - `06_Resultado_y_Analisis.tex`
  - `07_Conclusiones_y_Trabajos_Futuros.tex`

- **imagenes/**  
  Carpeta para todas las imágenes y figuras usadas en el documento.

- **commands.sty**  
  Archivo de comandos personalizados (título, autor, fecha, etc.).  
  Modifica aquí los datos generales del TFG.

## Cómo añadir elementos

### Portada
La portada se encuentra en `portada/portada_2.tex`.  
Puedes modificar el diseño o los datos desde ese archivo y desde `commands.sty`.

### Prefacio
El prefacio está en `prefacios/prefacio.tex`.  
Edita este archivo para cambiar el texto introductorio.

### Glosario
Para añadir términos al glosario:
1. Asegúrate de tener el paquete `glossaries` cargado en el preámbulo.
2. Añade términos en el archivo correspondiente (por ejemplo, `glosario.tex` o directamente en el preámbulo):
   ```latex
   \newglossaryentry{hpc}{
     name={HPC},
     description={High Performance Computing}
   }