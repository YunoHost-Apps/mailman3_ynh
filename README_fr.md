# Mailman3 pour YunoHost

[![Niveau d'intégration](https://dash.yunohost.org/integration/mailman3.svg)](https://dash.yunohost.org/appci/app/mailman3) ![](https://ci-apps.yunohost.org/ci/badges/mailman3.status.svg) ![](https://ci-apps.yunohost.org/ci/badges/mailman3.maintain.svg)  
[![Installer Mailman3 avec YunoHost](https://install-app.yunohost.org/install-with-yunohost.svg)](https://install-app.yunohost.org/?app=mailman3)

*[Read this readme in english.](./README.md)*
*[Lire ce readme en français.](./README_fr.md)*

> *Ce package vous permet d'installer Mailman3 rapidement et simplement sur un serveur YunoHost.
Si vous n'avez pas YunoHost, regardez [ici](https://yunohost.org/#/install) pour savoir comment l'installer et en profiter.*

## Vue d'ensemble

Un gestionnaire de liste de discussion par email

**Version incluse :** 1.0~ynh1

**Démo :** https://lists.mailman3.org/mailman3/lists/

## Captures d'écran

![](./doc/screenshots/screenshot1.webp)

## Avertissements / informations importantes

* Any known limitations, constrains or stuff not working, such as (but not limited to):
    * requiring a full dedicated domain
    * architectures not supported ?
    * not-working single-sign on or LDAP integration ?
    * the app requires an important amount of RAM / disk / .. to install or to work properly
    * etc...

* Other infos that people should be aware of, such as:
    * No LDAP support yet (apparently under development)
    * Users can also just sign up themselves to manage details
    * Users can use mailing lists without signing up?

## Post-installation steps

### Setup Admin User

You must [configure the admin user](http://docs.mailman3.org/en/latest/config-web.html#setting-up-admin-account):

```bash
$ cd /usr/share/mailman3-web
$ python3 manage.py createsuperuser
```

You should then attempt to log in with this user account in the web UI. Once you've logged in, a confirmation mail will be sent to your email address that you specified. Therefore, you should have something like [Rainloop](https://github.com/YunoHost-Apps/rainloop_ynh) installed to view mail on your YunoHost installation.

### Setup your main domain

You'll need to log in as administrator and visit the `/admin/site/site`.

If you're Mailman3 is setup on `https://myyunohost.org` then that would be the following:

> https://myyunohost.org/admin/site/site

### Configure incoming mail

Mailman3 implements an LMTP server for receiving mail from Postfix. This means that Mailman3 doesn't need anything from Dovecot. This is important to understand because Dovecot is the default YunoHost local delivery agent. Therefore, the default YunoHost Postfix configuration uses Dovecot. So, in order to deliver incoming mail, we need to override which delivery agent handles which mails based on the addresses. In other words, if you create a mailing list "mylist@myyunohost.org" you want Mailman3's LMTP server to receive this, *not* Dovecot, becaues Dovecot only delivers to LDAP created user accounts.

You'll need to add this to your Postfix configuration:

```bash
owner_request_special = no

transport_maps =
  hash:/var/lib/mailman3/data/postfix_lmtp

local_recipient_maps =
  hash:/var/lib/mailman3/data/postfix_lmtp

virtual_mailbox_maps = ldap:/etc/postfix/ldap-accounts.cf, hash:/var/lib/mailman3/data/postfix_lmtp
```

And then run:

```bash
$ sudo -su list mailman aliases
```

This is unfortunately a manual step at this point because the package remains experimental. Once it matures, this will be integrated into a hook or the default Postfix configuration. For now, remember that when you run `yunohost tools regen-conf postfix` or if any installation invokes `regen-conf`, your Postfix configuration will not be changed because it has diverged from the default configuration. This may cause you problems if YunoHost core expects that there is some new value in your Postfix configuration.

### Configure outgoing mail

Postfix relies on using SMTP which should be configured in your `/etc/postfix/main.cf`.

You should make sure that you have outgoing mail working before getting started with Mailman 3.

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

## Documentations et ressources

* Site officiel de l'app : http://www.list.org/
* Documentation officielle utilisateur : http://docs.mailman3.org/en/latest/userguide.html
* Documentation officielle de l'admin : https://docs.mailman3.org/en/latest/
* Dépôt de code officiel de l'app : https://gitlab.com/mailman/mailman-suite
* Documentation YunoHost pour cette app : https://yunohost.org/app_mailman3
* Signaler un bug : https://github.com/YunoHost-Apps/mailman3_ynh/issues

## Informations pour les développeurs

Merci de faire vos pull request sur la [branche testing](https://github.com/YunoHost-Apps/mailman3_ynh/tree/testing).

Pour essayer la branche testing, procédez comme suit.
```
sudo yunohost app install https://github.com/YunoHost-Apps/mailman3_ynh/tree/testing --debug
ou
sudo yunohost app upgrade mailman3 -u https://github.com/YunoHost-Apps/mailman3_ynh/tree/testing --debug
```

**Plus d'infos sur le packaging d'applications :** https://yunohost.org/packaging_apps