# HU-008 - Gestionar Usuarios y Roles

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

**Quiero** gestionar los usuarios y sus roles

**Para** controlar el acceso a las funcionalidades del ERP de acuerdo con las responsabilidades de cada colaborador.

---

## Criterios de aceptación

- [ ] Crear usuarios.
- [ ] Editar usuarios.
- [ ] Consultar usuarios.
- [ ] Activar o desactivar usuarios.
- [ ] Asignar uno o varios roles a un usuario.
- [ ] Restablecer contraseña.
- [ ] Bloquear usuarios cuando sea necesario.
- [ ] Consultar los permisos asignados a cada usuario.

---

## Reglas de negocio

### RN-001

Todo usuario debe tener al menos un rol asignado.

### RN-002

Un usuario puede tener múltiples roles.

### RN-003

Los usuarios desactivados no podrán iniciar sesión.

### RN-004

Únicamente los administradores podrán crear o modificar usuarios y roles.

### RN-005

Toda modificación de permisos deberá quedar registrada en la auditoría del sistema.

---

## Modelo

### Entidades

Se utilizarán los modelos estándar de Odoo.

| Modelo | Descripción |
|---------|-------------|
| `res.users` | Usuarios del sistema |
| `res.groups` | Roles o grupos de seguridad |

No se crearán modelos propios.

---

## Relaciones

Grupo (1) ───────────── (N) Usuarios

Usuario (N) ──────────── (N) Roles

---

## Dependencias

Ninguna.

---

## Seguridad

### Administrador ERP

- Crear usuarios
- Editar usuarios
- Desactivar usuarios
- Crear roles
- Asignar permisos

### Usuario ERP

- Consultar únicamente su propia información.

---

## Vistas

Se utilizarán las vistas estándar de Odoo.

En caso de requerirse, únicamente se personalizarán:

- Lista de Usuarios
- Formulario de Usuario
- Lista de Roles
- Formulario de Roles

---

## Menú

EnRutaCo

- Configuración
    - Seguridad
        - Usuarios
        - Roles

---

## Datos iniciales

### Roles

- Administrador ERP
- Director de Operaciones
- Coordinador Logístico
- Despachador
- Conductor
- Servicio al Cliente
- Analista Comercial
- Auditor
- Consulta

---

## Definition of Done

- [ ] Configuración de grupos realizada.
- [ ] Configuración de permisos realizada.
- [ ] Roles iniciales creados.
- [ ] Usuarios de prueba creados.
- [ ] Restricciones validadas.
- [ ] Instalación sin errores.
- [ ] Pruebas funcionales ejecutadas.