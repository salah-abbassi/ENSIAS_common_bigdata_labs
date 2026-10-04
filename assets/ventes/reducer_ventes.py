#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

sales_total = 0.0
old_key = None

for line in sys.stdin:
    line = line.strip()
    data = line.split("\t")
    
    if len(data) != 2:
        continue

    this_key, this_sale = data

    try:
        sale_amount = float(this_sale)
    except ValueError:
        continue

    if old_key and old_key != this_key:
        print(f"{old_key}\t{sales_total:.2f}")
        sales_total = 0.0

    old_key = this_key
    sales_total += sale_amount

# Émission du dernier magasin
if old_key is not None:
    print(f"{old_key}\t{sales_total:.2f}")