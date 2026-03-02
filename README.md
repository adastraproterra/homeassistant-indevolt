# Indevolt integration for Home Assistant

A Home Assistant custom integration to monitor and control [Indevolt](https://www.indevolt.com/) devices.


## Prerequisites
- [ ] Home Assistant has been installed according to the [official installation guide](https://www.home-assistant.io/installation/).
- [ ] The Indevolt device and Home Assistant server are on the **same local network**.
- [ ] The Indevolt device is powered on and has obtained an **IP address**.
  - Query via router’s management list;
  - Check in INDEVOLT App device settings;
- [ ] Ensure that the Indevolt device **API function is enabled**. This integration only supports OpenData HTTP mode.
<img width="800" alt="3http_mode" src="https://github.com/user-attachments/assets/67f8ed96-abb8-4368-b3f3-b2a3484bd4b9" />

- [ ] Confirm the firmware version meets the minimum requirement.

  | Model                       | Version                         |
  | --------------------------- | ------------------------------- |
  | BK1600/BK1600Ultra          | V1.3.0A_R006.072_M4848_00000039 |
  | SolidFlex2000/PowerFlex2000 | CMS: V1406.07.002B; Pfile: V0D.00.11 |

<img width="400" alt="4fw_version" src="https://github.com/user-attachments/assets/7fb6d58f-9c95-4945-b588-810e68481f5b" />


## Step 1: Download the indevolt integration folder

1. Click **Code** > **Download ZIP**.
2. Unzip the ZIP file to your computer.


## Step 2: Locate the HA configuration directory path

- **Home Assistant OS**: The configuration directory is located in `/config`.
- **Home Assistant Container**: You can access the configuration directory by locating the `configuration.yaml` file.

**Tip**: The directory should contain a `configuration.yaml` file.

```
config directory/
└── configuration.yaml
```

## Step 3: Create a custom integration directory

1. Enter the config directory.
2. Create the `custom_components` directory if it does not exist.

```
config directory/
├── custom_components/
└── configuration.yaml
```

**Note**: All custom integrations must be placed under `custom_components`, otherwise HA will not be able to recognize them.


## Step 4: Add the integration file

1. Create the `indevolt` directory in the config directory.
2. Copy all files from the unzipped folder (except `README.md`) into the `indevolt` directory.

Once installed correctly, your configuration directory should look like this:

```
config directory/
└── custom_components/
    └── indevolt/
        ├── __init__.py
        ├── config_flow.py
        ├── const.py
        ├── coordinator.py
        ├── entity.py
        ├── indevolt_api.py
        ├── manifest.json
        ├── number.py
        ├── select.py
        ├── sensor.py
        ├── service.yaml
        ├── switch.py
```

## Step 5: Restart Home Assistant

1. Select **Settings** > **System** in the web interface.
2. Click the restart icon in the upper right corner.
3. Click **Restart Home Assistant**.
4. Click **RESTART**.

<img width="1000" alt="5restart_ha" src="https://github.com/user-attachments/assets/1270a590-faf8-43a4-8989-27923d1f3887" />


## Step 6: Add integration to Home Assistant

1. After restarting, enter the web interface and select **Settings** > **Devices & services**.
2. Click **+ADD INTEGRATION** in the lower right corner.
3. Search for integration INDEVOLT.
4. Configuration parameters:
   - `host`: Device IP address, which can be obtained by checking the router/app.
   - `scan_interval`: Used to control the frequency of data updates, default is 30 seconds.
5. Click **SUBMIT** to finish the installation.
6. The power module and battery packs will be displayed after installation. Click Skip and Finish to complete the setup process.
  - Each power module supports up to 5 battery packs.
  - If no battery pack is connected, the corresponding field will be shown as None.
  - When battery packs are connected, the serial number (SN) of each battery pack will be displayed for identification.

<img width="600" alt="6add_integration" src="https://github.com/user-attachments/assets/b435073a-cd55-49fb-bcae-ffd698821c1a" />
<img width="300" alt="7add_device" src="https://github.com/user-attachments/assets/ce18f3e0-9658-4052-bbbd-02dfea022dbb" />


## View Integration

Select the INDEVOLT integration to display the device and entity information.

<img width="800" alt="8view_integration" src="https://github.com/user-attachments/assets/731e767d-c41c-4c5e-b1f6-a6eae28fffd7" />



## Update integration

1. Download the latest version of the integration file.
2. Replace the files in `custom_components/indevolt`.
3. Click the three-dot menu  next to the previously added device and select **Delete**.
4. Restart Home Assistant.
5. Click the button **Add Entry** and follow the same device setup process to add the device again.


## Create Automation: Set Real-Time Control

1. Go to **Settings** > **Automations & scenes**.
2. Click the button in the lower right corner **+ Create automation**.
3. Select **Create new automation**.
4. Click **+ Add Trigger** and configure the trigger event based on your requirements.
5. Click **+ Add Action** to configure the device action.
6. Search for mode and select Set SolidFlex2000/PowerFlex2000 Work Mode (as an example).
7. In the **Target** section, click **+ Choose Device** and select your device from the list.
8. In the **Work Mode** section, choose **Real-Time Control**, then configure **Status**, **Power**, and **Target SOC** as needed.
9. Click **Save** to complete the automation setup.


## FAQ

| Problem Description | Solutions |
| ------------------- | ----------|
| Integration not found in search list | Verify the integration file is located in the correct folder: `custom_components/indevolt`. |
| - Unable to add  device. <br> - Unable to connect to the device.  <br> - No data available   | This is typically caused by an **HTTP request failure**. <br>  1.  Verify the device is powered on.<br> 2. Confirm the device's IP address is correct.<br> 3. Check the device's network status in Indevolt app.<br>4. Ensure you have met all the [prerequisites](#prerequisites). |

If you encounter any issues, please check the **Home Assistant logs** for detailed error messages.

## Contribute

We welcome your feedback and contributions! Please feel free to open an issue with your suggestions or submit a pull request.
