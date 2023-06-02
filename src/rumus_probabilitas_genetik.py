def hitung_probabilitas_genetik(gen_orangtua1, gen_orangtua2):
    probabilitas = 0
    for gen1 in gen_orangtua1:
        for gen2 in gen_orangtua2:
            kombinasi_gen = gen1 + gen2
            if 'B' in kombinasi_gen or 'b' in kombinasi_gen:
                probabilitas += 1
    
    total_kombinasi = len(gen_orangtua1) * len(gen_orangtua2)
    probabilitas /= total_kombinasi
    
    return probabilitas