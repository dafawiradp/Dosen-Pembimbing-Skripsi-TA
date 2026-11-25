# Adapter Claude

## Claude Code

Letakkan folder skill pada salah satu lokasi project yang didukung Claude Code, misalnya:

```text
.claude/skills/dosen-pembimbing-skripsi-ta/
```

Pastikan `SKILL.md` berada tepat di dalam folder tersebut beserta seluruh folder `references/`. Panggil dengan `/dosen-pembimbing-skripsi-ta` atau biarkan Claude mengaktifkannya otomatis berdasarkan deskripsi skill.

## Claude.ai

Gunakan kemampuan Skills hanya jika tersedia pada akun atau lingkungan. Unggah folder atau ZIP yang memuat `SKILL.md` dan folder `references/`. Jika fitur upload belum tersedia, gunakan:

1. tempelkan isi `SKILL.md` sebagai instruksi proyek atau instruksi khusus;
2. unggah referensi yang relevan sebagai file konteks;
3. perintahkan Claude menggunakan skill secara eksplisit.

Jangan mengandalkan bahwa semua akun Claude.ai mendukung Skills.

## Packaging

Untuk ZIP, gunakan satu folder top-level bernama `dosen-pembimbing-skripsi-ta`. Jangan menyertakan `.git`, data penelitian, atau folder distribusi.

## Sumber kebenaran

Semua instruksi akademik berasal dari `../../SKILL.md` dan `../../references/`. Adapter ini hanya menjelaskan pemasangan dan pemanggilan.
