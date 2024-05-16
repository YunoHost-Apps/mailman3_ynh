<!--
Ohart ongi: README hau automatikoki sortu da <https://github.com/YunoHost/apps/tree/master/tools/readme_generator>ri esker
EZ editatu eskuz.
-->

# Mailman3 YunoHost-erako

[![Integrazio maila](https://dash.yunohost.org/integration/mailman3.svg)](https://dash.yunohost.org/appci/app/mailman3) ![Funtzionamendu egoera](https://ci-apps.yunohost.org/ci/badges/mailman3.status.svg) ![Mantentze egoera](https://ci-apps.yunohost.org/ci/badges/mailman3.maintain.svg)

[![Instalatu Mailman3 YunoHost-ekin](https://install-app.yunohost.org/install-with-yunohost.svg)](https://install-app.yunohost.org/?app=mailman3)

*[Irakurri README hau beste hizkuntzatan.](./ALL_README.md)*

> *Pakete honek Mailman3 YunoHost zerbitzari batean azkar eta zailtasunik gabe instalatzea ahalbidetzen dizu.*  
> *YunoHost ez baduzu, kontsultatu [gida](https://yunohost.org/install) nola instalatu ikasteko.*

## Aurreikuspena



**Paketatutako bertsioa:** 1.0~ynh2

**Demoa:** <https://lists.mailman3.org/mailman3/lists/>

## Pantaila-argazkiak

![Mailman3(r)en pantaila-argazkia](./doc/screenshots/screenshot1.webp)

## Ezespena / informazio garrantzitsua

* Any known limitations, constrains or stuff not working, such as (but not limited to):
    * requiring a full dedicated domain

* Other infos that people should be aware of, such as:
    * No LDAP support yet (apparently under development)
    * Users can also just sign up themselves to manage details
    * Users can use mailing lists without signing up?

Classical admin is available on the page: https://myyunohost.org/

Django admin on: https://myyunohost.org/admin/

## General Configuration

Mailman 3 or "The Mailman Suite" is made up of 5 moving parts. See the following documentation for more:

> http://docs.mailman3.org/en/latest/index.html#the-mailman-suite

On your YunoHost, all the configuration files you need to worry about are in:

* `/etc/mailman3/`
* `/usr/share/mailman3-web/`

The services you need to manage can be checked with:

* `systemctl status mailman3`
* `systemctl status mailman3-web`

It is important to note that this package makes use of the [mailman3-full](http://docs.mailman3.org/en/latest/prodsetup.html#distribution-packages) Debian package contained in the Debian Stretch backports repository. The default installation assumes the use of a SQLite3 database but the installation script overrides this and uses a PostgreSQL database instead.

Finally, you also configure things through the Django web admin available at `/admin/`.

## Limitations

* Migrating from Mailman 2.X is not officially supported, sorry. However, there is a manual and
  which details an experimental process. Please see [the documentation](https://docs.mailman3.org/en/latest/migration.html).

* Mailman3 must be configured to use a root domain (https://myyunohost.org and not https://myyunohost.org/mailman3).

* You must have a HTTPS certificate installed on the root domain.

* There may be only one installation per YunoHost.

## Dokumentazioa eta baliabideak

- Aplikazioaren webgune ofiziala: <http://www.list.org/>
- Erabiltzaileen dokumentazio ofiziala: <http://docs.mailman3.org/en/latest/userguide.html>
- Administratzaileen dokumentazio ofiziala: <https://docs.mailman3.org/en/latest/>
- Jatorrizko aplikazioaren kode-gordailua: <https://gitlab.com/mailman/mailman-suite>
- YunoHost Denda: <https://apps.yunohost.org/app/mailman3>
- Eman errore baten berri: <https://github.com/YunoHost-Apps/mailman3_ynh/issues>

## Garatzaileentzako informazioa

Bidali `pull request`a [`testing` abarrera](https://github.com/YunoHost-Apps/mailman3_ynh/tree/testing).

`testing` abarra probatzeko, ondorengoa egin:

```bash
sudo yunohost app install https://github.com/YunoHost-Apps/mailman3_ynh/tree/testing --debug
edo
sudo yunohost app upgrade mailman3 -u https://github.com/YunoHost-Apps/mailman3_ynh/tree/testing --debug
```

**Informazio gehiago aplikazioaren paketatzeari buruz:** <https://yunohost.org/packaging_apps>
