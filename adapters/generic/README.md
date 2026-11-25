# Adapter Universal

Gunakan adapter ini untuk agent yang tidak mendukung Agent Skills secara native.

## 1. Pemuatan instruksi

Berikan isi `SKILL.md` sebagai system instruction, developer instruction, atau konteks agent. Jika platform memiliki batas ukuran:

1. muat ringkasan workflow inti;
2. muat referensi yang relevan sesuai permintaan;
3. jangan kehilangan aturan anti-halusinasi dan konfirmasi.

## 2. Pemuatan referensi

Unggah atau salin file `references/` yang relevan. Agent tidak perlu memuat seluruh referensi untuk setiap pertanyaan. Berikan path yang dapat dibaca bila environment mendukung file access.

## 3. Aktivasi

Perintahkan:

```text
Ikuti seluruh aturan pada SKILL.md dan referensi yang relevan.
Gunakan status bukti dan protokol konfirmasi.
Jika sumber atau data tidak tersedia, nyatakan keterbatasannya.
```

## 4. Fallback

- tanpa pencarian web: jangan mengarang sumber;
- tanpa Python: lakukan analisis sederhana atau nyatakan keterbatasan;
- tanpa file reader: minta cuplikan atau berkas relevan;
- tanpa pedoman institusi: gunakan format netral dan minta pedoman.

## 5. Penggabungan satu file

Jika hanya satu file diperbolehkan, gabungkan `SKILL.md` dengan bagian referensi yang relevan ke dalam urutan:

1. frontmatter dan instruksi inti;
2. integritas dan konfirmasi;
3. referensi yang dibutuhkan;
4. checklist akhir.
