Instrucciones de Despliegue y Ejecución

Para reproducir este experimento y generar la gráfica comparativa de tiempos de ejecución, siga los siguientes pasos desde una terminal de Windows (CMD o PowerShell).

1. Requisitos Previos (Dependencias)
Antes de comenzar, asegúrese de tener instaladas las siguientes herramientas y librerías en su sistema:

    Python 3.x: Con las librerías ply y matplotlib instaladas (pip install ply matplotlib).

    Java Development Kit (JDK): Versión 11 o superior.

    ANTLR4: El archivo antlr-4.13.2-complete.jar debe estar descargado y ubicado en la raíz del proyecto.

    (Opcional para C) MinGW / GCC: Con los paquetes de flex y bison configurados en las variables de entorno.

2. Compilación del Analizador en Java (ANTLR4)
El analizador de Java requiere generar sus clases a partir de la gramática antes de su ejecución. Ubíquese en la raíz del proyecto y ejecute:

    Generación del código Lexer y Parser:
    java -jar antlr-4.13.2-complete.jar DockerCompose.g4

    Compilación de las clases generadas junto con el punto de entrada:
    javac -cp ".;antlr-4.13.2-complete.jar" *.java