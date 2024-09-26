<!--
Ohart ongi: README hau automatikoki sortu da <https://github.com/YunoHost/apps/tree/master/tools/readme_generator>ri esker
EZ editatu eskuz.
-->

# django-for-runners YunoHost-erako

[![Integrazio maila](https://dash.yunohost.org/integration/django-for-runners.svg)](https://ci-apps.yunohost.org/ci/apps/django-for-runners/) ![Funtzionamendu egoera](https://ci-apps.yunohost.org/ci/badges/django-for-runners.status.svg) ![Mantentze egoera](https://ci-apps.yunohost.org/ci/badges/django-for-runners.maintain.svg)

[![Instalatu django-for-runners YunoHost-ekin](https://install-app.yunohost.org/install-with-yunohost.svg)](https://install-app.yunohost.org/?app=django-for-runners)

*[Irakurri README hau beste hizkuntzatan.](./ALL_README.md)*

> *Pakete honek django-for-runners YunoHost zerbitzari batean azkar eta zailtasunik gabe instalatzea ahalbidetzen dizu.*  
> *YunoHost ez baduzu, kontsultatu [gida](https://yunohost.org/install) nola instalatu ikasteko.*

## Aurreikuspena

[![tests](https://github.com/YunoHost-Apps/django-for-runners_ynh/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/YunoHost-Apps/django-for-runners_ynh/actions/workflows/tests.yml)
[![codecov](https://codecov.io/github/jedie/for_runners_ynh/branch/main/graph/badge.svg)](https://app.codecov.io/github/jedie/for_runners_ynh)
[![for_runners_ynh @ PyPi](https://img.shields.io/pypi/v/for_runners_ynh?label=for_runners_ynh%20%40%20PyPi)](https://pypi.org/project/for_runners_ynh/)
[![Python Versions](https://img.shields.io/pypi/pyversions/for_runners_ynh)](https://github.com/YunoHost-Apps/django-for-runners_ynh/blob/main/pyproject.toml)
[![License GPL-3.0-or-later](https://img.shields.io/pypi/l/for_runners_ynh)](https://github.com/YunoHost-Apps/django-for-runners_ynh/blob/main/LICENSE)

[django-for-runners](https://github.com/jedie/django-for-runners) is a libre web-based management for your GPX tracks of your running (or other sports activity). Used [Python](https://www.python.org/)/[Django](https://www.djangoproject.com/).

Pull requests welcome ;)

This package for YunoHost used [django-yunohost-integration](https://github.com/YunoHost-Apps/django_yunohost_integration)

More screenshots are here: [jedie.github.io/tree/master/screenshots/django-for-runners](https://github.com/jedie/jedie.github.io/tree/master/screenshots/django-for-runners/README.creole)


**Paketatutako bertsioa:** 0.20.0~ynh2

## Pantaila-argazkiak

![django-for-runners(r)en pantaila-argazkia](./doc/screenshots/screenshot.png)

## Dokumentazioa eta baliabideak

- Jatorrizko aplikazioaren kode-gordailua: <https://github.com/jedie/django-for-runners>
- YunoHost Denda: <https://apps.yunohost.org/app/django-for-runners>
- Eman errore baten berri: <https://github.com/YunoHost-Apps/django-for-runners_ynh/issues>

## Garatzaileentzako informazioa

Bidali `pull request`a [`testing` abarrera](https://github.com/YunoHost-Apps/django-for-runners_ynh/tree/testing).

`testing` abarra probatzeko, ondorengoa egin:

```bash
sudo yunohost app install https://github.com/YunoHost-Apps/django-for-runners_ynh/tree/testing --debug
edo
sudo yunohost app upgrade django-for-runners -u https://github.com/YunoHost-Apps/django-for-runners_ynh/tree/testing --debug
```

**Informazio gehiago aplikazioaren paketatzeari buruz:** <https://yunohost.org/packaging_apps>
