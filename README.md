# Django-For-Runners for YunoHost

[![Integration level](https://dash.yunohost.org/integration/django-for-runners.svg)](https://dash.yunohost.org/appci/app/django-for-runners) ![](https://ci-apps.yunohost.org/ci/badges/django-for-runners.status.svg) ![](https://ci-apps.yunohost.org/ci/badges/django-for-runners.maintain.svg)
[![Install Django-For-Runners with YunoHost](https://install-app.yunohost.org/install-with-yunohost.png)](https://install-app.yunohost.org/?app=django-for-runners)

> *This package allows you to install Django-For-Runners quickly and simply on a YunoHost server.
If you don't have YunoHost, please consult [the guide](https://yunohost.org/#/install) to learn how to install it.*

Current status is pre-alpha: This app doesn't work, yet ;)

Pull requests welcome ;)

## Overview

Django-For-Runners is a libre web-based management to catalog things including state and location etc. using Python/Django.

## Screenshots

![](https://raw.githubusercontent.com/jedie/jedie.github.io/master/screenshots/django-for-runners/for-runers%20v0.6.0%202018-07-31%20GPX%20Track.png)
![](https://raw.githubusercontent.com/jedie/jedie.github.io/master/screenshots/django-for-runners/for-runners%20v0.4.0%202018-6-26%20GPX%20info.png)
![](https://raw.githubusercontent.com/jedie/jedie.github.io/master/screenshots/django-for-runners/for-runners%20v0.6.0%202018-07-19%20Event%20Costs.png)

## Admin account

An admin user is created at installation, the login is what you provided at installation, the password is **django-for-runners**.

## Settings and upgrades

Almost everything related to Django-For-Runners's configuration is handled in a `"../conf/ynh_for_runners_settings.py"` file.
You can edit the file `$final_path/local_settings.py` to enable or disable features.

# Miscellaneous


## SSO authentication

[SSOwat](https://github.com/YunoHost/SSOwat) is fully supported:

* First user (`$YNH_APP_ARG_ADMIN`) will be created as Django's super user
* All new users will be created as normal users
* Login via SSO is fully supported
* User Email, First / Last name will be updated from SSO data


## Links

 * Report a bug about this package: https://github.com/YunoHost-Apps/django-for-runners_ynh
 * Report a bug about Django-For-Runners itself: https://github.com/jedie/django-for-runners
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
-rw-r--r-- 1 django-for-runners django-for-runners 4737 Dec  8 08:39 ynh_for_runners_settings.py

root@yunohost:~# cd /opt/yunohost/django-for-runners/
root@yunohost:/opt/yunohost/django-for-runners# source venv/bin/activate
(venv) root@yunohost:/opt/yunohost/django-for-runners# ./manage.py check
Django-For-Runners v0.12.0rc2 (Django v2.2.17)
DJANGO_SETTINGS_MODULE='ynh_django-for-runners_settings'
PROJECT_PATH:/opt/yunohost/django-for-runners/venv/lib/python3.7/site-packages
BASE_PATH:/opt/yunohost/django-for-runners
System check identified no issues (0 silenced).

root@yunohost:~# tail -f /var/log/django-for-runners/django-for-runners.log
root@yunohost:~# cat /etc/systemd/system/for_runners.service

root@yunohost:~# systemctl reload-or-restart django-for-runners
root@yunohost:~# journalctl --unit=django-for-runners --follow
```

## local test

For quicker developing of Django-For-Runners in the context of YunoHost app,
it's possible to run the Django developer server with the settings
and urls made for YunoHost installation.

e.g.:
```bash
~$ git clone https://github.com/YunoHost-Apps/django-for-runners_ynh.git
~$ cd django-for-runners_ynh/
~/django-for-runners_ynh$ make
install-poetry         install or update poetry
install                install project via poetry
update                 update the sources and installation
local-test             Run local_test.py to run the project locally
local-diff-settings    Run "manage.py diffsettings" with local test

~/django-for-runners_ynh$ make install-poetry
~/django-for-runners_ynh$ make install
~/django-for-runners_ynh$ make local-test
```

Notes:

* SQlite database will be used
* A super user with username `test` and password `test` is created
* The page is available under `http://127.0.0.1:8000/app_path/`
