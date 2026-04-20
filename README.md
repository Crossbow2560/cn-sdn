# SDN Broadcast Traffic Control using Mininet & POX

## Problem Statement
Broadcast traffic in networks can cause congestion and inefficiency.
This project implements an SDN-based solution to control excessive broadcast traffic using Mininet and the POX controller.

------------------------------------------------------------

## Objectives
- Detect broadcast packets
- Limit unnecessary broadcast flooding
- Implement selective forwarding rules
- Analyze network behavior

------------------------------------------------------------

## Tools Used
- Mininet
- POX Controller
- Open vSwitch
- iperf

------------------------------------------------------------

## Approach

We extended the POX learning switch with custom logic:

- Allow ARP broadcast (required for communication)
- Block non-ARP broadcast traffic
- Maintain normal unicast forwarding

------------------------------------------------------------

## Setup & Execution

1. Clone POX:
git clone https://github.com/noxrepo/pox.git
cd pox

2. Run controller (baseline):
python3.9 pox.py forwarding.l2_learning

3. Run controller (broadcast control):
python3.9 pox.py smart_broadcast

4. Run Mininet:
sudo mn -c
sudo mn --topo single,3 --controller remote --switch ovsk

------------------------------------------------------------

## Scenario 1: Baseline (Normal Switch)

Run:
pingall

Screenshot:
screenshots/baseline_ping.png

Check flow rules:
sudo ovs-ofctl dump-flows s1

Screenshot:
screenshots/baseline_flows.png

Run iperf:
h2 iperf -s &
h1 iperf -c h2

Screenshot:
screenshots/baseline_iperf.png

------------------------------------------------------------

## Scenario 2: Broadcast Controlled Network

Run:
pingall

Screenshot:
screenshots/controlled_ping.png

Controller logs (example):
Blocking broadcast from 00:00:00:00:00:01

Screenshot:
screenshots/controller_logs.png

Check flow rules:
sudo ovs-ofctl dump-flows s1

Screenshot:
screenshots/controlled_flows.png

Run iperf:
h2 iperf -s &
h1 iperf -c h2

Screenshot:
screenshots/controlled_iperf.png

ARP Table Check:
h1 arp -n

Screenshot:
screenshots/arp_table.png

------------------------------------------------------------

## Observations

Baseline:
- Broadcast flooding present
- Network works normally

Controlled:
- Unnecessary broadcast reduced
- Network still functional
- Improved efficiency

------------------------------------------------------------

## Results

- Broadcast packets detected and filtered
- ARP allowed for correct communication
- Flow rules dynamically installed
- Network performance maintained

------------------------------------------------------------

## Conclusion

This project demonstrates how SDN can be used to intelligently control network traffic.
Selective broadcast filtering reduces unnecessary traffic while preserving essential functionality.

------------------------------------------------------------

## References
- Mininet Documentation
- POX Controller Documentation
- OpenFlow Specification

------------------------------------------------------------

## Author
Your Name
