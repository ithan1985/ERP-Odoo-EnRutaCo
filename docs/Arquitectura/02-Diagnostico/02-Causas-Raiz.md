1. Introducción

El análisis de brechas evidenció deficiencias relacionadas con la operación, la gestión de la información y la arquitectura tecnológica. Para comprender el origen de estas situaciones, es necesario analizar sus causas raíz desde una perspectiva integral, considerando personas, procesos, aplicaciones, datos y tecnología.

2. Relación Problema → Causa Raíz
Problema observado	Causa raíz
Información inconsistente entre áreas	Cada aplicación administra su propia información sin mecanismos de integración.
Reportes gerenciales tardíos	La consolidación de información depende de procesos manuales.
Baja trazabilidad de las operaciones	Los sistemas que soportan la operación funcionan de manera independiente.
Dependencia del conocimiento del personal	Los procesos no se encuentran suficientemente estandarizados y documentados.
Baja capacidad para soportar el crecimiento	La evolución tecnológica ha sido incremental y orientada a resolver necesidades puntuales.

Las causas identificadas se fundamentan en los hallazgos documentados durante el AS-IS.

3. Análisis por dominio
3.1 Negocio
Hallazgos
Crecimiento acelerado.
Operación distribuida.
Dependencia del conocimiento de las personas.
Causas
Procesos con un alto componente manual.
Conocimiento operativo concentrado en colaboradores con experiencia.
Crecimiento organizacional más rápido que la evolución de los procesos.
3.2 Procesos
Hallazgos
Validaciones manuales.
Conciliaciones entre áreas.
Retrabajos.
Causas
Ausencia de un flujo integrado de información.
Procesos ejecutados sobre diferentes plataformas.
Actividades manuales para completar el proceso de extremo a extremo.
3.3 Aplicaciones
Hallazgos
CRM en Excel.
TMS independiente.
AS/400 heredado.
Aplicación móvil aislada.
Causas
Incorporación de soluciones en distintos momentos de la evolución de la empresa.
Implementaciones orientadas a resolver necesidades específicas de cada área.
Falta de una arquitectura empresarial que guiara la evolución del ecosistema de aplicaciones.

La última causa es una inferencia arquitectónica basada en el crecimiento incremental descrito en el caso; no aparece formulada literalmente.

3.4 Datos
Hallazgos
Información distribuida.
Reportes manuales.
Datos diferentes entre áreas.
Causas
No existe una fuente única de información.
Los datos permanecen aislados en las aplicaciones.
La integración entre plataformas es limitada.
3.5 Tecnología
Hallazgos
Sistemas heterogéneos.
Baja interoperabilidad.
Causas
Evolución tecnológica incremental.
Falta de integración entre plataformas.
Arquitectura tecnológica orientada a aplicaciones individuales y no al ecosistema empresarial.

La tercera causa corresponde a una conclusión del análisis arquitectónico basada en la evidencia del caso.

4. Diagrama de causa–efecto
                 Crecimiento acelerado
                         │
        ┌────────────────┼────────────────┐
        │                │                │
        ▼                ▼                ▼
   Procesos         Aplicaciones       Datos
   manuales        independientes    fragmentados
        │                │                │
        └────────────────┼────────────────┘
                         ▼
             Baja capacidad de gestión
                         ▼
        Información tardía e inconsistente
                         ▼
         Dificultad para la toma de decisiones
5. Causas estructurales

Las siguientes causas tienen impacto transversal sobre toda la organización:

Causa estructural	Impacto
Fragmentación de aplicaciones	Información distribuida entre plataformas.
Procesos manuales	Retrabajos y demoras.
Ausencia de integración	Baja trazabilidad y duplicidad de información.
Dependencia del conocimiento tácito	Riesgo operativo ante rotación del personal.
Crecimiento organizacional sin evolución equivalente de la arquitectura	Dificultad para escalar la operación.
6. Conclusión

El análisis de causas raíz evidencia que los problemas observados no corresponden a una única aplicación o proceso, sino al efecto acumulado de decisiones tomadas a lo largo del crecimiento de la organización. Las principales causas están relacionadas con la fragmentación del ecosistema de aplicaciones, la dependencia de procesos manuales, la dispersión de la información y la ausencia de una arquitectura empresarial integrada. Estos resultados servirán de base para evaluar los riesgos, identificar oportunidades de mejora y definir la arquitectura objetivo (TO-BE).