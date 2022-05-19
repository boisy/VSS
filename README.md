# VSS - Virtual Security System

The Virtual Security System (VSS) PlugIn for Indigo allows you to create a "virtual alarm system" that can be in one of four states:

- Disarmed: the security system is not actively set to monitor triggers and any changes in sensors doesn't trigger.
- Stay Arm: the security system is armed; sensors should trigger any change of status outside the home only.
- Away Arm: the security system is armed; sensors should trigger any change of status inside and outside the home.
- Triggered: the security system has been triggered due to a change in a sensor's state.

These are the same states that most alarm systems have.

In Indigo, create actions to set the state of the VSS. Here are some examples:

  - A motion sensor outside your home. Create an action that checks if the state is "Stay Arm" or "Away Arm." If so, the action changes the state to "Triggered."
  - A motion sensor inside of your home. Create an action that checks if the state is "Away Arm." If so, the action changes the state to "Triggered."

Once you create the desired actions, create triggers to act on the state chnage.

  - A trigger that plays a noise over your HomePods using Airfoil Pro if the state of the security system changes to "Triggered."

## HomeKit Support

With the [HomeKitLink](https://github.com/Ghawken/HomeKitLink-Siri) plugin, you can expose your VSS to HomeKit through the Home app and set its state from there. When changing the security system state in the Home app, the state immediately is reflected in Indigo, and vice versa.
