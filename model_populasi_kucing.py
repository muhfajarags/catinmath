import math

def model_populasi_kucing(populasi_awal, tingkat_pertumbuhan, waktu):
    populasi = populasi_awal * (math.e ** (tingkat_pertumbuhan * waktu))
    return populasi