1. Visión General

La información de EnRutaCo se encuentra distribuida entre múltiples aplicaciones y herramientas, lo que dificulta disponer de una visión única del negocio. La consolidación de datos depende de procesos manuales y conciliaciones entre áreas.

2. Principales dominios de información

Con base en los procesos identificados, los principales dominios de datos son:

Dominio	Descripción
Clientes	Información de clientes corporativos y consumidores finales.
Pedidos	Solicitudes de transporte y entrega.
Operaciones Logísticas	Planeación, rutas y ejecución de la operación.
Transporte	Información asociada al movimiento de mercancías.
Entregas	Evidencia y estado de las entregas.
Facturación	Datos relacionados con la facturación de los servicios.
Servicio al Cliente	Casos, novedades y solicitudes de atención.

Estos dominios se derivan de los procesos y servicios descritos en el caso, no de un modelo de datos explícito.

3. Origen de los datos
Dominio	Fuente principal
Clientes	CRM en Excel
Pedidos	CRM / procesos operativos
Transporte	TMS
Facturación	AS/400
Operación en campo	Aplicación de mensajeros
Reportes	Consolidación manual

La fuente de cada dominio corresponde a las aplicaciones identificadas en el documento de Arquitectura de Aplicaciones.

4. Flujo de la información

De manera general, la información sigue el siguiente recorrido:

Cliente
    │
Registro del pedido
    │
Planeación logística
    │
Ejecución del transporte
    │
Entrega
    │
Facturación
    │
Reportes

El caso no documenta el flujo técnico de intercambio de datos entre aplicaciones; este esquema representa el flujo funcional de la información asociado al proceso de negocio.

5. Características de la gestión de datos

A partir del caso se identifican las siguientes características:

La información se encuentra distribuida en diferentes plataformas.
No existe una fuente única de información.
Los reportes requieren consolidaciones manuales.
La información no se encuentra integrada entre todas las áreas.
Las decisiones gerenciales dependen de datos obtenidos desde múltiples sistemas.
6. Problemas identificados
Problema	Evidencia
Información fragmentada	Los datos se encuentran en múltiples sistemas.
Duplicidad potencial	Diferentes áreas manejan información independiente.
Retrasos en la consolidación	Reportes elaborados manualmente.
Baja trazabilidad	Parte de la operación carece de seguimiento completo.
Baja confiabilidad para la toma de decisiones	La dirección no cuenta con información integrada y oportuna.
7. Observaciones del Arquitecto (AS-IS)

Del análisis del caso se concluye que:

Los datos están organizados por aplicación y no por dominios de negocio.
No se evidencia una estrategia de gobierno de datos.
La organización depende de actividades manuales para consolidar información.
La ausencia de integración limita la disponibilidad de información confiable para la toma de decisiones.

Estas observaciones describen la situación actual y no constituyen una propuesta de solución.