def hitung_energi_metabolis(berat_badan, tingkat_aktivitas):
    faktor_aktivitas = 1.0
    
    if tingkat_aktivitas == 'sedang':
        faktor_aktivitas = 1.4
    elif tingkat_aktivitas == 'tinggi':
        faktor_aktivitas = 1.6
    
    energi_metabolis = berat_badan * faktor_aktivitas * 70  # Anggap 70 kkal per kg berat badan
    
    return energi_metabolis
