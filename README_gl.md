<!--
NOTA: Este README foi creado automáticamente por <https://github.com/YunoHost/apps/tree/master/tools/readme_generator>
NON debe editarse manualmente.
-->

# Mailman3 para YunoHost

[![Nivel de integración](https://dash.yunohost.org/integration/mailman3.svg)](https://dash.yunohost.org/appci/app/mailman3) ![Estado de funcionamento](https://ci-apps.yunohost.org/ci/badges/mailman3.status.svg) ![Estado de mantemento](https://ci-apps.yunohost.org/ci/badges/mailman3.maintain.svg)

[![Instalar Mailman3 con YunoHost](https://install-app.yunohost.org/install-with-yunohost.svg)](https://install-app.yunohost.org/?app=mailman3)

*[Le este README en outros idiomas.](./ALL_README.md)*

> *Este paquete permíteche instalar Mailman3 de xeito rápido e doado nun servidor YunoHost.*  
> *Se non usas YunoHost, le a [documentación](https://yunohost.org/install) para saber como instalalo.*

## Vista xeral

* Users can just sign up themselves to manage details
* Users can use mailing lists without signing up?

## Limitations

* Migrating from Mailman 2.X is not officially supported, sorry. However, there is a manual and
  which details an experimental process. Please see [the documentation](https://docs.mailman3.org/en/latest/migration.html).

* Mailman3 must be configured to use a root domain (https://myyunohost.org and *not* https://myyunohost.org/mailman3).

* You must have a HTTPS certificate installed on the root domain.

* There may be only one installation per YunoHost.


**Versión proporcionada:** 3.3~ynh1

**Demo:** <https://lists.mailman3.org/mailman3/lists/>

## Capturas de pantalla

![Captura de pantalla de Mailman3](./doc/screenshots/screenshot1.webp)

## Documentación e recursos

- Web oficial da app: <http://www.list.org/>
- Documentación oficial para usuarias: <http://docs.mailman3.org/en/latest/userguide.html>
- Documentación oficial para admin: <https://docs.mailman3.org/en/latest/>
- Repositorio de orixe do código: <https://gitlab.com/mailman/mailman-suite>
- Tenda YunoHost: <https://apps.yunohost.org/app/mailman3>
- Informar dun problema: <https://github.com/YunoHost-Apps/mailman3_ynh/issues>

## Info de desenvolvemento

Envía a túa colaboración á [rama `testing`](https://github.com/YunoHost-Apps/mailman3_ynh/tree/testing).

Para probar a rama `testing`, procede deste xeito:

```bash
sudo yunohost app install https://github.com/YunoHost-Apps/mailman3_ynh/tree/testing --debug
ou
sudo yunohost app upgrade mailman3 -u https://github.com/YunoHost-Apps/mailman3_ynh/tree/testing --debug
```

**Máis info sobre o empaquetado da app:** <https://yunohost.org/packaging_apps>
