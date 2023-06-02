def hitung_imt_kucing(berat_badan, tinggi_badan):
    tinggi_meter = tinggi_badan / 100
    imt = berat_badan / (tinggi_meter ** 2)
    return imt