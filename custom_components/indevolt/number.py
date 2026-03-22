
from __future__ import annotations

from dataclasses import dataclass
from collections.abc import Awaitable, Callable

from homeassistant.components.number import (
    NumberEntity,
    NumberEntityDescription,
    NumberDeviceClass,
    NumberMode
)
from homeassistant.const import EntityCategory, PERCENTAGE, UnitOfPower


from .indevolt_api import IndevoltAPI
from .coordinator import IndevoltDeviceUpdateCoordinator
from .entity import IndevoltEntity


@dataclass(frozen=True, kw_only=True)
class IndevoltNumberEntityDescription(NumberEntityDescription):
    """Indevolt number entity description."""

    value_fn: Callable[[dict], int | None]
    set_fn: Callable[[IndevoltAPI, int], Awaitable[bool]]


NUMBERS_GEN2 = [
    IndevoltNumberEntityDescription(
        key="backup_soc",
        name="Backup SOC",
        device_class=NumberDeviceClass.BATTERY,
        entity_category=EntityCategory.CONFIG,
        native_min_value=5,
        native_max_value=100,
        native_step=1,
        native_unit_of_measurement=PERCENTAGE,
        value_fn=lambda data: data.get("6105"),
        set_fn=lambda api, value: api.set_data(
            point=1142,
            value=[value],
        ),
    ),
    IndevoltNumberEntityDescription(
        key="inverter_input_limit",
        name="Inverter Input Limit",
        device_class=NumberDeviceClass.POWER,
        entity_category=EntityCategory.CONFIG,
        native_min_value=50,
        native_max_value=2400,
        native_step=1,
        native_unit_of_measurement=UnitOfPower.WATT,
        value_fn=lambda data: data.get("11009"),
        set_fn=lambda api, value: api.set_data(
            point=1138,
            value=[value],
        ),
    ),
    IndevoltNumberEntityDescription(
        key="max_output_power",
        name="Max AC Output Power",
        device_class=NumberDeviceClass.POWER,
        entity_category=EntityCategory.CONFIG,
        native_min_value=50,
        native_max_value=2400,
        native_step=1,
        native_unit_of_measurement=UnitOfPower.WATT,
        value_fn=lambda data: data.get("11011"),
        set_fn=lambda api, value: api.set_data(
            point=1147,
            value=[value],
        ),
    ),
    IndevoltNumberEntityDescription(
        key="feed_in_power_limit",
        name="Feed-in Power Limit",
        device_class=NumberDeviceClass.POWER,
        entity_category=EntityCategory.CONFIG,
        native_min_value=50,
        native_max_value=2400,
        native_step=1,
        native_unit_of_measurement=UnitOfPower.WATT,
        value_fn=lambda data: data.get("11010"),
        set_fn=lambda api, value: api.set_data(
            point=1146,
            value=[value],
        ),
    ),
    IndevoltNumberEntityDescription(
        key="power_setting",
        name="Power (Real-time control)",
        device_class=NumberDeviceClass.POWER,
        entity_category=EntityCategory.CONFIG,
        native_min_value=50,
        native_max_value=2400,
        native_step=1,
        native_unit_of_measurement=UnitOfPower.WATT,
        value_fn=lambda data: None,
        set_fn=lambda api, value: api.set_data(
            point=47016,
            value=[value],
        ),
    ),
    IndevoltNumberEntityDescription(
        key="soc_setting",
        name="Target SOC (Real-time control)",
        device_class=NumberDeviceClass.BATTERY,
        entity_category=EntityCategory.CONFIG,
        native_min_value=5,
        native_max_value=100,
        native_step=1,
        native_unit_of_measurement=PERCENTAGE,
        value_fn=lambda data: None,
        set_fn=lambda api, value: api.set_data(
            point=47017,
            value=[value],
        ),
    ),
]


NUMBERS_GEN1 = [
    IndevoltNumberEntityDescription(
        key="power_setting",
        name="Power (Real-time control)",
        device_class=NumberDeviceClass.POWER,
        entity_category=EntityCategory.CONFIG,
        mode=NumberMode.SLIDER,
        native_min_value=0,
        native_step=1,
        native_unit_of_measurement=UnitOfPower.WATT,
        value_fn=lambda data: None,
        set_fn=lambda api, value: api.set_data(
            point=47016,
            value=[value],
        ),
    ),
    IndevoltNumberEntityDescription(
        key="soc_setting",
        name="Target SOC (Real-time control)",
        device_class=NumberDeviceClass.BATTERY,
        entity_category=EntityCategory.CONFIG,
        native_min_value=0,
        native_max_value=100,
        native_step=1,
        native_unit_of_measurement=PERCENTAGE,
        value_fn=lambda data: None,
        set_fn=lambda api, value: api.set_data(
            point=47017,
            value=[value],
        ),
    ),
]

async def async_setup_entry(hass, entry, async_add_entities):
    if "BK1600" in entry.data.get("device_model"):
        async_add_entities(
            IndevoltNumberEntity(entry.runtime_data, description) for description in NUMBERS_GEN1
        )
    else:
        async_add_entities(
            IndevoltNumberEntity(entry.runtime_data, description) for description in NUMBERS_GEN2
        )


class IndevoltNumberEntity(IndevoltEntity, NumberEntity):
    """Indevolt number entity."""

    def __init__(
        self,
        coordinator: IndevoltDeviceUpdateCoordinator,
        description: IndevoltNumberEntityDescription,
    ) -> None:
        super().__init__(coordinator)
        self.entity_description = description
        self._attr_unique_id = (f"{coordinator.config_entry.unique_id}_{description.key}")


    @property
    def device_info(self):
        return self.device_info_main()

    @property
    def native_max_value(self) -> int:
        if "BK1600" not in self.coordinator.config_entry.data.get("device_model"):
            return self.entity_description.native_max_value
        
        if self.entity_description.key != "power_setting":
            return self.entity_description.native_max_value
        
        state = self.coordinator.data.get("6001")
        if state == 1001:
            return 1200
        else:
            return 800 
    
    @property
    def native_value(self) -> int | None:
        return self.entity_description.value_fn(self.coordinator.data)

    async def async_set_native_value(self, value: int) -> None:
        await self.entity_description.set_fn(self.coordinator.api, value)
        await self.coordinator.async_refresh()

        
