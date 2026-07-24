# 03. CRM Odoo

## Objetivo

Definir la implementación del módulo CRM de Odoo para EnRutaCo S.A.S., estableciendo el alcance funcional, la configuración, la integración con el ERP y el soporte al proceso comercial para mejorar la gestión de clientes y oportunidades de negocio.

El CRM permitirá centralizar la información comercial, fortalecer la relación con los clientes y facilitar el seguimiento del ciclo de ventas.

---

# 1. Introducción

Actualmente, EnRutaCo administra parte de la información comercial mediante herramientas aisladas, lo que dificulta el seguimiento de clientes, oportunidades y actividades comerciales.

La implementación de Odoo CRM permitirá disponer de una plataforma integrada para administrar el ciclo comercial completo, desde la generación de un prospecto hasta la formalización del cliente y la creación de pedidos en el ERP.

---

# 2. Objetivos

- Centralizar la información comercial.
- Gestionar prospectos y clientes.
- Estandarizar el proceso de ventas.
- Mejorar el seguimiento de oportunidades.
- Incrementar la trazabilidad comercial.
- Facilitar la toma de decisiones mediante indicadores.

---

# 3. Alcance

La implementación comprende:

- Gestión de Prospectos (Leads)
- Gestión de Oportunidades
- Gestión de Clientes
- Pipeline Comercial
- Actividades Comerciales
- Cotizaciones
- Seguimiento de Negocios
- Reportes Comerciales

---

# 4. Funcionalidades

| Funcionalidad | Descripción |
|---------------|-------------|
| Leads | Registro de prospectos comerciales |
| Oportunidades | Gestión del proceso de venta |
| Pipeline | Seguimiento del estado de cada oportunidad |
| Actividades | Llamadas, reuniones y tareas comerciales |
| Cotizaciones | Generación y seguimiento de propuestas |
| Clientes | Administración de la información comercial |
| Reportes | Indicadores de desempeño comercial |

---

# 5. Parametrización

La configuración contempla:

## Comercial

- Equipos de ventas
- Vendedores
- Canales comerciales
- Etapas del pipeline

## Clientes

- Segmentos
- Categorías
- Condiciones comerciales
- Contactos

## Ventas

- Tipos de oportunidad
- Motivos de pérdida
- Probabilidad de cierre
- Actividades comerciales

---

# 6. Integraciones

| Sistema | Información Intercambiada |
|----------|---------------------------|
| ERP Odoo | Clientes, cotizaciones y pedidos |
| Power BI | Indicadores comerciales |
| Keycloak | Autenticación de usuarios |
| Kong Gateway | Exposición y consumo de APIs |

---

# 7. Datos a Migrar

Se migrarán:

- Clientes actuales
- Prospectos activos
- Contactos
- Historial comercial (cuando esté disponible)
- Catálogo de vendedores

La información será depurada antes de su carga para garantizar consistencia y calidad.

---

# 8. Pruebas

Las pruebas incluirán:

- Registro de prospectos
- Conversión de oportunidades
- Gestión del pipeline
- Generación de cotizaciones
- Integración con ERP
- Seguridad y perfiles de usuario
- Pruebas de aceptación (UAT)

---

# 9. Criterios de Éxito

La implementación será considerada exitosa cuando:

- Todos los clientes estén registrados en el CRM.
- El proceso comercial opere completamente en Odoo.
- Las oportunidades sean gestionadas mediante el pipeline.
- La integración con el ERP funcione correctamente.
- Los usuarios comerciales aprueben las pruebas funcionales.

---

# 10. Conclusiones

La implementación de Odoo CRM permitirá a EnRutaCo consolidar la gestión comercial en una única plataforma, mejorando la trazabilidad de las oportunidades de negocio, la administración de clientes y la integración con el ERP. Esto fortalecerá el proceso comercial y proporcionará información confiable para la toma de decisiones y el crecimiento de la organización.