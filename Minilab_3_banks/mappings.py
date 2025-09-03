from __future__ import absolute_import, print_function, unicode_literals
from ableton.v3.control_surface.mode import select_mode_for_main_view
from .midi import PAD_TRANSLATION_CHANNEL
from .Logging import log

def translate_pad_banks(cs):

    def inner():
        for pad in cs.elements.pad_bank_a_raw + cs.elements.pad_bank_b_raw:
            pad.set_channel(PAD_TRANSLATION_CHANNEL)

    return inner


def realign_encoder_values(cs):

    def inner():
        for encoder in cs.elements.encoders_raw:
            encoder.realign_value()

    return inner


def create_mappings(cs):
    log('::create_mappings::')
    return {'View_Based_Recording': dict(record_button='record_button'),
            'Transport': dict(play_button='play_button',
                              stop_button='stop_button',
                              metronome_tap_button='metronome_button',
                              shift_button='shift_button'),
            'Device': dict(bank_button='bank_button',
                         scroll_devices='shifted_display_encoder'),
            'DisplayEncoder': dict(encoder='display_encoder',
                                button='display_encoder_button'),
            'Mixer': dict(target_track_arm_button='shifted_display_encoder_button',
                          target_track_pan_control='pan_fader',
                          target_track_send_a_control='send_a_fader',
                          target_track_send_b_control='send_b_fader',
                          target_track_volume_control='volume_fader'),
            'View_Control': dict(),
            'Main_Modes': dict(mode_selection_control='firmware_element',
                               user=translate_pad_banks(cs),
                               main=dict(modes=[
                                   realign_encoder_values(cs),
                                   dict(component='Session',
                                        clip_launch_buttons='pad_bank_a'),
                                   dict(component='Drum_Group',
                                        matrix='pad_bank_b'),
                                   dict(component='Device',
                                        parameter_controls='encoders')]))}
