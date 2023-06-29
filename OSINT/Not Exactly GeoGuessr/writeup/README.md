# Writeup Not Exactly GeoGuessr

Ini foto Yujin, member dari IVE, girl group Korea Selatan. Karena gambarnya pixellated, kita perlu reverse image search dulu untuk cari gambar originalnya supaya bisa ngeliat konten gambarnya dengan jelas.

Nanti akan didapatkan foto originalnya, dan satu-satunya clue yang bisa membantu mencari lokasinya adalah street sign di atas Yujin.

![Alt text](./image.png)

Butuh sedikit ketelitian untuk baca kalau itu "Jamwon Hangang Park", yang lokasinya ada di Seoul. Kita buka di Google Maps:

![Alt text](image-1.png)

Oke, karena fotonya ada di sekitar Jamwon Hangang Park, kita cuma perlu cari di "pulau" yang ada Jamwon Hangang Park nya. Kita bisa pakai clue toko Burberry untuk filtering:

![Alt text](image-2.png)

Well, bisa dilihat bahwa toko Burberry di dekat Jamwon Hangang Park tidak terlalu banyak, jadi kita bisa cari satu per satu aja. Also note hint di deskripsi bahwa foto jalan yang kita cari di Google Street View sudah outdated 5 tahun, sehingga perlu ketelitian lebih untuk cari lokasinya.

Eventually, kita akan menemukan tempat ini:
![Alt text](image-3.png)

![Alt text](image-4.png)

Sekilas kelihatan beda karena ada satu gedung yang hilang, tapi kalau diteliti, ini adalah lokasi yang sama. Bisa dilihat dengan comparison ini:

![Alt text](image-7.png)

![Alt text](image-8.png)

- Dua gedung sama
- Ada pohon di depannya (walaupun di foto Yujin, pohonnya lagi mati karena musim dingin)
- Ada spot yang sama persis di lingkaran sebelah kanan

Oke, karena sudah dapat lokasinya, kita tinggal ambil nama jalan "behind her", yaitu Dosan-Daero dan di-format jadi `DosanDaero`. Jalan ini ada di district `Gangnam`, jadi flagnya `COMPFEST15{DosanDaero_Gangnam}`.