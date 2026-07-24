1. Visión General

La arquitectura de aplicaciones de EnRutaCo ha evolucionado de manera incremental. A lo largo de los años se incorporaron diferentes soluciones para resolver necesidades específicas de cada área, sin una arquitectura empresarial integrada. Como resultado, conviven plataformas heredadas, aplicaciones desarrolladas internamente, herramientas ofimáticas y procesos manuales.

2. Inventario de Aplicaciones
Aplicación	Dominio	Estado	Observaciones
AS/400 Facturación	Finanzas	Activo	Sistema heredado para facturación.
CRM en Excel	Comercial	Activo	Gestión comercial mediante hojas de cálculo.
TMS	Operaciones	Activo	Sistema de transporte sin integración con otras plataformas.
Aplicación de Mensajeros	Operaciones	Activo	Utilizada en campo, sin integración con el backend.
Herramientas Ofimáticas	Toda la organización	Activo	Apoyan procesos manuales y conciliaciones.

La información anterior corresponde a los sistemas mencionados explícitamente en el caso.

3. Relación Aplicaciones ↔ Procesos
Proceso	Aplicación principal
Gestión Comercial	CRM en Excel
Facturación	AS/400
Planeación y Transporte	TMS
Operación en Campo	App de Mensajeros
Reportes	Herramientas ofimáticas

El caso no documenta aplicaciones adicionales para estos procesos; por ello no se agregan otras herramientas.

4. Integración entre Aplicaciones

El caso evidencia un bajo nivel de integración.

Origen	Destino	Integración
CRM Excel	AS/400	No documentada
CRM Excel	TMS	No documentada
TMS	App Mensajeros	No documentada
App Mensajeros	Facturación	No documentada

La información disponible indica que existen sistemas desconectados y un TMS sin integración, pero no describe interfaces específicas entre aplicaciones.

5. Características del Landscape

La arquitectura presenta las siguientes características observadas en el caso:

Sistemas desarrollados en momentos diferentes.
Aplicaciones con objetivos específicos por área.
Ausencia de una arquitectura integrada.
Dependencia de herramientas ofimáticas.
Procesos soportados por actividades manuales.
Información distribuida entre múltiples plataformas.

6. Riesgos Identificados

Sin proponer soluciones, el caso permite identificar los siguientes riesgos asociados a la arquitectura de aplicaciones:

Riesgo	Evidencia
Información fragmentada	Diferentes áreas manejan datos distintos.
Baja integración	Sistemas desconectados.
Dependencia de procesos manuales	Conciliaciones y validaciones manuales.
Retrasos en la información	Reportes gerenciales disponibles únicamente al final de la semana.
Dependencia del conocimiento tácito	Los colaboradores compensan limitaciones tecnológicas mediante experiencia.
7. Observaciones del Arquitecto (AS-IS)

A partir del caso, se puede concluir que:

Las aplicaciones cumplen funciones específicas para cada área.
No existe evidencia de una estrategia de integración empresarial.
La arquitectura responde a un crecimiento incremental de la organización.
La operación continúa siendo posible gracias a la combinación de sistemas, herramientas ofimáticas y actividades manuales.

Estas observaciones describen el estado actual y no constituyen recomendaciones de diseño.