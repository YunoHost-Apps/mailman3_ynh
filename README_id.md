<!--
N.B.: README ini dibuat secara otomatis oleh <https://github.com/YunoHost/apps/tree/master/tools/readme_generator>
Ini TIDAK boleh diedit dengan tangan.
-->

# Mailman3 untuk YunoHost

[![Tingkat integrasi](https://apps.yunohost.org/badge/integration/mailman3)](https://ci-apps.yunohost.org/ci/apps/mailman3/)
![Status kerja](https://apps.yunohost.org/badge/state/mailman3)
![Status pemeliharaan](https://apps.yunohost.org/badge/maintained/mailman3)

[![Pasang Mailman3 dengan YunoHost](https://install-app.yunohost.org/install-with-yunohost.svg)](https://install-app.yunohost.org/?app=mailman3)

*[Baca README ini dengan bahasa yang lain.](./ALL_README.md)*

> *Paket ini memperbolehkan Anda untuk memasang Mailman3 secara cepat dan mudah pada server YunoHost.*  
> *Bila Anda tidak mempunyai YunoHost, silakan berkonsultasi dengan [panduan](https://yunohost.org/install) untuk mempelajari bagaimana untuk memasangnya.*

## Ringkasan

* Users can just sign up themselves to manage details
* Users can use mailing lists without signing up?

## Limitations

* Migrating from Mailman 2.X is not officially supported, sorry. However, there is a manual and
  which details an experimental process. Please see [the documentation](https://docs.mailman3.org/en/latest/migration.html).

* Mailman3 must be configured to use a root domain (https://myyunohost.org and *not* https://myyunohost.org/mailman3).

* You must have a HTTPS certificate installed on the root domain.

* There may be only one installation per YunoHost.


**Versi terkirim:** 3.3~ynh1

**Demo:** <https://lists.mailman3.org/mailman3/lists/>

## Tangkapan Layar

![Tangkapan Layar pada Mailman3](./doc/screenshots/screenshot1.webp)

## Dokumentasi dan sumber daya

- Website aplikasi resmi: <http://www.list.org/>
- Dokumentasi pengguna resmi: <http://docs.mailman3.org/en/latest/userguide.html>
- Dokumentasi admin resmi: <https://docs.mailman3.org/en/latest/>
- Depot kode aplikasi hulu: <https://gitlab.com/mailman/mailman-suite>
- Gudang YunoHost: <https://apps.yunohost.org/app/mailman3>
- Laporkan bug: <https://github.com/YunoHost-Apps/mailman3_ynh/issues>

## Info developer

Silakan kirim pull request ke [`testing` branch](https://github.com/YunoHost-Apps/mailman3_ynh/tree/testing).

Untuk mencoba branch `testing`, silakan dilanjutkan seperti:

```bash
sudo yunohost app install https://github.com/YunoHost-Apps/mailman3_ynh/tree/testing --debug
atau
sudo yunohost app upgrade mailman3 -u https://github.com/YunoHost-Apps/mailman3_ynh/tree/testing --debug
```

**Info lebih lanjut mengenai pemaketan aplikasi:** <https://yunohost.org/packaging_apps>
