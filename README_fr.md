# django-for-runners pour YunoHost

[![Niveau d'intégration](https://dash.yunohost.org/integration/django-for-runners.svg)](https://dash.yunohost.org/appci/app/django-for-runners) ![](https://ci-apps.yunohost.org/ci/badges/django-for-runners.status.svg) ![](https://ci-apps.yunohost.org/ci/badges/django-for-runners.maintain.svg)
[![Installer django-for-runners avec YunoHost](https://install-app.yunohost.org/install-with-yunohost.svg)](https://install-app.yunohost.org/?app=django-for-runners)

*[Read this readme in english.](./README.md)*
*[Lire ce readme en français.](./README_fr.md)*

> *Ce package vous permet d'installer django-for-runners rapidement et simplement sur un serveur YunoHost.
Si vous n'avez pas YunoHost, regardez [ici](https://yunohost.org/#/install) pour savoir comment l'installer et en profiter.*

## Vue d'ensemble

![Logo](https://raw.githubusercontent.com/jedie/django-for-runners/main/src/for_runners/static/Django-ForRunners128.png)

[django-for-runners](https://github.com/jedie/django-for-runners) is a libre web-based management for your GPX tracks of your running (or other sports activity). Used [Python](https://www.python.org/)/[Django](https://www.djangoproject.com/).


[![pytest](https://github.com/YunoHost-Apps/django-for-runners_ynh/actions/workflows/pytest.yml/badge.svg?branch=master)](https://github.com/YunoHost-Apps/django-for-runners_ynh/actions/workflows/pytest.yml) [![YunoHost apps package linter](https://github.com/YunoHost-Apps/django-for-runners_ynh/actions/workflows/package_linter.yml/badge.svg)](https://github.com/YunoHost-Apps/django-for-runners_ynh/actions/workflows/package_linter.yml) [![Coverage Status on codecov.io](https://codecov.io/gh/YunoHost-Apps/django-for-runners_ynh/branch/master/graph/badge.svg)](https://codecov.io/gh/YunoHost-Apps/django-for-runners_ynh)

![django-for-runners @ PyPi](https://img.shields.io/pypi/v/django-for-runners?label=django-for-runners%20%40%20PyPi)
![Python Versions](https://img.shields.io/pypi/pyversions/django-for-runners)
![License GPL V3+](https://img.shields.io/pypi/l/django-for-runners)

Pull requests welcome ;)

This package for YunoHost used [django-yunohost-integration](https://github.com/YunoHost-Apps/django_yunohost_integration)

More screenshots are here: [jedie.github.io/tree/master/screenshots/django-for-runners](https://github.com/jedie/jedie.github.io/tree/master/screenshots/django-for-runners/README.creole)


**Version incluse :** 0.13.0rc1~ynh1



## Captures d'écran

![](./doc/screenshots/for_runers_v060_2018_07_31_gpx_track.png)
![](./doc/screenshots/for_runners_v060_2018_07_19_event_costs.png)
![](./doc/screenshots/for_runners_v040_2018_6_26_gpx_info.png)

## Avertissements / informations importantes

## Settings and upgrades

Almost everything related to django-for-runners's configuration is handled in a `"../conf/settings.py"` file.
You can edit the file `/opt/yunohost/django-for-runners/local_settings.py` to enable or disable features.

Test sending emails:

```bash
ssh admin@yourdomain.tld
root@yunohost:~# cd /opt/yunohost/django-for-runners/
root@yunohost:/opt/yunohost/django-for-runners# source venv/bin/activate
(venv) root@yunohost:/opt/yunohost/django-for-runners# ./manage.py sendtestemail --admins
```

Background info: Error mails are send to all [settings.ADMINS](https://docs.djangoproject.com/en/2.2/ref/settings/#std:setting-ADMINS). By default the YunoHost admin is inserted here.
To check current ADMINS run:

```bash
(venv) root@yunohost:/opt/yunohost/django-for-runners# ./manage.py sendtestemail --admins
```

If you prefere to send error emails to a extrnal email address, just do something like this:

```bash
echo "ADMINS = (('Your Name', 'example@domain.tld'),)" >> /opt/yunohost/django-for-runners/local_settings.py
```

To check the effective settings, run this:
```bash
(venv) root@yunohost:/opt/yunohost/django-for-runners# ./manage.py diffsettings
```


# Miscellaneous


## SSO authentication

[SSOwat](https://github.com/YunoHost/SSOwat) is fully supported via [django_ynh](https://github.com/YunoHost-Apps/django_ynh):

* First user (`$YNH_APP_ARG_ADMIN`) will be created as Django's super user
* All new users will be created as normal users
* Login via SSO is fully supported
* User Email, First / Last name will be updated from SSO data


## Links

 * Report a bug about this package: https://github.com/YunoHost-Apps/django-for-runners_ynh
 * Report a bug about django-for-runners itself: https://github.com/jedie/django-for-runners
 * YunoHost website: https://yunohost.org/

---

# Developer info

## package installation / debugging

Please send your pull request to https://github.com/YunoHost-Apps/django-for-runners_ynh

Try 'main' branch, e.g.:
```bash
sudo yunohost app install https://github.com/YunoHost-Apps/django-for-runners_ynh/tree/master --debug
or
sudo yunohost app upgrade django-for-runners -u https://github.com/YunoHost-Apps/django-for-runners_ynh/tree/master --debug
```

Try 'testing' branch, e.g.:
```bash
sudo yunohost app install https://github.com/YunoHost-Apps/django-for-runners_ynh/tree/testing --debug
or
sudo yunohost app upgrade django-for-runners -u https://github.com/YunoHost-Apps/django-for-runners_ynh/tree/testing --debug
```

To remove call e.g.:
```bash
sudo yunohost app remove django-for-runners
```

Backup / remove / restore cycle, e.g.:
```bash
yunohost backup create --apps django-for-runners
yunohost backup list
archives:
  - django-for-runners-pre-upgrade1
  - 20201223-163434
yunohost app remove django-for-runners
yunohost backup restore 20201223-163434 --apps django-for-runners
```

Debug installation, e.g.:
```bash
root@yunohost:~# ls -la /var/www/django-for-runners/
total 18
drwxr-xr-x 4 root root 4 Dec  8 08:36 .
drwxr-xr-x 6 root root 6 Dec  8 08:36 ..
drwxr-xr-x 2 root root 2 Dec  8 08:36 media
drwxr-xr-x 7 root root 8 Dec  8 08:40 static

root@yunohost:~# ls -la /opt/yunohost/django-for-runners/
total 58
drwxr-xr-x 5 django-for-runners django-for-runners   11 Dec  8 08:39 .
drwxr-xr-x 3 root        root           3 Dec  8 08:36 ..
-rw-r--r-- 1 django-for-runners django-for-runners  460 Dec  8 08:39 gunicorn.conf.py
-rw-r--r-- 1 django-for-runners django-for-runners    0 Dec  8 08:39 local_settings.py
-rwxr-xr-x 1 django-for-runners django-for-runners  274 Dec  8 08:39 manage.py
-rw-r--r-- 1 django-for-runners django-for-runners  171 Dec  8 08:39 secret.txt
drwxr-xr-x 6 django-for-runners django-for-runners    6 Dec  8 08:37 venv
-rw-r--r-- 1 django-for-runners django-for-runners  115 Dec  8 08:39 wsgi.py
-rw-r--r-- 1 django-for-runners django-for-runners 4737 Dec  8 08:39 settings.py

root@yunohost:~# cd /opt/yunohost/django-for-runners/
root@yunohost:/opt/yunohost/django-for-runners# source venv/bin/activate
(venv) root@yunohost:/opt/yunohost/django-for-runners# ./manage.py check
django-for-runners v0.8.2 (Django v2.2.17)
DJANGO_SETTINGS_MODULE='settings'
PROJECT_PATH:/opt/yunohost/django-for-runners/venv/lib/python3.7/site-packages
BASE_PATH:/opt/yunohost/django-for-runners
System check identified no issues (0 silenced).

root@yunohost:~# tail -f /var/log/django-for-runners/django-for-runners.log
root@yunohost:~# cat /etc/systemd/system/django-for-runners.service

root@yunohost:~# systemctl reload-or-restart django-for-runners
root@yunohost:~# journalctl --unit=for_runners --follow
```

## local test

For quicker developing of django-for-runners in the context of YunoHost app,
it's possible to run the Django developer server with the settings
and urls made for YunoHost installation.

e.g.:
```bash
~$ git clone https://github.com/YunoHost-Apps/django-for-runners_ynh.git
~$ cd django-for-runners_ynh/
~/django-for-runners_ynh$ make
install-poetry         install or update poetry
install                install django-for-runners via poetry
update                 update the sources and installation
local-test             Run local_test.py to run django-for-runners_ynh locally
~/django-for-runners_ynh$ make install-poetry
~/django-for-runners_ynh$ make install
~/django-for-runners_ynh$ make local-test
```

Notes:

* SQlite database will be used
* A super user with username `test` and password `test` is created
* The page is available under `http://127.0.0.1:8000/app_path/`

## Documentations et ressources

* Site officiel de l'app : https://github.com/jedie/django-for-runners
* Dépôt de code officiel de l'app : https://github.com/jedie/django-for-runners
* Documentation YunoHost pour cette app : https://yunohost.org/app_django-for-runners
* Signaler un bug : https://github.com/YunoHost-Apps/django-for-runners_ynh/issues

## Informations pour les développeurs

Merci de faire vos pull request sur la [branche testing](https://github.com/YunoHost-Apps/django-for-runners_ynh/tree/testing).

Pour essayer la branche testing, procédez comme suit.
```
sudo yunohost app install https://github.com/YunoHost-Apps/django-for-runners_ynh/tree/testing --debug
ou
sudo yunohost app upgrade django-for-runners -u https://github.com/YunoHost-Apps/django-for-runners_ynh/tree/testing --debug
```

**Plus d'infos sur le packaging d'applications :** https://yunohost.org/packaging_apps
