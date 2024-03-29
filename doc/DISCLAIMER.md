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
root@yunohost:~# systemctl status django-for-runners
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
