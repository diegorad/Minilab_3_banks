from __future__ import absolute_import, print_function, unicode_literals
import Live
from ableton.v3.control_surface import Component
from ableton.v3.control_surface.controls import EncoderControl, ButtonControl

from .Logging import log

class DisplayEncoderComponent(Component):
    encoder = EncoderControl()
    button = ButtonControl()

    def __init__(self, *a, **k):
        super().__init__(*a, **k)
        self._transport = None
        self._device = None
        self._encoder = None
        
    def set_encoder(self, control):
        self._encoder = control

    def set_button(self, control):
        self._button = control
        if control:
            control.add_value_listener(self._on_button)
    
    def set_components(self, TransportComponent, device):
        self._transport = TransportComponent
        self._device = device
        if self._encoder:
            self._transport.arrangement_position_encoder(self._encoder)
#    
    def _on_button(self, value):
        current_view = Live.Application.Application.View.focused_document_view
        log(f'Current view: {current_view}')
        if not (self._encoder and self._transport and self._device):
            return
        if value:  # pressed
            self._transport.arrangement_position_encoder.set_control_element(None)
            self._device.device_scroll_encoder.set_control_element(self._encoder)
        else:
            self._device.device_scroll_encoder.set_control_element(None)
            self._transport.arrangement_position_encoder.set_control_element(self._encoder)

    
    