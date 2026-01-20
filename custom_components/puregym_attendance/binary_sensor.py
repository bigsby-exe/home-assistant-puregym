"""Binary sensor platform for PureGym Attendance."""
from homeassistant.components.binary_sensor import BinarySensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import BINARY_SENSOR
from .const import BINARY_SENSOR_DEVICE_CLASS
from .const import DOMAIN
from .entity import PuregymAttendanceEntity


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities,
) -> None:
    """Setup binary_sensor platform."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_entities(
        [
            PuregymAttendanceBinarySensor(
                coordinator, entry
            )
        ]
    )


class PuregymAttendanceBinarySensor(
    PuregymAttendanceEntity, BinarySensorEntity
):
    """PureGym Attendance binary sensor class."""

    _attr_name = BINARY_SENSOR.replace("_", " ").title()
    _attr_device_class = BINARY_SENSOR_DEVICE_CLASS

    @property
    def is_on(self):
        """Return true if attendance data is available."""
        if self.coordinator.data is None:
            return False
        return self.coordinator.data.get("totalPeopleInGym") is not None
