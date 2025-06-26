# Minilab_3_banks
Custom remote script for Ableton for the Minilab 3.

This custom remote script allows the MiniLab 3 to access **parameter banks**. When a new device or bank is selected, the encoders align to the values of  the parameters they control. No more jumping values when movign the encoders. It also repurpose two buttons of the *Transport Bank* of the Minilab 3. The *Loop* button now cycles through the parameter banks; the name of the device and the selected bank are displayed on the Minilab 3 display. And the *Tap* button now toggles the metronome on and off. Additionally, when moving the playhead using the display encoder, the Minilab 3 display will now show the `Bar.Beat.Tick` time instead of minutes and seconds. 

Installation
------------

1. 	[Download](https://github.com/diegorad/Minilab_3_banks/archive/refs/heads/main.zip) the files in this repository.
1.	Stop Live if it is running.
1.	Add the `Minilab_3_banks` folder to Ableton Live's Remote Scripts library:

	The folder `Minilab_3_banks` contains the custom remote script. To install it follow the [official Ableton's guide to install a third-party remote script](https://help.ableton.com/hc/en-us/articles/209072009-Installing-third-party-remote-scripts).
1. 	Connect your **Minilab 3** device to your computer using a USB cable.
1.	Open Live and enable **Minilab 3 banks** as a Control Surface:

	In Live’s Preferences go to the *Link, Tempo & MIDI* tab and select *MiniLab 3 banks* from the dropdown list of available Control Surfaces. As MIDI Input select `Minilab3 (MIDI)`. As MIDI Output select `Minilab3 (MIDI)`. *Takeover mode* can be set to None.

This script is an extenstion on my [previous custom script](https://github.com/diegorad/MiniLab_3_Notify) which only aligns the encoders to the values of the parameters they control when a new device is selected.

**Important note:**
This script has only been tested in Ableton 12.1.5. Due to updates on Live's embedded python, this script does not work on Live 12.0 and older versions. However, if you are running Live 12.0, it is possible to replace the `.pyc` files of this script with copies of the original ones provided with Ableton to make it work.
