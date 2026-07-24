# HU-001 - Administrar Empresas

## Objetivo

Como administrador del sistema
quiero registrar empresas
para que los módulos puedan asociar información a ellas.

## Criterios de aceptación

- Crear empresa
- Editar empresa
- Consultar empresa
- Desactivar empresa
- NIT único

## Modelo

enrutaco.company

Campos:
- name
- legal_name
- vat
- email
- phone
- website
- active

## Reglas de negocio

- NIT único.
- No eliminar registros.
- Nombre obligatorio.

## Definition of Done

- Modelo
- ACL
- Vistas
- Menú
- Datos demo
- Instalación correcta