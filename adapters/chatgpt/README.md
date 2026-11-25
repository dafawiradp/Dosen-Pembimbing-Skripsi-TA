# Adapter ChatGPT

## Skills melalui API atau runtime yang mendukung

OpenAI Skills kompatibel dengan struktur folder berisi `SKILL.md`. Zipping harus menghasilkan satu folder top-level:

```text
dosen-pembimbing-skripsi-ta/
├── SKILL.md
└── references/
```

Unggah ZIP melalui API atau runtime yang mendukung Skills. Setelah skill terpasang, instruksikan model secara eksplisit: `Gunakan skill dosen-pembimbing-skripsi-ta`.

Untuk local shell, berikan path folder skill kepada runtime; untuk hosted shell, gunakan skill reference sesuai konfigurasi API yang tersedia.

## ChatGPT dengan file/instruction

Jika akun tidak memiliki fitur Skills:

1. unggah atau tempelkan `SKILL.md` sebagai instruksi konteks;
2. unggah file referensi yang relevan;
3. katakan bahwa referensi akademik harus dibaca sebelum menjawab;
4. lampirkan dokumen skripsi atau data hanya melalui mekanisme file pengguna.

Tidak semua antarmuka ChatGPT mendukung zip skill, system instruction, atau tool analysis. Jangan mengklaim dukungan yang belum tersedia.

## Penggunaan ZIP

Gunakan `python scripts\validate_skill.py --package dosen-pembimbing-skripsi-ta.zip`. Pastikan ZIP tidak berisi file pribadi atau data penelitian.
