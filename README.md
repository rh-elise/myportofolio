Nama : Rheina Uliana

NPM : 2506600801

Kelas : PBP A

# My Portfolio

Portfolio website yang dibuat menggunakan Django dengan pendekatan desain **Neo-Brutalism**. Proyek ini dibuat sebagai bagian dari Tugas 1.

## Instruksi Setup

Ikuti langkah-langkah berikut untuk menjalankan proyek secara lokal.

### 1. Clone Repository

Clone repository ini ke komputer lokal:

```bash
git clone https://github.com/rh-elise/myportofolio.git
```

### 2. Masuk ke Direktori Proyek

```bash
cd myportofolio
```

### 3. Aktifkan Virtual Environment

**Windows:**

```bash
env\Scripts\activate
```

**Mac/Linux:**

```bash
source env/bin/activate
```

### 4. Install Dependencies

Install seluruh dependencies yang dibutuhkan:

```bash
pip install -r requirements.txt
```

### 5. Jalankan Server Django

```bash
python manage.py runserver
```

### 6. Buka Website

Setelah server berhasil dijalankan, buka browser dan akses:

`http://localhost:8000/`

---

## Contoh Data Dummy (untuk Testing)

Jika ingin mencoba mengisi database dengan beberapa data contoh, buka Django shell terlebih dahulu:

```bash
python manage.py shell
```

Setelah shell terbuka, jalankan kode-kode berikut sesuai model yang ingin diisi.

### Artworks

```python
from main.models import Artworks

# --- Kategori: Monochrome ---
Artworks.objects.create(
    title="Tipsy",
    image="/static/img/art-tipsy.jpg",
    category="Monochrome",
)

Artworks.objects.create(
    title="Roman",
    image="/static/img/art-roman.jpg",
    category="Monochrome",
)

# --- Kategori: Animation ---
Artworks.objects.create(
    title="Minor Piece",
    video="/static/img/art-minor-piece.mp4",
    category="Animation",
)

Artworks.objects.create(
    title="Agate Caressing The Night",
    video="/static/img/art-agate-caressing-the-night.mp4",
    category="Animation",
)

# --- Kategori: Rendered ---
Artworks.objects.create(
    title="Profile Picture 1",
    image="/static/img/art-profile-picture-1.jpg",
    category="Rendered",
)

Artworks.objects.create(
    title="Profile Picture 2",
    image="/static/img/art-profile-picture-2.jpg",
    category="Rendered",
)

Artworks.objects.create(
    title="Lab 3 DDP0 26",
    image="/static/img/art-lab-3-ddp0-26.jpg",
    category="Rendered",
)

# --- Kategori: Pixel ---
Artworks.objects.create(
    title="RISTEK Submission",
    image="/static/img/art-ristek-submission-spritesheet.png",
    category="Pixel",
)

Artworks.objects.create(
    title="Necronomi Jam Clam",
    image="/static/img/art-necronomi-jam-clam-spritesheet.png",
    category="Pixel",
)
```

### Projects

```python
from main.models import Projects

Projects.objects.create(
    title="Wait, New Rule!",
    description="A 2.5D platformer where you dodge hazards including a floor that is literally lava. Just when you feel safe, a new card rule drops and changes everything.",
    image="/static/img/cover-wait-new-rule.png",
    link="https://marlioboro.itch.io/wait-new-rules"
)

Projects.objects.create(
    title="Brine & Blade",
    description="A top-down 2D roguelite bullet-hell starring a pirate dragged into a cosmic abyss. Slash through bullet storms, parry what you cannot dodge, and fight your way back to the surface.",
    image="/static/img/cover-brine-and-blade.png",
    link="https://marlioboro.itch.io/brine-and-blade"
)

Projects.objects.create(
    title="Where Do You Belong?",
    description="A puzzle deduction game where you work as a train conductor guiding living passengers and lost souls to where they belong. Inspect identities by day, uncover the dead by night, and make every decision count.",
    image="/static/img/cover-where-do-you-belong.png",
    link="https://mir4na.itch.io/where-do-you-belong"
)
```

### Experience

```python
from main.models import Experience

Experience.objects.create(
    title="Teaching Assistant – Calculus I (Short Semester)",
    category="volunteer",
    year=2026,
    status="completed",
    description="Supported student comprehension of fundamental calculus concepts through guided tutorial sessions and assignment grading during an intensive short-semester course."
)
```

Setelah selesai menambahkan data, keluar dari shell dengan:

```python
exit()
```

---

## Pengungkapan Penggunaan AI (AI Disclosure) & Catatan Pengerjaan

### Pesan Singkat untuk Kak Asdos

Halo Kak! Kalau di Tugas 1 kemarin saya sempat meminta maaf karena cukup banyak mengandalkan *vibecoding* karena *deadline*, di Tugas 2 ini saya mencoba untuk benar-benar mengubah cara saya mengerjakan tugas.

Sekarang saya mencoba membuat dan memahami kodenya sendiri sebisa saya. Kalau sudah bingung atau menemukan error yang belum saya mengerti, baru saya bertanya kepada AI. Jadi, saya masih menggunakan AI, tetapi saya mencoba untuk tidak langsung meminta AI mengerjakan semuanya.

Untuk bagian UI, saya masih cukup banyak menggunakan bantuan AI, terutama untuk implementasi CSS, *responsive layout*, dan beberapa perbaikan tampilan. Namun, desain dan arahan mengenai tampilan tetap saya tentukan sendiri. Saya juga mencoba membaca *script* yang diberikan AI dan memahami bagian-bagiannya sebisa saya, walaupun saya masih cukup awam tentang hal tersebut.

### Kapan Saya Menggunakan AI di Tugas Ini?

Saya menggunakan AI terutama ketika menemukan hal yang belum saya pahami, mengalami error, atau ketika ada pekerjaan yang cukup repetitif.

Beberapa contohnya adalah:

* **Troubleshooting Error & Routing:** Ketika menemukan *error* di terminal atau masih bingung mengenai hubungan `urls.py` pada proyek dengan `urls.py` pada aplikasi, saya menggunakan AI untuk membantu menjelaskan masalah dan alur *routing* tersebut.
* **Membantu Pekerjaan Repetitif:** Saya menggunakan AI untuk membantu melakukan perubahan yang cukup banyak dan berulang, misalnya ketika mengganti penamaan dari `arts` menjadi `artworks` di beberapa bagian project.
* **UI dan CSS:** Untuk implementasi tampilan, saya masih banyak menggunakan bantuan AI, terutama dalam mengatur CSS, posisi elemen, dan *responsive layout*. Saya memberikan arahan mengenai tampilan yang saya inginkan, kemudian menggunakan hasil dari AI sebagai dasar untuk diperbaiki kembali.
* **JavaScript:** Saya juga menggunakan AI ketika ingin memahami atau membuat beberapa interaksi sederhana pada frontend, terutama yang berkaitan dengan event dari mouse dan keyboard.

### Evaluasi Penggunaan AI

Dari Tugas 2 ini, saya merasa cara saya menggunakan AI sudah cukup berbeda dibandingkan Tugas 1. Saya mulai menyadari bahwa kalau langsung meminta AI membuat semuanya, saya memang bisa mendapatkan hasil lebih cepat, tetapi saya sendiri jadi kurang memahami kode yang digunakan.

Karena itu, kali ini saya mencoba membiasakan diri untuk mencari tahu terlebih dahulu sebelum bertanya kepada AI. Ketika akhirnya meminta bantuan AI, saya juga mencoba membaca *script* yang diberikan dan memahami sebisanya. Walaupun masih banyak bagian yang belum saya pahami sepenuhnya, setidaknya saya mulai terbiasa melihat kode dan mencoba mencari tahu fungsi dari setiap bagiannya.

Beberapa hal baru yang saya pahami selama pengerjaan adalah:

* **Modularitas HTML (`include`):** Saya baru mengetahui bahwa file HTML yang panjang dapat dipisahkan menjadi beberapa file yang lebih kecil, misalnya untuk *navbar* atau *footer*, kemudian digunakan kembali dengan `{% include 'nama_file.html' %}`. Menurut saya, ini cukup membantu karena struktur file menjadi lebih rapi dan tidak semuanya berada dalam satu file HTML.

* **Event pada JavaScript:** Saya juga mulai memahami sedikit mengenai bagaimana JavaScript dapat mendeteksi suatu event, misalnya ketika mouse digerakkan atau ketika tombol keyboard ditekan. Sebelumnya saya belum terlalu memahami bagaimana interaksi seperti itu bisa dibuat pada website.

### Proses Pengerjaan

Secara umum, proses pengerjaan Tugas 2 saya lakukan melalui beberapa tahap:

1. **Mencoba Implementasi Sendiri**

   Saya mencoba menerapkan materi tersebut ke project saya sendiri. Saya berusaha menulis kode dan memahami alurnya terlebih dahulu sebelum meminta bantuan.

2. **Mencari Bantuan Ketika Menemui Masalah**

   Jika saya menemukan error atau tidak tahu bagaimana cara melanjutkan, saya baru menggunakan AI untuk bertanya mengenai masalah tersebut. Saya mencoba memberikan konteks dan kode yang sedang saya kerjakan agar bantuan yang diberikan lebih sesuai dengan masalahnya.

3. **Implementasi dan Perbaikan UI**

   Untuk bagian UI, saya masih menggunakan cukup banyak bantuan AI dalam menerjemahkan desain menjadi HTML dan CSS, termasuk membuat tampilan *responsive*. Saya kemudian melihat hasilnya dan memberikan arahan jika tampilannya belum sesuai dengan desain yang saya inginkan.

54. **Mencoba Memahami Hasil Kode**

   Setelah mendapatkan solusi atau kode dari AI, saya mencoba membaca dan memahami *script* tersebut sebisa saya. Walaupun saya masih awam dan belum memahami semua bagian, proses ini membuat saya mulai lebih terbiasa membaca kode daripada hanya langsung menggunakannya.

Dari keseluruhan proses ini, saya merasa ada perubahan dari cara saya mengerjakan Tugas 1. Saya masih menggunakan AI dan untuk bagian UI bahkan masih banyak bergantung pada bantuan AI, tetapi sekarang saya mencoba untuk tidak langsung menyerahkan seluruh proses pengerjaan kepadanya. Saya mencoba belajar dari tutorial, mengerjakan sendiri terlebih dahulu, lalu menggunakan AI ketika memang membutuhkan bantuan.

### Styling README.md

Saya juga menggunakan AI untuk membantu merapikan format dan struktur penulisan `README.md` ini agar lebih mudah dibaca. Isi dan pengalaman yang dituliskan tetap berdasarkan proses pengerjaan yang saya lakukan sendiri.

### Log Obrolan AI

1. [Link Chat 1](https://opncd.ai/share/B04zqg7p)

---

# Pertanyaan Reflektif

## Tugas 2

### 1. Alur Request-Response (MVT) pada Django

Ketika pengguna membuka halaman portofolio, browser terlebih dahulu mengirimkan HTTP request ke website. Request tersebut akan diterima oleh `urls.py` utama pada proyek Django, yang kemudian menentukan aplikasi mana yang menangani URL tersebut. Setelah diarahkan ke `urls.py` milik aplikasi portofolio, URL tersebut dicocokkan dengan pola yang tersedia dan Django akan memanggil view yang sesuai. Jika URL memiliki parameter tertentu, misalnya ID sebuah project, parameter tersebut juga dapat diteruskan ke view agar data yang diproses sesuai dengan project yang diminta.

Selanjutnya, view menangani logika yang diperlukan untuk menampilkan halaman. Jika halaman membutuhkan data dari database, view akan meminta data tersebut melalui model. Model menjadi penghubung antara aplikasi dengan database, sehingga data project dapat diambil tanpa harus ditulis langsung di dalam HTML.

Setelah mendapatkan data yang dibutuhkan, view meneruskannya ke template. Template kemudian menggunakan data tersebut untuk membentuk halaman HTML yang akan ditampilkan kepada pengguna. Hasil akhirnya dikirim kembali sebagai HTTP response ke browser, sehingga pengguna dapat melihat halaman portofolio beserta data project yang sesuai.

Dari alur ini saya memahami bahwa setiap bagian dalam MVT memiliki tanggung jawab yang berbeda. `urls.py` menentukan ke mana request diarahkan, view mengatur prosesnya, model menangani data, sedangkan template berfokus pada bagaimana data tersebut ditampilkan.

### 2. Mengapa Data (Model dan Temoplate) Dipisahkan?

Data untuk bagian portofolio sebaiknya disimpan pada model daripada ditulis langsung di dalam template karena data dan tampilan memiliki fungsi yang berbeda. Jika nama project, deskripsi, gambar, dan informasi lainnya ditulis langsung di dalam HTML, setiap perubahan atau penambahan project akan membuat saya harus mengubah kode template secara manual.

Hal ini berkaitan dengan keterbatasan static web yang saya temukan pada Tugas 1. Saat jumlah project masih sedikit, melakukan hardcode mungkin masih terasa mudah. Namun, jika jumlah project semakin banyak, cara tersebut akan menjadi semakin sulit untuk dipelihara karena data tersebar di dalam kode HTML.

Dengan menyimpan data pada model, saya dapat menggunakan satu template untuk menampilkan banyak project dari database menggunakan looping. Jika ingin menambahkan atau mengubah project, yang perlu diubah adalah datanya, bukan struktur HTML untuk setiap project. Menurut saya, cara ini membuat aplikasi lebih mudah dan siap untuk dikembangkan menjadi fitur yang lebih dinamis, seperti pencarian atau filter berdasarkan kategori.

### 3. Makemigrations vs Migrate

`makemigrations` dan `migrate` sama-sama berkaitan dengan perubahan struktur database, tetapi memiliki fungsi yang berbeda. `makemigrations` digunakan untuk membuat file migrasi berdasarkan perubahan yang dilakukan pada `models.py`. File tersebut berisi instruksi mengenai perubahan struktur database yang perlu dilakukan oleh Django.

Sementara itu, `migrate` digunakan untuk menerapkan instruksi dari file migrasi tersebut ke database. Jadi, `makemigrations` dapat dipahami sebagai proses mencatat perubahan model menjadi sebuah migrasi, sedangkan `migrate` adalah proses menjalankan perubahan tersebut pada database.

Sebagai contoh, jika saya menambahkan atribut baru bernama `link_github` pada model project, perubahan tersebut belum langsung membuat kolom baru pada database. Saya perlu menjalankan `makemigrations` terlebih dahulu agar Django membuat file migrasi yang mencatat perubahan tersebut. Setelah itu, saya menjalankan `migrate` agar perubahan tersebut benar-benar diterapkan pada database dan kolom `link_github` dapat digunakan untuk menyimpan data.