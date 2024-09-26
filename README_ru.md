<!--
Важно: этот README был автоматически сгенерирован <https://github.com/YunoHost/apps/tree/master/tools/readme_generator>
Он НЕ ДОЛЖЕН редактироваться вручную.
-->

# django-for-runners для YunoHost

[![Уровень интеграции](https://dash.yunohost.org/integration/django-for-runners.svg)](https://ci-apps.yunohost.org/ci/apps/django-for-runners/) ![Состояние работы](https://ci-apps.yunohost.org/ci/badges/django-for-runners.status.svg) ![Состояние сопровождения](https://ci-apps.yunohost.org/ci/badges/django-for-runners.maintain.svg)

[![Установите django-for-runners с YunoHost](https://install-app.yunohost.org/install-with-yunohost.svg)](https://install-app.yunohost.org/?app=django-for-runners)

*[Прочтите этот README на других языках.](./ALL_README.md)*

> *Этот пакет позволяет Вам установить django-for-runners быстро и просто на YunoHost-сервер.*  
> *Если у Вас нет YunoHost, пожалуйста, посмотрите [инструкцию](https://yunohost.org/install), чтобы узнать, как установить его.*

## Обзор

[![tests](https://github.com/YunoHost-Apps/django-for-runners_ynh/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/YunoHost-Apps/django-for-runners_ynh/actions/workflows/tests.yml)
[![codecov](https://codecov.io/github/jedie/for_runners_ynh/branch/main/graph/badge.svg)](https://app.codecov.io/github/jedie/for_runners_ynh)
[![for_runners_ynh @ PyPi](https://img.shields.io/pypi/v/for_runners_ynh?label=for_runners_ynh%20%40%20PyPi)](https://pypi.org/project/for_runners_ynh/)
[![Python Versions](https://img.shields.io/pypi/pyversions/for_runners_ynh)](https://github.com/YunoHost-Apps/django-for-runners_ynh/blob/main/pyproject.toml)
[![License GPL-3.0-or-later](https://img.shields.io/pypi/l/for_runners_ynh)](https://github.com/YunoHost-Apps/django-for-runners_ynh/blob/main/LICENSE)

[django-for-runners](https://github.com/jedie/django-for-runners) is a libre web-based management for your GPX tracks of your running (or other sports activity). Used [Python](https://www.python.org/)/[Django](https://www.djangoproject.com/).

Pull requests welcome ;)

This package for YunoHost used [django-yunohost-integration](https://github.com/YunoHost-Apps/django_yunohost_integration)

More screenshots are here: [jedie.github.io/tree/master/screenshots/django-for-runners](https://github.com/jedie/jedie.github.io/tree/master/screenshots/django-for-runners/README.creole)


**Поставляемая версия:** 0.20.0~ynh2

## Снимки экрана

![Снимок экрана django-for-runners](./doc/screenshots/screenshot.png)

## Документация и ресурсы

- Репозиторий кода главной ветки приложения: <https://github.com/jedie/django-for-runners>
- Магазин YunoHost: <https://apps.yunohost.org/app/django-for-runners>
- Сообщите об ошибке: <https://github.com/YunoHost-Apps/django-for-runners_ynh/issues>

## Информация для разработчиков

Пришлите Ваш запрос на слияние в [ветку `testing`](https://github.com/YunoHost-Apps/django-for-runners_ynh/tree/testing).

Чтобы попробовать ветку `testing`, пожалуйста, сделайте что-то вроде этого:

```bash
sudo yunohost app install https://github.com/YunoHost-Apps/django-for-runners_ynh/tree/testing --debug
или
sudo yunohost app upgrade django-for-runners -u https://github.com/YunoHost-Apps/django-for-runners_ynh/tree/testing --debug
```

**Больше информации о пакетировании приложений:** <https://yunohost.org/packaging_apps>
