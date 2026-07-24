# HU-007 - Gestionar Parámetros del Sistema

## Estado
Backlog

## Prioridad
Media

## Sprint
2

## Módulo
enrutaco_base

---

## Descripción

**Como** administrador del sistema

**Quiero** gestionar los parámetros generales de configuración del ERP

**Para** centralizar la configuración del sistema y evitar cambios en el código fuente cuando se requieran ajustes funcionales o técnicos.

---

## Criterios de aceptación

- [ ] Crear un parámetro del sistema.
- [ ] Editar un parámetro existente.
- [ ] Consultar parámetros.
- [ ] Activar o desactivar parámetros.
- [ ] Definir una clave única.
- [ ] Definir el valor del parámetro.
- [ ] Clasificar los parámetros por categoría.
- [ ] Registrar una descripción funcional.
- [ ] No permitir claves duplicadas.

---

## Reglas de negocio

### RN-001
La clave del parámetro debe ser única.

### RN-002
El nombre del parámetro debe ser único.

### RN-003
El valor puede ser modificado únicamente por administradores.

### RN-004
Los parámetros desactivados no serán utilizados por el sistema.

### RN-005
Los parámetros deberán poder ser consultados por cualquier módulo del ERP.

---

## Modelo

**Entidad**

`enrutaco.system.parameter`

| Campo | Tipo | Obligatorio | Observaciones |
|--------|------|-------------|---------------|
| key | Char | Sí | Clave técnica única |
| name | Char | Sí | Nombre del parámetro |
| category | Selection | Sí | Categoría |
| value | Char | Sí | Valor |
| description | Text | No | Descripción funcional |
| active | Boolean | Sí | Activo |

### Categorías

- General
- Logística
- Transporte
- Despacho
- Última Milla
- CRM
- Integraciones
- Seguridad

---

## Relaciones

No aplica.

Los parámetros podrán ser consultados desde cualquier módulo del ERP.

---

## Dependencias

Ninguna.

---

## Seguridad

### Administrador ERP

- Crear
- Editar
- Consultar
- Desactivar

### Usuario ERP

- Consultar

---

## Vistas

- Lista
- Formulario
- Búsqueda

### Menú

EnRutaCo

- Configuración
  - Sistema
    - Parámetros

---

## Datos iniciales

| Clave | Nombre | Valor |
|--------|---------|-------|
| company.default_country | País por defecto | CO |
| logistics.default_weight_unit | Unidad de peso | KG |
| logistics.default_volume_unit | Unidad de volumen | M3 |
| security.session_timeout | Tiempo de sesión | 30 |
| system.timezone | Zona horaria | America/Bogota |

---

## Definition of Done

- [ ] Modelo implementado.
- [ ] Restricciones de negocio implementadas.
- [ ] Seguridad configurada.
- [ ] Menú creado.
- [ ] Vistas funcionales.
- [ ] Datos iniciales cargados.
- [ ] Instalación sin errores.
- [ ] Pruebas funcionales ejecutadas.