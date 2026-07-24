# HU-006 - Gestionar Tipos de Vehículo

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

**Quiero** gestionar el catálogo de tipos de vehículo

**Para** clasificar la flota utilizada en las operaciones logísticas y facilitar la asignación de vehículos según las características del servicio.

---

## Criterios de aceptación

- [ ] Crear un tipo de vehículo.
- [ ] Editar un tipo de vehículo.
- [ ] Consultar tipos de vehículo.
- [ ] Activar o desactivar un tipo de vehículo.
- [ ] Registrar el código del tipo de vehículo.
- [ ] Registrar la capacidad de carga.
- [ ] Registrar la capacidad volumétrica.
- [ ] Registrar el número máximo de pallets.
- [ ] No permitir códigos duplicados.

---

## Reglas de negocio

### RN-001
El código del tipo de vehículo debe ser único.

### RN-002
El nombre del tipo de vehículo debe ser único.

### RN-003
Las capacidades deben ser mayores a cero.

### RN-004
No se eliminan tipos de vehículo; únicamente se desactivan.

### RN-005
El catálogo podrá ser utilizado por los módulos de Transporte, Despacho y Última Milla.

---

## Modelo

**Entidad**

`enrutaco.vehicle.type`

| Campo | Tipo | Obligatorio | Observaciones |
|--------|------|-------------|---------------|
| code | Char | Sí | Código interno |
| name | Char | Sí | Nombre |
| description | Text | No | Descripción |
| payload_kg | Float | Sí | Capacidad de carga (kg) |
| volume_m3 | Float | No | Capacidad volumétrica (m³) |
| pallet_capacity | Integer | No | Número máximo de pallets |
| active | Boolean | Sí | Activo |

---

## Relaciones

Tipo de Vehículo (1) ──────────── (N) Vehículos *(módulo Transporte)*

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
  - Catálogos
    - Tipos de Vehículo

---

## Datos iniciales

| Código | Tipo |
|---------|------|
| MOTO | Motocicleta |
| VAN | Furgón |
| NPR | Camión NPR |
| NQR | Camión NQR |
| TRACTO | Tractocamión |

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