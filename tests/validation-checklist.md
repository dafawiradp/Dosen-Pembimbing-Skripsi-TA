# Validation Checklist

## Metadata dan struktur

- [ ] `SKILL.md` valid dan memiliki name `dosen-pembimbing-skripsi-ta`.
- [ ] description jelas dan maksimal 1024 karakter.
- [ ] nama parent folder dan metadata name konsisten.
- [ ] seluruh referensi wajib tersedia.
- [ ] seluruh adapter tersedia.

## Instruksi akademik

- [ ] alur masalah sampai kesimpulan tersedia.
- [ ] metode, data, hasil, pembahasan, dan kesimpulan dibedakan.
- [ ] integritas data dicakup.
- [ ] source verification dicakup.
- [ ] citation management dicakup.

## Anti-halusinasi

- [ ] larangan mengarang jurnal, DOI, kutipan, data, dan hasil tersedia.
- [ ] fakta, data pengguna, perhitungan, interpretasi, hipotesis, dan ketidaktahuan dibedakan.
- [ ] sumber yang tidak ditemukan dinyatakan dengan status jelas.

## Konfirmasi

- [ ] perubahan substansial memerlukan konfirmasi.
- [ ] penyuntingan minor dapat dilakukan langsung.
- [ ] format masalah, rekomendasi, alasan, dampak, dan konfirmasi tersedia.

## Cross-platform

- [ ] adapter tidak menduplikasi aturan akademik.
- [ ] Claude, Gemini/Antigravity, ChatGPT, Copilot, dan generic dijelaskan.
- [ ] fallback untuk pencarian, Python, dan file dibahas.
- [ ] status produk yang belum diverifikasi ditandai.

## Packaging

- [ ] ZIP memiliki satu folder top-level.
- [ ] package berisi `SKILL.md`, referensi, dan script yang perlu.
- [ ] package tidak berisi `.git`, data pribadi, atau berkas skripsi pengguna.
