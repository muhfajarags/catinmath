def hitung_kebutuhan_makanan(berat_badan, tingkat_aktivitas):
    faktor_aktivitas = 1.2  # Faktor aktivitas default untuk kucing yang tidak aktif
    
    if tingkat_aktivitas == 'sedang':
        faktor_aktivitas = 1.4
    elif tingkat_aktivitas == 'tinggi':
        faktor_aktivitas = 1.6
    
    kebutuhan_kalori = berat_badan * faktor_aktivitas
    
    return kebutuhan_kalori