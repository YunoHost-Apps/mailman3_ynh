<!--
Nota bene : ce README est automatiquement généré par <https://github.com/YunoHost/apps/tree/master/tools/readme_generator>
Il NE doit PAS être modifié à la main.
-->

# Mailman3 pour YunoHost

[![Niveau d’intégration](https://apps.yunohost.org/badge/integration/mailman3)](https://ci-apps.yunohost.org/ci/apps/mailman3/)
![Statut du fonctionnement](https://apps.yunohost.org/badge/state/mailman3)
![Statut de maintenance](https://apps.yunohost.org/badge/maintained/mailman3)

[![Installer Mailman3 avec YunoHost](https://install-app.yunohost.org/install-with-yunohost.svg)](https://install-app.yunohost.org/?app=mailman3)

*[Lire le README dans d'autres langues.](./ALL_README.md)*

> *Ce package vous permet d’installer Mailman3 rapidement et simplement sur un serveur YunoHost.*  
> *Si vous n’avez pas YunoHost, consultez [ce guide](https://yunohost.org/install) pour savoir comment l’installer et en profiter.*

## Vue d’ensemble

* Users can just sign up themselves to manage details
* Users can use mailing lists without signing up?

## Limitations

* Migrating from Mailman 2.X is not officially supported, sorry. However, there is a manual and
  which details an experimental process. Please see [the documentation](https://docs.mailman3.org/en/latest/migration.html).

* Mailman3 must be configured to use a root domain (https://myyunohost.org and *not* https://myyunohost.org/mailman3).

* You must have a HTTPS certificate installed on the root domain.

* There may be only one installation per YunoHost.


**Version incluse :** 3.3~ynh1

**Démo :** <https://lists.mailman3.org/mailman3/lists/>

## Captures d’écran

![Capture d’écran de Mailman3](./doc/screenshots/screenshot1.webp)

## Documentations et ressources

- Site officiel de l’app : <http://www.list.org/>
- Documentation officielle utilisateur : <http://docs.mailman3.org/en/latest/userguide.html>
- Documentation officielle de l’admin : <https://docs.mailman3.org/en/latest/>
- Dépôt de code officiel de l’app : <https://gitlab.com/mailman/mailman-suite>
- YunoHost Store : <https://apps.yunohost.org/app/mailman3>
- Signaler un bug : <https://github.com/YunoHost-Apps/mailman3_ynh/issues>

## Informations pour les développeurs

Merci de faire vos pull request sur la [branche `testing`](https://github.com/YunoHost-Apps/mailman3_ynh/tree/testing).

Pour essayer la branche `testing`, procédez comme suit :

```bash
sudo yunohost app install https://github.com/YunoHost-Apps/mailman3_ynh/tree/testing --debug
ou
sudo yunohost app upgrade mailman3 -u https://github.com/YunoHost-Apps/mailman3_ynh/tree/testing --debug
```

**Plus d’infos sur le packaging d’applications :** <https://yunohost.org/packaging_apps>
