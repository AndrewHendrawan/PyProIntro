print("Meskipun Kamu mengetahui semua ini, kami tetao memberikanmu kamus kecil. Jangan ragu untuk menyalin informasi dari sini ke dalam aplikasi Anda!")
meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "ROFL":"tanggapan terhadap lelucon",
            "SHEESH" : "sedikit ketidaksetujuan",
            "CREEPY":"menakutkan, tidak menyenangkan",
            "AGGRO":"untuk menjadi agressif/marah"
            }

word = input("\nKetik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")
word = word.lower()

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("Word not found")
    # Apa yang harus kita lakukan jika kata itu tidak ditemukan?
