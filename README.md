# ERP-Odoo EnRutaCo Business Lab

Laboratorio académico basado en Odoo para analizar sistemas de información, arquitectura empresarial, procesos, gobierno de datos y transformación digital a partir del caso EnRutaCo S.A.S.

## Visión

Este proyecto busca construir un laboratorio académico reproducible, en español, para estudiantes de Maestría.

Odoo se utiliza como plataforma de simulación empresarial, no como objeto principal de enseñanza. El objetivo no es aprender a operar Odoo, sino usar un ERP como medio para analizar una organización, comprender sus procesos, evaluar información, identificar capacidades empresariales y justificar decisiones de transformación digital.

## Caso De Estudio

La organización utilizada es EnRutaCo S.A.S., una empresa colombiana del sector logístico con crecimiento acelerado, operación nacional, sistemas desconectados, datos fragmentados y presión competitiva.

Los estudiantes asumen el rol de consultores estratégicos responsables de analizar la situación actual y proponer una hoja de ruta de transformación empresarial.

El caso completo se encuentra en:

`01-Caso/Caso-EnRutaCo.pdf`

## Alcance Del Proyecto

El laboratorio incluye:

- Caso empresarial EnRutaCo como hilo conductor.
- Ambiente ERP reproducible con Docker Compose.
- Configuración funcional básica de Odoo.
- Datos académicos controlados.
- Laboratorios guiados por preguntas de negocio.
- Material docente y estudiantil.
- Evaluación basada en análisis, argumentación y toma de decisiones.

El laboratorio no incluye:

- Desarrollo comercial de módulos Odoo.
- Personalizaciones complejas sin justificación pedagógica.
- Automatizaciones avanzadas antes de tener fundamentos.
- Sustituir el análisis empresarial por operación técnica del ERP.
- Convertir el repositorio en un curso de administración de Odoo.

## Modelo Pedagógico

El laboratorio se basa en aprendizaje por caso y simulación de consultoría.

Los estudiantes trabajan con información progresiva, formulan hipótesis, analizan procesos, evalúan datos, identifican riesgos y preparan recomendaciones para un comité directivo.

El docente actúa como facilitador, guía metodológico y representante del comité directivo.

## Objetivos De Aprendizaje

Al finalizar el laboratorio, el estudiante debe poder:

1. Diagnosticar problemas organizacionales relacionados con sistemas de información.
2. Relacionar procesos de negocio, capacidades empresariales y plataformas tecnológicas.
3. Analizar brechas entre arquitectura actual y arquitectura objetivo.
4. Evaluar riesgos operativos, tecnológicos, financieros, de datos y de adopción.
5. Aplicar criterios básicos de gobierno de datos.
6. Interpretar KPIs logísticos y convertirlos en decisiones de transformación.
7. Priorizar iniciativas bajo restricciones de presupuesto, riesgo e impacto.
8. Diseñar un roadmap empresarial 2026-2029.
9. Explicar el rol de un ERP dentro de un ecosistema de sistemas de información.
10. Defender recomendaciones ante un comité directivo.

## Arquitectura Del Laboratorio

El proyecto se organiza en cinco capas:

1. **Capa De Caso Empresarial**  
   Narrativa, contexto, actores, restricciones, indicadores base, problemas y decisiones esperadas.

2. **Capa Académica**  
   Laboratorios, guías, rúbricas, entregables, criterios de evaluación y materiales para docente y estudiante.

3. **Capa ERP**  
   Uso de Odoo para representar empresa, usuarios, roles, clientes, almacenes, servicios logísticos, datos maestros y procesos base.

4. **Capa De Datos**  
   Datasets académicos, datos maestros, transacciones simuladas, KPIs, incidencias, costos, trazabilidad y escenarios de análisis.

5. **Capa De Infraestructura**  
   Docker Compose, PostgreSQL, Odoo, variables de entorno, volúmenes, healthchecks, scripts y documentación operativa.

## Principios Del Proyecto

- Odoo es medio, no fin.
- Todo componente debe responder una pregunta de negocio.
- Simplicidad antes que sofisticación.
- Docker Compose es el estándar de ejecución.
- La documentación es parte del producto académico.
- Los datos deben ser suficientes para aprender, no exhaustivos.
- Cada decisión importante debe quedar trazable.
- No se introduce código sin documentación.
- No se agregan dependencias sin justificación pedagógica.
- No se implementa funcionalidad que no contribuya a un objetivo de aprendizaje.

## Roadmap

### Iteración 0: Plan Maestro

Definir visión, alcance, modelo pedagógico, arquitectura de alto nivel, principios, roadmap y criterios de éxito.

### Iteración 1: Fundaciones Documentales

Alinear estructura del repositorio, completar documentación base, manuales mínimos, decisiones ADR y reglas de uso.

### Iteración 2: Infraestructura Reproducible

Construir ambiente Docker Compose con Odoo, PostgreSQL, volúmenes, variables, healthchecks y scripts documentados.

### Iteración 3: Modelo Base De EnRutaCo

Configurar empresa, usuarios, roles, moneda, impuestos, almacenes, ciudades, clientes, servicios logísticos y datos maestros iniciales.

### Iteración 4: Datos, Procesos Y Laboratorios

Crear datasets académicos y laboratorios guiados sobre diagnóstico As-Is, procesos críticos, ERP, datos, arquitectura To-Be y priorización de inversión.

### Iteración 5: Evaluación Y Material Docente

Crear rúbricas, guía del profesor, guía del estudiante, entregables, escenarios alternativos y criterios de presentación ante comité directivo.

## Criterios De Éxito

El proyecto será exitoso si:

- Un docente puede ejecutar el laboratorio con Docker Compose.
- Un estudiante entiende el caso sin conocimientos técnicos previos de Odoo.
- Cada laboratorio tiene una pregunta de negocio, una actividad y un entregable evaluable.
- Los datos permiten discutir decisiones reales.
- La arquitectura del repositorio es clara y progresiva.
- El uso de Odoo apoya el aprendizaje sin dominarlo.
- Los estudiantes producen recomendaciones justificadas técnica, financiera y estratégicamente.
- El caso EnRutaCo permanece como hilo conductor.
- El laboratorio permite discutir transformación digital, arquitectura empresarial, procesos, datos y toma de decisiones.
- El proyecto puede reiniciarse, reproducirse y mantenerse fácilmente.

## Estado Actual

El proyecto se encuentra en etapa de definición y fundación documental.

Las siguientes iteraciones desarrollarán progresivamente la infraestructura, el modelo base de EnRutaCo, los datasets, los laboratorios y el material docente.