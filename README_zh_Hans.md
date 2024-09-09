<!--
注意：此 README 由 <https://github.com/YunoHost/apps/tree/master/tools/readme_generator> 自动生成
请勿手动编辑。
-->

# YunoHost 上的 django-for-runners

[![集成程度](https://dash.yunohost.org/integration/django-for-runners.svg)](https://ci-apps.yunohost.org/ci/apps/django-for-runners/) ![工作状态](https://ci-apps.yunohost.org/ci/badges/django-for-runners.status.svg) ![维护状态](https://ci-apps.yunohost.org/ci/badges/django-for-runners.maintain.svg)

[![使用 YunoHost 安装 django-for-runners](https://install-app.yunohost.org/install-with-yunohost.svg)](https://install-app.yunohost.org/?app=django-for-runners)

*[阅读此 README 的其它语言版本。](./ALL_README.md)*

> *通过此软件包，您可以在 YunoHost 服务器上快速、简单地安装 django-for-runners。*  
> *如果您还没有 YunoHost，请参阅[指南](https://yunohost.org/install)了解如何安装它。*

## 概况

[![tests](https://github.com/YunoHost-Apps/django-for-runners_ynh/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/YunoHost-Apps/django-for-runners_ynh/actions/workflows/tests.yml)
[![codecov](https://codecov.io/github/jedie/for_runners_ynh/branch/main/graph/badge.svg)](https://app.codecov.io/github/jedie/for_runners_ynh)
[![for_runners_ynh @ PyPi](https://img.shields.io/pypi/v/for_runners_ynh?label=for_runners_ynh%20%40%20PyPi)](https://pypi.org/project/for_runners_ynh/)
[![Python Versions](https://img.shields.io/pypi/pyversions/for_runners_ynh)](https://github.com/YunoHost-Apps/django-for-runners_ynh/blob/main/pyproject.toml)
[![License GPL-3.0-or-later](https://img.shields.io/pypi/l/for_runners_ynh)](https://github.com/YunoHost-Apps/django-for-runners_ynh/blob/main/LICENSE)

[django-for-runners](https://github.com/jedie/django-for-runners) is a libre web-based management for your GPX tracks of your running (or other sports activity). Used [Python](https://www.python.org/)/[Django](https://www.djangoproject.com/).

Pull requests welcome ;)

This package for YunoHost used [django-yunohost-integration](https://github.com/YunoHost-Apps/django_yunohost_integration)

More screenshots are here: [jedie.github.io/tree/master/screenshots/django-for-runners](https://github.com/jedie/jedie.github.io/tree/master/screenshots/django-for-runners/README.creole)


**分发版本：** 0.20.0~ynh2

## 截图

![django-for-runners 的截图](./doc/screenshots/screenshot.png)

## 文档与资源

- 上游应用代码库： <https://github.com/jedie/django-for-runners>
- YunoHost 商店： <https://apps.yunohost.org/app/django-for-runners>
- 报告 bug： <https://github.com/YunoHost-Apps/django-for-runners_ynh/issues>

## 开发者信息

请向 [`testing` 分支](https://github.com/YunoHost-Apps/django-for-runners_ynh/tree/testing) 发送拉取请求。

如要尝试 `testing` 分支，请这样操作：

```bash
sudo yunohost app install https://github.com/YunoHost-Apps/django-for-runners_ynh/tree/testing --debug
或
sudo yunohost app upgrade django-for-runners -u https://github.com/YunoHost-Apps/django-for-runners_ynh/tree/testing --debug
```

**有关应用打包的更多信息：** <https://yunohost.org/packaging_apps>
