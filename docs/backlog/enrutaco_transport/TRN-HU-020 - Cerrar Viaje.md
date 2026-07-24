# TRN-HU-020 - Cerrar Viaje

## Estado
Pendiente

## Prioridad
Alta

## Sprint
Por definir

## Módulo
enrutaco_transport

## Descripción
**Como** coordinador de transporte

**Quiero** cerrar administrativamente un viaje una vez finalizada la operación.

**Para** mejorar el control operativo y financiero de la operación.

## Criterios de aceptación
- Crear, consultar y actualizar información cuando aplique.
- Validar reglas de negocio.
- Registrar auditoría.
- Respetar permisos por rol.

## Reglas de negocio
- No se puede cerrar un viaje con incidencias críticas abiertas.
- Todos los costos deben estar asociados a un viaje válido.

## Modelo(s)
Por definir durante el diseño funcional.

## Relaciones
Viajes, vehículos, conductores, flota, logística y despacho.

## Dependencias
TRN-HU-001 a TRN-HU-015.

## Seguridad
Acceso restringido al personal autorizado.

## Vistas
Lista, formulario, búsqueda y reportes.

## Datos iniciales
No aplica.

## Definition of Done
- Desarrollo implementado.
- Pruebas funcionales aprobadas.
- Documentación actualizada.
