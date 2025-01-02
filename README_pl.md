<!--
To README zostało automatycznie wygenerowane przez <https://github.com/YunoHost/apps/tree/master/tools/readme_generator>
Nie powinno być ono edytowane ręcznie.
-->

# Mailman3 dla YunoHost

[![Poziom integracji](https://apps.yunohost.org/badge/integration/mailman3)](https://ci-apps.yunohost.org/ci/apps/mailman3/)
![Status działania](https://apps.yunohost.org/badge/state/mailman3)
![Status utrzymania](https://apps.yunohost.org/badge/maintained/mailman3)

[![Zainstaluj Mailman3 z YunoHost](https://install-app.yunohost.org/install-with-yunohost.svg)](https://install-app.yunohost.org/?app=mailman3)

*[Przeczytaj plik README w innym języku.](./ALL_README.md)*

> *Ta aplikacja pozwala na szybką i prostą instalację Mailman3 na serwerze YunoHost.*  
> *Jeżeli nie masz YunoHost zapoznaj się z [poradnikiem](https://yunohost.org/install) instalacji.*

## Przegląd

* Users can just sign up themselves to manage details
* Users can use mailing lists without signing up?

## Limitations

* Migrating from Mailman 2.X is not officially supported, sorry. However, there is a manual and
  which details an experimental process. Please see [the documentation](https://docs.mailman3.org/en/latest/migration.html).

* Mailman3 must be configured to use a root domain (https://myyunohost.org and *not* https://myyunohost.org/mailman3).

* You must have a HTTPS certificate installed on the root domain.

* There may be only one installation per YunoHost.


**Dostarczona wersja:** 3.3~ynh1

**Demo:** <https://lists.mailman3.org/mailman3/lists/>

## Zrzuty ekranu

![Zrzut ekranu z Mailman3](./doc/screenshots/screenshot1.webp)

## Dokumentacja i zasoby

- Oficjalna strona aplikacji: <http://www.list.org/>
- Oficjalna dokumentacja: <http://docs.mailman3.org/en/latest/userguide.html>
- Oficjalna dokumentacja dla administratora: <https://docs.mailman3.org/en/latest/>
- Repozytorium z kodem źródłowym: <https://gitlab.com/mailman/mailman-suite>
- Sklep YunoHost: <https://apps.yunohost.org/app/mailman3>
- Zgłaszanie błędów: <https://github.com/YunoHost-Apps/mailman3_ynh/issues>

## Informacje od twórców

Wyślij swój pull request do [gałęzi `testing`](https://github.com/YunoHost-Apps/mailman3_ynh/tree/testing).

Aby wypróbować gałąź `testing` postępuj zgodnie z instrukcjami:

```bash
sudo yunohost app install https://github.com/YunoHost-Apps/mailman3_ynh/tree/testing --debug
lub
sudo yunohost app upgrade mailman3 -u https://github.com/YunoHost-Apps/mailman3_ynh/tree/testing --debug
```

**Więcej informacji o tworzeniu paczek aplikacji:** <https://yunohost.org/packaging_apps>
