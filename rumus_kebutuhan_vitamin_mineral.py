def hitung_kebutuhan_vitamin_mineral(berat_badan, jenis_makanan):
    kebutuhan_vitamin = 0
    kebutuhan_mineral = 0
    
    if jenis_makanan == 'Kering':
        kebutuhan_vitamin = berat_badan * 0.2
        kebutuhan_mineral = berat_badan * 0.4
    elif jenis_makanan == 'Basah':
        kebutuhan_vitamin = berat_badan * 0.3
        kebutuhan_mineral = berat_badan * 0.5
    
    return kebutuhan_vitamin, kebutuhan_mineral