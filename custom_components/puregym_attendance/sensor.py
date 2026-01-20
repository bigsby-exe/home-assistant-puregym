"""Sensor platform for PureGym Attendance."""
from homeassistant.components.sensor import SensorEntity, SensorStateClass
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import DOMAIN
from .const import ICON
from .const import SENSOR
from .entity import PuregymAttendanceEntity


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities,
) -> None:
    """Setup sensor platform."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_entities(
        [PuregymAttendanceSensor(coordinator, entry)]
    )


class PuregymAttendanceSensor(PuregymAttendanceEntity, SensorEntity):
    """PureGym Attendance Sensor class."""

    _attr_name = SENSOR.capitalize()
    _attr_icon = ICON
    _attr_state_class = SensorStateClass.MEASUREMENT
    _attr_native_unit_of_measurement = "people"

    @property
    def native_value(self):
        """Return the native value of the sensor."""
        if self.coordinator.data is None:
            return None
        return self.coordinator.data.get("totalPeopleInGym")
