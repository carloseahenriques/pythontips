#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

# Bilioteca Geopy
# https://pypi.org/project/geopy/

from geopy.distance import geodesic

print(geodesic((-22.986, -43.198), (-22.986, -43.200)).kilometers)
print(geodesic((-22.986, -43.198), (-22.986, -43.200)).meters)
