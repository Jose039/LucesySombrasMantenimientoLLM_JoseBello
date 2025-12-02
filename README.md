# Caso Práctico: **Luces y Sombras del Uso de LLMs en el Mantenimiento del Software**

Bienvenido al caso práctico donde exploraremos cómo los **Modelos de Lenguaje (LLMs)** pueden ayudar y a veces dificultar el **mantenimiento de software**.

## 🧩 Escenario

Imagina la siguiente situación:

> *Sois nuevos trabajadores en una gran empresa que os ha contratado hace unos meses. Tras un periodo de adaptación al estilo de trabajo, se os asigna vuestra primera gran tarea individual: entender un código en Python desarrollado por un antiguo empleado que ya no está en la empresa. Este código es fundamental para el próximo proyecto, y vuestro jefe quiere que lo entendáis, lo analicéis y realicéis las modificaciones necesarias, ya que la semana que viene deberéis presentarlo a vuestros superiores.*

Por suerte, vuestros “ángeles de la guarda”, **David y Adrián**, os guiarán para que vuestro jefe no os despida y podáis conservar este trabajo que tanto esfuerzo os costó conseguir. Utilizaremos una IA que nos ayudará a detectar errores y mejorar la legibilidad del código.

La herramienta seleccionada es **Codium**, una plataforma de revisión de código con IA que detecta errores y propone mejoras para mantener la calidad.

A continuación se detallan los pasos previos, los pasos principales y las tareas necesarias para superar la práctica y entregar el mejor resultado posible.

---

# 🛠️ Pasos Previos

Aseguraos de tener lo siguiente:

- Visual Studio Code instalado.
- Python 3 instalado. Si no lo tenéis, podéis descargarlo desde:  
  https://www.python.org/downloads/
- Extensión **Qodo** (icono de oso hormiguero) instalada en VSCode. Usar vuestro usuario de GitHub para mayor facilidad
- Haber **forkeado** este repositorio:  
  https://github.com/davidabuinESI/LucesySombrasMantenimientoLLM.git  
  Añadiéndole vuestro nombre.
- Haber clonado vuestro repositorio forkeado para obtener los archivos **`app.py`** y **`app_test.py`**.

---

# 📋 Pasos a Seguir

1. Abrir el repositorio clonado en VSCode.
2. Crear un archivo Markdown llamado **`AnalisisNombre.md`**, reemplazando *Nombre* por el vuestro.
3. Realizar un **análisis individual** del archivo `app.py`, dicho análisis quedará en el documnto .md.  
   En vuestro Markdown deberéis anotar los cambios y mejoras que aplicaríais al código.
5. Ejecutar los tests y **apuntar el resultado**.  
   Para ello, basta con ejecutar el archivo `app_test.py`.
6. Abrir el chat de Qodo e insertar el siguiente mensaje (en inglés, para obtener mejores resultados):

    Refactor this code to make it clean, use descriptive variable names, add Type Hints and docstrings. Refactor and improve this code in a new file called "RefactoringName.py".
*(cambiar "Name" por vuestro nombre)*

7. Comparar `app.py` con `RefactoringName.py`.  
Debéis observar las diferencias entre vuestras ideas y las modificaciones propuestas por la IA.
8. Añadir a vuestro Markdown las principales diferencias encontradas entre vuestro análisis y la refactorización de la IA.
9. Ejecutar nuevamente el test.  
- ¿Habéis obtenido el mismo resultado?  
- Si no, ¿a qué se debe?  
Responded a estas preguntas en el Markdown.
9. Revisar el código refactorizado por la IA e intentar detectar:
- Modificaciones innecesarias  
- Introducción de bugs lógicos  
- Deuda técnica añadida por la refactorización
- Entre otros (revisar guía más abajo)
10. Subir a vuestro repositorio forkeado:
 - El archivo Markdown  
 - El archivo generado por la IA (**`RefactoringName.py`**)

---


## Tabla de Categorías de Fallos en Software

| **Categoría de Fallo** | **Descripción** | **Ejemplos Comunes** |
|------------------------|------------------|------------------------|
| **1. Fallos de Lógica y Errores de Programación (Bugs)** | Errores que causan un comportamiento incorrecto o la detención del programa. | - Errores de ejecución (Runtime Errors): divisiones por cero, null pointer exceptions.<br>- Errores lógicos: el programa se ejecuta, pero produce resultados incorrectos (por ejemplo, una fórmula matemática mal implementada). |
| **2. Fallos de Diseño y Arquitectura** | Problemas que afectan la estructura, escalabilidad y flexibilidad del sistema. | - Alto acoplamiento: módulos demasiado interconectados.<br>- Baja cohesión: una clase o módulo hace demasiadas cosas no relacionadas.<br>- Diseño rígido: difícil añadir nuevas características o modificar el sistema. |
| **3. Fallos de Mantenibilidad y Documentación** | Problemas que dificultan entender, modificar o extender el código. | - Código duplicado: aumenta riesgo de errores.<br>- Falta de pruebas: ausencia de tests unitarios o de integración.<br>- Documentación inexistente u obsoleta: complica comprender el sistema. |
| **4. Fallos de Rendimiento y Recursos** | Problemas que no rompen el código, pero lo hacen lento o inestable en producción. | - Ineficiencia algorítmica: algoritmos lentos para grandes volúmenes de datos.<br>- Fugas de memoria (memory leaks).<br>- Consultas a bases de datos ineficientes: falta de índices, consultas mal diseñadas. |



# 📦 Archivos a Entregar

- Archivo Python **`RefactoringName.py`** generado por la IA.
- Archivo Markdown **`AnalisisNombre.md`** con análisis, respuestas y comparaciones.
- En la entrega del campus:

      - Enlace a vuestro repositorio forkeado (en los comentarios)
      - El archivo Markdown creado.

---
