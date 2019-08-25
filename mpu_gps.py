#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

# mpu documentations

import mpu

#Ponto A
l0 = (-22.895292, -43.295627)

#Ponto B
l1 = (-22.895643, -43.291014)

distance = mpu.haversine_distance(l0, l1) * 1000
print(distance,"metros")
