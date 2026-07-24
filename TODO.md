# ERP EnRutaCo - Roadmap de Desarrollo

## Estado del Proyecto

### Infraestructura
- [x] Crear repositorio Git
- [x] Configurar estructura del proyecto
- [x] Configurar Docker Compose
- [x] Configurar PostgreSQL
- [x] Configurar Odoo 19 Community
- [x] Crear base de datos `enrutaco_dev`
- [x] Configurar `.gitignore`
- [x] Configurar `.env.example`
- [x] Crear Tag `v0.1.0`

---

# Fase 1 - Infraestructura (v0.1.0)

**Estado:** ✅ Finalizada

## Objetivos

- Docker
- PostgreSQL
- Odoo 19
- Persistencia
- Configuración local
- Git

---

# Fase 2 - Arquitectura Funcional (v0.2.0)

**Estado:** ✅ Finalizada

## Documentación MVP

- [x] Crear carpeta `docs/MVP`
- [x] AS-IS
- [x] TO-BE
- [x] Requerimientos
- [x] Casos de Uso
- [x] Product Backlog

## Validación

- [x] Revisar documentación
- [x] Commit cambios
- [x] Merge develop → main
- [x] Crear tag v0.2.0
- [x] Push main
- [x] Push tags

---

# Fase 3 - Módulo Base (v0.3.0)

**Estado:** ⏳ Pendiente

## enrutaco_base

### Configuración

- [ ] Manifest
- [ ] Estructura del módulo
- [ ] Menús
- [ ] Configuración
- [ ] Parámetros del sistema

### Seguridad

- [ ] Grupos
- [ ] ACL
- [ ] Record Rules

### Catálogos

- [ ] Empresa
- [ ] Sedes
- [ ] Países
- [ ] Departamentos
- [ ] Ciudades
- [ ] Tipos de vehículo

### Datos

- [ ] Configuración inicial
- [ ] Datos demo

---

# Fase 4 - CRM (v0.4.0)

**Estado:** ⏳ Pendiente

## Clientes

- [ ] Clientes
- [ ] Contactos
- [ ] Direcciones

## CRM

- [ ] Leads
- [ ] Oportunidades
- [ ] Pipeline Comercial

## Ventas

- [ ] Cotizaciones
- [ ] Pedidos
- [ ] Conversión Lead → Venta

---

# Fase 5 - Logística (v0.5.0)

**Estado:** ⏳ Pendiente

## Centros Logísticos

- [ ] Centros
- [ ] Bodegas
- [ ] Zonas

## Cobertura

- [ ] Cobertura Nacional
- [ ] Ciudades
- [ ] Rutas
- [ ] Matriz Origen/Destino

---

# Fase 6 - Transporte (v0.6.0)

**Estado:** ⏳ Pendiente

## Flota

- [ ] Vehículos
- [ ] Tipos
- [ ] Capacidad

## Conductores

- [ ] Conductores
- [ ] Licencias
- [ ] Disponibilidad

---

# Fase 7 - Despachos (v0.7.0)

**Estado:** ⏳ Pendiente

## Operación

- [ ] Ordenes de Transporte
- [ ] Planeación
- [ ] Asignación
- [ ] Estados
- [ ] Seguimiento

---

# Fase 8 - Última Milla (v0.8.0)

**Estado:** ⏳ Pendiente

## Entregas

- [ ] Confirmación
- [ ] Evidencias
- [ ] Firma Digital
- [ ] Geolocalización
- [ ] Tracking

---

# Fase 9 - KPIs e Integraciones (v0.9.0)

**Estado:** ⏳ Pendiente

## Indicadores

- [ ] OTIF
- [ ] SLA
- [ ] Costo por envío
- [ ] Productividad

## Dashboards

- [ ] Operación
- [ ] Gerencia
- [ ] Dirección

## Integraciones

- [ ] API REST
- [ ] Eventos
- [ ] Importadores
- [ ] Exportadores

---

# Fase 10 - Producción (v1.0.0)

**Estado:** ⏳ Pendiente

## Infraestructura AWS

- [ ] Lightsail / EC2
- [ ] Docker
- [ ] PostgreSQL
- [ ] Backups
- [ ] SSL
- [ ] Dominio
- [ ] CI/CD

## Documentación

- [ ] Arquitectura
- [ ] Manual de Instalación
- [ ] Manual Técnico
- [ ] Manual Funcional
- [ ] ADRs

## Release

- [ ] Pruebas finales
- [ ] Release Candidate
- [ ] Tag `v1.0.0`

---

# Versiones

- [x] **v0.1.0** Infraestructura
- [ ] **v0.2.0** Arquitectura Funcional (MVP)
- [ ] **v0.3.0** Módulo Base
- [ ] **v0.4.0** CRM
- [ ] **v0.5.0** Logística
- [ ] **v0.6.0** Transporte
- [ ] **v0.7.0** Despachos
- [ ] **v0.8.0** Última Milla
- [ ] **v0.9.0** KPIs e Integraciones
- [ ] **v1.0.0** ERP EnRutaCo