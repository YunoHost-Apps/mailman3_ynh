<!--
注意：此 README 由 <https://github.com/YunoHost/apps/tree/master/tools/readme_generator> 自动生成
请勿手动编辑。
-->

# YunoHost 上的 Mailman3

[![集成程度](https://apps.yunohost.org/badge/integration/mailman3)](https://ci-apps.yunohost.org/ci/apps/mailman3/)
![工作状态](https://apps.yunohost.org/badge/state/mailman3)
![维护状态](https://apps.yunohost.org/badge/maintained/mailman3)

[![使用 YunoHost 安装 Mailman3](https://install-app.yunohost.org/install-with-yunohost.svg)](https://install-app.yunohost.org/?app=mailman3)

*[阅读此 README 的其它语言版本。](./ALL_README.md)*

> *通过此软件包，您可以在 YunoHost 服务器上快速、简单地安装 Mailman3。*  
> *如果您还没有 YunoHost，请参阅[指南](https://yunohost.org/install)了解如何安装它。*

## 概况

* Users can just sign up themselves to manage details
* Users can use mailing lists without signing up?

## Limitations

* Migrating from Mailman 2.X is not officially supported, sorry. However, there is a manual and
  which details an experimental process. Please see [the documentation](https://docs.mailman3.org/en/latest/migration.html).

* Mailman3 must be configured to use a root domain (https://myyunohost.org and *not* https://myyunohost.org/mailman3).

* You must have a HTTPS certificate installed on the root domain.

* There may be only one installation per YunoHost.


**分发版本：** 3.3~ynh1

**演示：** <https://lists.mailman3.org/mailman3/lists/>

## 截图

![Mailman3 的截图](./doc/screenshots/screenshot1.webp)

## 文档与资源

- 官方应用网站： <http://www.list.org/>
- 官方用户文档： <http://docs.mailman3.org/en/latest/userguide.html>
- 官方管理文档： <https://docs.mailman3.org/en/latest/>
- 上游应用代码库： <https://gitlab.com/mailman/mailman-suite>
- YunoHost 商店： <https://apps.yunohost.org/app/mailman3>
- 报告 bug： <https://github.com/YunoHost-Apps/mailman3_ynh/issues>

## 开发者信息

请向 [`testing` 分支](https://github.com/YunoHost-Apps/mailman3_ynh/tree/testing) 发送拉取请求。

如要尝试 `testing` 分支，请这样操作：

```bash
sudo yunohost app install https://github.com/YunoHost-Apps/mailman3_ynh/tree/testing --debug
或
sudo yunohost app upgrade mailman3 -u https://github.com/YunoHost-Apps/mailman3_ynh/tree/testing --debug
```

**有关应用打包的更多信息：** <https://yunohost.org/packaging_apps>
