# Adapter Gemini dan Antigravity

## Antigravity

Untuk workspace, letakkan skill pada:

```text
.agents/skills/dosen-pembimbing-skripsi-ta/
```

Pastikan `SKILL.md` dan `references/` berada dalam folder skill. Antigravity dapat mengaktifkan skill secara otomatis atau melalui `/dosen-pembimbing-skripsi-ta`.

Lokasi global yang didukung pada Antigravity dapat menggunakan `~/.gemini/config/skills/dosen-pembimbing-skripsi-ta/`. Konfigurasi lokal selalu lebih aman untuk repository.

## Gemini CLI atau lingkungan pengembang

Gunakan lokasi `.agents/skills/` hanya jika versi CLI atau IDE yang digunakan mendukung Agent Skills. Jika tidak, jadikan repository sebagai context atau instruction source dan berikan file referensi secara eksplisit.

## Gemini App

Gemini App tidak dapat diasumsikan memiliki mekanisme skill yang identik dengan Antigravity atau Gemini CLI. Jika fitur attachment/instruction tersedia:

1. unggah `SKILL.md`;
2. unggah referensi yang dibutuhkan;
3. perintahkan model untuk mengikuti isi skill;
4. unggah berkas penelitian pengguna secara terpisah dan hanya untuk sesi yang bersangkutan.

## Pembeda produk

- Gemini App: mekanisme UI dan akun menentukan akses.
- Gemini CLI/Code Assist: dapat mendukung workspace instructions atau Agent Skills bergantung pada versi.
- Antigravity: mendukung `.agents/skills/` dan global skill sesuai dokumentasi produk.

Status kompatibilitas harus diperbarui setelah pengujian terhadap versi yang digunakan.
