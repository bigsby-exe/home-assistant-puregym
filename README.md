# PureGym Attendance

> **Note:** This is a fork of [nckltcha/puregym-attendance](https://github.com/nckltcha/puregym-attendance) with updates and fixes. The original repository is maintained by [@nckltcha](https://github.com/nckltcha).

## What is this?

PureGym Attendance is a Home Assistant custom integration that connects to the PureGym API to display the current number of people at your local gym in real-time. This allows you to:

- Monitor gym occupancy levels
- Create automations based on gym attendance (e.g., avoid peak hours)
- Track attendance patterns over time
- Get notified when the gym is less crowded

The integration provides a sensor that updates every 30 seconds with the current attendance count from your home gym.


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