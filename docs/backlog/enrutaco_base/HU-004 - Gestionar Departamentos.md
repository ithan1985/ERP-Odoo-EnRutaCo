# HU-004 - Administrar Departamentos

## Estado
Backlog

## Prioridad
Alta

## Sprint
1

## Módulo
enrutaco_base

---

## Descripción

**Como** administrador del sistema

**Quiero** administrar el catálogo de departamentos o estados

**Para** organizar la estructura geográfica utilizada por sucursales, clientes, proveedores y demás procesos del ERP.

---

## Criterios de aceptación

- [ ] Crear un departamento.
- [ ] Editar un departamento.
- [ ] Consultar departamentos.
- [ ] Activar o desactivar un departamento.
- [ ] Asociar el departamento a un país.
- [ ] Registrar el código del departamento.
- [ ] No permitir códigos duplicados dentro del mismo país.

---

## Reglas de negocio

### RN-001
Todo departamento debe pertenecer a un país.

### RN-002
El nombre del departamento debe ser único dentro del país.

### RN-003
El código del departamento debe ser único dentro del país.

### RN-004
No se eliminan departamentos; únicamente se desactivan.

### RN-005
Un país puede tener múltiples departamentos.

---

## Modelo

**Entidad**

`enrutaco.department`

| Campo | Tipo | Obligatorio | Observaciones |
|--------|------|-------------|---------------|
| country_id | Many2one | Sí | País |
| code | Char | Sí | Código interno |
| name | Char | Sí | Nombre del departamento |
| active | Boolean | Sí | Activo |

---

## Relaciones

País (1) ──────────── (N) Departamentos

Departamento (1) ──── (N) Ciudades

---

## Dependencias

- HU-003 Administrar Países

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
  - Ubicaciones
    - Departamentos

---

## Datos iniciales

| País | Código | Departamento |
|------|---------|--------------|
| Colombia | DC | Bogotá D.C. |
| Colombia | ANT | Antioquia |
| Colombia | VAL | Valle del Cauca |
| Colombia | ATL | Atlántico |

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