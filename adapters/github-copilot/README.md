# Adapter GitHub Copilot

## Lokasi project

GitHub Copilot mendukung Agent Skills pada lokasi project seperti:

```text
.github/skills/dosen-pembimbing-skripsi-ta/
.agents/skills/dosen-pembimbing-skripsi-ta/
.claude/skills/dosen-pembimbing-skripsi-ta/
```

Pilih lokasi yang didukung versi/surface Copilot yang digunakan. Jika repository ini sendiri digunakan sebagai lokasi skill, pertahankan satu folder project dan hindari duplikasi salinan antar lokasi.

## Pemanggilan

Copilot dapat mengaktifkan skill otomatis berdasarkan deskripsi atau instruksi pengguna dapat menyebut nama skill secara eksplisit.

Contoh:

```text
Gunakan skill dosen-pembimbing-skripsi-ta untuk meninjau konsistensi Bab III dan Bab IV.
```

## Lokasi personal

Lokasi personal bergantung pada Copilot app/CLI/IDE dan tidak semua surface cloud dapat mengaksesnya. Gunakan setup guide yang sesuai dan jangan mengasumsikan bahwa personal skill tersedia dalam cloud sandbox.

## Ketersediaan referensi

Pastikan folder `references/` ikut terpasang. Jika reference tidak tersedia, GitHub Copilot harus membacanya dari repository atau meminta pengguna menyediakannya.
