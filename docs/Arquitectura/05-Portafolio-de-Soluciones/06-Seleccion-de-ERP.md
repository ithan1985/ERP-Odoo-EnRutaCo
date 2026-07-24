# 06. Selección de ERP

## Objetivo

Documentar el proceso de selección del sistema Enterprise Resource Planning (ERP) que soportará la Arquitectura Empresarial Objetivo de EnRutaCo S.A.S., justificando la elección de la plataforma que mejor responde a las necesidades estratégicas, operativas y tecnológicas de la organización.

Este documento consolida los resultados de la evaluación de alternativas realizada durante el Portafolio de Soluciones y establece la plataforma ERP que será utilizada como núcleo de la transformación digital de EnRutaCo.

---

# 1. Introducción

La transformación empresarial de EnRutaCo requiere una plataforma tecnológica que permita integrar los procesos de negocio, eliminar la fragmentación de aplicaciones y proporcionar una fuente única de información para la organización.

Como parte del proceso de Arquitectura Empresarial se identificó la necesidad de reemplazar el ecosistema actual compuesto por aplicaciones aisladas, hojas de cálculo y sistemas heredados, por una solución integrada que soporte el crecimiento proyectado de la empresa.

Para ello se realizó un proceso de evaluación comparativa de diferentes plataformas ERP disponibles en el mercado, considerando criterios funcionales, técnicos, financieros y estratégicos.

El resultado de este proceso permitió seleccionar la plataforma que ofrece el mejor equilibrio entre capacidades funcionales, flexibilidad, costo de propiedad y alineación con la arquitectura objetivo.

---

# 2. Objetivos de la Selección

La selección del ERP busca cumplir los siguientes objetivos:

- Centralizar la gestión empresarial.
- Integrar los procesos de negocio.
- Reducir la fragmentación tecnológica.
- Mejorar la trazabilidad de la información.
- Facilitar la automatización de procesos.
- Incrementar la escalabilidad tecnológica.
- Reducir el costo total de propiedad (TCO).
- Proporcionar una plataforma preparada para el crecimiento futuro.

---

# 3. Requerimientos del Negocio

A partir del diagnóstico organizacional y de la Arquitectura de Negocio TO-BE se identificaron los principales requerimientos que debe satisfacer el ERP.

## Requerimientos Funcionales

- Gestión comercial.
- Gestión de clientes.
- Gestión de ventas.
- Gestión de compras.
- Gestión de inventarios.
- Gestión financiera y contable.
- Facturación.
- Gestión documental.
- Reportes operacionales.
- Integración con procesos logísticos.

---

## Requerimientos Técnicos

- Arquitectura web.
- APIs para integración.
- Base de datos relacional.
- Soporte para múltiples usuarios.
- Escalabilidad.
- Seguridad empresarial.
- Integración con herramientas BI.
- Compatibilidad con infraestructura Cloud.

---

## Requerimientos Estratégicos

- Bajo costo de implementación.
- Facilidad de adopción.
- Ecosistema de módulos.
- Comunidad activa.
- Flexibilidad para evolucionar.
- Independencia tecnológica.
- Reducción de deuda técnica.

---
# 4. Criterios de Evaluación

Para garantizar una selección objetiva se definieron criterios agrupados en diferentes dimensiones.

| Dimensión | Criterio |
|-----------|----------|
| Funcional | Cobertura de procesos empresariales |
| Técnica | Arquitectura, APIs e integración |
| Escalabilidad | Capacidad de crecimiento |
| Flexibilidad | Configuración y personalización |
| Implementación | Tiempo y complejidad |
| Ecosistema | Comunidad y módulos disponibles |
| Financiera | Costo total de propiedad (TCO) |
| Soporte | Disponibilidad de especialistas |
| Riesgo | Dependencia tecnológica |
| Estratégica | Alineación con la Arquitectura Empresarial |

Cada criterio fue evaluado considerando las necesidades específicas de EnRutaCo y los objetivos definidos para el programa de transformación.

# 5. Evaluación de Alternativas

Como resultado del proceso de Arquitectura Empresarial se identificaron cinco alternativas ERP que satisfacen, en diferente medida, los requerimientos funcionales y tecnológicos de EnRutaCo.

Las soluciones evaluadas corresponden a plataformas ampliamente utilizadas en el mercado y representan diferentes enfoques en términos de costos, complejidad de implementación y cobertura funcional.

Las alternativas analizadas fueron:

- Odoo Community
- SAP S/4HANA
- Oracle Fusion Cloud ERP
- Microsoft Dynamics 365 Finance & Supply Chain
- ERPNext

---

## 5.1 Odoo Community

### Descripción

Odoo Community es una plataforma ERP de código abierto que ofrece una arquitectura modular, permitiendo implementar únicamente las funcionalidades requeridas por la organización.

Su ecosistema cuenta con una amplia comunidad internacional y una gran cantidad de módulos desarrollados tanto por la comunidad como por partners especializados.

### Fortalezas

- Arquitectura modular.
- Código abierto.
- Bajo costo de licenciamiento.
- Amplias capacidades de integración mediante APIs.
- Facilidad de personalización.
- Comunidad activa.
- Compatible con despliegues Cloud.
- Escalable mediante módulos.

### Limitaciones

- Algunas funcionalidades avanzadas requieren desarrollos adicionales.
- Menor cobertura nativa para procesos altamente especializados.
- Dependencia de un partner para implementaciones complejas.

---

## 5.2 SAP S/4HANA

### Descripción

SAP S/4HANA es una plataforma ERP empresarial orientada a organizaciones de gran tamaño con procesos altamente complejos y presencia global.

Proporciona una cobertura funcional muy amplia y un elevado nivel de integración entre procesos.

### Fortalezas

- Cobertura funcional muy completa.
- Amplias capacidades analíticas.
- Alto nivel de madurez.
- Ecosistema consolidado.
- Amplio soporte internacional.

### Limitaciones

- Alto costo de licenciamiento.
- Implementaciones de larga duración.
- Elevada complejidad técnica.
- Alto costo de operación.
- Mayor esfuerzo de adopción organizacional.

---

## 5.3 Oracle Fusion Cloud ERP

### Descripción

Oracle Fusion Cloud ERP ofrece una solución SaaS orientada a organizaciones que buscan una plataforma completamente administrada en la nube.

Su enfoque privilegia la estandarización de procesos y la integración con el ecosistema Oracle.

### Fortalezas

- Plataforma Cloud nativa.
- Alta disponibilidad.
- Funcionalidad empresarial robusta.
- Escalabilidad.
- Actualizaciones automáticas.

### Limitaciones

- Alto costo de suscripción.
- Menor flexibilidad para personalizaciones profundas.
- Dependencia del ecosistema Oracle.

---

## 5.4 Microsoft Dynamics 365

### Descripción

Microsoft Dynamics 365 integra capacidades ERP y CRM dentro del ecosistema Microsoft, facilitando la interoperabilidad con herramientas como Microsoft 365, Azure y Power Platform.

### Fortalezas

- Integración con el ecosistema Microsoft.
- Interfaz moderna.
- Capacidades analíticas integradas.
- Arquitectura Cloud.

### Limitaciones

- Costos crecientes por licenciamiento.
- Personalizaciones complejas.
- Dependencia del ecosistema Microsoft.

---

## 5.5 ERPNext

### Descripción

ERPNext es una solución ERP de código abierto orientada principalmente a pequeñas y medianas organizaciones.

Ofrece una implementación relativamente sencilla y una cobertura funcional adecuada para escenarios menos complejos.

### Fortalezas

- Open Source.
- Bajo costo.
- Arquitectura moderna.
- Facilidad de implementación.

### Limitaciones

- Ecosistema más reducido.
- Menor disponibilidad de especialistas.
- Cobertura funcional inferior frente a otras alternativas.
- Comunidad más pequeña.

---

# 6. Matriz Comparativa

Con base en los criterios definidos anteriormente se realizó una evaluación cualitativa de las alternativas.

| Criterio | Odoo | SAP | Oracle | Dynamics | ERPNext |
|----------|:----:|:---:|:------:|:--------:|:-------:|
| Cobertura funcional | 4 | 5 | 5 | 5 | 3 |
| Flexibilidad | 5 | 3 | 3 | 4 | 4 |
| Integración mediante APIs | 5 | 5 | 5 | 5 | 4 |
| Escalabilidad | 4 | 5 | 5 | 5 | 3 |
| Tiempo de implementación | 5 | 2 | 3 | 3 | 4 |
| Complejidad | 5 | 2 | 3 | 3 | 4 |
| Comunidad | 5 | 5 | 5 | 5 | 3 |
| Costo Total de Propiedad (TCO) | 5 | 1 | 2 | 2 | 5 |
| Independencia tecnológica | 5 | 2 | 2 | 2 | 5 |
| Alineación con EnRutaCo | 5 | 3 | 3 | 4 | 4 |

> Escala de evaluación:
>
> - **5:** Excelente
> - **4:** Muy Bueno
> - **3:** Adecuado
> - **2:** Limitado
> - **1:** Deficiente

La evaluación evidencia que Odoo Community presenta el mejor equilibrio entre funcionalidad, flexibilidad, facilidad de implementación y costo total de propiedad para el contexto de EnRutaCo.

# 7. Alternativa Seleccionada

Como resultado del proceso de evaluación, **Odoo Community** fue seleccionado como la plataforma ERP que mejor satisface los requerimientos estratégicos, funcionales y tecnológicos de EnRutaCo.

La decisión se fundamenta en el equilibrio entre cobertura funcional, flexibilidad, costo total de propiedad y facilidad de integración con el resto de la Arquitectura de Solución.

La plataforma será complementada con componentes especializados para aquellas capacidades que exceden el alcance estándar del ERP, manteniendo un enfoque de arquitectura modular y desacoplada.

---

## 7.1 Justificación Estratégica

La selección de Odoo responde a los siguientes factores estratégicos:

- Alineación con la Arquitectura Empresarial Objetivo.
- Soporte para la estandarización de procesos.
- Arquitectura modular que facilita una implementación gradual.
- Reducción de la fragmentación tecnológica identificada en el diagnóstico.
- Capacidad de integrarse con plataformas especializadas mediante APIs.
- Bajo costo total de propiedad en comparación con soluciones empresariales tradicionales.
- Independencia frente a modelos de licenciamiento propietarios.

Estas características permiten construir una plataforma sostenible, adaptable al crecimiento de EnRutaCo y alineada con el roadmap de transformación definido para el periodo 2026–2029.

---

## 7.2 Justificación Funcional

Desde la perspectiva funcional, Odoo proporciona cobertura para la mayoría de los procesos empresariales identificados durante la Arquitectura de Negocio.

| Proceso de Negocio | Cobertura con Odoo |
|--------------------|--------------------|
| Gestión Comercial | Alta |
| Gestión de Clientes | Alta |
| Gestión de Ventas | Alta |
| Gestión de Compras | Alta |
| Gestión de Inventarios | Alta |
| Gestión Financiera | Alta |
| Facturación | Alta |
| Gestión Documental | Media |
| Gestión Logística | Parcial (requiere complementos especializados) |
| Indicadores Operativos | Integración con Power BI |

La evaluación demuestra que la plataforma cubre de forma nativa la mayor parte de los procesos administrativos y comerciales, mientras que las capacidades logísticas especializadas se complementarán mediante módulos específicos e integraciones.

---

## 7.3 Justificación Técnica

Desde el punto de vista tecnológico, Odoo ofrece una arquitectura alineada con los principios definidos para la Arquitectura de Solución.

Entre sus principales capacidades se destacan:

- Arquitectura web.
- Plataforma modular.
- APIs para integración.
- Base de datos PostgreSQL.
- Compatibilidad con Docker.
- Despliegue en infraestructura Cloud.
- Escalabilidad horizontal.
- Integración con herramientas de Business Intelligence.

Estas características facilitan su incorporación dentro del ecosistema compuesto por Kong Gateway, Keycloak, Microsoft Power BI y Amazon Web Services.

---

## 7.4 Justificación Financiera

Desde la perspectiva financiera, Odoo representa la alternativa con mejor relación entre inversión y beneficios esperados.

Los principales factores considerados fueron:

- Ausencia de costos de licenciamiento para la edición Community.
- Menor inversión inicial frente a plataformas empresariales tradicionales.
- Reducción del costo total de propiedad (TCO).
- Implementaciones de menor duración.
- Menores costos de actualización y mantenimiento.
- Disponibilidad de una amplia comunidad de desarrolladores y partners.

Aunque la implementación requiere inversión en configuración, desarrollo, migración de datos y capacitación, el costo global estimado resulta significativamente inferior al de otras alternativas evaluadas.

---

# 8. Riesgos de la Alternativa Seleccionada

La adopción de Odoo implica una serie de riesgos que deberán ser gestionados durante el proyecto de implementación.

| Riesgo | Impacto | Mitigación |
|---------|:------:|------------|
| Personalizaciones excesivas | Alto | Priorizar la configuración estándar y establecer un proceso formal de aprobación para desarrollos. |
| Dependencia del partner implementador | Medio | Documentar las soluciones, fortalecer capacidades internas y exigir transferencia de conocimiento. |
| Integración con aplicaciones especializadas | Medio | Diseñar una arquitectura basada en APIs utilizando Kong Gateway. |
| Calidad de los datos migrados | Alto | Ejecutar procesos de depuración, validación y pruebas antes de la migración. |
| Resistencia al cambio | Alto | Implementar un plan integral de gestión del cambio y capacitación. |
| Crecimiento futuro de requerimientos | Medio | Adoptar una arquitectura modular que facilite la incorporación de nuevas capacidades. |

La gestión temprana de estos riesgos contribuirá al éxito del programa de transformación.

---

# 9. Factores Críticos de Éxito

La implementación del ERP dependerá de diversos factores organizacionales y tecnológicos.

Los principales factores identificados son:

- Compromiso de la alta dirección.
- Participación activa de las áreas de negocio.
- Definición clara del alcance del proyecto.
- Calidad de la información a migrar.
- Gobierno del proyecto.
- Gestión efectiva del cambio.
- Capacitación de los usuarios.
- Adopción de buenas prácticas de implementación.
- Integración adecuada con las demás plataformas de la solución.

El seguimiento continuo de estos factores permitirá reducir riesgos y maximizar los beneficios esperados.

---

# 10. Recomendaciones

Con base en la evaluación realizada, se recomienda:

- Adoptar Odoo Community como plataforma ERP corporativa.
- Implementar el ERP de manera incremental, priorizando los procesos de mayor impacto para el negocio.
- Minimizar las personalizaciones, privilegiando la configuración estándar y el uso de módulos existentes.
- Implementar una arquitectura de integración basada en APIs para desacoplar las aplicaciones y facilitar futuras evoluciones.
- Establecer un gobierno de arquitectura que supervise las decisiones de diseño y la evolución de la solución.
- Ejecutar un programa de gestión del cambio que acompañe la adopción de la nueva plataforma.

Estas recomendaciones buscan asegurar que la implementación del ERP contribuya al logro de los objetivos estratégicos definidos para EnRutaCo.

# 11. Conclusiones

El proceso de selección del ERP permitió identificar la plataforma que mejor responde a las necesidades actuales y futuras de EnRutaCo, considerando aspectos funcionales, tecnológicos, financieros y estratégicos.

La evaluación comparativa evidenció que **Odoo Community** ofrece el mejor equilibrio entre cobertura funcional, flexibilidad, facilidad de integración y costo total de propiedad (TCO), siendo la alternativa más adecuada para soportar la transformación empresarial planteada en la Arquitectura Objetivo.

La decisión de adoptar una plataforma de código abierto reduce la dependencia de fabricantes, facilita la evolución de la solución y permite una implementación incremental alineada con el Business Transformation Roadmap 2026–2029.

Asimismo, la selección de Odoo no implica que todas las capacidades empresariales deban resolverse exclusivamente con el ERP. La Arquitectura de Solución contempla un ecosistema de plataformas especializadas —como Microsoft Power BI, Kong Gateway, Keycloak y Amazon Web Services— que complementan las capacidades del ERP y conforman una solución empresarial integrada.

Finalmente, este documento constituye la base para iniciar el diseño detallado de la solución y la planificación de la implementación, asegurando que las decisiones tecnológicas permanezcan alineadas con la Arquitectura Empresarial y los objetivos estratégicos de EnRutaCo.

---

# 12. Próximos Pasos

Una vez seleccionada la plataforma ERP, el programa de transformación deberá avanzar hacia las siguientes actividades:

1. Definir el alcance funcional de la primera fase de implementación.
2. Elaborar el plan de implementación del ERP.
3. Diseñar la arquitectura de integraciones entre aplicaciones.
4. Definir la estrategia de migración de datos.
5. Configurar la infraestructura tecnológica requerida.
6. Diseñar los ambientes de desarrollo, pruebas y producción.
7. Elaborar el plan de pruebas funcionales e integrales.
8. Definir el plan de capacitación y gestión del cambio.
9. Preparar la estrategia de despliegue (Go-Live).
10. Establecer el modelo de soporte y mejora continua.

Estas actividades permitirán iniciar la fase de ejecución del programa de transformación empresarial de forma organizada y controlada.

---

# Anexo A. Matriz de Trazabilidad de Requerimientos vs. Odoo

La siguiente matriz relaciona los principales requerimientos identificados durante la Arquitectura Empresarial con las capacidades proporcionadas por Odoo.

| Requerimiento | Cobertura en Odoo | Observaciones |
|-----------------------------|------------------|-----------------------------------------------|
| Gestión Comercial | Completa | Módulo CRM y Ventas. |
| Gestión de Clientes | Completa | CRM integrado. |
| Gestión de Ventas | Completa | Ventas, cotizaciones y pedidos. |
| Gestión de Compras | Completa | Compras y proveedores. |
| Gestión de Inventarios | Completa | Inventario y almacenes. |
| Gestión Financiera | Completa | Contabilidad y facturación. |
| Facturación | Completa | Facturación electrónica (requiere localización colombiana). |
| Gestión Documental | Parcial | Puede complementarse con módulos documentales. |
| Gestión Logística | Parcial | Requiere módulos Fleet y desarrollos específicos para operaciones logísticas. |
| Gestión de KPIs | Parcial | Complementada mediante Microsoft Power BI. |
| Integración mediante APIs | Completa | APIs REST/XML-RPC y servicios de integración. |
| Seguridad | Completa | Integración con Keycloak para SSO y gestión centralizada de identidades. |

La evaluación demuestra que Odoo cubre la mayor parte de los requerimientos identificados para EnRutaCo, mientras que las capacidades especializadas serán soportadas por componentes complementarios definidos en la Arquitectura de Solución.

---

# Anexo B. Mapa de Módulos de Odoo para EnRutaCo

La implementación propuesta contempla una adopción modular del ERP, priorizando los procesos de mayor impacto para el negocio.

| Dominio de Negocio | Módulo Odoo |
|--------------------|-------------|
| Gestión Comercial | CRM |
| Ventas | Sales |
| Compras | Purchase |
| Inventarios | Inventory |
| Facturación | Invoicing |
| Contabilidad | Accounting |
| Contactos | Contacts |
| Flota de Vehículos | Fleet |
| Recursos Humanos | Employees (opcional) |
| Gastos | Expenses (opcional) |
| Documentos | Documents (opcional) |
| Proyectos | Project (para iniciativas internas) |
| Help Desk | Módulo comunitario o desarrollo específico según necesidades |

La incorporación de módulos se realizará de forma incremental, siguiendo las prioridades establecidas en el Business Transformation Roadmap y evitando implementar funcionalidades que no aporten valor inmediato al negocio.

---

# Relación con la Arquitectura Empresarial

La selección de Odoo constituye una decisión arquitectónica derivada de los principios, requerimientos y objetivos definidos durante el proceso de Arquitectura Empresarial.

La plataforma seleccionada soporta la Arquitectura de Negocio, la Arquitectura de Aplicaciones, la Arquitectura de Datos y la Arquitectura Tecnológica descritas en los documentos anteriores, garantizando la trazabilidad entre la estrategia empresarial y la solución tecnológica.

Este documento marca la transición entre la fase de diseño arquitectónico y la fase de implementación, proporcionando el fundamento para la configuración del ERP, el desarrollo de integraciones, la migración de datos y el despliegue progresivo de la solución.