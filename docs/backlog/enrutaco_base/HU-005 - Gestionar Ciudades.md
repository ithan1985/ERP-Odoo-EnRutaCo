# HU-005 - Administrar Ciudades

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

**Quiero** administrar el catálogo de ciudades

**Para** disponer de una ubicación geográfica estándar utilizada por sucursales, clientes, proveedores, rutas de transporte y operaciones logísticas.

---

## Criterios de aceptación

- [ ] Crear una ciudad.
- [ ] Editar una ciudad.
- [ ] Consultar ciudades.
- [ ] Activar o desactivar una ciudad.
- [ ] Asociar la ciudad a un departamento.
- [ ] Registrar el código DANE (opcional).
- [ ] No permitir ciudades duplicadas dentro del mismo departamento.

---

## Reglas de negocio

### RN-001
Toda ciudad debe pertenecer a un departamento.

### RN-002
El nombre de la ciudad debe ser único dentro del departamento.

### RN-003
El código DANE debe ser único cuando exista.

### RN-004
No se eliminan ciudades; únicamente se desactivan.

### RN-005
Un departamento puede tener múltiples ciudades.

---

## Modelo

**Entidad**

`enrutaco.city`

| Campo | Tipo | Obligatorio | Observaciones |
|--------|------|-------------|---------------|
| department_id | Many2one | Sí | Departamento |
| code | Char | No | Código DANE |
| name | Char | Sí | Ciudad |
| active | Boolean | Sí | Activo |

---

## Relaciones

Departamento (1) ──────────── (N) Ciudades

Ciudad (1) ────────────────── (N) Sucursales

Ciudad (1) ────────────────── (N) Clientes

Ciudad (1) ────────────────── (N) Proveedores

---

## Dependencias

- HU-003 Administrar Países
- HU-004 Administrar Departamentos

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
    - Ciudades

---

## Datos iniciales

| Departamento | Código | Ciudad |
|--------------|---------|---------|
| Bogotá D.C. | 11001 | Bogotá |
| Antioquia | 05001 | Medellín |
| Valle del Cauca | 76001 | Cali |
| Atlántico | 08001 | Barranquilla |

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