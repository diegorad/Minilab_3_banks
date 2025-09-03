from __future__ import absolute_import, print_function, unicode_literals
import Live
from ableton.v3.control_surface.components import DeviceComponent as DeviceComponentBase
from ableton.v3.control_surface.controls import ButtonControl, EncoderControl
from ableton.v3.control_surface import Component
from .Logging import log

class DeviceComponent(DeviceComponentBase):
    __events__ = ('device_event', )
    
    bank_button = ButtonControl(color='Device.BankOff', pressed_color='Device.BankOn')
    shifted_display_encoder = EncoderControl()    
    
    def __init__(self, *a, **k):
        super(DeviceComponent, self).__init__(*a, **k)
        self._bank_index = 0
        self._last_sent_message = None
                    
    @bank_button.pressed
    def bank_button(self, _):
        log("Bank button press")
        if(self.device):
            #Scroll banks
            if self._bank_index < self._banking_info.device_bank_count(self.device) - 1:
                self._bank_index += 1
            else:
                self._bank_index = 0 #Wrap around
            
            #Set bank
            self._device_bank_registry.set_device_bank(self.device, self._bank_index)
            
            log(f'Bank button: {self}')
            bank_name = self.bank_name
            device_name = self.device.name
            
            #Display device_name and bank_name in the Minilab 3
            self.notify_device_event(device_name, bank_name)
    
    def get_device_index(self, device, devices):
        index = 0
        for d in devices:
        	if d == device:
        		return index
        	index = index + 1
        return -1
    
    @shifted_display_encoder.value
    def scroll_devices(self, value, _):
        track = self.song.view.selected_track
        selected_device = track.view.selected_device
        
        log(f'::scroll_devices::{selected_device}')
        
        #log(f'Value: {value}')
        if value > 0:
            direction = 1
        elif value < 0:
            direction = -1
        else:
            direction = 0
        
        index = self.get_device_index(selected_device, track.devices) + direction
        index = max(0, min(len(track.devices)-1, index))
        #log(f'Index: {index}')
        
        try:
            device = track.devices[index]
            bank_name = self.bank_name
            self.song.view.select_device(device)
            self.notify_device_event(device.name, bank_name)
        except:
            #log('No valid device')
            pass