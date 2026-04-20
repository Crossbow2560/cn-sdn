from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.forwarding.l2_learning import LearningSwitch

log = core.getLogger()

class SmartSwitch(LearningSwitch):

    def _handle_PacketIn(self, event):
        packet = event.parsed

        if packet.dst.is_multicast:
            if packet.type != 0x0806:  # ARP
                log.info("Blocking broadcast from %s", packet.src)
                return
            
        super()._handle_PacketIn(event)


def launch():
    def start_switch(event):
        log.info("Smart switch connected")
        SmartSwitch(event.connection, transparent=False)

    core.openflow.addListenerByName("ConnectionUp", start_switch)
