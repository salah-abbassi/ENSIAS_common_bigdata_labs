#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

for line in sys.stdin:
    line = line.strip()
    data = line.split("\t")
    
    # Vérification que la ligne a bien les 6 colonnes
    if len(data) == 6:
        # --- Lignes TODO ---
        store = data[5]
        cost = data[4]
        print(f"{store}\t{cost}")

        magasin = data[2]
        print(f"{magasin}\t1")
