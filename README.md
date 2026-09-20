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

Halo Kak! Melanjutkan progres dari Tugas 2, di Tugas 3 ini saya masih terus berusaha mengurangi kebiasaan *vibecoding*. Saya mencoba mengerjakan tutorialnya secara perlahan agar lebih memahami alur kerja Django secara keseluruhan. Sejauh ini, pemahaman saya mengenai alur dari URL → View → Model → Template sudah mulai membaik.

Namun, untuk Tugas 3 ini saya masih harus mengakui bahwa saya cukup banyak membutuhkan bantuan AI, terutama ketika berhadapan dengan logika di `views.py` dan saat mengatur *styling* pada frontend.

### Kapan dan Bagaimana Saya Menggunakan AI di Tugas Ini?

**Logika Views (Update, Delete, & JSON)**

Awalnya saya mencoba menulis kode sendiri, tetapi karena implementasinya cukup berbeda dari materi sebelumnya, saya masih kebingungan pada bagian Update dan Delete. Saya juga mengalami kesulitan ketika membuat fungsi untuk mengambil data dalam bentuk JSON. Sebagai contoh, pada kode berikut:

```python
def get_projects_json(request: HttpRequest) -> HttpResponse:

    title_query = request.GET.get("title", "").strip()

    projects = Projects.objects.all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    data = serializers.serialize("json", projects)

    return HttpResponse(data, content_type="application/json")
```

Saya masih kurang memahami maksud dari beberapa bagian seperti `request.GET.get()` dan `serializers.serialize()`. Karena itu, saya memberikan instruksi kepada AI untuk membantu membuat fungsi tersebut sekaligus meminta penjelasan mengenai alasan setiap bagian kode digunakan.

Jadi, pada bagian ini AI tidak hanya saya gunakan untuk mendapatkan kode yang bisa langsung dijalankan, tetapi juga sebagai tempat untuk menanyakan bagian yang belum saya pahami. Setelah mendapatkan penjelasan, saya mencoba mengikuti kembali alur kode tersebut agar lebih memahami prosesnya.

**Data Cleaning pada Forms**

Saya juga menggunakan AI untuk membantu memahami proses data cleaning atau validasi pada `forms.py`, terutama agar input yang diberikan pengguna sesuai dengan kebutuhan aplikasi. Ketika terjadi error saat form di-submit, saya biasanya menyalin pesan error tersebut ke AI dan menanyakan kemungkinan letak kesalahannya.

Setelah itu, saya mencoba melihat kembali kode yang bermasalah dan memahami penyebab error tersebut, bukan hanya mengganti kode berdasarkan jawaban AI.

**HTML & CSS (Masih Banyak Dibantu AI)**

Untuk urusan tampilan seperti *styling* form, pembuatan tombol Delete, dan *responsive layout*, saya masih cukup banyak bergantung pada AI. Tema Neo-Brutalism yang saya gunakan juga membuat bagian CSS cukup kompleks untuk saya implementasikan sendiri dari awal.

Meskipun begitu, saya tetap mencoba membaca struktur HTML yang dihasilkan dan memahami bagian mana yang menggunakan `extends`, `include`, maupun struktur template Django lainnya. Jadi, pada bagian frontend saya memang masih membutuhkan banyak bantuan AI, tetapi saya berusaha tidak hanya mengambil hasil akhirnya tanpa melihat bagaimana kode tersebut digunakan.

### Refleksi Diri

Proses pengerjaan Tugas 3 membuat saya semakin sadar bahwa bagian backend dan logika pengolahan data cukup *tricky*, terutama ketika mulai berhadapan dengan Primary Key, proses Update dan Delete, serta pengembalian data dalam bentuk JSON.

Saya memang masih cukup bergantung pada AI, terutama untuk bagian tampilan dan beberapa logika di `views.py`. Namun, dibandingkan tugas-tugas awal, saya mulai mengubah cara menggunakan AI. Ketika menemukan kode yang belum saya pahami, saya mencoba menanyakan alasan kode tersebut ditulis dan mengikuti alurnya kembali, bukan hanya menempelkan kode sampai program berhasil dijalankan.

Menurut saya, perubahan kecil ini membuat proses pengerjaan terasa lebih membantu untuk belajar. Saya memang belum sepenuhnya bisa membuat semua bagian tanpa bantuan AI, tetapi setidaknya saya mulai lebih terbiasa membaca kode, mencari tahu penyebab error, dan memahami hubungan antarbagian dalam Django.

### Styling README.md

Saya juga menggunakan AI untuk membantu merapikan format dan struktur penulisan `README.md` ini agar lebih mudah dibaca. Isi dan pengalaman yang dituliskan tetap berdasarkan proses pengerjaan yang saya lakukan sendiri.

### Log Obrolan AI

1. [Link Chat 1](https://opncd.ai/share/hvIrr8IH)
1. [Link Chat 2](https://opncd.ai/share/0BwNh7SM)


---

# Pertanyaan Reflektif

## Tugas 3

### 1. Mengapa Menggunakan ModelForm, dan Mengapa Wajib Ada `{% csrf_token %}`?

Menurut saya, penggunaan ModelForm membuat proses pembuatan form menjadi jauh lebih jelas dan terstruktur. Dari tutorial yang saya ikuti, saya memahami bahwa ModelForm dapat menggunakan struktur yang sudah didefinisikan pada `models.py` untuk membentuk form secara otomatis. Hal ini cukup terasa ketika saya membuat form untuk data Experience dan Projects, karena saya tidak perlu membuat setiap input dari awal secara manual.

Jika menggunakan form HTML biasa, saya perlu menuliskan setiap tag `<input>`, menentukan tipe input, serta mengatur bagaimana data tersebut nantinya diproses. Dengan ModelForm, sebagian proses tersebut sudah ditangani oleh Django berdasarkan field yang terdapat pada model. Menurut saya, hal ini membuat kode menjadi lebih ringkas dan mengurangi pekerjaan yang sebenarnya berulang.

Walaupun begitu, saya masih menemukan kesulitan pada bagian tampilan. ModelForm membantu dari sisi struktur dan proses pengolahan data, tetapi tampilannya tetap perlu saya sesuaikan dengan desain portofolio yang menggunakan tema Neo-Brutalism. Pada bagian *styling* inilah saya masih cukup banyak menggunakan AI untuk membantu memperbaiki CSS agar tampilan form sesuai dengan desain yang saya inginkan.

Untuk `{% csrf_token %}`, saya belum memahami seluruh detail teknisnya, tetapi dari yang saya pelajari, token ini digunakan sebagai salah satu mekanisme keamanan pada form Django untuk mencegah *Cross-Site Request Forgery* (CSRF). Secara sederhana, token tersebut dapat dianalogikan seperti tiket yang diberikan kepada pengguna ketika membuka halaman form. Saat form dikirim, Django akan memeriksa token tersebut untuk memastikan bahwa request berasal dari halaman yang memang diizinkan. Jika token tidak sesuai atau tidak ada, request dapat ditolak.

Dari sini saya memahami bahwa `{% csrf_token %}` bukan sekadar bagian yang harus ditambahkan agar form dapat berjalan, tetapi merupakan bagian dari mekanisme keamanan ketika aplikasi menerima data dari pengguna.

### 2. Mengapa JSON Lebih Disukai Dibandingkan XML?

Menurut saya, JSON lebih praktis digunakan dibandingkan XML untuk pertukaran data karena strukturnya lebih ringkas dan mudah dibaca. XML menggunakan tag pembuka dan penutup untuk setiap data, misalnya `<nama>Rheina</nama>`. Jika data yang dikirim cukup banyak, penggunaan tag tersebut membuat struktur XML menjadi lebih panjang.

JSON menggunakan struktur key-value, misalnya `"nama": "Rheina"`. Bentuknya juga cukup familiar karena mirip dengan dictionary pada Python maupun object pada JavaScript. Karena struktur datanya lebih sederhana dan ringkas, JSON terasa lebih mudah dibaca ketika saya melihat data yang dikembalikan oleh sebuah web.

Hal ini juga relevan dengan proses pengembangan portofolio saya karena saya mulai mempelajari penggunaan JavaScript untuk berinteraksi dengan data dari backend. Format JSON dapat digunakan untuk mengirim data dari Django ke frontend sehingga data tersebut dapat diolah kembali tanpa harus menuliskan seluruh data secara langsung di dalam HTML.

Dari perbandingan tersebut, saya memahami bahwa JSON bukan berarti selalu lebih baik dalam semua kondisi, tetapi lebih praktis untuk kebutuhan pertukaran data pada aplikasi web yang sedang saya kerjakan karena bentuknya sederhana dan mudah diproses oleh JavaScript.

### 3. Alur Mengembalikan Data Portofolio dalam Bentuk JSON

Setelah mencoba memahami implementasinya, saya melihat bahwa proses mengembalikan data portofolio dalam bentuk JSON masih mengikuti alur request dan response pada Django.

Pertama, pengguna atau frontend mengirim request ke URL tertentu. Request tersebut kemudian diarahkan melalui `urls.py` menuju view yang sesuai, misalnya fungsi `get_projects_json`.

Selanjutnya, view meminta data project melalui model. Django kemudian mengambil data tersebut dari database. Pada tahap ini, data yang diperoleh masih berupa QuerySet, yaitu struktur data yang digunakan Django untuk merepresentasikan hasil query dari database.

Karena data tersebut masih dalam bentuk objek Python, data perlu diubah menjadi format yang dapat digunakan oleh frontend. Proses perubahan struktur data tersebut disebut serialisasi. Dalam kasus ini, data project diubah menjadi JSON sehingga dapat dikirim melalui HTTP response.

Setelah proses tersebut selesai, view mengembalikan data dalam bentuk `HttpResponse` dengan `content_type="application/json"`. Browser atau frontend kemudian dapat menerima response tersebut dan menggunakan data JSON yang diberikan.

Dari alur ini saya memahami bahwa prosesnya kurang lebih tetap mengikuti konsep MVT yang sebelumnya saya pelajari. Perbedaannya terletak pada hasil akhirnya. Jika pada halaman biasa view mengirim data ke template untuk menghasilkan HTML, pada endpoint JSON view mengubah data menjadi JSON dan mengembalikannya sebagai response yang dapat digunakan oleh frontend.