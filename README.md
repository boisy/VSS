# VSS - Virtual Security System

The Virtual Security System (VSS) PlugIn for Indigo allows you to create a "virtual security system" that can be in one of five states:

- Disarmed: the security system is not actively set to monitor triggers and any changes in sensors doesn't trigger.
- Stay Arm: the security system is armed for monitoring while someone is home; sensors should trigger any change of status outside the home only.
- Away Arm: the security system is armed for monitoring when no one is home; sensors should trigger any change of status inside and outside the home.
- Night Arm: the security system is armed for night monitoring; sensors should trigger any change of status inside and outside the home.
- Triggered: the security system has been triggered due to a change in a sensor's state.

These are the same states that most security systems have.

## Using the Plugin

1. Install the plugin and create a new VSS device.

2. Create actions to set the state of the device under certain conditions. Here are some examples:

  - You have a motion sensor outside your home. Create an action that checks if the state is "Stay Arm" or "Away Arm." If so, the action changes the state to "Triggered."
  - You have a motion sensor inside of your home. Create an action that checks if the state is "Away Arm." If so, the action changes the state to "Triggered."

Once you create the desired actions, create triggers to act on the state chnage.

  - A trigger that plays a noise over your HomePods using Airfoil Pro if the state of the security system changes to "Triggered."

## HomeKit Support

With the [HomeKitLink](https://github.com/Ghawken/HomeKitLink-Siri) plugin, you can expose your VSS to HomeKit through the Home app and set its state from there. When changing the security system state in the Home app, the state immediately is reflected in Indigo, and vice versa.
