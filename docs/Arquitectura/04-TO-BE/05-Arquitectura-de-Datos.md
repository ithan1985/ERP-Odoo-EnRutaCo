1. Introducción

La Arquitectura de Datos Objetivo busca transformar la información en un activo estratégico de la organización. Para ello, se propone un modelo basado en dominios de información claramente definidos, con responsabilidades de gestión establecidas y mecanismos que garanticen la calidad, trazabilidad y disponibilidad de los datos.

2. Objetivos

La Arquitectura de Datos permitirá:

Disponer de una única fuente de verdad por dominio.
Reducir duplicidad de información.
Incrementar la calidad de los datos.
Facilitar la integración entre aplicaciones.
Mejorar la disponibilidad de información para la toma de decisiones.
Garantizar la trazabilidad de la operación.
3. Dominios de Datos
Dominio	Descripción
Clientes	Información de clientes corporativos y personas naturales.
Productos y Servicios	Catálogo de servicios logísticos ofrecidos por la empresa.
Pedidos	Solicitudes de transporte y logística realizadas por los clientes.
Transporte	Vehículos, rutas, conductores y órdenes de transporte.
Entregas	Evidencias, estados y confirmaciones de entrega.
Facturación	Facturas, notas crédito, cuentas por cobrar y recaudos.
Recursos Humanos	Colaboradores, roles y asignaciones.
Activos	Vehículos, equipos y demás activos empresariales.
Indicadores	KPIs operativos, financieros y estratégicos.
4. Modelo Conceptual de Datos
Cliente
    │
    ▼
Pedido
    │
    ▼
Orden de Transporte
    │
    ▼
Entrega
    │
    ▼
Factura

Relaciones complementarias:

Un cliente puede generar múltiples pedidos.
Un pedido puede generar una o varias órdenes de transporte.
Una orden de transporte puede incluir varias entregas.
Cada entrega genera información para la facturación y el seguimiento.
5. Sistemas Maestros (System of Record)
Dominio	Sistema Maestro
Clientes	Plataforma Comercial
Pedidos	Plataforma ERP
Transporte	TMS
Entregas	TMS
Facturación	Plataforma ERP
Contabilidad	Plataforma ERP
Recursos Humanos	Plataforma ERP
Activos	Plataforma ERP
Indicadores	Plataforma BI

Cada dominio tendrá un único sistema autorizado para crear y mantener la información principal.

6. Flujo de Información
Cliente
    │
    ▼
Plataforma Comercial
    │
    ▼
ERP
    │
    ▼
TMS
    │
    ▼
Aplicación Móvil
    │
    ▼
Portal Cliente
    │
    ▼
Plataforma BI

Este flujo garantiza que la información viaje de forma controlada entre las diferentes aplicaciones.

7. Gobierno de Datos

Se propone establecer los siguientes roles:

Rol	Responsabilidad
Data Owner	Responsable funcional del dominio de datos.
Data Steward	Garantiza la calidad y consistencia de la información.
Arquitecto de Datos	Define estándares y modelos de información.
Equipo de TI	Implementa y mantiene las soluciones tecnológicas.
8. Reglas de Calidad de Datos

Los dominios de información deberán cumplir con los siguientes criterios:

Criterio	Objetivo
Completitud	Datos obligatorios diligenciados.
Consistencia	Sin contradicciones entre sistemas.
Exactitud	Información correcta y validada.
Oportunidad	Datos disponibles cuando el negocio los requiera.
Integridad	Relaciones válidas entre entidades.
Unicidad	Sin registros duplicados.
9. Intercambio de Datos
Origen	Destino	Información
Plataforma Comercial	ERP	Clientes y pedidos.
ERP	TMS	Órdenes de transporte.
TMS	Portal del Cliente	Estado de entregas.
Aplicación Móvil	TMS	Evidencias y novedades.
ERP	Plataforma BI	Información financiera.
TMS	Plataforma BI	Indicadores operativos.
10. Ciclo de Vida de los Datos
Creación
      │
      ▼
Validación
      │
      ▼
Actualización
      │
      ▼
Consulta
      │
      ▼
Archivo
      │
      ▼
Retención
      │
      ▼
Eliminación

Cada dominio deberá definir políticas específicas de retención y disposición de la información conforme a la normativa aplicable.

11. Beneficios Esperados
Negocio
Información confiable para la toma de decisiones.
Mejor coordinación entre áreas.
Mayor satisfacción del cliente.
Datos
Reducción de duplicidades.
Mayor calidad.
Trazabilidad completa.
Tecnología
Integraciones simplificadas.
Menor complejidad.
Mejor gobernanza de la información.
12. Conclusión

La Arquitectura de Datos Objetivo establece un modelo de gestión de información basado en dominios, sistemas maestros y reglas de gobierno. Este enfoque permitirá que los datos se conviertan en un activo estratégico para EnRutaCo, soportando procesos integrados y decisiones basadas en información confiable.