"""Constants for PureGym Attendance."""
# Base component constants
NAME = "PureGym Attendance"
DOMAIN = "puregym_attendance"
DOMAIN_DATA = f"{DOMAIN}_data"
VERSION = "0.0.2"

ATTRIBUTION = "Data provided by PureGym"
ISSUE_URL = "https://github.com/bigsby-exe/home-assistant-puregym/issues"

# Icons
ICON = "mdi:account-group"

# Device classes
BINARY_SENSOR_DEVICE_CLASS = "connectivity"

# Platforms
BINARY_SENSOR = "binary_sensor"
SENSOR = "sensor"
SWITCH = "switch"

PLATFORMS = [BINARY_SENSOR, SENSOR, SWITCH]

# Configuration and options
CONF_ENABLED = "enabled"
CONF_USERNAME = "username"
CONF_PASSWORD = "password"

# Defaults
DEFAULT_NAME = DOMAIN


STARTUP_MESSAGE = f"""
-------------------------------------------------------------------
{NAME}
Version: {VERSION}
This is a custom integration!
If you have any issues with this you need to open an issue here:
{ISSUE_URL}
-------------------------------------------------------------------
"""
