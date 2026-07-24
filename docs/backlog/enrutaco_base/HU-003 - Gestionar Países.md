# HU-003 - Administrar Países

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

**Quiero** administrar el catálogo de países

**Para** disponer de una ubicación geográfica estandarizada que pueda ser utilizada por clientes, proveedores, sucursales, empleados y demás procesos del ERP.

---

## Criterios de aceptación

- [ ] Crear un país.
- [ ] Editar un país.
- [ ] Consultar países.
- [ ] Activar o desactivar un país.
- [ ] Registrar el nombre del país.
- [ ] Registrar el código ISO 3166-1 Alpha-2.
- [ ] Registrar el código ISO 3166-1 Alpha-3 (opcional).
- [ ] Registrar el código telefónico internacional.
- [ ] No permitir códigos ISO duplicados.

---

## Reglas de negocio

### RN-001
El código ISO Alpha-2 debe ser único.

### RN-002
El nombre del país debe ser único.

### RN-003
No se eliminan países; únicamente se desactivan.

### RN-004
El código ISO debe almacenarse en mayúsculas.

### RN-005
Los países podrán ser utilizados por otros módulos mediante relaciones.

---

## Modelo

**Entidad**

`enrutaco.country`

| Campo | Tipo | Obligatorio | Observaciones |
|--------|------|-------------|---------------|
| name | Char | Sí | Nombre del país |
| iso2 | Char | Sí | Código ISO Alpha-2 |
| iso3 | Char | No | Código ISO Alpha-3 |
| phone_code | Char | No | Indicativo telefónico |
| active | Boolean | Sí | Activo |

---

## Relaciones

País (1) ──────────── (N) Departamentos

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
  - Ubicaciones
    - Países

---

## Datos iniciales

| País | ISO2 | ISO3 | Indicativo |
|------|------|------|------------|
| Colombia | CO | COL | +57 |

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