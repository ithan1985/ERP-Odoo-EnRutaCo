# HU-002 - Administrar Sucursales

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

**Quiero** registrar y administrar las sucursales de la empresa

**Para** organizar la operación logística, asignar recursos y soportar los procesos de transporte, despacho y última milla.

---

## Criterios de aceptación

- [ ] Crear una sucursal.
- [ ] Editar una sucursal.
- [ ] Consultar sucursales.
- [ ] Activar o desactivar una sucursal.
- [ ] Asociar la sucursal a una empresa.
- [ ] Definir la ciudad donde opera.
- [ ] Definir la dirección física.
- [ ] Definir datos de contacto.
- [ ] El código de la sucursal debe ser único por empresa.

---

## Reglas de negocio

### RN-001
Toda sucursal debe pertenecer a una empresa.

### RN-002
El código de la sucursal debe ser único dentro de la empresa.

### RN-003
No se eliminan sucursales; únicamente se desactivan.

### RN-004
La ciudad es obligatoria.

### RN-005
Una empresa puede tener múltiples sucursales.

---

## Modelo

**Entidad**

`enrutaco.branch`

| Campo | Tipo | Obligatorio | Observaciones |
|--------|------|-------------|---------------|
| company_id | Many2one | Sí | Empresa |
| code | Char | Sí | Código interno |
| name | Char | Sí | Nombre |
| city_id | Many2one | Sí | Ciudad |
| address | Char | Sí | Dirección |
| phone | Char | No | Teléfono |
| email | Char | No | Correo |
| manager | Char | No | Responsable |
| active | Boolean | Sí | Activo |

---

## Relaciones

Empresa (1) ──────────── (N) Sucursales

Ciudad (1) ───────────── (N) Sucursales

---

## Dependencias

- HU-001 Administrar Empresas
- HU-005 Administrar Ciudades

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

Menú

EnRutaCo

- Configuración
  - Empresas
  - Sucursales

---

## Datos iniciales

| Empresa | Código | Nombre |
|----------|---------|---------|
| EnRutaCo S.A.S. | BOG | Bogotá Principal |

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