# Alarm-System-with-Micro-bit
  Device control with python


Data storage on Micro: bit

The system can save 3 different user profiles. For each user we will save the following information:
  1.name - the username;
  2.pin - a 4-digit code used for armament and disarmament.
  
The following commands will be used to configure user profiles:

  1.profile add name pin - adds a new profile; if the profile has been added successfully the message Profile added will be displayed; if there is already a profile with the same name, the pin will be changed; if an attempt is made to add a fourth profile, the following message will be displayed: Could not save profile. Limit exceeded .; if the pin does not have 4 digits the following message will be displayed: Could not save profile. Invalid pin.
  
  2.profile delete name - deletes the profile identified by the name; if the deletion was successful the following text will be displayed: Profile deleted; if the deletion could not be performed because the profile does not exist, the following message will be displayed: Could not delete profile. Profile name does not exist.
  
Armament

To arm the alarm system, press buttons A and B at the same time, at which point the LED grid will enter pin input mode.

If the pin is inserted correctly, the armament will be signaled by displaying a smiling face, and if the pin is not correct, a sad face will be displayed.

After signaling the armature, until disarming, the system will turn on the entire LED array.
