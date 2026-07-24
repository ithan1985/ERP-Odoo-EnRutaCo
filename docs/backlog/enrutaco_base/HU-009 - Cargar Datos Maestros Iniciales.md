# HU-009 - Cargar Datos Maestros Iniciales

## Estado

Backlog

## Prioridad

Alta

## Sprint

2

## Módulo

enrutaco_base

---

## Descripción

**Como** administrador del sistema

**Quiero** cargar los datos maestros iniciales

**Para** disponer de la información base necesaria para la operación del ERP desde su instalación.

---

## Criterios de aceptación

- [ ] Cargar países.
- [ ] Cargar departamentos.
- [ ] Cargar ciudades principales.
- [ ] Cargar tipos de vehículo.
- [ ] Cargar empresa inicial.
- [ ] Cargar sucursal principal.
- [ ] Validar la integridad referencial durante la carga.
- [ ] Permitir reinstalar el módulo sin inconsistencias.

---

## Reglas de negocio

### RN-001

La carga debe realizarse automáticamente durante la instalación del módulo.

### RN-002

No deben crearse registros duplicados.

### RN-003

Las relaciones entre catálogos deben mantenerse consistentes.

### RN-004

La carga debe ser idempotente.

---

## Componentes

Archivos XML / CSV ubicados en:

- data/company.xml
- data/countries.xml
- data/departments.xml
- data/cities.xml
- data/vehicle_types.xml
- data/branches.xml

---

## Dependencias

- HU-001 Gestionar Empresas
- HU-002 Gestionar Sucursales
- HU-003 Gestionar Países
- HU-004 Gestionar Departamentos
- HU-005 Gestionar Ciudades
- HU-006 Gestionar Tipos de Vehículo

---

## Definition of Done

- [ ] Datos cargados automáticamente.
- [ ] Sin registros duplicados.
- [ ] Relaciones válidas.
- [ ] Instalación exitosa.
- [ ] Pruebas funcionales ejecutadas.