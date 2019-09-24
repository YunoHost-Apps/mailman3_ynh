# Mailman3 for YunoHost

[![Integration level](https://dash.yunohost.org/integration/mailman3.svg)](https://dash.yunohost.org/appci/app/mailman3)
[![Install Mailman3 with YunoHost](https://install-app.yunohost.org/install-with-yunohost.png)](https://install-app.yunohost.org/?app=mailman3)

*[Lire ce readme en français.](./README_fr.md)*

> This package allow you to install Mailman3 quickly and simply on a YunoHost server.

*If you don't have YunoHost, please see [here](https://yunohost.org/#/install) to know how to install and enjoy it.*

## Status

**Experimental.**

## Overview

This is GNU Mailman, a mailing list management system distributed under the terms of the GNU General Public License (GPL) version 3 or later. Mailman is written in Python which is available for all platforms that Mailman is supported on, including GNU/Linux and most other Unix-like operating systems (e.g. Solaris, *BSD, MacOSX, etc.).

> http://docs.mailman3.org/en/latest/userguide.html

**Shipped version:** 3.2.0

## Screenshots

![](https://image.slidesharecdn.com/hyperkitty-160201173833/95/hyperkitty-a-web-interface-for-gnu-mailman-3-8-638.jpg?cb=1454349750)

## Demo

* [Official demo](https://lists.mailman3.org/mailman3/lists/)

No user/password is provided, so you must sign up.

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

If you're Mailman3 is setup on `myyunohost.org` then that would be the following:

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

## General Configuration

Mailman3 is made up of 3 moving parts:

* Mailman3 Core: https://mailman.readthedocs.io
* Postorious: https://postorius.readthedocs.io
* Hyperkitty: https://hyperkitty.readthedocs.io

There is also documentation for "the suite" which is all the parts together:

* https://docs.mailman3.org

On your YunoHost, all the configuration files you need to worry about are in:

* `/etc/mailman3/`

It is important to note that this package makes use of the [mailman3-full](http://docs.mailman3.org/en/latest/prodsetup.html#distribution-packages) Debian package contained in the Debian Stretch backports repository.

Finally, you also configure things through the Django web admin available at `/admin/`.

## YunoHost specific features

#### Multi-users support

* No LDAP support
* Users can also just sign up themselves to manage details
* Users can use mailing lists without signing up

#### Supported architectures

* x86-64b - [![Build Status](https://ci-apps.yunohost.org/ci/logs/mailman3%20%28Apps%29.svg)](https://ci-apps.yunohost.org/ci/apps/mailman3/)
* ARMv8-A - [![Build Status](https://ci-apps-arm.yunohost.org/ci/logs/mailman3%20%28Apps%29.svg)](https://ci-apps-arm.yunohost.org/ci/apps/mailman3/)

## Limitations

* Migrating from Mailman 2.X is not supported. This is a manual and
  experimental process. Please see [the documentation](https://docs.mailman3.org/en/latest/migration.html).

* Mailman3 must be configured to use a root domain (myyunohost.org and not myyunohost.org/mailman3).

* You must have a HTTPS certificate installed on the root domain.

* There may be only one installation per YunoHost.

## Mirroring

* https://github.com/YunoHost-Apps/mailman3_ynh
* https://hack.decentral1.se/yunohost-packages/mailman3_ynh

## Links

 * Report a bug: https://github.com/YunoHost-Apps/mailman3_ynh/issues
 * App website: http://docs.mailman3.org/en/latest/index.html
 * Upstream app repository: https://gitlab.com/mailman/mailman-suite
 * YunoHost website: https://yunohost.org/

---

Developers info
----------------

**Only if you want to use a testing branch for coding, instead of merging directly into master.**

Please make your pull request against the [testing branch](https://github.com/YunoHost-Apps/mailman3_ynh/tree/testing).

To try the testing branch:

```
$ yunohost app install https://github.com/YunoHost-Apps/mailman3_ynh/tree/testing --debug
```

Or to upgrade from the testing branch:

```bash
$ yunohost app upgrade mailman3 -u https://github.com/YunoHost-Apps/mailman3_ynh/tree/testing --debug
```
