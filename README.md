# PureGym Attendance

> **Note:** This is a fork of [nckltcha/puregym-attendance](https://github.com/nckltcha/puregym-attendance) with updates and fixes. The original repository is maintained by [@nckltcha](https://github.com/nckltcha).

[![GitHub Release][releases-shield]][releases]
[![GitHub Activity][commits-shield]][commits]
[![License][license-shield]](LICENSE)

[![pre-commit][pre-commit-shield]][pre-commit]
[![Black][black-shield]][black]

[![hacs][hacsbadge]][hacs]
[![Project Maintenance][maintenance-shield]][user_profile]
[![BuyMeCoffee][buymecoffeebadge]][buymecoffee]

[![Discord][discord-shield]][discord]
[![Community Forum][forum-shield]][forum]

## What is this?

PureGym Attendance is a Home Assistant custom integration that connects to the PureGym API to display the current number of people at your local gym in real-time. This allows you to:

- Monitor gym occupancy levels
- Create automations based on gym attendance (e.g., avoid peak hours)
- Track attendance patterns over time
- Get notified when the gym is less crowded

The integration provides a sensor that updates every 30 seconds with the current attendance count from your home gym.

![example][exampleimg]

## Installation

### Option 1: Install via HACS (Recommended)

1. Make sure you have [HACS](https://hacs.xyz) installed in your Home Assistant instance
2. In HACS, go to **Integrations**
3. Click the three dots (⋮) in the top right corner and select **Custom repositories**
4. Add this repository URL: `https://github.com/bigsby-exe/home-assistant-puregym`
5. Select **Integration** as the category
6. Click **Add**
7. Search for "PureGym Attendance" in HACS and click **Download**
8. Restart Home Assistant
9. Go to **Settings** → **Devices & Services** → **Add Integration**
10. Search for "PureGym Attendance" and follow the setup wizard

### Option 2: Manual Installation

1. Open your Home Assistant configuration directory (where `configuration.yaml` is located)
2. If you don't have a `custom_components` folder, create it
3. Create a folder called `puregym_attendance` inside `custom_components`
4. Download all files from the `custom_components/puregym_attendance/` directory in this repository
5. Place all downloaded files in the `custom_components/puregym_attendance/` folder you created
6. Restart Home Assistant
7. Go to **Settings** → **Devices & Services** → **Add Integration**
8. Search for "PureGym Attendance" and follow the setup wizard

Your folder structure should look like this:

```text
config/
└── custom_components/
    └── puregym_attendance/
        ├── __init__.py
        ├── api.py
        ├── config_flow.py
        ├── const.py
        ├── entity.py
        ├── manifest.json
        ├── sensor.py
        └── ... (other files)
```

## Configuration

Configuration is done entirely through the Home Assistant UI:

1. Go to **Settings** → **Devices & Services**
2. Click **Add Integration** and search for "PureGym Attendance"
3. Enter your PureGym username and password
4. The integration will automatically detect your home gym and start monitoring attendance

**Note:** Your PureGym credentials are stored securely in Home Assistant and are only used to authenticate with the PureGym API.

<!---->

## Contributions are welcome!

If you want to contribute to this please read the [Contribution guidelines](CONTRIBUTING.md)

## Credits

This project is a fork of [nckltcha/puregym-attendance](https://github.com/nckltcha/puregym-attendance), originally created by [@nckltcha](https://github.com/nckltcha). If you find this integration useful, consider supporting the original author: [Buy Me a Coffee][buymecoffee]

The original project was generated from [@oncleben31](https://github.com/oncleben31)'s [Home Assistant Custom Component Cookiecutter](https://github.com/oncleben31/cookiecutter-homeassistant-custom-component) template.

Code template was mainly taken from [@Ludeeus](https://github.com/ludeeus)'s [integration_blueprint][integration_blueprint] template

---

[integration_blueprint]: https://github.com/custom-components/integration_blueprint
[black]: https://github.com/psf/black
[black-shield]: https://img.shields.io/badge/code%20style-black-000000.svg?style=for-the-badge
[buymecoffee]: https://www.buymeacoffee.com/nckltcha
[buymecoffeebadge]: https://img.shields.io/badge/buy%20me%20a%20coffee-donate-yellow.svg?style=for-the-badge
[commits-shield]: https://img.shields.io/github/commit-activity/y/bigsby-exe/home-assistant-puregym.svg?style=for-the-badge
[commits]: https://github.com/bigsby-exe/home-assistant-puregym/commits/main
[hacs]: https://hacs.xyz
[hacsbadge]: https://img.shields.io/badge/HACS-Custom-orange.svg?style=for-the-badge
[discord]: https://discord.gg/Qa5fW2R
[discord-shield]: https://img.shields.io/discord/330944238910963714.svg?style=for-the-badge
[exampleimg]: example.png
[forum-shield]: https://img.shields.io/badge/community-forum-brightgreen.svg?style=for-the-badge
[forum]: https://community.home-assistant.io/
[license-shield]: https://img.shields.io/github/license/bigsby-exe/home-assistant-puregym.svg?style=for-the-badge
[maintenance-shield]: https://img.shields.io/badge/maintainer-%40bigsby--exe-blue.svg?style=for-the-badge
[pre-commit]: https://github.com/pre-commit/pre-commit
[pre-commit-shield]: https://img.shields.io/badge/pre--commit-enabled-brightgreen?style=for-the-badge
[releases-shield]: https://img.shields.io/github/release/bigsby-exe/home-assistant-puregym.svg?style=for-the-badge
[releases]: https://github.com/bigsby-exe/home-assistant-puregym/releases
[user_profile]: https://github.com/bigsby-exe
