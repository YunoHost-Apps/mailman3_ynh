<!--
N.B.: Questo README è stato automaticamente generato da <https://github.com/YunoHost/apps/tree/master/tools/readme_generator>
NON DEVE essere modificato manualmente.
-->

# Mailman3 per YunoHost

[![Livello di integrazione](https://dash.yunohost.org/integration/mailman3.svg)](https://dash.yunohost.org/appci/app/mailman3) ![Stato di funzionamento](https://ci-apps.yunohost.org/ci/badges/mailman3.status.svg) ![Stato di manutenzione](https://ci-apps.yunohost.org/ci/badges/mailman3.maintain.svg)

[![Installa Mailman3 con YunoHost](https://install-app.yunohost.org/install-with-yunohost.svg)](https://install-app.yunohost.org/?app=mailman3)

*[Leggi questo README in altre lingue.](./ALL_README.md)*

> *Questo pacchetto ti permette di installare Mailman3 su un server YunoHost in modo semplice e veloce.*  
> *Se non hai YunoHost, consulta [la guida](https://yunohost.org/install) per imparare a installarlo.*

## Panoramica



**Versione pubblicata:** 1.0~ynh2

**Prova:** <https://lists.mailman3.org/mailman3/lists/>

## Screenshot

![Screenshot di Mailman3](./doc/screenshots/screenshot1.webp)

## Attenzione/informazioni importanti

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

## Documentazione e risorse

- Sito web ufficiale dell’app: <http://www.list.org/>
- Documentazione ufficiale per gli utenti: <http://docs.mailman3.org/en/latest/userguide.html>
- Documentazione ufficiale per gli amministratori: <https://docs.mailman3.org/en/latest/>
- Repository upstream del codice dell’app: <https://gitlab.com/mailman/mailman-suite>
- Store di YunoHost: <https://apps.yunohost.org/app/mailman3>
- Segnala un problema: <https://github.com/YunoHost-Apps/mailman3_ynh/issues>

## Informazioni per sviluppatori

Si prega di inviare la tua pull request alla [branch di `testing`](https://github.com/YunoHost-Apps/mailman3_ynh/tree/testing).

Per provare la branch di `testing`, si prega di procedere in questo modo:

```bash
sudo yunohost app install https://github.com/YunoHost-Apps/mailman3_ynh/tree/testing --debug
o
sudo yunohost app upgrade mailman3 -u https://github.com/YunoHost-Apps/mailman3_ynh/tree/testing --debug
```

**Maggiori informazioni riguardo il pacchetto di quest’app:** <https://yunohost.org/packaging_apps>
