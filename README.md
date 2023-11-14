# AJAX

## **INTEGRANTES**
- Sebastián Bustamante
    - sbusta16@eafit.edu.co
- Valeria Castro
    - vcastro@eafit.edu.co
- Juan Pablo Ramirez
    - jurami35@eafit.edu.co
- Diego Fernando Martinez
    - dimarti22@eafit.edu.co

## **TIPO DE PROYECTO**
Análisis de datos, para interpolar los resultados en una visión efectiva de las posibles soluciones que se puede realizar mediante la Gamificación.

## **TECNOLOGÍAS EMERGENTES QUE EMPLEARÁ LA SOLUCIÓN**
En la etapa actual el saber cual de las tecnologías a usar son inciertas puesto que el tipo de desarrollo el cual estamos realizando (MID-ANO), este se determina en la etapa 2 del desarrollo.

Estamos utilizando este tipo de desarrollo ya que es el que mayor facilidad de definición de objetivo y herramientas para la solución del proyecto. 

## **¿CÓMO SERÁ LA VISIÓN DE FUTURO DE LA SOLUCIÓN?**

Durante esta fase de la metodología elegída podemos decir que:
Es un estudio de los patrones de comportamiento encontrados en los flujos de datos determinados por las etapas iniciales, las cuales ofrecerán soluciones de gamificacion a las plataformas de SAI (de momento Ulises)

## **¿CUÁL ES EL DESAFÍO PARA EL EQUIPO?**
- Aplicar un análisis de datos eficiente.
- Aprender todo sobre la gamificación, sus métodos y su comportamiento.
- Apropiarnos de la metodología de desarrollo MID-ANO.
- Entender los tipos de análisis de datos (ADE y ADC)


## **DIFERENCIADORES QUE TENDRÁ LA SOLUCIÓN PLANTEADA**

El posible uso de machine learning para el análisis de datos orientados en la gamificación y posibilidad de escalar a las otras plataformas de SAI.


## **USUARIOS DEL PRODUCTO Y MERCADO POTENCIAL**
- Los Estudiantes.
- Los Administradores de SAI.

### **Vigilancia tecnológica**

Como estamos haciendo uso de la metodología MID-ANO, la cual consta de 3 fases, en la primera fase se determina el objetivo a llegar y que variables se van a utilizar para llegar a ese objetivo, por otro lado, en la fase 2 se tratan los datos, en esa fase elegimos que tecnologías vamos a utilizar, aunque esta lejana, se puede deducir cual sera una de las posibles tecnologías a usar, la cual podría ser machine learning.

### **Estado del arte**

La analítica de datos es la exploración y comprensión de la información en grandes cantidades para descubrir patrones ocultos, correlaciones y otras posibilidades, con el fin de evitar problemas futuros, optimizar procesos de producción, entre otros usos.

# **ESPECIFICACIÓN PRODUCTO MINIMO VIABLE (MPV)**

## **DESCRIPCIÓN TÉCNICA DE LA SOLUCIÓN**
El modelo analiza grandes cantidades de datos, buscando patrones los cuales le ayudaran para predecir un futuro estado o movimiento del flujo del sistema. 

Se muestran los resultados de manera organizada en una interfaz de visualización interactiva al usuario (SAI) y consecuente los usuarios realizarán los ajustes necesarios a la plataforma.
 
## **CONSIDERACIONES NO FUNCIONALES O DE ATRIBUTOS DE CALIDAD CLAVES PARA DESARROLLAR EL MPV**

- **INTEGRIDAD:**
Nuestro sistema no debe modificar o alterar los datos, durante la clasificación o envío de estos ya que afecta el análisis.

- **ESCALABILIDAD:** 
El sistema debe de ser escalable, ya que los datos irán aumentando con el paso del tiempo.  

- **CONFIABILIDAD:**
El sistema debe tener el minímo porcentaje de error para que las predicciones futuras sean lo mas acertadas. 

# **PROCESO UCD**
## **HOT IDEA**
Vamos a realizar un análisis de datos de las distintas plataformas de parte de SAI; De momento estará enfocada en la plataforma ulises pero se puede escalar a las demás plataformas, el alcance se definirá en la primera etapa. El cual está dividida en etapas las cuales entregarán el objetivo y por ende los recursos a usar para la realización de un modelo de solución para dicha plataforma centrada en métodos de gamificación.

## **IDEAS DE DISEÑO**
- Los datos no serán mostrado al usuario tipo 'Estudiante'.
- Mostrar Los datos en una herramienta visual interactiva. 
- Clasificar los datos según periodos de tiempo.
- Se debe predecir un posible flujo de datos futuro.

## **NOTAS DE ENTREVISTAS**
Puesto que método que estamos usando se divide en diferentes capas, como ya se ha mencionado anteriormente; el realizar las entrevistas en esta etapa del proyecto no pertinente, puesto que la identificación de el tema de las entrevistas no se puede realizar si anteriormente no se a diseñado y aceptado los modelos a implementar, ya que estos modelos poseen las posibles direcciones y variables que va tomar para la solución del proyecto.


# ARQUITECTURA BASE

### GESTIÓN DE LA CONFIGURACIÓN Y AMBIENTE 
Actualizar el documento de Plan de Configuración de entorno de la entrega anterior y adjuntar el archivo en formato PDF.

### DEFINICIÓN DE ARQUITECTURA V1
La arquitectura planteada en este documento se basa en 4 vistas que definen aspectos en los siguientes frentes:

- **_Vista Conceptual:_** visión que los usuarios tienen de la aplicación.
- **_Vista Lógica:_** visión desde los principales elementos y principios del diseño.
- **_Vista Física:_** visión desde la distribución del procesamiento entre los dispositivos.
- _**Vista de Implementación:**_ visión que muestra cómo serán el movimiento que tiene o que tuvo y mostrar su historial montados los diferentes componentes de la aplicación y la forma en que interactúan.


### ATRIBUTOS DE CALIDAD DEL SISTEMA
Esta sección explica cómo la arquitectura presentada cumple con cada una de las propiedades de calidad del sistema requeridas. Si bien gran parte de esta información será intrínseca a las vistas documentadas en las secciones anteriores, a menudo es útil presentar parte de ella por separado. En particular, si una propiedad de calidad, como la seguridad o el rendimiento, depende de las características documentadas en varias vistas diferentes, debe explicarlo aquí. Por ejemplo, la escalabilidad puede depender de las optimizaciones en el modelo de datos (documentado en la Vista de información) junto con los componentes de equilibrio de carga (documentados en la Vista de implementación).


#### Seguridad
- El sistema debe mantener la integridad de los datos.

#### Disponibilidad y resiliencia
- El sistema debe estar disponible la mayor cantidad de tiempo posible con respecto a 24 horas, en caso de fallos arreglarse en menos de 30 minutos.

#### Otros atributos de calidad
- El sistema no debe repetir en tiempos cortos una sola solución, debe dar distintas soluciones en un tiempo minimo de 30 minutos.
- El sistema debe ser facíl de usar, debe usar un lenguaje conocido y no tecnico.

## ESTADO DEL ARTE, VIGILANCIA TECNOLÓGICA Y SELECCIÓN DE LA TECNOLOGÍA
**Estado del Arte**: Las técnicas de aprendizaje automático (o Machine Learning) están experimentando un auge sin precedentes en diversos ámbitos tanto el académico como en el empresarial, y constituyen una importante palanca de transformación. Si bien estas técnicas eran conocidas en los dos ámbitos, diversos factores están provocando que su uso sea mas intensivo cuando antes era minoritario, y que se extienda a otros campos cuando antes prácticamente no eran utilizadas, tanto por los elevados costes de implantación como por los escasos beneficios inicialmente esperados de su aplicación. [n]managementsolutions.com/sites/default/files/publicaciones/esp/machine-learning.pdf

**Vigilancia tecnológica (VT)**: Buscando competidores en el área de toma de decisiones para gamificiacion encontramos las siguientes empresas:

**Bunchbal**l: La empresa bunchball presenta un servicio de análisis de comportamientos a travez de una plata forma llamada Nitro, en esta se capturan datos y se implementan estrategias de gamificación basadas en los datos capturados para mejorar el engagement de clientes y trabajadores.
[n]https://www.bunchball.com/

**Gamifica**: Es una empresa dedicada a crear soluciones de gamificación para empresas call-center, ofrece una plataforma en la cual se pueden hacer concursos, crear retos, y asignar medallas entre otras opciones de gamificación para incentivar a los trabajadores a mejorar su productividad.
[n]https://www.gamificagroup.com/

Para distinguimos de los competidores nosotros presentamos un servicio 100% personalizado usando modelos descriptivos de Machine Learning, sin necesidad de interfaces mediadoras, si no conectados directamente a la lógica de negocios de la empresa, así pudiendo dar soluciones más acertadas sobre cuales elementos de gamificación pueden ser más efectivos para mejorar el engagement de la empresa.

**Justificación**: Observando las necesidades del PO al no tener herramientas que le permitan decidir cuál de todas las opciones de gamificación implementar, llegamos a la conclusión que la mejor solución sería crear un modelo descriptivo a través de un ciclo autónomo que simule el comportamiento de los estudiantes en la plataforma y así darle una buena retroalimentación al PO parra que pueda tomar decisiones optimas sobre cual tipo de gamificación implementar.


# ESPECIFICACIÓN DE LA TECNOLOGÍA
Machine Learning
Drool

Estas dos tecnologías facilitan el analísis de grandes cantidades de datos y su manipulación.

### CLIENTE WEB Y/O MÓVIL

Cliente Web
 
### LENGUAJES DE PROGRAMACIÓN
 
Por el momento el lenguaje de programación que tenemos propuesto es Python, pues tiene librerias que facilitan la automatización de procesos.

### LIMITACIONES

La mayoria de los integrantes no tenemos experiencia con analísis de datos, lo cual dificulta la elección de tecnologías, ya que debemos hacer un analísis previo.

###  PLATAFORMA DE GESTIÓN DE PROYECTOS

**Azure DevOps**

###   AMBIENTE DE DESARROLLO, PRUEBAS Y PRODUCCIÓN
 
Por el momento tenemos como intención usar IaaS Amazon cloud, porque es conocido por algunos miembros del equipo, lo cual facilita el comprender y usar esta herramienta.

 
### PLATAFORMAS PARA CLOUD COMPUTING
 
Amazon Cloud
 
### BIBLIOTECAS DATA SCIENCE
 
- PyOD 
- Vaex 
- Yellowbrick 
- Pandarallel

# Concluciones

El proyecto nos permitió conocer a los usuarios a través de un medio virtual, pues el comportamiento de estos en un medio como Ulises es la vía para conocer cómo se puede aplicar una gamificación en espacios académicos con el fin de atraer a los usuarios, incrementar el uso de la plataforma y hacer que se sientan en un ambiente donde el aprendizaje no se sienta forzado, si no, sea algo que disfruten.

El análisis del flujo en la plataforma permite conocer hacia donde debe ser dirigida la atención de los estudiantes, donde hay menos visitas y deben apropiarse más, donde debe ser enfocada la gamificación para que los usuarios frecuenten más esos lugares olvidados.

La definición de una metodología es algo muy importante en la elaboración de trabajos como este, pues gracias a que definimos una metodología, se tenía claro el objetivo de cada paso e investigación realizada.

Para lograr este proyecto se realizó un trabajo investigativo, para poder llegar a conclusiones que aporten en el estudio de los flujos en la plataforma, para ello, fue necesario definir una serie de modelos preestablecidos que aportaban en la construcción del modelo final.

# **Bibliografía**

"Analítica de datos para qué sirve y qué es?", Osma Peña, Poliverso, https://www.poli.edu.co/blog/poliverso/analitica-de-datos.
