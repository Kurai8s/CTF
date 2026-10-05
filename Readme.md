# 🛡️ CYBER INFILTRATION: Terminal Adventure Game

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Platform-Linux%20%7C%20WSL-green?style=for-the-badge&logo=linux&logoColor=white" alt="Platform">
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="License">
</p>

<p align="center">
  <em>Sebuah simulasi terminal Linux berbasis teks (CLI) yang dirancang untuk mengajarkan perintah Linux/WSL melalui pengalaman bermain peran sebagai agen siber elit.</em>
</p>

---

## 🎯 Fitur Utama
- 🕹️ **10 Level Progresif**: Dari pengintaian dasar hingga manipulasi *environment variable*.
- 💻 **Simulasi File System Virtual**: Aman untuk dicoba, tidak merusak sistem asli Anda.
- ⌨️ **Perintah Nyata**: Kuasai `cd`, `ls`, `cat`, `grep`, `chmod`, `tar`, `gzip`, `ps`, `kill`, `curl`, `find`, `export`, dan `echo`.
- 🛠️ **Mode Debug**: Perintah `level [1-10]` dan `restart` untuk pengujian cepat.

## 🚀 Cara Menjalankan

Pastikan Anda memiliki **Python 3** terinstal di sistem Linux atau WSL Anda.

```bash
# 1. Clone repository ini
git clone https://github.com/Kurai8s/CTF.git
cd NAMA_REPO

# 2. Jalankan game
python3 game.py

🎮 Cheat Sheet Perintah
Perintah
Fungsi dalam Game
ls [-a]
Melihat isi direktori (tambahkan -a untuk file tersembunyi)
cd [dir]
Pindah direktori
cat / grep
Membaca dan mencari teks dalam file
chmod / tar / gzip
Manipulasi izin file dan arsip kompresi
ps / kill
Manajemen dan penghentian proses sistem
curl / find
Simulasi permintaan jaringan dan pencarian file rekursif
export / echo
Manipulasi environment variable
submit [jawaban]
Memvalidasi misi dan naik ke level berikutnya

🗺️ Peta Misi (Klik untuk melihat detail)
<details>
<summary><b>📡 Level 1: Reconnaissance (Pengintaian)</b></summary>
<br>
<strong>Misi:</strong> Temukan password admin yang tersembunyi di log sistem.<br>
<strong>Perintah Kunci:</strong> <code>cd</code>, <code>cat</code>, <code>grep</code><br>
<strong>Target Submit:</strong> <code>SHADOW_NET</code>
</details>

<details>
<summary><b>🔓 Level 2: Privilege Escalation (Eskalasi Hak Akses)</b></summary>
<br>
<strong>Misi:</strong> File script terkunci. Ubah izinnya, jalankan, dan ambil kuncinya.<br>
<strong>Perintah Kunci:</strong> <code>chmod +x</code>, <code>./[file]</code><br>
<strong>Target Submit:</strong> <code>ESCALATION_99</code>
</details>

<details>
<summary><b>📦 Level 3: Exfiltration (Ekstraksi Data)</b></summary>
<br>
<strong>Misi:</strong> Kompres data rahasia dan pindahkan ke tempat persembunyian.<br>
<strong>Perintah Kunci:</strong> <code>gzip</code>, <code>mv</code><br>
<strong>Target Submit:</strong> <code>DONE</code>
</details>

<details>
<summary><b>💀 Level 4: System Hijack (Pembajakan Sistem)</b></summary>
<br>
<strong>Misi:</strong> Matikan proses firewall musuh yang memblokir akses root.<br>
<strong>Perintah Kunci:</strong> <code>ps</code>, <code>kill [PID]</code><br>
<strong>Target Submit:</strong> <code>FLAG_ROOT</code>
</details>

<details>
<summary><b>🌐 Level 5: Network Recon (Rekonstruksi Jaringan)</b></summary>
<br>
<strong>Misi:</strong> Ambil token rahasia dari API lokal.<br>
<strong>Perintah Kunci:</strong> <code>curl</code><br>
<strong>Target Submit:</strong> <code>SECRET_TOKEN_77</code>
</details>

<details>
<summary><b>🔍 Level 6: Forensics (Forensik Digital)</b></summary>
<br>
<strong>Misi:</strong> Temukan file yang hilang di antara tumpukan direktori.<br>
<strong>Perintah Kunci:</strong> <code>find [dir] -name [file]</code><br>
<strong>Target Submit:</strong> <code>FORENSIC_MASTER</code>
</details>

<details>
<summary><b>📊 Level 7: Log Analysis (Analisis Log)</b></summary>
<br>
<strong>Misi:</strong> Hitung berapa kali pola "ERROR" muncul di syslog.<br>
<strong>Perintah Kunci:</strong> <code>grep -c</code><br>
<strong>Target Submit:</strong> <code>3</code>
</details>

<details>
<summary><b>👻 Level 8: Hidden & Octal (Tersembunyi & Oktal)</b></summary>
<br>
<strong>Misi:</strong> Akses file konfigurasi tersembunyi dan ubah izinnya secara paksa.<br>
<strong>Perintah Kunci:</strong> <code>ls -a</code>, <code>chmod 777</code><br>
<strong>Target Submit:</strong> <code>OCTAL_KEY_88</code>
</details>

<details>
<summary><b>📂 Level 9: Archiving (Pengarsipan)</b></summary>
<br>
<strong>Misi:</strong> Ekstrak payload arsip dan baca isinya.<br>
<strong>Perintah Kunci:</strong> <code>tar -xvf</code><br>
<strong>Target Submit:</strong> <code>ARCHIVE_MASTER_99</code>
</details>

<details>
<summary><b>👑 Level 10: Environment Variables (Variabel Lingkungan)</b></summary>
<br>
<strong>Misi:</strong> Set variabel sistem, verifikasi nilainya, dan klaim kemenangan.<br>
<strong>Perintah Kunci:</strong> <code>export</code>, <code>echo $VAR</code><br>
<strong>Target Submit:</strong> <code>CYBER_GOD_10</code>
</details>

🛠️ Kontribusi
Project ini dibuat sebagai alat edukasi interaktif. Kontribusi untuk menambah level, perintah baru, atau perbaikan bug sangat dipersilakan melalui Pull Request.
<p align="center">
<sub>Dibuat dengan 💻 dan ☕ oleh <strong>My Lord</strong></sub>
</p>