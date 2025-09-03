from __future__ import absolute_import, print_function, unicode_literals
import Live
from ableton.v3.control_surface import Component
from ableton.v3.control_surface.controls import EncoderControl, ButtonControl
from ableton.v3.control_surface.mode import select_mode_for_main_view

from .Logging import log

class DisplayEncoderComponent(Component):
    encoder = EncoderControl()
    button = ButtonControl()

    def __init__(self, *a, **k):
        super(DisplayEncoderComponent, self).__init__(*a, **k)
        self._transport = None
        self._device = None
        self._encoder = None
        self._view = None
        
        #View listener
        self._app_view = Live.Application.get_application().view
        if not self._app_view.focused_document_view_has_listener(self._on_view_changed):
            self._app_view.add_focused_document_view_listener(self._on_view_changed)
        
    def set_encoder(self, control):
        self._encoder = control
        log(f'::set_encoder::self._encoder: {self._encoder}')
        if self._encoder:
            self._on_view_changed()

    def set_button(self, control):
        self._button = control
        if control:
            control.add_value_listener(self._on_button)
    
    def set_components(self, TransportComponent, DeviceComponent, ViewControlComponent):
        self._transport = TransportComponent
        self._device = DeviceComponent
        self._view = ViewControlComponent      

    def _on_button(self, value):
        if not (self._encoder and self._transport and self._device):
            return
            
        self._transport.map_metronome_tap_button(value)
        
        if value:
            self._transport.arrangement_position_encoder.set_control_element(None)
            self._view.set_scene_encoder(None)
            self._view.set_track_encoder(self._encoder)
        else:
            self._view.set_track_encoder(None)
            self._on_view_changed()
        
    def _on_view_changed(self):
        self._app_view = Live.Application.get_application().view
        current_view = self._app_view.focused_document_view     
        log(f"Current view change: {current_view}")
        
        if current_view == "Arranger":
            self._transport.arrangement_position_encoder.set_control_element(self._encoder)
            self._view.set_scene_encoder(None)
        elif current_view == "Session":
            self._transport.arrangement_position_encoder.set_control_element(None)
            self._view.set_scene_encoder(self._encoder)
        else:
            log("::_on_view_changed::undefined")
