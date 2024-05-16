<!--
Este archivo README esta generado automaticamente<https://github.com/YunoHost/apps/tree/master/tools/readme_generator>
No se debe editar a mano.
-->

# Mailman3 para Yunohost

[![Nivel de integración](https://dash.yunohost.org/integration/mailman3.svg)](https://dash.yunohost.org/appci/app/mailman3) ![Estado funcional](https://ci-apps.yunohost.org/ci/badges/mailman3.status.svg) ![Estado En Mantención](https://ci-apps.yunohost.org/ci/badges/mailman3.maintain.svg)

[![Instalar Mailman3 con Yunhost](https://install-app.yunohost.org/install-with-yunohost.svg)](https://install-app.yunohost.org/?app=mailman3)

*[Leer este README en otros idiomas.](./ALL_README.md)*

> *Este paquete le permite instalarMailman3 rapidamente y simplement en un servidor YunoHost.*  
> *Si no tiene YunoHost, visita [the guide](https://yunohost.org/install) para aprender como instalarla.*

## Descripción general

* Users can just sign up themselves to manage details
* Users can use mailing lists without signing up?

## Limitations

* Migrating from Mailman 2.X is not officially supported, sorry. However, there is a manual and
  which details an experimental process. Please see [the documentation](https://docs.mailman3.org/en/latest/migration.html).

* Mailman3 must be configured to use a root domain (https://myyunohost.org and *not* https://myyunohost.org/mailman3).

* You must have a HTTPS certificate installed on the root domain.

* There may be only one installation per YunoHost.


**Versión actual:** 3.3~ynh1

**Demo:** <https://lists.mailman3.org/mailman3/lists/>

## Capturas

![Captura de Mailman3](./doc/screenshots/screenshot1.webp)

## Documentaciones y recursos

- Sitio web oficial: <http://www.list.org/>
- Documentación usuario oficial: <http://docs.mailman3.org/en/latest/userguide.html>
- Documentación administrador oficial: <https://docs.mailman3.org/en/latest/>
- Repositorio del código fuente oficial de la aplicación : <https://gitlab.com/mailman/mailman-suite>
- Catálogo YunoHost: <https://apps.yunohost.org/app/mailman3>
- Reportar un error: <https://github.com/YunoHost-Apps/mailman3_ynh/issues>

## Información para desarrolladores

Por favor enviar sus correcciones a la [`branch testing`](https://github.com/YunoHost-Apps/mailman3_ynh/tree/testing

Para probar la rama `testing`, sigue asÍ:

```bash
sudo yunohost app install https://github.com/YunoHost-Apps/mailman3_ynh/tree/testing --debug
o
sudo yunohost app upgrade mailman3 -u https://github.com/YunoHost-Apps/mailman3_ynh/tree/testing --debug
```

**Mas informaciones sobre el empaquetado de aplicaciones:** <https://yunohost.org/packaging_apps>
