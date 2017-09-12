#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

for index in range(16,1000):
    os.system('mkdir -p nfs-pv{:0>4}'.format(index))