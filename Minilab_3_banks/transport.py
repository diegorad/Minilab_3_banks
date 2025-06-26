from __future__ import absolute_import, print_function, unicode_literals
import Live
from ableton.v3.base import sign
from ableton.v3.control_surface.components import TransportComponent as TransportComponentBase
from ableton.v3.control_surface.controls import ButtonControl, EncoderControl, ToggleButtonControl
from ableton.v3.live import move_current_song_time
#from .Logging import log

#Beat int to bars.beats.sixteenths
def beat_to_bbt(beat_float, numerator):
    bars = int(beat_float // numerator) + 1
    beats = int(beat_float % numerator) + 1
    sixteenths = int((beat_float * 4) % 4) + 1
    return f"{bars}.{beats}.{sixteenths}"

class TransportComponent(TransportComponentBase):
    __events__ = ('transport_event', )
    arrangement_position_encoder = EncoderControl()
    metronome_button = ToggleButtonControl(color='Transport.MetronomeOff',
                                           on_color='Transport.MetronomeOn')

    @arrangement_position_encoder.value
    def arrangement_position_encoder(self, value, _):
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
        
    @metronome_button.toggled
    def metronome_button(self, toggled, _):
        self.song.metronome = toggled
        self.notify_transport_event(
            'Metronome', 'ON' if toggled else 'OFF')
