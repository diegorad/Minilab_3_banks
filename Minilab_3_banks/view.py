from __future__ import absolute_import, print_function, unicode_literals
import Live
from ableton.v3.control_surface.controls import EncoderControl
from ableton.v3.control_surface.components import ViewControlComponent as ViewControlComponentBase
from ableton.v3.control_surface import Component
from .Logging import log

class ViewControlComponent(ViewControlComponentBase):
    log('::ViewControlComponent::')
    
    def __init__(self, *a, **k):
        super().__init__(*a, **k)
        log('::ViewControlComponent::init')