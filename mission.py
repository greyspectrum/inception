#!/usr/bin/env python3

import time
import sys

string = '''\nFLASH PRIORITY ONE TELEX:

STRAP 1 COMINT NOFORN
=====================

A client has contacted us with a request that requires a
very particular set of skills. The client has emphasized
the necessity of discretion in this matter.

Given the sensitivity of the client's request, we naturally
thought of your team.

Below, you will see find a list of IP addresses. These
machines collectively store secret information that is of
interest to our client. We have reason to beleive that this
confidential information has been encoded and sharded
across these three machines, in order to thwart exfiltration.

In order to access the machines, you must create cryptographic
keys to authenticate to the security system. Do so by entering
the following command in a shell:

    ssh-keygen -t ed25519 -o -a 100

In order to recieve payment for your services, you
must access these secure machines, extract the secrets,
assemble them, and decode the information.

As usual, any contractual relationship with your team
will be publicly denied, should you be compromised.

SYSTEM INFORMATION:

10.242.118.30

10.242.118.31

10.242.118.32

GOOD LUCK.

THIS MESSAGE WILL BE DELETED FROM YOUR SYSTEM... NOW.
\n'''

for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.025)
