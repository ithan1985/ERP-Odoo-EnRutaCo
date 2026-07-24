1. Introducción

Toda iniciativa de transformación empresarial se desarrolla dentro de un conjunto de restricciones organizacionales y bajo determinados supuestos. Documentar estos elementos permite reducir riesgos, alinear expectativas y garantizar que las decisiones de arquitectura sean consistentes con el contexto del proyecto.

2. Restricciones del Negocio
Código	Restricción	Impacto
RS-01	La operación logística debe mantenerse durante la transformación.	Alto
RS-02	La transformación debe minimizar la interrupción de los procesos críticos.	Alto
RS-03	Las mejoras deben responder a los objetivos estratégicos del negocio.	Alto
3. Restricciones Organizacionales
Código	Restricción	Impacto
RS-04	La adopción de nuevos procesos requiere gestión del cambio.	Alto
RS-05	Será necesario capacitar a los usuarios en los nuevos procesos y herramientas.	Medio
RS-06	La transformación deberá involucrar a todas las áreas impactadas.	Alto
4. Restricciones Tecnológicas

A partir del caso de estudio se identifican las siguientes restricciones:

Código	Restricción
RS-07	Existen múltiples aplicaciones que soportan procesos críticos.
RS-08	Parte de la operación depende de sistemas heredados.
RS-09	La información se encuentra distribuida entre diferentes aplicaciones.

Estas restricciones provienen del estado actual documentado durante el AS-IS.

5. Supuestos

Para el diseño de la Arquitectura Objetivo se adoptan los siguientes supuestos:

Código	Supuesto
SU-01	La organización mantendrá su estrategia de crecimiento.
SU-02	La dirección apoyará el proceso de transformación.
SU-03	Los procesos podrán rediseñarse cuando sea necesario.
SU-04	Será posible integrar o reemplazar gradualmente aplicaciones existentes.
SU-05	Los datos actuales podrán migrarse hacia la nueva arquitectura mediante un proceso controlado.

Nota: Estos supuestos corresponden a hipótesis de trabajo para el caso de estudio. Deberán validarse antes de la ejecución del proyecto.

6. Dependencias

La transformación dependerá de iniciativas complementarias, entre ellas:

Dependencia	Descripción
Gobierno de procesos	Definición y estandarización de procesos.
Gobierno de datos	Definición de responsables y reglas de calidad de datos.
Gestión del cambio	Acompañamiento a usuarios durante la adopción.
Capacitación	Formación en nuevos procesos y herramientas.
Gobierno de arquitectura	Seguimiento al cumplimiento de principios y criterios definidos.
7. Riesgos Asociados a los Supuestos
Supuesto	Riesgo si no se cumple
SU-01	La arquitectura puede quedar sobredimensionada o insuficiente.
SU-02	Retrasos en la toma de decisiones y baja adopción.
SU-03	Persistencia de procesos ineficientes.
SU-04	Mayor complejidad en la integración tecnológica.
SU-05	Problemas de calidad y continuidad de la información.
8. Criterios para Revisar Restricciones

Durante el proyecto, las restricciones y supuestos deberán revisarse en los siguientes hitos:

Finalización del diseño TO-BE.
Inicio de la implementación.
Antes de cada fase de despliegue.
Durante la gestión de cambios relevantes del proyecto.
9. Conclusión

Las restricciones y supuestos documentados proporcionan el contexto necesario para diseñar una Arquitectura Objetivo realista y alineada con las capacidades de EnRutaCo. Su revisión periódica permitirá ajustar las decisiones arquitectónicas conforme evolucione el proyecto y reducir los riesgos asociados a la transformación.