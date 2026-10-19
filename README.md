# kuru — Studio kuru

Beranda web pribadi untuk kuru (developer, artist, animator). Menampilkan nama, bio singkat, penganalan suka cita, skills (CapCut, coding, manajemen proyek, Krita, Ibis Paint, Adobe Premiere Pro, After Effects), serta link Discord, GitHub, dan Spotify.

## Sorotan Fitur

- **Gamifikasi & Interaktif:** button klik masuk berfungsi sebagai suara pintu kayu, garis hujan animasi di latar belakang, secara otomatis mengisi galeri animasi, mendeteksi status aktivis Discord melalui API Lanyard, sehingga ~memori dinamis + waktu nyata~ hidup di halaman ini. Pada konfigurasi default, memprioritaskan privasi dan menyembunyikan status saat orang asing mengunjungi.

- **Audio dunia lain (tidak menghalangi):** Aplikasi pemutar audio di pojok kanan bawah — menampilkan visualizer, memutar `bgm.m4a` setelah klik masuk (update otomatis disiapkan). Auto-play ditolak browser; pengguna berinteraksi terlebih dahulu diperlukan. Bisa mengulangi, berhenti, dan menampilkan pesan darurat saat berkas tidak ditemukan.

- **Portofolio & aset:** Showcase karya animasi (gambar beserta info sketsa yang acak ditampilkan di "Specials"), Skills grid bergaya tab dengan visualisasi kemajuan (ikon yang sesuai, label, dan persentase). Avatar dapat diganti hanya dengan mengubah nama file `kuru.gif` (sebelumnya SVG), asset berubah tanpa mengubah HTML.

- **Narasi yang mengalir:** Secara otomatis mengetik loop animator (`developer` > `artist` > `animator` > `suami nya vestia zeta 💙`) dengan efek cursor berkedip dan transisi halus; menangani flag motion-reduced browser tanpa animasi.

## Jalankan di localhost

Buka `index.html` langsung di browser (file://), atau siapkan server statis (`npx http-server .`).

Mendesain & mengode situs ini sepenuhnya dengan tangan tanpa menggunakan AI — didorong oleh kode plain HTML/CSS/JS yang terstruktur, dengan preview animations, asset dinamis, dan UI sederhana, melakukan penyimpangan minimal dengan UX yang ramah pengguna, gerakan yang halus, dan menggunakan pahlawan CSS/JS yang baik, menerapkan umpan balik pengguna yang menghindari klik berulang tanpa perlu, dan menerapkan motion-reduced / perilaku aksesibilitas.

## Aset

- Semua media (mp4, m4a, gif, gambar) hanya untuk akses internal saja; tidak ada pengunggahan publik di repo.
- Logo dibuat di Krita/Adobe Illustrator, animasi di After Effects, situs dibuat di VS Code.
- Bot Discord: Ibutsu — layanan autentikasi, admin portal, dan admin Discord (khusus di sini).
- Kirim masukan + lapor bug di DM Discord himmell_ (track, halaman berikutnya, respons penuh segera tersedia).

## Disimpan dalam file (skrip & bonus tersembunyi)

- `check-portal.py` — memeriksa prasyarat situs (audio, src Discord).
- `images/*.jpg|png|svg` — avatar, logo, dan asset visual yang disorot dari berbagai proyek (kuru, Senyawa, Jarnix, komisaris Ocean, Forest).
- `index.html` mencakup koneksi API Lanyard streaming, bagian animasi, sistem mouse-tracking, musik & emotion yang memiliki konteks, metadata Spotify saat ini (terhubung ke lanyard).

**Model:** minimalist, persisten, mengurangi ketergantungan eksternal, mengatur terlebih dahulu dan membiarkan HTML yang mengatur. Tidak ada kerangka kerja eksternal selain browser API inti, pahlawan CSS, transformasi sederhana di tempat yang tepat, tanpa nuansa desain berat, fokus pada keamanan non-clickjacking, dan bersifat static-first.

Sederhanakan satu hal pada satu waktu; solusi yang berkelanjutan untuk hidup yang mereka dapatkan.

Hak Cipta © 2026 kuru (developer/seniman/animator) – Anime Lover