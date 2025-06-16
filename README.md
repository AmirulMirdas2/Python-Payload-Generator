# Python Payload Generator

Sebuah alat bantu baris perintah (CLI) yang ditulis dengan Python untuk membuat payload *code injection* yang ter-obfuscate secara otomatis. Alat ini dirancang untuk membantu para peneliti keamanan dan pemain CTF dalam mempelajari dan mem-bypass filter keamanan sederhana.

---

### ⚠️ Peringatan Penggunaan & Penafian (Disclaimer)

**Alat ini dibuat murni untuk tujuan edukasi dan penelitian keamanan dalam lingkungan yang sah dan terkontrol (seperti platform CTF atau laboratorium pribadi).**

Penulis tidak bertanggung jawab atas segala bentuk penyalahgunaan atau kerusakan yang disebabkan oleh penggunaan alat ini. Penggunaan alat ini untuk menyerang target yang tidak Anda miliki izinnya adalah tindakan ilegal. **Gunakan dengan risiko Anda sendiri.**

---

### ✨ Fitur

* **Mode Ganda:** Mendukung dua mode pembuatan payload:
    1.  **Mode Sederhana:** Untuk perintah dasar seperti `open('file.txt').read()`.
    2.  **Mode Lanjutan:** Untuk perintah berantai yang lebih kompleks seperti `__import__('os').popen('ls').read()`.
* **Obfuscation `chr()`:** Secara otomatis mengubah semua string (nama fungsi, argumen, metode) menjadi format `chr()` untuk mem-bypass filter naif yang memblokir kata kunci.
* **Interaktif:** Antarmuka baris perintah yang mudah digunakan untuk pembuatan payload secara cepat.

---

### 🚀 Instalasi & Persyaratan

Tidak diperlukan instalasi khusus. Anda hanya memerlukan **Python 3.x** yang sudah terpasang di sistem Anda.

Kloning repositori ini:
```bash
git clone https://github.com/AmirulMirdas2/Python-Payload-Generator.git
cd Python-Payload-Generator
```

---

### ⚙️ Cara Penggunaan

Jalankan skrip dari terminal Anda:
```bash
python payload_generator.py
```

Program akan menampilkan menu untuk memilih mode yang diinginkan. Cukup ikuti instruksi di layar.

**Contoh Sesi:**
```
Pilih mode generator:
  1. Mode Sederhana (misal: open('file.txt').read())
  2. Mode Lanjutan  (misal: __import__('os').popen('ls').read())
  (Ketik 'exit' atau 'quit' untuk keluar)
Pilihan mode (1 atau 2) > 2

Masukkan perintah lanjutan > __import__('os').popen('ls').read()

[+] Parsing (Mode Lanjutan) berhasil:
    - Fungsi 1: __import__ (Arg: os)
    - Fungsi 2: popen (Arg: ls)
    - Fungsi 3: read

✅ Payload Anda Siap:
------------------------------------------
getattr(__builtins__, chr(95)+...).__getattribute__(chr(112)+...)(chr(108)+...).__getattribute__(chr(114)+...)()
------------------------------------------
```

---

### 📝 Lisensi

Proyek ini dilisensikan di bawah **MIT License**. Lihat file `LICENSE` untuk detailnya.
