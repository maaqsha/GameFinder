# 07_Knowledge_Base.md

# Basis Pengetahuan (Knowledge Base)

## Tujuan

Dokumen ini mendefinisikan pengetahuan keputusan yang digunakan untuk membangun basis aturan Fuzzy Mamdani. Setiap aturan fuzzy harus mengikuti prinsip-prinsip ini.

------------------------------------------------------------------------

# KB-01 Kompatibilitas PC

Kompatibilitas PC merupakan prioritas tertinggi.

Jika level PC pengguna lebih rendah dari level PC yang dibutuhkan oleh game, rekomendasi harus diturunkan secara signifikan.

------------------------------------------------------------------------

# KB-02 Anggaran

Game yang berada di dalam jangkauan anggaran pengguna akan lebih diutamakan.

Game yang melebihi anggaran pengguna akan menerima rekomendasi yang lebih rendah.

------------------------------------------------------------------------

# KB-03 Rating

Game dengan rating Steam yang lebih tinggi lebih diminati.

Game dengan rating rendah seharusnya jarang menerima rekomendasi tinggi.

------------------------------------------------------------------------

# KB-04 Waktu Bermain

Game yang perkiraan waktu bermainnya sesuai dengan preferensi pengguna akan menerima rekomendasi yang lebih tinggi.

------------------------------------------------------------------------

# KB-05 Genre

Genre bukanlah variabel fuzzy.

Genre hanya digunakan untuk menyaring kandidat game sebelum proses inferensi fuzzy dilakukan.

------------------------------------------------------------------------

# KB-06 Urutan Prioritas

Tingkat kepentingan setiap variabel adalah:

1.  Level PC
2.  Rating
3.  Anggaran
4.  Waktu Bermain

------------------------------------------------------------------------

# KB-07 Sangat Direkomendasikan (Highly Recommended)

Sebuah game hanya boleh diklasifikasikan sebagai **Sangat Direkomendasikan** apabila hampir seluruh kriteria penting cocok dengan preferensi pengguna.

------------------------------------------------------------------------

# KB-08 Direkomendasikan (Recommended)

Sebuah game diklasifikasikan sebagai **Direkomendasikan** jika sebagian besar kriteria cocok dan tidak ada ketidakcocokan yang kritis.

------------------------------------------------------------------------

# KB-09 Kurang Direkomendasikan (Less Recommended)

Digunakan ketika beberapa kriteria hanya sebagian yang cocok atau terdapat satu atau lebih faktor penting yang mengurangi kecocokan.

------------------------------------------------------------------------

# KB-10 Tidak Direkomendasikan (Not Recommended)

Diberikan apabila terdapat ketidakcocokan besar, terutama dalam hal kompatibilitas PC atau ada beberapa kriteria penting sekaligus yang tidak terpenuhi.

------------------------------------------------------------------------

# KB-11 Interpretasi Skor

Skor Rekomendasi:

        Skor Kategori
  --------- --------------------
      0--25 Tidak Direkomendasikan
     26--50 Kurang Direkomendasikan
     51--75 Direkomendasikan
    76--100 Sangat Direkomendasikan

------------------------------------------------------------------------

# KB-12 Konsistensi Aturan

-   Masukan yang serupa harus menghasilkan keluaran yang serupa.
-   Tidak boleh ada aturan yang saling bertentangan.
-   Setiap kombinasi masukan harus secara tepat memetakan pada satu keluaran.

------------------------------------------------------------------------

# KB-13 Skalabilitas

Menambahkan game baru ke dalam basis data tidak boleh mewajibkan adanya perubahan pada basis aturan fuzzy.

------------------------------------------------------------------------

# KB-14 Penjelasan (Explainability)

Setiap rekomendasi harus dapat dijelaskan menggunakan aturan pengetahuan (knowledge rules) ini daripada menggunakan skor sembarang yang tidak beralasan.

------------------------------------------------------------------------

# Kesimpulan

Keseluruhan basis aturan yang berjumlah 81 ini harus dihasilkan berdasarkan basis pengetahuan (knowledge base) ini demi memastikan konsistensi, kemudahan penjelasan (explainability), dan kemudahan pemeliharaan (maintainability).
