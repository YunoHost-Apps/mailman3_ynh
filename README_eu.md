<!--
Ohart ongi: README hau automatikoki sortu da <https://github.com/YunoHost/apps/tree/master/tools/readme_generator>ri esker
EZ editatu eskuz.
-->

# Mailman3 YunoHost-erako

[![Integrazio maila](https://apps.yunohost.org/badge/integration/mailman3)](https://ci-apps.yunohost.org/ci/apps/mailman3/)
![Funtzionamendu egoera](https://apps.yunohost.org/badge/state/mailman3)
![Mantentze egoera](https://apps.yunohost.org/badge/maintained/mailman3)

[![Instalatu Mailman3 YunoHost-ekin](https://install-app.yunohost.org/install-with-yunohost.svg)](https://install-app.yunohost.org/?app=mailman3)

*[Irakurri README hau beste hizkuntzatan.](./ALL_README.md)*

> *Pakete honek Mailman3 YunoHost zerbitzari batean azkar eta zailtasunik gabe instalatzea ahalbidetzen dizu.*  
> *YunoHost ez baduzu, kontsultatu [gida](https://yunohost.org/install) nola instalatu ikasteko.*

## Aurreikuspena

* Users can just sign up themselves to manage details
* Users can use mailing lists without signing up?

## Limitations

* Migrating from Mailman 2.X is not officially supported, sorry. However, there is a manual and
  which details an experimental process. Please see [the documentation](https://docs.mailman3.org/en/latest/migration.html).

* Mailman3 must be configured to use a root domain (https://myyunohost.org and *not* https://myyunohost.org/mailman3).

* You must have a HTTPS certificate installed on the root domain.

* There may be only one installation per YunoHost.


**Paketatutako bertsioa:** 3.3~ynh1

**Demoa:** <https://lists.mailman3.org/mailman3/lists/>

## Pantaila-argazkiak

![Mailman3(r)en pantaila-argazkia](./doc/screenshots/screenshot1.webp)

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
