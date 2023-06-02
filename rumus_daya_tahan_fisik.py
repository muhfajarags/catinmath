def hitung_daya_tahan_fisik(umur_kucing, berat_badan, tingkat_aktivitas):
    faktor_umur = 1.0
    
    if umur_kucing < 1:
        faktor_umur = 1.2
    elif umur_kucing < 3:
        faktor_umur = 1.0
    elif umur_kucing < 6:
        faktor_umur = 0.8
    else:
        faktor_umur = 0.6
    
    faktor_aktivitas = 1.0
    
    if tingkat_aktivitas == 'sedang':
        faktor_aktivitas = 1.2
    elif tingkat_aktivitas == 'tinggi':
        faktor_aktivitas = 1.4
    
    daya_tahan_fisik = faktor_umur * faktor_aktivitas * berat_badan
    return daya_tahan_fisik
