from __future__ import absolute_import, print_function, unicode_literals
import Live
from ableton.v3.base import sign
from ableton.v3.control_surface.components import TransportComponent as TransportComponentBase
from ableton.v3.control_surface.controls import ButtonControl, EncoderControl, ToggleButtonControl
from ableton.v3.live import move_current_song_time
from .Logging import log

#Beat int to bars.beats.sixteenths
def beat_to_bbt(beat_float, numerator):
    bars = int(beat_float // numerator) + 1
    beats = int(beat_float % numerator) + 1
    sixteenths = int((beat_float * 4) % 4) + 1
    return f"{bars}.{beats}.{sixteenths}"

class TransportComponent(TransportComponentBase):
    log("::TransportComponent::")
    __events__ = ('transport_event', )
    
    arrangement_position_encoder = EncoderControl()
    metronome_tap_button = ButtonControl()
    shift_button = ButtonControl()
    
    def __init__(self, *a, **k):
        super(TransportComponent, self).__init__(*a, **k)
        self._metronome_tap_button = None

        self._song = Live.Application.get_application().get_document()

    def set_shift_button(self, control):
        self._shift_button = control
        if control:
            control.add_value_listener(self._on_shift_button)
            
    def set_metronome_tap_button(self, control):
        self._metronome_tap_button = control
        log(f'::set_metronome_tap_button::self._metronome_tap_button: {self._metronome_tap_button}')
        if self._metronome_tap_button:
            self.metronome_button.set_control_element(self._metronome_tap_button)
    
    
    def map_metronome_tap_button(self, value):
        log("::map_metronome_button::value: {value}")
        
        if not (self._metronome_tap_button):
            return
        if value:
            log("::map_metronome_button::pressed")
            self.metronome_button.set_control_element(None)
            self.tap_tempo_button.set_control_element(self._metronome_tap_button)
        else:
            log("::map_metronome_button::released")
            self.metronome_button.set_control_element(self._metronome_tap_button)
            self.tap_tempo_button.set_control_element(None)
            
    @arrangement_position_encoder.value
    def arrangement_position_encoder(self, value, _):
        log('::arrangement_position_encoder::')
        
        move_current_song_time(self.song, sign(value))
        
        numerator = self.song.signature_numerator  #Beats per bar
        
        if(value >= 0): #Current_song_time returns the previous bar time, offset is required
            offset = 1
        else:
            offset = -1
        
        beat_time = self.song.current_song_time + offset
        
        if(beat_time < 0):
            beat_time = 0
        
        current_time_string = beat_to_bbt(beat_time, numerator)
        
        self.notify_transport_event('', current_time_string)