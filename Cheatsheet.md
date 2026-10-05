
### 2. Salin ini untuk `CHEATSHEET.md`

```markdown
# 📜 Cheat Sheet: Cyber Infiltration

Panduan cepat perintah Linux yang digunakan dalam game ini.

## 📁 Navigasi & File
| Perintah | Contoh | Keterangan |
| :--- | :--- | :--- |
| `ls` | `ls` atau `ls -a` | Lihat isi folder (`-a` untuk file tersembunyi) |
| `cd` | `cd /var/log` | Pindah ke direktori lain |
| `cat` | `cat auth.log` | Baca isi file teks |
| `grep` | `grep ERROR syslog` | Cari kata tertentu dalam file |
| `find` | `find /var -name key.txt` | Cari file secara rekursif |

## ⚙️ Sistem & Manipulasi
| Perintah | Contoh | Keterangan |
| :--- | :--- | :--- |
| `chmod` | `chmod +x script.sh` atau `chmod 777 file` | Ubah izin akses file |
| `./` | `./script.sh` | Jalankan file yang memiliki izin eksekusi |
| `gzip` | `gzip data.txt` | Kompres file menjadi `.gz` |
| `tar` | `tar -xvf backup.tar` | Ekstrak file arsip `.tar` |
| `ps` | `ps` | Lihat daftar proses yang berjalan |
| `kill` | `kill 999` | Hentikan proses berdasarkan PID |

## 🌐 Jaringan & Environment
| Perintah | Contoh | Keterangan |
| :--- | :--- | :--- |
| `curl` | `curl http://localhost/api` | Ambil data dari URL/API |
| `export`| `export KEY=123` | Buat variabel lingkungan |
| `echo` | `echo $KEY` | Tampilkan isi variabel |

## 🎮 Perintah Khusus Game
- `submit [jawaban]` : Validasi misi untuk naik level.
- `level [1-10]` : Lompat ke level tertentu (Mode Debug).
- `restart` : Ulangi level saat ini dari awal.
- `exit` : Keluar dari game.