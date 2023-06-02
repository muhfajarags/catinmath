def hitung_kebutuhan_cairan(berat_badan, tingkat_aktivitas):
    faktor_aktivitas = 1.0
    
    if tingkat_aktivitas == 'sedang':
        faktor_aktivitas = 1.2
    elif tingkat_aktivitas == 'tinggi':
        faktor_aktivitas = 1.4
    
    kebutuhan_cairan = berat_badan * faktor_aktivitas * 50  # Anggap 50 ml per kg berat badan
    
    return kebutuhan_cairan