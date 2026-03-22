from homeassistant.components.sensor import SensorEntity, SensorDeviceClass, SensorEntityDescription, SensorStateClass
from homeassistant.helpers.entity import EntityCategory
from dataclasses import dataclass
from collections.abc import Callable
from typing import Final
from homeassistant.const import (
    UnitOfEnergy,
    UnitOfPower,
    UnitOfFrequency,
    UnitOfElectricCurrent,
    UnitOfTemperature,
    UnitOfElectricPotential,
    PERCENTAGE
)
from .entity import IndevoltEntity


@dataclass(frozen=True, kw_only=True)
class IndevoltSensorEntityDescription(SensorEntityDescription):
    """Custom entity description class for Indevolt sensors."""
    name: str = ""
    value_fn: Callable[[str], float | int | str | None] = lambda value: value
    entity_category: EntityCategory | None = None

SENSORS_GEN1: Final = (
    IndevoltSensorEntityDescription(
        key="1664",
        name="DC Input Power1",
        native_unit_of_measurement=UnitOfPower.WATT,
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT
    ),
    IndevoltSensorEntityDescription(
        key="1665",
        name="DC Input Power2",
        native_unit_of_measurement=UnitOfPower.WATT,
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT
    ),
    IndevoltSensorEntityDescription(
        key="2108",
        name="Total AC Output Power",
        native_unit_of_measurement=UnitOfPower.WATT,
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT
    ),
    IndevoltSensorEntityDescription(
        key="1502",
        name="Daily Production",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING
    ),
    IndevoltSensorEntityDescription(
        key="1505",
        name="Cumulative Production",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
        value_fn=lambda value: value * 0.001
    ),
    IndevoltSensorEntityDescription(
        key="2101",
        name="Total AC Input Power",
        native_unit_of_measurement=UnitOfPower.WATT,
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT
    ),
    IndevoltSensorEntityDescription(
        key="2107",
        name="Total AC Input Energy",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING
    ),
    IndevoltSensorEntityDescription(
        key="1501",
        name="Total DC Output Power",
        native_unit_of_measurement=UnitOfPower.WATT,
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT
    ),
    IndevoltSensorEntityDescription(
        key="6000",
        name="Battery Power",
        native_unit_of_measurement=UnitOfPower.WATT,
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT
    ),
    IndevoltSensorEntityDescription(
        key="6002",
        name="Battery SOC",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.BATTERY,
        state_class=SensorStateClass.MEASUREMENT
    ),
    IndevoltSensorEntityDescription(
        key="6105",
        name="Emergency power supply",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.BATTERY,
        state_class=SensorStateClass.MEASUREMENT
    ),
    IndevoltSensorEntityDescription(
        key="6004",
        name="Battery Daily Charging Energy",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING
    ),
    IndevoltSensorEntityDescription(
        key="6005",
        name="Battery Daily Discharging Energy",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING
    ),
    IndevoltSensorEntityDescription(
        key="6006",
        name="Battery Total Charging Energy",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING
    ),
    IndevoltSensorEntityDescription(
        key="6007",
        name="Battery Total Discharging Energy",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING
    ),
    IndevoltSensorEntityDescription(
        key="21028",
        name="Meter Power",
        native_unit_of_measurement=UnitOfPower.WATT,
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT
    ),
    IndevoltSensorEntityDescription(
        key="7101",
        name="Working mode",
        device_class=SensorDeviceClass.ENUM,
        entity_category=EntityCategory.DIAGNOSTIC,
        value_fn=lambda value: {
            0: "Outdoor Portable",
            1: "Self-consumed Prioritized",
            4: "Real-Time Control",
            5: "Charge/Discharge Schedule"
        }.get(value)
    ),
    IndevoltSensorEntityDescription(
        key="6001",
        name="Battery Charge/Discharge State",
        device_class=SensorDeviceClass.ENUM,
        entity_category=EntityCategory.DIAGNOSTIC,
        value_fn=lambda value: {
            1000: "Static",
            1001: "Charging",
            1002: "Discharging"
        }.get(value)
    ),
    IndevoltSensorEntityDescription(
        key="7120",
        name="Meter Connection Status",
        device_class=SensorDeviceClass.ENUM,
        entity_category=EntityCategory.DIAGNOSTIC,
        value_fn=lambda value: {
            1000: "ON",
            1001: "OFF"
        }.get(value)
    ),
)

SENSORS_GEN2: Final = (
    # Firmware Version Information
    IndevoltSensorEntityDescription(
        key="1118",	
        name="Firmware PG2000Series EMS",
        entity_category=EntityCategory.DIAGNOSTIC,
        value_fn=lambda value: format_firmware_version(version=value)
    ),
    IndevoltSensorEntityDescription(
        key="1109",	
        name="Firmware PG2000Series BMS-MB",
        entity_category=EntityCategory.DIAGNOSTIC,
        value_fn=lambda value: format_firmware_version(version=value)
    ),
    IndevoltSensorEntityDescription(
        key="1119",	
        name="Firmware PG2000Series PCS",
        entity_category=EntityCategory.DIAGNOSTIC,
        value_fn=lambda value: format_firmware_version(version=value)
    ),
    IndevoltSensorEntityDescription(
        key="1120",	
        name="Firmware PG2000Series DCDC",
        entity_category=EntityCategory.DIAGNOSTIC,
        value_fn=lambda value: format_firmware_version(version=value)
    ),
    # System Operating Information
    IndevoltSensorEntityDescription(
        key="142",
        name="Rated Capacity",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING
    ),
    IndevoltSensorEntityDescription(
        key="2101",
        name="Total AC Input Power",
        native_unit_of_measurement=UnitOfPower.WATT,
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT
    ),
    IndevoltSensorEntityDescription(
        key="2108",
        name="Total AC Output Power",
        native_unit_of_measurement=UnitOfPower.WATT,
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT
    ),
    # Cluster Information
    IndevoltSensorEntityDescription(
        key="606",
        name="Master-Slave Identification",
        device_class=SensorDeviceClass.ENUM,
        entity_category=EntityCategory.DIAGNOSTIC,
        value_fn=lambda value: {
            "1000": "Master",
            "1001": "Slave",
            "1002": "None"
        }.get(value)
    ),
    # Bypass Power
    IndevoltSensorEntityDescription(
        key="667",
        name="Bypass Power",
        native_unit_of_measurement=UnitOfPower.WATT,
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT
    ),
    # Electrical Energy Information
    IndevoltSensorEntityDescription(
        key="2107",
        name="Total AC Input Energy",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING
    ),
    IndevoltSensorEntityDescription(
        key="2104",
        name="Total AC Output Energy",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING
    ),
    IndevoltSensorEntityDescription(
        key="2105",
        name="Off-grid Output Energy",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING
    ),
    IndevoltSensorEntityDescription(
        key="11034",
        name="Bypass Input Energy",
        native_unit_of_measurement=UnitOfEnergy.WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING
    ),
    IndevoltSensorEntityDescription(
        key="1502",
        name="Daily Production",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING
    ),
    IndevoltSensorEntityDescription(
        key="6004",
        name="Battery Daily Charging Energy",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING
    ),
    IndevoltSensorEntityDescription(
        key="6005",
        name="Battery Daily Discharging Energy",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING
    ),
    IndevoltSensorEntityDescription(
        key="6006",
        name="Battery Total Charging Energy",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING
    ),
    IndevoltSensorEntityDescription(
        key="6007",
        name="Battery Total Discharging Energy",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING
    ),
    # Electricity Meter Status
    IndevoltSensorEntityDescription(
        key="7120",
        name="Meter Connection Status",
        device_class=SensorDeviceClass.ENUM,
        entity_category=EntityCategory.DIAGNOSTIC,
        value_fn=lambda value: {
            1000: "ON",
            1001: "OFF"
        }.get(value)
    ),
    IndevoltSensorEntityDescription(
        key="11016",
        name="Meter Power",
        native_unit_of_measurement=UnitOfPower.WATT,
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT
    ),
    # Grid Information
    IndevoltSensorEntityDescription(
        key="2600",
        name="Grid Voltage",
        native_unit_of_measurement=UnitOfElectricPotential.VOLT,
        device_class=SensorDeviceClass.VOLTAGE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    IndevoltSensorEntityDescription(
        key="2612",
        name="Grid Frequency",
        native_unit_of_measurement=UnitOfFrequency.HERTZ,
        device_class=SensorDeviceClass.FREQUENCY,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    # Battery Pack Operating Parameters
    IndevoltSensorEntityDescription(
        key="6000",
        name="Battery Power",
        native_unit_of_measurement=UnitOfPower.WATT,
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT
    ),
    IndevoltSensorEntityDescription(
        key="6002",
        name="Battery SOC Total",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.BATTERY,
        state_class=SensorStateClass.MEASUREMENT
    ),
    IndevoltSensorEntityDescription(
        key="9008",
        name="Battery SN-MB",
        entity_category=EntityCategory.DIAGNOSTIC,
    ),
    IndevoltSensorEntityDescription(
        key="9000",
        name="Battery SOC-MB",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.BATTERY,
        state_class=SensorStateClass.MEASUREMENT
    ),
    IndevoltSensorEntityDescription(
        key="9004",
        name="Battery V-MB",
        native_unit_of_measurement=UnitOfElectricPotential.VOLT,
        device_class=SensorDeviceClass.VOLTAGE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    IndevoltSensorEntityDescription(
        key="9013",
        name="Battery I-MB",
        native_unit_of_measurement=UnitOfElectricCurrent.AMPERE,
        device_class=SensorDeviceClass.CURRENT,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    IndevoltSensorEntityDescription(
        key="9012",
        name="Battery Temp-MB",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    IndevoltSensorEntityDescription(
        key="9009",
        name="Battery Cell1 V-MB",
        native_unit_of_measurement=UnitOfElectricPotential.VOLT,
        device_class=SensorDeviceClass.VOLTAGE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    IndevoltSensorEntityDescription(
        key="9011",
        name="Battery Cell2 V-MB",
        native_unit_of_measurement=UnitOfElectricPotential.VOLT,
        device_class=SensorDeviceClass.VOLTAGE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    # PV Operating Parameters
    IndevoltSensorEntityDescription(
        key="1501",
        name="Total DC Output Power",
        native_unit_of_measurement=UnitOfPower.WATT,
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT
    ),
    IndevoltSensorEntityDescription(
        key="1632",
        name="DC Input Current 1",
        native_unit_of_measurement=UnitOfElectricCurrent.AMPERE,
        device_class=SensorDeviceClass.CURRENT,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    IndevoltSensorEntityDescription(
        key="1600",
        name="DC Input Voltage 1",
        native_unit_of_measurement=UnitOfElectricPotential.VOLT,
        device_class=SensorDeviceClass.VOLTAGE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    IndevoltSensorEntityDescription(
        key="1664",
        name="DC Input Power 1",
        native_unit_of_measurement=UnitOfPower.WATT,
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT
    ),
    IndevoltSensorEntityDescription(
        key="1633",
        name="DC Input Current 2",
        native_unit_of_measurement=UnitOfElectricCurrent.AMPERE,
        device_class=SensorDeviceClass.CURRENT,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    IndevoltSensorEntityDescription(
        key="1601",
        name="DC Input Voltage 2",
        native_unit_of_measurement=UnitOfElectricPotential.VOLT,
        device_class=SensorDeviceClass.VOLTAGE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    IndevoltSensorEntityDescription(
        key="1665",
        name="DC Input Power 2",
        native_unit_of_measurement=UnitOfPower.WATT,
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT
    ),
    IndevoltSensorEntityDescription(
        key="1634",
        name="DC Input Current 3",
        native_unit_of_measurement=UnitOfElectricCurrent.AMPERE,
        device_class=SensorDeviceClass.CURRENT,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    IndevoltSensorEntityDescription(
        key="1602",
        name="DC Input Voltage 3",
        native_unit_of_measurement=UnitOfElectricPotential.VOLT,
        device_class=SensorDeviceClass.VOLTAGE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    IndevoltSensorEntityDescription(
        key="1666",
        name="DC Input Power 3",
        native_unit_of_measurement=UnitOfPower.WATT,
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT
    ),
    IndevoltSensorEntityDescription(
        key="1635",
        name="DC Input Current 4",
        native_unit_of_measurement=UnitOfElectricCurrent.AMPERE,
        device_class=SensorDeviceClass.CURRENT,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    IndevoltSensorEntityDescription(
        key="1603",
        name="DC Input Voltage 4",
        native_unit_of_measurement=UnitOfElectricPotential.VOLT,
        device_class=SensorDeviceClass.VOLTAGE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    IndevoltSensorEntityDescription(
        key="1667",
        name="DC Input Power 4",
        native_unit_of_measurement=UnitOfPower.WATT,
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT
    )
)

BATTERY_PACK1_SENSORS = {
    IndevoltSensorEntityDescription(
        key="1136",	
        name="Firmware SFA/PFA DCDC1",
        entity_category=EntityCategory.DIAGNOSTIC,
        value_fn=lambda value: format_firmware_version(version=value)
    ),
    IndevoltSensorEntityDescription(
        key="1137",	
        name="Firmware SFA/PFA BMS1",
        entity_category=EntityCategory.DIAGNOSTIC,
        value_fn=lambda value: format_firmware_version(version=value)
    ),
    IndevoltSensorEntityDescription(
        key="9016",
        name="Battery SOC-Pack1",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.BATTERY,
        state_class=SensorStateClass.MEASUREMENT
    ),
    IndevoltSensorEntityDescription(
        key="9020",
        name="Battery V-Pack1",
        native_unit_of_measurement=UnitOfElectricPotential.VOLT,
        device_class=SensorDeviceClass.VOLTAGE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    IndevoltSensorEntityDescription(
        key="19173",
        name="Battery I-Pack1",
        native_unit_of_measurement=UnitOfElectricCurrent.AMPERE,
        device_class=SensorDeviceClass.CURRENT,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    IndevoltSensorEntityDescription(
        key="9030",
        name="Battery Temp-Pack1",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    IndevoltSensorEntityDescription(
        key="9021",
        name="Battery Cell1 V-Pack1",
        native_unit_of_measurement=UnitOfElectricPotential.VOLT,
        device_class=SensorDeviceClass.VOLTAGE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    IndevoltSensorEntityDescription(
        key="9023",
        name="Battery Cell2 V-Pack1",
        native_unit_of_measurement=UnitOfElectricPotential.VOLT,
        device_class=SensorDeviceClass.VOLTAGE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
}

BATTERY_PACK2_SENSORS = {
    IndevoltSensorEntityDescription(
        key="1138",	
        name="Firmware SFA/PFA DCDC2",
        entity_category=EntityCategory.DIAGNOSTIC,
        value_fn=lambda value: format_firmware_version(version=value)
    ),
    IndevoltSensorEntityDescription(
        key="1139",	
        name="Firmware SFA/PFA BMS2",
        entity_category=EntityCategory.DIAGNOSTIC,
        value_fn=lambda value: format_firmware_version(version=value)
    ),
    IndevoltSensorEntityDescription(
        key="9035",
        name="Battery SOC-Pack2",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.BATTERY,
        state_class=SensorStateClass.MEASUREMENT
    ),
    IndevoltSensorEntityDescription(
        key="9039",
        name="Battery V-Pack2",
        native_unit_of_measurement=UnitOfElectricPotential.VOLT,
        device_class=SensorDeviceClass.VOLTAGE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    IndevoltSensorEntityDescription(
        key="19174",
        name="Battery I-Pack2",
        native_unit_of_measurement=UnitOfElectricCurrent.AMPERE,
        device_class=SensorDeviceClass.CURRENT,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    IndevoltSensorEntityDescription(
        key="9049",
        name="Battery Temp-Pack2",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    IndevoltSensorEntityDescription(
        key="9040",
        name="Battery Cell1 V-Pack2",
        native_unit_of_measurement=UnitOfElectricPotential.VOLT,
        device_class=SensorDeviceClass.VOLTAGE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    IndevoltSensorEntityDescription(
        key="9042",
        name="Battery Cell2 V-Pack2",
        native_unit_of_measurement=UnitOfElectricPotential.VOLT,
        device_class=SensorDeviceClass.VOLTAGE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
}

BATTERY_PACK3_SENSORS = {
    IndevoltSensorEntityDescription(
        key="1140",	
        name="Firmware SFA/PFA DCDC3",
        entity_category=EntityCategory.DIAGNOSTIC,
        value_fn=lambda value: format_firmware_version(version=value)
    ),
    IndevoltSensorEntityDescription(
        key="1141",	
        name="Firmware SFA/PFA BMS3",
        entity_category=EntityCategory.DIAGNOSTIC,
        value_fn=lambda value: format_firmware_version(version=value)
    ),
    IndevoltSensorEntityDescription(
        key="9054",
        name="Battery SOC-Pack3",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.BATTERY,
        state_class=SensorStateClass.MEASUREMENT
    ),
    IndevoltSensorEntityDescription(
        key="9058",
        name="Battery V-Pack3",
        native_unit_of_measurement=UnitOfElectricPotential.VOLT,
        device_class=SensorDeviceClass.VOLTAGE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    IndevoltSensorEntityDescription(
        key="19175",
        name="Battery I-Pack3",
        native_unit_of_measurement=UnitOfElectricCurrent.AMPERE,
        device_class=SensorDeviceClass.CURRENT,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    IndevoltSensorEntityDescription(
        key="9068",
        name="Battery Temp-Pack3",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    IndevoltSensorEntityDescription(
        key="9059",
        name="Battery Cell1 V-Pack3",
        native_unit_of_measurement=UnitOfElectricPotential.VOLT,
        device_class=SensorDeviceClass.VOLTAGE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    IndevoltSensorEntityDescription(
        key="9061",
        name="Battery Cell2 V-Pack3",
        native_unit_of_measurement=UnitOfElectricPotential.VOLT,
        device_class=SensorDeviceClass.VOLTAGE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
}

BATTERY_PACK4_SENSORS = {
    IndevoltSensorEntityDescription(
        key="1142",	
        name="Firmware SFA/PFA DCDC4",
        entity_category=EntityCategory.DIAGNOSTIC,
        value_fn=lambda value: format_firmware_version(version=value)
    ),
    IndevoltSensorEntityDescription(
        key="1143",	
        name="Firmware SFA/PFA BMS4",
        entity_category=EntityCategory.DIAGNOSTIC,
        value_fn=lambda value: format_firmware_version(version=value)
    ),
    IndevoltSensorEntityDescription(
        key="9149",
        name="Battery SOC-Pack4",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.BATTERY,
        state_class=SensorStateClass.MEASUREMENT
    ),
    IndevoltSensorEntityDescription(
        key="9153",
        name="Battery V-Pack4",
        native_unit_of_measurement=UnitOfElectricPotential.VOLT,
        device_class=SensorDeviceClass.VOLTAGE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    IndevoltSensorEntityDescription(
        key="19176",
        name="Battery I-Pack4",
        native_unit_of_measurement=UnitOfElectricCurrent.AMPERE,
        device_class=SensorDeviceClass.CURRENT,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    IndevoltSensorEntityDescription(
        key="9163",
        name="Battery Temp-Pack4",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    IndevoltSensorEntityDescription(
        key="9154",
        name="Battery Cell1 V-Pack4",
        native_unit_of_measurement=UnitOfElectricPotential.VOLT,
        device_class=SensorDeviceClass.VOLTAGE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    IndevoltSensorEntityDescription(
        key="9156",
        name="Battery Cell2 V-Pack4",
        native_unit_of_measurement=UnitOfElectricPotential.VOLT,
        device_class=SensorDeviceClass.VOLTAGE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
}

BATTERY_PACK5_SENSORS = {
    IndevoltSensorEntityDescription(
        key="1098",	
        name="Firmware SFA/PFA DCDC5",
        entity_category=EntityCategory.DIAGNOSTIC,
        value_fn=lambda value: format_firmware_version(version=value)
    ),
    IndevoltSensorEntityDescription(
        key="1099",	
        name="Firmware SFA/PFA BMS5",
        entity_category=EntityCategory.DIAGNOSTIC,
        value_fn=lambda value: format_firmware_version(version=value)
    ),
    IndevoltSensorEntityDescription(
        key="9202",
        name="Battery SOC-Pack5",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.BATTERY,
        state_class=SensorStateClass.MEASUREMENT
    ),
    IndevoltSensorEntityDescription(
        key="9206",
        name="Battery V-Pack5",
        native_unit_of_measurement=UnitOfElectricPotential.VOLT,
        device_class=SensorDeviceClass.VOLTAGE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    IndevoltSensorEntityDescription(
        key="19177",
        name="Battery I-Pack5",
        native_unit_of_measurement=UnitOfElectricCurrent.AMPERE,
        device_class=SensorDeviceClass.CURRENT,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    IndevoltSensorEntityDescription(
        key="9216",
        name="Battery Temp-Pack5",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    IndevoltSensorEntityDescription(
        key="9219",
        name="Battery Cell1 V-Pack5",
        native_unit_of_measurement=UnitOfElectricPotential.VOLT,
        device_class=SensorDeviceClass.VOLTAGE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    IndevoltSensorEntityDescription(
        key="9222",
        name="Battery Cell2 V-Pack5",
        native_unit_of_measurement=UnitOfElectricPotential.VOLT,
        device_class=SensorDeviceClass.VOLTAGE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
}

BATTERY_PACK_SENSORS = {
    1: BATTERY_PACK1_SENSORS,
    2: BATTERY_PACK2_SENSORS,
    3: BATTERY_PACK3_SENSORS,
    4: BATTERY_PACK4_SENSORS,
    5: BATTERY_PACK5_SENSORS,
}


async def async_setup_entry(hass, entry, async_add_entities):
    """
    Set up the sensor platform for Indevolt.
    
    This function is called by Home Assistant when the integration is set up.
    It creates sensor entities for each defined sensor description.
    """
    # Create an entity for each sensor description.
    if "BK1600" in entry.data.get("device_model"):
        async_add_entities(
            IndevoltSensorEntity(entry.runtime_data, description)
            for description in SENSORS_GEN1
            if entry.runtime_data.data.get(description.key) is not None
        )
    else:
        entities = []

        for description in SENSORS_GEN2:
            if entry.runtime_data.data.get(description.key) is not None:
                entities.append(IndevoltSensorEntity(entry.runtime_data, description))

        for pack_id, sensors in BATTERY_PACK_SENSORS.items():
            for description in sensors:
                if entry.runtime_data.data.get(description.key) is not None:
                    entities.append(IndevoltBatterySensorEntity(entry.runtime_data, description, pack_id))

        async_add_entities(entities)

class IndevoltSensorEntity(IndevoltEntity, SensorEntity):
    """Represents a sensor entity for Indevolt devices."""

    # Enable entity name as the only name (without device name prefix)
    _attr_has_entity_name = True

    def __init__(self, coordinator, description: IndevoltSensorEntityDescription):
        super().__init__(coordinator)
        self.entity_description = description
        self._attr_unique_id = f"{coordinator.config_entry.unique_id}_{description.key}"

    @property
    def device_info(self):
        return self.device_info_main()

    @property
    def native_value(self):
        """Return the current value of the sensor in its native unit."""    
        return self.entity_description.value_fn(self.coordinator.data.get(self.entity_description.key))


class IndevoltBatterySensorEntity(IndevoltEntity, SensorEntity):
    def __init__(self, coordinator, description, pack_id: int):
        super().__init__(coordinator)
        self.entity_description = description
        self.pack_id = pack_id
        self._attr_unique_id = (
            f"{coordinator.config_entry.unique_id}_battery_{pack_id}_{description.key}"
        )

    @property
    def available(self):
        return bool(self.device_info.get("serial_number"))

    @property
    def device_info(self):
        return self.device_info_battery(self.pack_id)

    @property
    def native_value(self):
        return self.entity_description.value_fn(
            self.coordinator.data.get(self.entity_description.key)
        )


def format_firmware_version(version: int | str) -> str:
    """Format firmware version number."""

    v = str(version)

    if len(v) == 5:
        return f"{int(v[0])}.{v[1:3]}.{v[3:5]}"

    elif len(v) == 3:
        return f"{int(v[0])}.{v[1:3]}"

    else:
        return v
