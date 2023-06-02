def konversi_umur_kucing(bulan_kucing):
    umur_manusia = 0
    
    if bulan_kucing < 6:
        umur_manusia = bulan_kucing
    elif bulan_kucing < 12:
        umur_manusia = 6 + ((bulan_kucing - 6) * 0.5)
    else:
        umur_manusia = 10 + ((bulan_kucing - 12) * 0.333)
    
    return umur_manusia