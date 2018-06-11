import textfsm
import pprint

interfaces = '''Interface GigabitEthernet0/0 "outside", is up, line protocol is up
  Hardware is i82540EM rev03, BW 1000 Mbps, DLY 10 usec
	Auto-Duplex(Full-duplex), Auto-Speed(1000 Mbps)
	Input flow control is unsupported, output flow control is off
	MAC address 0cd1.56da.2c01, MTU 1500
	IP address 192.168.1.221, subnet mask 255.255.255.0
	5618749 packets input, 523372841 bytes, 0 no buffer
	Received 34530 broadcasts, 0 runts, 0 giants
	0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored, 0 abort
	0 pause input, 0 resume input
	0 L2 decode drops
	65 packets output, 5985 bytes, 0 underruns
	0 pause output, 0 resume output
	0 output errors, 0 collisions, 1 interface resets
	0 late collisions, 0 deferred
	147 input reset drops, 0 output reset drops
	input queue (blocks free curr/low): hardware (476/447)
	output queue (blocks free curr/low): hardware (511/509)
  Traffic Statistics for "outside":
	34432 packets input, 2593638 bytes
	53 packets output, 4147 bytes
	18282 packets dropped
      1 minute input rate 1 pkts/sec,  150 bytes/sec
      1 minute output rate 0 pkts/sec,  0 bytes/sec
      1 minute drop rate, 1 pkts/sec
      5 minute input rate 2 pkts/sec,  152 bytes/sec
      5 minute output rate 0 pkts/sec,  0 bytes/sec
      5 minute drop rate, 1 pkts/sec
Interface GigabitEthernet0/1 "dmz", is up, line protocol is up
  Hardware is i82540EM rev03, BW 1000 Mbps, DLY 10 usec
	Auto-Duplex(Full-duplex), Auto-Speed(1000 Mbps)
	Input flow control is unsupported, output flow control is off
	MAC address 0cd1.56da.2c02, MTU 1500
	IP address 10.60.0.1, subnet mask 255.255.255.0
	0 packets input, 0 bytes, 0 no buffer
	Received 0 broadcasts, 0 runts, 0 giants
	0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored, 0 abort
	0 pause input, 0 resume input
	0 L2 decode drops
	248000 packets output, 22311570 bytes, 0 underruns
	0 pause output, 0 resume output
	0 output errors, 0 collisions, 1 interface resets
	0 late collisions, 0 deferred
	0 input reset drops, 0 output reset drops
	input queue (blocks free curr/low): hardware (511/511)
	output queue (blocks free curr/low): hardware (511/509)
  Traffic Statistics for "dmz":
        0 packets input, 0 bytes
	1758 packets output, 133560 bytes
	0 packets dropped
      1 minute input rate 0 pkts/sec,  0 bytes/sec
      1 minute output rate 0 pkts/sec,  8 bytes/sec
      1 minute drop rate, 0 pkts/sec
      5 minute input rate 0 pkts/sec,  0 bytes/sec
      5 minute output rate 0 pkts/sec,  8 bytes/sec
      5 minute drop rate, 0 pkts/sec
Interface GigabitEthernet0/2 "", is administratively down, line protocol is up
  Hardware is i82540EM rev03, BW 1000 Mbps, DLY 10 usec
	Auto-Duplex(Full-duplex), Auto-Speed(1000 Mbps)
	Input flow control is unsupported, output flow control is off
	Available but not configured via nameif
	MAC address 0cd1.56da.2c03, MTU not set
	IP address unassigned
	0 packets input, 0 bytes, 0 no buffer
	Received 0 broadcasts, 0 runts, 0 giants
	0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored, 0 abort
	0 pause input, 0 resume input
	0 L2 decode drops
	0 packets output, 0 bytes, 0 underruns
	0 pause output, 0 resume output
        0 output errors, 0 collisions, 1 interface resets
	0 late collisions, 0 deferred
	0 input reset drops, 0 output reset drops
	input queue (blocks free curr/low): hardware (511/511)
	output queue (blocks free curr/low): hardware (511/511)
Interface GigabitEthernet0/3 "", is administratively down, line protocol is up
  Hardware is i82540EM rev03, BW 1000 Mbps, DLY 10 usec
	Auto-Duplex(Full-duplex), Auto-Speed(1000 Mbps)
	Input flow control is unsupported, output flow control is off
	Available but not configured via nameif
	MAC address 0cd1.56da.2c04, MTU not set
	IP address unassigned
	0 packets input, 0 bytes, 0 no buffer
	Received 0 broadcasts, 0 runts, 0 giants
	0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored, 0 abort
	0 pause input, 0 resume input
	0 L2 decode drops
	0 packets output, 0 bytes, 0 underruns
	0 pause output, 0 resume output
	0 output errors, 0 collisions, 1 interface resets
	0 late collisions, 0 deferred
	0 input reset drops, 0 output reset drops
	input queue (blocks free curr/low): hardware (511/511)
        output queue (blocks free curr/low): hardware (511/511)
Interface GigabitEthernet0/4 "", is administratively down, line protocol is up
  Hardware is i82540EM rev03, BW 1000 Mbps, DLY 10 usec
	Auto-Duplex(Full-duplex), Auto-Speed(1000 Mbps)
	Input flow control is unsupported, output flow control is off
	Available but not configured via nameif
	MAC address 0cd1.56da.2c05, MTU not set
	IP address unassigned
	0 packets input, 0 bytes, 0 no buffer
	Received 0 broadcasts, 0 runts, 0 giants
	0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored, 0 abort
	0 pause input, 0 resume input
	0 L2 decode drops
	0 packets output, 0 bytes, 0 underruns
	0 pause output, 0 resume output
	0 output errors, 0 collisions, 1 interface resets
	0 late collisions, 0 deferred
	0 input reset drops, 0 output reset drops
	input queue (blocks free curr/low): hardware (511/511)
	output queue (blocks free curr/low): hardware (511/511)
Interface GigabitEthernet0/5 "", is administratively down, line protocol is up
  Hardware is i82540EM rev03, BW 1000 Mbps, DLY 10 usec
	Auto-Duplex(Full-duplex), Auto-Speed(1000 Mbps)
        Input flow control is unsupported, output flow control is off
	Available but not configured via nameif
	MAC address 0cd1.56da.2c06, MTU not set
	IP address unassigned
	0 packets input, 0 bytes, 0 no buffer
	Received 0 broadcasts, 0 runts, 0 giants
	0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored, 0 abort
	0 pause input, 0 resume input
	0 L2 decode drops
	0 packets output, 0 bytes, 0 underruns
	0 pause output, 0 resume output
	0 output errors, 0 collisions, 1 interface resets
	0 late collisions, 0 deferred
	0 input reset drops, 0 output reset drops
	input queue (blocks free curr/low): hardware (511/511)
	output queue (blocks free curr/low): hardware (511/511)
Interface GigabitEthernet0/6 "", is administratively down, line protocol is up
  Hardware is i82540EM rev03, BW 1000 Mbps, DLY 10 usec
	Auto-Duplex(Full-duplex), Auto-Speed(1000 Mbps)
	Input flow control is unsupported, output flow control is off
	Available but not configured via nameif
	MAC address 0cd1.56da.2c07, MTU not set
	IP address unassigned
        0 packets input, 0 bytes, 0 no buffer
	Received 0 broadcasts, 0 runts, 0 giants
	0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored, 0 abort
	0 pause input, 0 resume input
	0 L2 decode drops
	0 packets output, 0 bytes, 0 underruns
	0 pause output, 0 resume output
	0 output errors, 0 collisions, 1 interface resets
	0 late collisions, 0 deferred
	0 input reset drops, 0 output reset drops
	input queue (blocks free curr/low): hardware (511/511)
	output queue (blocks free curr/low): hardware (511/511)
Interface Management0/0 "", is administratively down, line protocol is up
  Hardware is i82540EM rev03, BW 1000 Mbps, DLY 10 usec
	Auto-Duplex(Full-duplex), Auto-Speed(1000 Mbps)
	Input flow control is unsupported, output flow control is off
	Available but not configured via nameif
	MAC address 0cd1.56da.2c00, MTU not set
	IP address unassigned
	0 packets input, 0 bytes, 0 no buffer
	Received 0 broadcasts, 0 runts, 0 giants
	0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored, 0 abort
	0 pause input, 0 resume input
        0 L2 decode drops
	0 packets output, 0 bytes, 0 underruns
	0 pause output, 0 resume output
	0 output errors, 0 collisions, 1 interface resets
	0 late collisions, 0 deferred
	0 input reset drops, 0 output reset drops
	input queue (blocks free curr/low): hardware (511/511)
	output queue (blocks free curr/low): hardware (511/511)'''

# open the template file
with open('./templates/asa_int.template', 'r') as f:
    template = textfsm.TextFSM(f)

# run the interface data through the template parser
results = template.ParseText(interfaces)


pprint.pprint(results)