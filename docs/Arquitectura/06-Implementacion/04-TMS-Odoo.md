# 04. TMS Odoo

## Objetivo

Definir la implementación de la solución Transportation Management System (TMS) para EnRutaCo S.A.S., soportada en Odoo Fleet y módulos especializados, con el propósito de planificar, ejecutar y controlar las operaciones de transporte, distribución y última milla de forma integrada con el ERP.

La solución permitirá mejorar la trazabilidad de los envíos, optimizar la utilización de la flota y aumentar el cumplimiento de los niveles de servicio establecidos por la organización.

---

# 1. Introducción

La operación logística constituye el núcleo del negocio de EnRutaCo. Actualmente, la planificación de rutas, el seguimiento de entregas y el control de la operación presentan limitaciones derivadas del uso de aplicaciones aisladas y procesos manuales.

La implementación del TMS permitirá integrar la gestión logística con el ERP, proporcionando información en tiempo real sobre pedidos, vehículos, rutas y entregas, mejorando la eficiencia operativa y la experiencia del cliente.

---

# 2. Objetivos

- Centralizar la operación logística.
- Optimizar la planificación de rutas.
- Mejorar la utilización de la flota.
- Incrementar la trazabilidad de los envíos.
- Monitorear el cumplimiento de los SLA.
- Reducir tiempos y costos operativos.

---

# 3. Alcance

La implementación comprende:

- Gestión de Vehículos
- Gestión de Conductores
- Planeación de Rutas
- Asignación de Pedidos
- Seguimiento de Entregas
- Gestión de Novedades
- Confirmación de Entregas (POD)
- Indicadores Logísticos

---

# 4. Funcionalidades

| Funcionalidad | Descripción |
|---------------|-------------|
| Gestión de Flota | Administración de vehículos y su información básica. |
| Conductores | Gestión de operadores asignados a la flota. |
| Planeación de Rutas | Organización de recorridos de distribución. |
| Asignación de Despachos | Relación entre pedidos, vehículos y conductores. |
| Seguimiento de Entregas | Consulta del estado de los despachos. |
| Gestión de Incidencias | Registro de novedades durante la operación. |
| Confirmación de Entrega | Registro de la entrega al cliente (Proof of Delivery). |
| Reportes | Indicadores de desempeño logístico. |

---

# 5. Parametrización

La configuración inicial contempla:

## Flota

- Vehículos
- Tipos de vehículo
- Capacidades
- Estados
- Centros de operación

## Operación

- Rutas
- Zonas de cobertura
- Tipos de servicio
- Prioridades
- Horarios de operación

## Despachos

- Estados del despacho
- Motivos de novedad
- Tipos de entrega
- Reglas de asignación

---

# 6. Integraciones

| Sistema | Información Intercambiada |
|----------|---------------------------|
| ERP Odoo | Pedidos, clientes, productos y estados de entrega |
| CRM Odoo | Información de clientes y compromisos comerciales |
| Power BI | Indicadores logísticos |
| Keycloak | Autenticación de usuarios |
| Kong Gateway | Integración mediante APIs |

---

# 7. Datos a Migrar

Se migrarán:

- Vehículos
- Conductores
- Rutas
- Zonas logísticas
- Clientes asociados a rutas
- Catálogos operativos

La información será validada y depurada antes de su migración para garantizar consistencia y calidad.

---

# 8. Pruebas

Las pruebas comprenderán:

- Planeación de rutas
- Asignación de vehículos
- Registro de despachos
- Seguimiento de entregas
- Registro de incidencias
- Confirmación de entrega
- Integración con ERP y CRM
- Pruebas de aceptación por usuarios (UAT)

---

# 9. Criterios de Éxito

La implementación del TMS será considerada exitosa cuando:

- Todas las operaciones logísticas sean gestionadas desde la plataforma.
- Los pedidos puedan asignarse correctamente a rutas y vehículos.
- El estado de las entregas se actualice oportunamente.
- Las integraciones con ERP y CRM funcionen correctamente.
- Los indicadores logísticos estén disponibles para la toma de decisiones.
- Los usuarios operativos aprueben las pruebas funcionales.

---

# 10. Conclusiones

La implementación del TMS sobre Odoo permitirá a EnRutaCo integrar la gestión logística con el resto de sus procesos empresariales, mejorando la planificación de rutas, el seguimiento de entregas y el control operativo. La disponibilidad de información en tiempo real contribuirá a optimizar los niveles de servicio, reducir costos logísticos y fortalecer la capacidad de respuesta frente a las necesidades de los clientes.