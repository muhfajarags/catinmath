import math

def kucing_pertumbuhan(populasi_awal, tingkat_pertumbuhan, waktu):
    return populasi_awal * math.exp(tingkat_pertumbuhan * waktu)