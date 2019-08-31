#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import ntplib
from time import ctime

c = ntplib.NTPClient()
response = c.request('pool.ntp.org', version=3)
print(ctime(response.tx_time))
