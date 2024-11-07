# -*- coding: utf-8 -*-
"""
Samanlikning av årlege kostnadar for elbil og bensinbil

Laga av 05.11.2024
Spyder editor

@author: EN

"""

def berekne_aarleg_kostnad ():
    K = 10000  # forventa køyrelengde i km per år

    """ Definisjon av faste kostnadar """
    elbil_forsikring = 5000  # forsikring kr/år
    bensin_forsikring = 7500  # forsikring kr/år
    
    """Definisjon av variable kostnadar """
    trafikkforsikring = 8.38  # avgift i kr/dag
    elbil_drivstoff_kwh = 0.2  # kwh/km
    elbil_lading = 2  #kr/kwh
    bensin_drivstoff = 1  # kr/km
    elbil_bomavgift = 0.1  # kr/km
    bensin_bomavgift = 0.3  # kr/km
    
    # Berekne årlege kostnadar på elbil
    elbil_trafikkforsikring_aarleg = (trafikkforsikring*365)
    elbil_drivstoff_aarleg = (elbil_lading*elbil_drivstoff_kwh*K)
    elbil_bomavgift_aarleg = (elbil_bomavgift*K)
    elbil_total = elbil_forsikring+elbil_trafikkforsikring_aarleg+elbil_drivstoff_aarleg+elbil_bomavgift_aarleg
    
    # Berekne årlege kostnadar på bensinbil
    bensin_trafikkforsikring_aarleg = (trafikkforsikring*365)
    bensin_drivstoff_aarleg = bensin_drivstoff*K
    bensin_bomavgift_aarleg = bensin_bomavgift*K
    bensin_total = bensin_forsikring+bensin_trafikkforsikring_aarleg+bensin_drivstoff_aarleg+bensin_bomavgift_aarleg
    
    # Kostnadsdifferanse
    differanse = bensin_total-elbil_total
    
    print("Årleg kostnad for elbil i kr", elbil_total)
    print("Årleg kostnad for bensinbil i kr", bensin_total)
    print("Differanse i kr per år", differanse)
    
# Hent resultat
berekne_aarleg_kostnad()