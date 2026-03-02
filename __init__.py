from __future__ import annotations

"""Home Assistant integration for indevolt device."""

import logging
from typing import Any

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, ServiceCall
from homeassistant.exceptions import ConfigEntryNotReady, ServiceValidationError
from homeassistant.helpers import device_registry as dr
from .const import DOMAIN, PLATFORMS
from .coordinator import IndevoltDeviceUpdateCoordinator

_LOGGER = logging.getLogger(__name__)

async def async_setup(hass: HomeAssistant, config: dict[str, Any]) -> bool:
    """
    Set up the indevolt integration component.
    This function is called when the integration is added to the Home Assistant configuration.
    """
    hass.data.setdefault(DOMAIN, {})
    if not hass.services.has_service(DOMAIN, "set_solidflex_powerflex_work_mode"):
        _register_services(hass)
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """
    Set up indevolt from a config entry.
    This is the main setup function called when a config entry is added.
    It initializes the coordinator and sets up platforms.
    """
    hass.data.setdefault(DOMAIN, {})
    
    try:
        coordinator = IndevoltDeviceUpdateCoordinator(hass, entry.data)
        # Perform initial data refresh.
        await coordinator.async_config_entry_first_refresh()
        # Store coordinator in hass.data for platform access.
        entry.runtime_data = coordinator

        # Set up all platforms (sensors, switches, etc.).
        await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
        return True 
    
    except Exception as err:
        _LOGGER.exception("Unexpected error occurred while setting config entry.")
        
        # Clean up partially created resources.
        if entry.entry_id in hass.data.get(DOMAIN, {}):
            del hass.data[DOMAIN][entry.entry_id]
        
        raise ConfigEntryNotReady from err

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """
    Unload a config entry and clean up resources.
    This is called when the integration is removed or reloaded.
    """
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    
    if unload_ok:
        coordinator = hass.data[DOMAIN].pop(entry.entry_id)
        await coordinator.async_shutdown()
        
        if not hass.data[DOMAIN]:
            hass.data.pop(DOMAIN)
    
    return unload_ok

def _register_services(hass: HomeAssistant) -> None:
    """Register Indevolt services."""

    async def handle_set_work_mode(call: ServiceCall):

        device_ids = call.data.get("device_id")

        if not device_ids:
            raise ServiceValidationError("No device selected")

        mode: str = call.data["mode"]

        MODE_MAP = {
            "Self-Consumed Prioritized": 1,
            "Real-Time Control": 4,
            "Charge/Discharge Schedule": 5,
        }

        device_registry = dr.async_get(hass)
        
        for device_id in device_ids:

            device = device_registry.async_get(device_id)
            entry_id = next(iter(device.config_entries), None)

            entry = hass.config_entries.async_get_entry(entry_id)
            coordinator = entry.runtime_data
            api = coordinator.api

            await api.set_data(
                point=47005,
                value=[MODE_MAP[mode]],
            )

            if mode == "Real-Time Control":
                state: str = call.data.get("state", "Standby")
                power: int = call.data.get("power", 0)
                soc: int = call.data.get("soc", 5)

                STATE_MAP = {
                    "Standby": 0,
                    "Charging": 1,
                    "Discharging": 2,
                }

                await api.set_data(
                    point=47015,
                    value=[
                        STATE_MAP.get(state),
                        power,
                        soc,
                    ],
                )

            await coordinator.async_request_refresh()

    hass.services.async_register(
        DOMAIN,
        "set_solidflex_powerflex_work_mode",
        handle_set_work_mode,
    )

    hass.services.async_register(
        DOMAIN,
        "set_bk1600_work_mode",
        handle_set_work_mode,
    )
