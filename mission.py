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

You may find the following Unix tools of use:

    ssh
    scp
    base64
    cat

You may access documentation on any of these tools by typing:

    man example

... where "example" is the name of the tool. This will give 
you access to the manual page. In addition, you may wish to 
review how to give other users access to a system by adding
their SSH key to authorized keys.

In order to recieve payment for your services, you
must access these secure machines, extract the secrets,
assemble them, and decode the information.

As usual, any contractual relationship with your team
will be publicly denied, should you be compromised.

SYSTEM INFORMATION:

140.247.152.7

140.247.152.8

140.247.152.10

GOOD LUCK.

THIS MESSAGE WILL BE DELETED FROM YOUR SYSTEM... NOW.
\n'''

for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.025)
