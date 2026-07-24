# 05. Arquitectura de Solución

## Objetivo

Definir la Arquitectura de Solución que permitirá materializar la Arquitectura Empresarial Objetivo de EnRutaCo S.A.S., especificando los componentes funcionales, las plataformas tecnológicas seleccionadas, las relaciones entre ellas y los principios que guiarán el diseño e implementación de la solución.

La Arquitectura de Solución constituye el puente entre la Arquitectura Empresarial y la implementación tecnológica, proporcionando una visión integral del ecosistema que soportará los procesos de negocio de la organización.

---

# 1. Introducción

Como resultado del proceso de Arquitectura Empresarial se definió una arquitectura objetivo orientada a procesos, integrada mediante servicios y soportada por plataformas tecnológicas modernas.

Posteriormente, la evaluación de alternativas permitió seleccionar las soluciones que mejor responden a las necesidades estratégicas de EnRutaCo, considerando criterios de funcionalidad, escalabilidad, integración, costo total de propiedad y sostenibilidad.

La Arquitectura de Solución consolida dichas decisiones en un modelo único que describe cómo interactuarán las diferentes plataformas para soportar la operación del negocio.

Este documento constituye el referente técnico para las fases posteriores de diseño detallado, implementación, pruebas y despliegue.

---

# 2. Objetivos de la Solución

La solución propuesta tiene como finalidad proporcionar una plataforma integrada que permita:

- Centralizar la operación empresarial.
- Integrar los procesos críticos del negocio.
- Eliminar la fragmentación tecnológica existente.
- Facilitar el intercambio de información entre aplicaciones.
- Mejorar la trazabilidad de las operaciones logísticas.
- Soportar la toma de decisiones mediante analítica empresarial.
- Incrementar la seguridad de la información.
- Facilitar el crecimiento futuro de la organización.

Estos objetivos se encuentran alineados con la Arquitectura Empresarial Objetivo y con los lineamientos estratégicos definidos para el programa de transformación.

---

# 3. Principios de Diseño

La Arquitectura de Solución se fundamenta en los siguientes principios:

### Principios de Negocio

- La tecnología debe soportar los procesos del negocio.
- La información constituye un activo estratégico.
- La experiencia del cliente es un objetivo prioritario.
- Los procesos deberán estandarizarse antes de automatizarse.

### Principios de Aplicaciones

- Configuración antes que personalización.
- Integración mediante APIs.
- Reutilización de servicios.
- Bajo acoplamiento entre aplicaciones.
- Escalabilidad horizontal cuando sea posible.

### Principios de Datos

- Fuente única de información (Single Source of Truth).
- Calidad de datos por diseño.
- Gobierno corporativo de datos.
- Datos compartidos mediante servicios estandarizados.

### Principios Tecnológicos

- Cloud First.
- Seguridad por diseño (Security by Design).
- Alta disponibilidad.
- Escalabilidad.
- Observabilidad y monitoreo continuo.

---

# 4. Componentes de la Arquitectura de Solución

La solución propuesta está conformada por un conjunto de plataformas especializadas que trabajan de manera integrada para soportar los procesos empresariales de EnRutaCo.

| Dominio | Plataforma Seleccionada | Función Principal |
|----------|-------------------------|-------------------|
| ERP | Odoo 19 Community | Gestión integrada de procesos administrativos, financieros y operativos. |
| CRM | Odoo CRM | Gestión comercial, clientes y oportunidades de negocio. |
| TMS | Odoo Fleet + Desarrollo Especializado | Planeación y seguimiento de la operación logística. |
| Business Intelligence | Microsoft Power BI | Analítica empresarial y tableros de control. |
| API Management | Kong Gateway | Integración y exposición de servicios entre aplicaciones. |
| Gestión de Identidades | Keycloak | Autenticación, autorización y Single Sign-On (SSO). |
| Plataforma Cloud | Amazon Web Services (AWS) | Infraestructura para el despliegue de la solución. |

Cada uno de estos componentes cumple un rol específico dentro del ecosistema empresarial y fue seleccionado mediante el proceso de Evaluación de Alternativas desarrollado previamente.

---

# 5. Vista General de la Arquitectura

La Arquitectura de Solución adopta un enfoque por capas que facilita la separación de responsabilidades, mejora la mantenibilidad del ecosistema y favorece la evolución futura de la plataforma.

Las principales capas de la solución son:

## Capa de Canales

Corresponde a los puntos de interacción con usuarios internos y externos.

Incluye:

- Portal Web.
- Aplicación móvil para mensajeros.
- Clientes web de Odoo.
- Consolas administrativas.
- Dashboards ejecutivos de Power BI.

---

## Capa de Negocio

Implementa las capacidades empresariales mediante los módulos funcionales de las plataformas seleccionadas.

Entre las principales capacidades se encuentran:

- Gestión Comercial.
- Gestión de Clientes.
- Gestión de Pedidos.
- Gestión Logística.
- Gestión Financiera.
- Gestión de Inventarios.
- Servicio al Cliente.

Esta capa concentra la lógica del negocio y soporta los procesos definidos en la Arquitectura de Negocio TO-BE.

# 6. Arquitectura de Aplicaciones

La Arquitectura de Aplicaciones define cómo las plataformas seleccionadas colaboran para soportar los procesos de negocio de EnRutaCo, asegurando la interoperabilidad entre los diferentes dominios funcionales y evitando la duplicidad de funcionalidades.

Cada aplicación asume responsabilidades claramente definidas dentro del ecosistema empresarial.

---

## 6.1 Distribución de Responsabilidades

| Plataforma | Responsabilidad Principal |
|------------|---------------------------|
| Odoo ERP | Gestión financiera, compras, inventarios, ventas, facturación y procesos administrativos. |
| Odoo CRM | Gestión de clientes, oportunidades comerciales, actividades comerciales y seguimiento de ventas. |
| Odoo Fleet + Desarrollo Especializado | Gestión de vehículos, asignación de recursos logísticos y soporte a la operación de transporte. |
| Microsoft Power BI | Analítica empresarial, indicadores y tableros ejecutivos. |
| Kong Gateway | Integración entre aplicaciones mediante APIs. |
| Keycloak | Gestión de identidades, autenticación, autorización y Single Sign-On (SSO). |

La separación de responsabilidades reduce el acoplamiento entre aplicaciones y facilita la evolución independiente de cada componente.

---

## 6.2 Interacciones entre Aplicaciones

Las aplicaciones intercambian información mediante servicios expuestos a través de la plataforma de integración, evitando conexiones punto a punto y promoviendo una arquitectura orientada a servicios.

Los principales flujos de información son:

| Origen | Destino | Información Intercambiada |
|---------|----------|---------------------------|
| CRM | ERP | Clientes, oportunidades convertidas y pedidos confirmados. |
| ERP | TMS | Órdenes de despacho, productos, inventarios y datos logísticos. |
| TMS | ERP | Estado de entregas, novedades y confirmación de servicios. |
| ERP | Power BI | Información financiera, ventas, inventarios y operaciones. |
| CRM | Power BI | Indicadores comerciales y comportamiento de clientes. |
| TMS | Power BI | KPIs logísticos, tiempos de entrega y desempeño operativo. |
| Keycloak | Todas las aplicaciones | Autenticación y autorización de usuarios. |

Este modelo garantiza una integración consistente y facilita la incorporación futura de nuevas aplicaciones.

---

# 7. Arquitectura de Integración

La integración constituye uno de los pilares de la Arquitectura de Solución, permitiendo que las diferentes plataformas compartan información de manera segura, estandarizada y desacoplada.

Para ello se adopta un modelo basado en APIs administradas mediante Kong Gateway.

---

## 7.1 Principios de Integración

La arquitectura de integración seguirá los siguientes lineamientos:

- API First.
- Reutilización de servicios.
- Bajo acoplamiento entre aplicaciones.
- Integración mediante estándares abiertos (REST/JSON).
- Seguridad mediante OAuth2/OpenID Connect.
- Versionamiento de APIs.
- Monitoreo y trazabilidad de servicios.

Estos principios facilitan la interoperabilidad y reducen la complejidad de mantenimiento del ecosistema.

---

## 7.2 Componentes de Integración

| Componente | Función |
|------------|---------|
| Kong Gateway | Publicación, administración y seguridad de APIs. |
| Odoo REST APIs | Exposición de funcionalidades del ERP y CRM. |
| Servicios de Integración | Orquestación del intercambio de información entre plataformas. |
| Keycloak | Gestión de autenticación y autorización para las APIs. |

Esta arquitectura evita integraciones punto a punto y centraliza la administración de los servicios empresariales.

---

## 7.3 Flujos de Integración

Los principales flujos de integración son:

1. El CRM registra una oportunidad comercial.
2. Al concretarse la venta, el ERP genera el pedido correspondiente.
3. El ERP envía la información logística al TMS.
4. El TMS actualiza el estado de las entregas.
5. El ERP registra la facturación y el cierre operativo.
6. Power BI consolida la información para la generación de indicadores.
7. Todas las aplicaciones validan la identidad de los usuarios mediante Keycloak.

Este flujo garantiza la continuidad de la información durante todo el ciclo operativo.

---

# 8. Arquitectura de Datos

La Arquitectura de Datos establece la forma en que la información será administrada, compartida y protegida dentro del ecosistema empresarial.

El objetivo principal es garantizar que todos los procesos utilicen información consistente, confiable y disponible en el momento oportuno.

---

## 8.1 Principios para la Gestión de Datos

La solución adopta los siguientes principios:

- Fuente única de información (Single Source of Truth).
- Gobierno corporativo de datos.
- Calidad de datos desde el origen.
- Datos compartidos mediante servicios.
- Eliminación de duplicidad de información.
- Trazabilidad de la información.
- Seguridad y privacidad por diseño.

---

## 8.2 Dominios de Información

La solución administrará los siguientes dominios de datos.

| Dominio | Plataforma Principal |
|----------|----------------------|
| Clientes | Odoo CRM |
| Productos | Odoo ERP |
| Inventarios | Odoo ERP |
| Pedidos | Odoo ERP |
| Facturación | Odoo ERP |
| Información Financiera | Odoo ERP |
| Vehículos | Odoo Fleet |
| Operaciones Logísticas | TMS |
| Indicadores Corporativos | Power BI |

Cada dominio tiene un sistema responsable (System of Record), evitando inconsistencias y duplicidad de información.

---

## 8.3 Flujo de Información

La información seguirá un flujo lógico entre las plataformas:

1. Los datos son creados o actualizados en el sistema responsable.
2. Las APIs publican la información requerida por otros sistemas.
3. Las aplicaciones consumidoras utilizan únicamente los servicios autorizados.
4. Power BI consolida la información proveniente de los diferentes dominios.
5. Los usuarios consultan indicadores y reportes mediante tableros ejecutivos.

Este modelo asegura la consistencia de los datos y facilita la gobernanza de la información en toda la organización.

# 9. Arquitectura Tecnológica

La Arquitectura Tecnológica define la plataforma de infraestructura que soportará las aplicaciones, los servicios de integración y los componentes de datos que conforman la Arquitectura de Solución.

El diseño propuesto adopta un enfoque **Cloud First**, utilizando servicios administrados que permitan mejorar la disponibilidad, escalabilidad y resiliencia del ecosistema tecnológico de EnRutaCo.

---

## 9.1 Principios Tecnológicos

La arquitectura tecnológica se fundamenta en los siguientes principios:

- Cloud First.
- Alta disponibilidad.
- Escalabilidad horizontal.
- Automatización de la infraestructura.
- Observabilidad y monitoreo continuo.
- Seguridad por diseño (Security by Design).
- Automatización del despliegue.
- Optimización del costo total de propiedad (TCO).

Estos principios garantizan una plataforma preparada para soportar el crecimiento proyectado del negocio y facilitar la evolución futura de la arquitectura.

---

## 9.2 Componentes Tecnológicos

La solución estará soportada por los siguientes componentes tecnológicos.

| Dominio | Tecnología | Función |
|----------|------------|---------|
| Plataforma Cloud | Amazon Web Services (AWS) | Infraestructura base para el despliegue de la solución. |
| Contenedores | Docker | Empaquetado y despliegue de aplicaciones. |
| Base de Datos | PostgreSQL | Persistencia de la información empresarial. |
| API Gateway | Kong Gateway | Gestión y seguridad de las APIs corporativas. |
| Gestión de Identidades | Keycloak | Autenticación, autorización y Single Sign-On (SSO). |
| Analítica | Microsoft Power BI | Explotación y visualización de datos. |
| Monitoreo | Amazon CloudWatch | Supervisión de infraestructura y aplicaciones. |
| Almacenamiento | Amazon S3 | Respaldo y almacenamiento de archivos corporativos. |

La combinación de estos componentes proporciona una plataforma moderna, integrada y preparada para evolucionar conforme crezcan las necesidades del negocio.

---

## 9.3 Características de la Plataforma

La infraestructura tecnológica deberá ofrecer las siguientes capacidades:

- Alta disponibilidad.
- Escalabilidad automática.
- Balanceo de carga.
- Respaldo automatizado.
- Recuperación ante desastres.
- Monitoreo continuo.
- Gestión centralizada de configuraciones.
- Administración remota.
- Actualizaciones controladas.

Estas capacidades permitirán garantizar la continuidad del servicio y reducir los tiempos de indisponibilidad.

---

# 10. Arquitectura de Seguridad

La seguridad constituye un componente transversal de la Arquitectura de Solución y debe incorporarse desde el diseño hasta la operación de las plataformas.

La estrategia propuesta sigue el principio de **Security by Design**, integrando controles preventivos, detectivos y correctivos en todos los niveles de la solución.

---

## 10.1 Principios de Seguridad

La solución adoptará los siguientes principios:

- Seguridad por diseño.
- Menor privilegio (Least Privilege).
- Defensa en profundidad.
- Gestión centralizada de identidades.
- Cifrado de la información en tránsito y en reposo.
- Auditoría y trazabilidad.
- Gestión continua de vulnerabilidades.
- Cumplimiento de políticas corporativas.

---

## 10.2 Componentes de Seguridad

| Componente | Función |
|------------|---------|
| Keycloak | Gestión de usuarios, autenticación y autorización. |
| OAuth 2.0 / OpenID Connect | Protección de APIs y autenticación federada. |
| HTTPS/TLS | Cifrado de comunicaciones entre componentes. |
| Roles y Permisos | Control de acceso basado en roles (RBAC). |
| Auditoría | Registro de eventos y trazabilidad de operaciones. |
| Gestión de Secretos | Protección de credenciales y configuraciones sensibles. |

Estos mecanismos garantizan la protección de los activos de información y reducen los riesgos asociados al acceso no autorizado.

---

## 10.3 Controles de Seguridad

Los principales controles implementados serán:

| Dominio | Controles |
|----------|-----------|
| Identidad | Single Sign-On, autenticación multifactor (MFA), gestión de sesiones. |
| Aplicaciones | Validación de entradas, control de accesos, gestión de errores. |
| APIs | Autenticación, autorización, limitación de tráfico (Rate Limiting) y registro de accesos. |
| Datos | Cifrado, respaldos y control de acceso. |
| Infraestructura | Segmentación de redes, firewalls y monitoreo continuo. |

La aplicación de estos controles fortalece la postura de seguridad de la organización y facilita el cumplimiento de políticas corporativas y regulatorias.

---

# 11. Arquitectura de Infraestructura

La Arquitectura de Infraestructura describe el entorno tecnológico donde serán desplegadas las aplicaciones y servicios que conforman la solución.

El diseño prioriza la disponibilidad, escalabilidad y resiliencia, permitiendo soportar la operación logística de EnRutaCo con altos niveles de confiabilidad.

---

## 11.1 Capas de Infraestructura

La infraestructura se organiza en las siguientes capas:

| Capa | Componentes |
|-------|-------------|
| Acceso | Navegadores web, aplicaciones móviles y clientes administrativos. |
| Balanceo | Balanceadores de carga para distribuir el tráfico entre servicios. |
| Aplicaciones | Odoo ERP, Odoo CRM, TMS, Kong Gateway y Keycloak. |
| Datos | PostgreSQL y almacenamiento de archivos corporativos. |
| Analítica | Microsoft Power BI. |
| Monitoreo | Amazon CloudWatch y herramientas de observabilidad. |

Esta organización facilita el aislamiento de responsabilidades y mejora la capacidad de administración de la plataforma.

---

## 11.2 Disponibilidad y Continuidad

La infraestructura deberá garantizar la continuidad del negocio mediante los siguientes mecanismos:

- Despliegue en múltiples zonas de disponibilidad (Multi-AZ).
- Balanceo automático de carga.
- Respaldos programados.
- Replicación de bases de datos.
- Estrategias de recuperación ante desastres (Disaster Recovery).
- Monitoreo continuo de servicios.
- Gestión de incidentes y alertas.

Estas capacidades permitirán reducir el impacto de fallas y mantener la disponibilidad de los servicios críticos.

---

## 11.3 Consideraciones de Escalabilidad

La solución ha sido diseñada para soportar el crecimiento proyectado de EnRutaCo mediante mecanismos de escalabilidad tanto vertical como horizontal.

Las principales estrategias consideradas son:

- Escalamiento horizontal de servicios de aplicación.
- Incremento dinámico de capacidad de infraestructura según demanda.
- Separación entre capas de aplicación y datos.
- Uso de almacenamiento escalable para documentos y archivos.
- Monitoreo continuo del desempeño para ajustar recursos de manera proactiva.

Este enfoque permitirá que la arquitectura evolucione sin requerir rediseños significativos a medida que aumente el volumen de operaciones o se incorporen nuevas capacidades digitales.

# 12. Vista Integral de la Arquitectura de Solución

La Arquitectura de Solución integra los componentes de negocio, aplicaciones, datos, integración, seguridad e infraestructura en un ecosistema tecnológico coherente, alineado con los objetivos estratégicos de EnRutaCo.

La solución se estructura siguiendo un modelo de arquitectura por capas, donde cada componente cumple una responsabilidad específica y se comunica mediante interfaces estandarizadas.

## 12.1 Vista Conceptual

```text
                    Usuarios Internos / Clientes / Mensajeros
                                      │
                ┌─────────────────────┴─────────────────────┐
                │                                           │
          Portal Web                                 Aplicación Móvil
                │                                           │
                └─────────────────────┬─────────────────────┘
                                      │
                              Kong API Gateway
                                      │
                ┌──────────────┬───────────────┬──────────────┐
                │              │               │              │
            Odoo ERP      Odoo CRM        TMS/Fleet      Keycloak
                │              │               │              │
                └──────────────┴───────────────┴──────────────┘
                                      │
                                 PostgreSQL
                                      │
                              Microsoft Power BI
                                      │
                         Dashboards e Indicadores
```

Esta arquitectura promueve un bajo acoplamiento entre aplicaciones, facilita la escalabilidad y permite incorporar nuevos componentes sin afectar significativamente el ecosistema existente.

---

## 12.2 Capas de la Solución

| Capa | Componentes |
|------|-------------|
| Canales | Portal Web, Aplicaciones móviles, Clientes Web de Odoo, Dashboards Power BI |
| Integración | Kong Gateway |
| Negocio | Odoo ERP, Odoo CRM, TMS |
| Seguridad | Keycloak |
| Datos | PostgreSQL, Almacenamiento Corporativo |
| Analítica | Microsoft Power BI |
| Infraestructura | AWS, Docker, CloudWatch, Amazon S3 |

Cada capa proporciona servicios a la capa superior y consume servicios de la capa inferior, favoreciendo una arquitectura modular y mantenible.

---

# 13. Trazabilidad con la Arquitectura Empresarial

La Arquitectura de Solución implementa las capacidades definidas en la Arquitectura Empresarial Objetivo, garantizando la alineación entre la estrategia del negocio y la tecnología.

## 13.1 Trazabilidad Estratégica

| Objetivo Estratégico | Capacidad Empresarial | Solución Tecnológica |
|----------------------|-----------------------|----------------------|
| Mejorar la eficiencia operativa | Gestión integrada de procesos | Odoo ERP |
| Incrementar la satisfacción del cliente | Gestión comercial y servicio al cliente | Odoo CRM |
| Optimizar la operación logística | Planeación y seguimiento logístico | Odoo Fleet + Desarrollo TMS |
| Fortalecer la toma de decisiones | Analítica empresarial | Microsoft Power BI |
| Reducir la fragmentación tecnológica | Integración de aplicaciones | Kong Gateway |
| Incrementar la seguridad | Gestión de identidades y accesos | Keycloak |
| Mejorar la escalabilidad | Infraestructura Cloud | Amazon Web Services |

Esta trazabilidad asegura que cada componente tecnológico responda a una necesidad específica del negocio y contribuya al logro de los objetivos estratégicos.

---

## 13.2 Trazabilidad de Capacidades

| Capacidad | Aplicación Responsable | Tecnología Soporte |
|------------|------------------------|--------------------|
| Gestión Comercial | Odoo CRM | AWS |
| Gestión Financiera | Odoo ERP | PostgreSQL |
| Gestión de Inventarios | Odoo ERP | PostgreSQL |
| Gestión de Pedidos | Odoo ERP | PostgreSQL |
| Gestión Logística | TMS | AWS |
| Gestión de Clientes | Odoo CRM | PostgreSQL |
| Business Intelligence | Power BI | Power BI Service |
| Integración Empresarial | Kong Gateway | Docker |
| Gestión de Identidades | Keycloak | Docker |

La asignación de responsabilidades evita duplicidad funcional y facilita el gobierno del ecosistema tecnológico.

---

# 14. Beneficios de la Arquitectura de Solución

La implementación de la Arquitectura de Solución permitirá generar beneficios en múltiples dimensiones de la organización.

## 14.1 Beneficios para el Negocio

- Integración de procesos críticos.
- Mayor agilidad operacional.
- Incremento en la satisfacción de clientes.
- Reducción de tiempos de respuesta.
- Mejor soporte al crecimiento del negocio.

---

## 14.2 Beneficios Tecnológicos

- Disminución de la complejidad tecnológica.
- Eliminación de aplicaciones redundantes.
- Integración estandarizada mediante APIs.
- Mayor disponibilidad y escalabilidad.
- Reducción de la deuda técnica.

---

## 14.3 Beneficios para la Gestión de la Información

- Fuente única de información para los procesos corporativos.
- Mayor calidad y consistencia de los datos.
- Indicadores disponibles en tiempo real.
- Mejor trazabilidad de la información.
- Soporte a la toma de decisiones basada en datos.

---

## 14.4 Beneficios Organizacionales

- Estandarización de procesos.
- Mayor colaboración entre áreas.
- Fortalecimiento del gobierno de arquitectura y datos.
- Mejor adopción tecnológica mediante gestión del cambio.
- Incremento de las competencias digitales del talento humano.

---

# 15. Riesgos Arquitectónicos

Aunque la solución propuesta reduce significativamente las brechas identificadas en la arquitectura actual, existen riesgos que deberán ser gestionados durante su implementación y operación.

| Riesgo | Impacto | Estrategia de Mitigación |
|---------|:------:|--------------------------|
| Personalizaciones excesivas del ERP | Alto | Priorizar configuración estándar y establecer un proceso formal para aprobar desarrollos. |
| Dependencias entre plataformas | Medio | Implementar integración desacoplada mediante APIs administradas por Kong Gateway. |
| Baja calidad de los datos migrados | Alto | Ejecutar procesos de depuración, validación y gobierno de datos antes de la migración. |
| Incremento de la complejidad operativa | Medio | Documentar la arquitectura, automatizar despliegues y fortalecer el monitoreo. |
| Riesgos de ciberseguridad | Alto | Aplicar controles de seguridad por diseño, autenticación centralizada y monitoreo continuo. |
| Crecimiento del volumen transaccional | Medio | Diseñar una infraestructura escalable y realizar revisiones periódicas de capacidad. |

La gestión continua de estos riesgos contribuirá a preservar la integridad de la arquitectura y garantizar su evolución controlada.

---

# 16. Conclusiones

La Arquitectura de Solución representa la materialización técnica de la Arquitectura Empresarial Objetivo de EnRutaCo, integrando procesos, aplicaciones, datos e infraestructura en un ecosistema coherente y alineado con la estrategia del negocio.

La solución propuesta adopta principios modernos de arquitectura, como integración mediante APIs, gestión centralizada de identidades, enfoque Cloud First y separación por capas, permitiendo reducir la complejidad tecnológica y mejorar la capacidad de adaptación de la organización.

Asimismo, la selección de plataformas como Odoo, Microsoft Power BI, Kong Gateway, Keycloak y Amazon Web Services responde al proceso de evaluación de alternativas realizado previamente y proporciona una base sólida para soportar el crecimiento proyectado de EnRutaCo durante el horizonte estratégico 2026–2029.

Finalmente, este documento constituye el referente para las fases posteriores de diseño detallado, implementación, pruebas y despliegue, asegurando que todas las decisiones técnicas permanezcan alineadas con los principios y objetivos definidos por la Arquitectura Empresarial.