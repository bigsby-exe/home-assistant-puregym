"""Switch platform for PureGym Attendance."""
from homeassistant.components.switch import SwitchEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import DOMAIN
from .const import ICON
from .const import SWITCH
from .entity import PuregymAttendanceEntity


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities,
) -> None:
    """Setup switch platform."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_entities(
        [
            PuregymAttendanceSwitch(
                coordinator, entry
            )
        ]
    )


class PuregymAttendanceSwitch(
    PuregymAttendanceEntity, SwitchEntity
):
    """PureGym Attendance switch class."""

    _attr_name = SWITCH.replace("_", " ").title()
    _attr_icon = ICON

    async def async_turn_on(self, **kwargs):  # pylint: disable=unused-argument
        """Turn on the switch."""
        # Switch functionality not implemented in API
        await self.coordinator.async_request_refresh()

    async def async_turn_off(self, **kwargs):  # pylint: disable=unused-argument
        """Turn off the switch."""
        # Switch functionality not implemented in API
        await self.coordinator.async_request_refresh()

    @property
    def is_on(self):
        """Return true if the switch is on."""
        # Switch functionality not implemented - always return False
        return False
