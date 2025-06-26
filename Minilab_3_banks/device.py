from __future__ import absolute_import, print_function, unicode_literals
import Live
from ableton.v3.control_surface.components import DeviceComponent as DeviceComponentBase
from ableton.v3.control_surface.controls import ButtonControl
#from .Logging import log

# Device Component added to handle parameter banks

class DeviceComponent(DeviceComponentBase):
    __events__ = ('device_event', )
    
    bank_button = ButtonControl(color='Device.BankOff', pressed_color='Device.BankOn')
    
    def __init__(self, *a, **k):
        super(DeviceComponent, self).__init__(*a, **k)
        self._bank_index = 0
        self._last_sent_message = None
                    
    @bank_button.pressed
    def bank_button(self, _):
        if(self.device):
            #Scroll banks
            if self._bank_index < self._banking_info.device_bank_count(self.device) - 1:
                self._bank_index += 1
            else:
                self._bank_index = 0 #Wrap around
            
            #Set bank
            self._device_bank_registry.set_device_bank(self.device, self._bank_index)
            
            bank_name = self.bank_name
            device_name = self.device.name
            
            #Display device_name and bank_name in the Minilab 3
            self.notify_device_event(device_name, bank_name)