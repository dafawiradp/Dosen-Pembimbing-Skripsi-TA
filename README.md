# Dosen Pembimbing Skripsi/TA

Repository ini menyediakan satu Agent Skill lintas platform untuk membimbing penyusunan skripsi atau tugas akhir secara akademis, kritis, sistematis, dan berbasis bukti.

## Tujuan

- membantu perencanaan penelitian dan pemetaan gap;
- mendukung desain metodologi dan pertanyaan penelitian;
- membantu tinjauan pustaka, pencarian sumber, sitasi, dan novelty;
- mendukung pengelolaan serta analisis data;
- membantu pembahasan ilmiah, konsistensi naskah, dan proofreading;
- menekankan anti-halusinasi, integritas data, dan konfirmasi pengguna.

## Fitur utama

- satu sumber instruksi utama: `SKILL.md`;
- referensi modular sesuai kebutuhan;
- adapter untuk Claude, Gemini/Antigravity, ChatGPT, GitHub Copilot, dan agent umum;
- script validasi metadata dan tautan internal;
- paket ZIP distribusi;
- test cases dan checklist validasi.

## Arsitektur

```text
SKILL.md                 # sumber instruksi utama
references/              # prosedur akademik modular
adapters/                # instruksi pemasangan per platform
scripts/validate_skill.py
tests/
.github/workflows/
```

Perubahan aturan pembimbingan dilakukan pada `SKILL.md` atau referensi yang relevan. Adapter tidak boleh menyalin atau membuat aturan akademik alternatif.

## Status kompatibilitas

| Platform | Metode Instalasi | Status |
|---|---|---|
| Claude Code | Project skill atau paket kompatibel | Native support |
| Claude.ai | Skills upload jika fitur tersedia pada akun | Compatible with adapter |
| Antigravity | `.agents/skills/dosen-pembimbing-skripsi-ta/` atau skill global | Native support |
| Gemini | Bergantung pada produk; manual injection atau kompatibilitas Agent Skills | Not verified per product |
| ChatGPT | OpenAI Skills API atau upload/workflow yang mendukung file | Compatible with adapter |
| GitHub Copilot | `.github/skills/`, `.agents/skills/`, atau lokasi personal yang didukung | Native support |
| Generic Agent | Masukkan `SKILL.md` dan referensi sebagai instruksi/file | Manual installation |

Status menunjukkan hasil verifikasi dokumentasi umum, bukan jaminan bahwa setiap versi atau akun memiliki fitur yang sama. Detail: lihat `adapters/`.

## Instalasi cepat

### Claude Code

Salin repository ke folder project:

```text
.claude/skills/dosen-pembimbing-skripsi-ta/
```

Kemudian panggil `/dosen-pembimbing-skripsi-ta` atau biarkan Claude mengaktifkannya secara otomatis.

### GitHub Copilot

Salin atau letakkan skill pada salah satu lokasi project yang didukung, misalnya:

```text
.github/skills/dosen-pembimbing-skripsi-ta/
.agents/skills/dosen-pembimbing-skripsi-ta/
```

Verifikasi lokasi yang didukung oleh versi Copilot yang digunakan.

### Antigravity

Letakkan skill pada:

```text
.agents/skills/dosen-pembimbing-skripsi-ta/
```

Untuk skill global, gunakan lokasi yang berlaku pada instalasi Antigravity; lihat `adapters/gemini/README.md`.

### Claude.ai, Gemini, atau ChatGPT

Ikuti `adapters/<platform>/README.md`. Jika fitur native tidak tersedia, gunakan paket ZIP atau salin isi instruksi dan referensi yang relevan ke system instruction serta unggah file pendukung.

## Packaging

Validasi repository:

```powershell
python scripts\validate_skill.py
```

Buat paket distribusi:

```powershell
python scripts\validate_skill.py --package dist\dosen-pembimbing-skripsi-ta.zip
```

Paket berisi satu folder skill dengan `SKILL.md`, `LICENSE`, `references/`, dan `scripts/`. File pengujian, adapter, dokumentasi repository, dan konfigurasi GitHub tidak dimasukkan.

## Pengujian

Lihat:

- `tests/test-cases.md`
- `tests/validation-checklist.md`

Jalankan validasi otomatis pada Python 3.11+:

```powershell
python scripts\validate_skill.py
```

## Pengembangan

1. ubah sumber utama atau referensi;
2. jalankan validasi;
3. ujikan skenario regresi;
4. perbarui changelog;
5. buka pull request.

Lihat `CONTRIBUTING.md`.

## Lisensi

Repository dilisensikan dengan MIT License. Lihat `LICENSE`.
