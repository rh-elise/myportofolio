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

### 5. Jalankan Migrasi

Terapkan skema database, termasuk migrasi relasi star pada model `Experience`:

```bash
python manage.py migrate
```

### 6. Jalankan Test

Pastikan seluruh test, termasuk test API Experience dan test Tutorial 07, lulus:

```bash
python manage.py test main
```

Gunakan `main` agar file `test_e2e.py` (Selenium) tidak ikut dijalankan.

### 7. Jalankan Server Django

```bash
python manage.py runserver
```

### 8. Buka Website

Setelah server berhasil dijalankan, buka browser dan akses:

`http://localhost:8000/`

### 9. Buat Grup Editor (via Admin)

Editor adalah pengguna yang boleh mengubah data Experience dengan `PUT`/`PATCH`, tetapi tidak boleh membuat atau menghapus data.

```bash
python manage.py createsuperuser
```

Setelah itu:

1. Buka `http://localhost:8000/admin/` dan login sebagai superuser.
2. Buat grup bernama **Editor**.
3. Berikan permission **`main | experience | Can change experience`** kepada grup tersebut.
4. Tambahkan akun Editor ke grup **Editor**.

Hak akses ini dicek oleh `IsPortfolioOwnerOrEditorOrReadOnly` melalui `request.user.has_perm("main.change_experience")`, sehingga API dan halaman edit memakai aturan yang sama.

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

Halo Kak! Dalam pengerjaan portfolio ini, saya menggunakan AI sebagai alat bantu diskusi, debugging, dan review. Saya tetap menentukan arah pengerjaan dan memeriksa hasil perubahan karena beberapa saran AI tidak selalu sesuai dengan struktur project yang sudah saya buat.

### Kapan dan Bagaimana Saya Menggunakan AI?

**Tools & Strategi Prompting**

Tool AI yang saya gunakan adalah OpenCode. Saya biasanya memberikan konteks terlebih dahulu, seperti bagian kode yang sedang dikerjakan, traceback, atau screenshot hasil implementasi. Dengan begitu, AI bisa memberikan saran berdasarkan kondisi project, bukan hanya menghasilkan kode secara umum.

Prompt yang saya gunakan juga tidak selalu meminta AI membuat sesuatu dari awal. Saya lebih sering meminta penjelasan mengenai penyebab masalah, membandingkan beberapa pendekatan, atau melakukan review terhadap kode yang sudah ada. Contohnya, saya meminta AI memeriksa konsistensi antara data JSON dan template, serta mencari bagian yang masih perlu diperbaiki.

**Debugging**

AI cukup membantu ketika saya menemukan error yang penyebabnya belum langsung terlihat. Saya memberikan traceback setelah menjalankan project, misalnya `ImportError require_POST`, `TemplateDoesNotExist`, dan `NoReverseMatch`, lalu meminta AI membantu menelusuri kemungkinan sumber masalahnya.

Saya tetap membuka file yang berkaitan dan memeriksa perubahan yang disarankan sebelum menjalankan ulang project. Dengan cara ini, saya mendapat petunjuk untuk memulai proses debugging tanpa harus langsung mencoba perubahan secara acak.

**CSS & JavaScript**

Untuk bagian tampilan dan interaksi halaman, saya menggunakan AI untuk mendiskusikan penerapan CSS maupun JavaScript berdasarkan rancangan dan hasil implementasi. Hasil awalnya tidak selalu sesuai. Contohnya, aturan `.button` sempat ikut memengaruhi badge star, sedangkan tampilan search sempat menjadi terlalu sederhana dibandingkan desain yang saya inginkan.

Saya kemudian memeriksa selector dan aturan yang menyebabkan masalah tersebut sebelum menyesuaikannya. Beberapa bagian juga saya kerjakan terlebih dahulu, seperti skeleton Experience dan penggunaan `strip_tags`, kemudian meminta AI membantu melakukan review.

**Implementasi API DRF**

Dalam mengembangkan API menggunakan Django REST Framework, saya menggunakan AI untuk membantu memahami dan menerapkan konsep dari tutorial ke dalam project yang sudah ada. Saya berdiskusi mengenai struktur API, serializer, permission, views, serta cara menghubungkan API dengan frontend.

Saya juga meminta penjelasan tambahan ketika menemukan konsep atau bagian kode yang belum saya pahami. Salah satu hal yang saya pelajari adalah bagaimana optimasi query dapat membantu menghindari pengambilan data berulang. Untuk keputusan implementasi, saya tetap mempertimbangkan kesesuaiannya dengan struktur dan kebutuhan project.

**Testing & Review**

Saya menggunakan AI untuk membantu memeriksa test, menelusuri penyebab test yang gagal, dan mencari bagian implementasi yang belum konsisten. Saya juga memanfaatkannya untuk pengecekan tambahan, seperti mencari sisa `TODO`, bahasa Indonesia yang masih tertinggal, file modal yang terduplikasi, dan ketidaksesuaian antara JSON dengan template.

Setelah itu, saya menjalankan pemeriksaan pada project, termasuk `python manage.py check`, pengecekan migration, dan `python manage.py test main`. Hasil pengujian terakhir menunjukkan 65 test berhasil lulus dan Django system check tidak menemukan masalah. Namun, pengecekan tampilan akhir secara langsung di browser masih perlu saya lakukan sendiri.

### Keterbatasan AI yang Saya Temui

Walaupun menggunakan agentic AI yang dapat membantu memahami beberapa file dalam project, AI tetap tidak selalu memahami seluruh maksud dan rancangan yang saya inginkan. Saran yang diberikan terkadang terlihat benar secara teknis, tetapi belum tentu cocok dengan struktur kode atau kebutuhan project.

AI juga bisa menghasilkan kode yang perlu diperbaiki kembali, memberikan solusi yang terlalu umum, atau menyarankan pendekatan yang berbeda dari pola yang sudah digunakan sebelumnya. Karena itu, saya tidak bisa langsung menganggap setiap jawaban AI sebagai solusi akhir. Saya tetap perlu memeriksa kode, memahami dampak perubahannya, dan menjalankan pengujian.

### Perbaikan Manual yang Saya Lakukan

Beberapa hasil dari AI tidak langsung saya gunakan. Saya melakukan penyesuaian ketika hasilnya tidak sesuai dengan struktur project atau desain.

- **Styling:** saya memperbaiki selector yang terlalu umum agar tidak memengaruhi komponen lain.
- **Template & modal:** saya memastikan posisi `{% include %}` berada pada struktur template yang benar.
- **Test:** saya menyesuaikan asersi dengan bentuk data yang sebenarnya dikembalikan setelah perubahan implementasi.
- **Serializer:** saya membetulkan referensi model `Experience`, `Meta.model`, field `status`, dan nama `validate_thumbnail` yang sebelumnya tidak sesuai.
- **Permission:** saya memilih penggunaan `has_perm("main.change_experience")` daripada hanya mengecek nama grup agar konsisten dengan halaman edit.
- **JavaScript:** saya menyesuaikan penggunaan data dari API, event delegation untuk tombol star dan hapus, serta header `X-CSRFToken` pada request yang mengubah data.

Keputusan mengenai bagian yang dikembangkan, rancangan fitur, dan kesesuaian implementasi dengan project tetap saya pertimbangkan sendiri. AI lebih banyak membantu pada proses diskusi, implementasi, pencarian masalah, dan review.

### Refleksi Diri

Saya merasa penggunaan AI dalam pengerjaan portfolio ini masih cukup banyak, terutama ketika menemukan error atau bagian kode yang belum saya pahami. Namun, dari proses tersebut saya mulai menyadari bahwa hasil AI tidak selalu bisa langsung digunakan. Saya tetap perlu membaca kode, memahami perubahan yang diberikan, dan memastikan hasilnya sesuai dengan kebutuhan project.

Saya juga belajar untuk tidak hanya menerima solusi pertama yang diberikan AI. Ketika ada beberapa pendekatan, saya perlu memahami perbedaannya dan mempertimbangkan mana yang paling sesuai. Untuk pengerjaan berikutnya, saya ingin mencoba menyelesaikan masalah yang sudah pernah saya pelajari terlebih dahulu sebelum meminta bantuan AI. Dengan begitu, AI dapat lebih saya gunakan sebagai teman diskusi dan alat untuk memeriksa pemahaman.

### Styling README.md

Saya juga menggunakan AI untuk membantu merapikan format dan struktur penulisan `README.md` ini agar lebih mudah dibaca. Isi dan pengalaman yang dituliskan tetap berdasarkan proses pengerjaan yang saya lakukan sendiri.

### Log Obrolan AI

1. [Link Chat 1](https://drive.google.com/file/d/18iycGxKFX1xnQ0iXhym5_Xy36NpwiXwP/view?usp=sharing)

---

# Pertanyaan Reflektif

## Tugas 1

### 1. Penggunaan Elemen Semantik

Penggunaan elemen semantik cukup membantu, terutama karena saya sudah terbiasa merancang UI/UX menggunakan Figma. Ketika membuat desain di Figma, saya biasanya berpikir dalam bentuk bagian-bagian halaman, misalnya bagian navigasi, isi utama, dan bagian tertentu yang memiliki fungsi berbeda. Konsep tersebut cukup membantu ketika saya mulai menyusun struktur HTML.

Awalnya saya masih agak bingung membedakan `<section>` dengan `class`, karena keduanya sama-sama terasa seperti digunakan untuk mengelompokkan elemen. Setelah menggunakannya, saya mulai memahami bahwa `<section>` merupakan bagian dari struktur atau isi halaman, sedangkan `class` lebih berfungsi sebagai penanda yang dapat digunakan untuk memilih dan memberikan styling pada elemen melalui CSS.

Menurut saya, penggunaan elemen semantik membuat struktur HTML lebih mudah dipahami karena saya tidak hanya membuat kumpulan `div` tanpa pembagian yang jelas. Saya jadi lebih terbiasa memikirkan setiap bagian halaman sebagai sebuah struktur yang memiliki fungsi, bukan hanya sebagai elemen yang harus diberi CSS.

### 2. Tantangan Tata Letak pada Mobile

Tantangan tata letak terbesar adalah memastikan website tetap nyaman dilihat ketika ukuran layar menjadi jauh lebih kecil. Desain yang terlihat baik pada *desktop* tidak selalu bisa langsung digunakan dengan ukuran dan susunan yang sama pada *mobile*. Kalau semua elemen hanya diperkecil, beberapa bagian justru menjadi terlalu sempit atau saling bertabrakan.

Ketika menemukan masalah tersebut, saya membandingkan hasil implementasi dengan desain yang saya inginkan, kemudian memberikan prompt lanjutan kepada AI untuk memperbaikinya. Beberapa perubahan yang saya minta antara lain:

* Mengecilkan ukuran *card project* dan *art* agar lebih proporsional pada layar kecil.
* Memindahkan deskripsi dan judul proyek ke bawah gambar pada tampilan *mobile*, sedangkan pada *desktop* posisinya berada di samping.
* Mengubah *layout* deretan tombol dari horizontal menjadi vertikal agar tidak terlalu sempit.
* Mengatur kembali posisi deskripsi profil karena sebelumnya sempat menabrak dan menutupi foto *background* utama ketika ukuran layar mengecil.

Dari proses ini saya belajar bahwa *responsive design* bukan hanya tentang membuat semua ukuran menjadi lebih kecil. Struktur dan posisi elemen juga perlu disesuaikan dengan ruang yang tersedia supaya informasi tetap memiliki hierarki yang jelas dan tidak saling bertabrakan.

### 3. Batasan Static Web dan Pengembangan Selanjutnya

Batasan utama dari *static web* murni adalah kontennya masih banyak yang di-*hardcode* di dalam HTML. Selama isi portofolionya masih sedikit, cara ini mungkin masih bisa dilakukan, tetapi akan menjadi semakin merepotkan ketika jumlah kontennya bertambah.

Hal ini cukup terasa pada portfolio saya karena ada banyak gambar karya beserta nama dan informasi lainnya. Kalau saya ingin mengganti atau menambahkan sebuah karya, saya perlu menyiapkan gambar dan kemudian menyesuaikan bagian yang berkaitan dengan gambar dan teks tersebut di dalam project. Kalau jumlah project terus bertambah, cara seperti ini akan semakin tidak praktis.

Karena itu, pengembangan yang paling ingin saya lakukan selanjutnya adalah membuat sistem yang menggunakan **database** dan **panel admin**. Data seperti nama project, deskripsi, dan gambar dapat disimpan sebagai data, bukan ditulis langsung di HTML.

Dengan cara tersebut, halaman website bisa mengambil data dari database secara dinamis. Saya juga bisa menambahkan atau mengubah project melalui form atau panel admin tanpa harus mencari dan mengubah banyak bagian dari kode HTML. Menurut saya, ini akan membuat portfolio lebih mudah dikembangkan ketika jumlah kontennya semakin banyak.

## Tugas 2

### 1. Alur Request-Response (MVT) pada Django

Ketika pengguna membuka halaman portofolio, browser terlebih dahulu mengirimkan HTTP request ke website. Request tersebut akan diterima oleh `urls.py` utama pada proyek Django, yang kemudian menentukan aplikasi mana yang menangani URL tersebut. Setelah diarahkan ke `urls.py` milik aplikasi portofolio, URL tersebut dicocokkan dengan pola yang tersedia dan Django akan memanggil view yang sesuai. Jika URL memiliki parameter tertentu, misalnya ID sebuah project, parameter tersebut juga dapat diteruskan ke view agar data yang diproses sesuai dengan project yang diminta.

Selanjutnya, view menangani logika yang diperlukan untuk menampilkan halaman. Jika halaman membutuhkan data dari database, view akan meminta data tersebut melalui model. Model menjadi penghubung antara aplikasi dengan database, sehingga data project dapat diambil tanpa harus ditulis langsung di dalam HTML.

Setelah mendapatkan data yang dibutuhkan, view meneruskannya ke template. Template kemudian menggunakan data tersebut untuk membentuk halaman HTML yang akan ditampilkan kepada pengguna. Hasil akhirnya dikirim kembali sebagai HTTP response ke browser, sehingga pengguna dapat melihat halaman portofolio beserta data project yang sesuai.

Dari alur ini saya memahami bahwa setiap bagian dalam MVT memiliki tanggung jawab yang berbeda. `urls.py` menentukan ke mana request diarahkan, view mengatur prosesnya, model menangani data, sedangkan template berfokus pada bagaimana data tersebut ditampilkan.

### 2. Mengapa Data (Model dan Template) Dipisahkan?

Data untuk bagian portofolio sebaiknya disimpan pada model daripada ditulis langsung di dalam template karena data dan tampilan memiliki fungsi yang berbeda. Jika nama project, deskripsi, gambar, dan informasi lainnya ditulis langsung di dalam HTML, setiap perubahan atau penambahan project akan membuat saya harus mengubah kode template secara manual.

Hal ini berkaitan dengan keterbatasan static web yang saya temukan pada Tugas 1. Saat jumlah project masih sedikit, melakukan hardcode mungkin masih terasa mudah. Namun, jika jumlah project semakin banyak, cara tersebut akan menjadi semakin sulit untuk dipelihara karena data tersebar di dalam kode HTML.

Dengan menyimpan data pada model, saya dapat menggunakan satu template untuk menampilkan banyak project dari database menggunakan looping. Jika ingin menambahkan atau mengubah project, yang perlu diubah adalah datanya, bukan struktur HTML untuk setiap project. Menurut saya, cara ini membuat aplikasi lebih mudah dan siap untuk dikembangkan menjadi fitur yang lebih dinamis, seperti pencarian atau filter berdasarkan kategori.

### 3. Makemigrations vs Migrate

`makemigrations` dan `migrate` sama-sama berkaitan dengan perubahan struktur database, tetapi memiliki fungsi yang berbeda. `makemigrations` digunakan untuk membuat file migrasi berdasarkan perubahan yang dilakukan pada `models.py`. File tersebut berisi instruksi mengenai perubahan struktur database yang perlu dilakukan oleh Django.

Sementara itu, `migrate` digunakan untuk menerapkan instruksi dari file migrasi tersebut ke database. Jadi, `makemigrations` dapat dipahami sebagai proses mencatat perubahan model menjadi sebuah migrasi, sedangkan `migrate` adalah proses menjalankan perubahan tersebut pada database.

Sebagai contoh, jika saya menambahkan atribut baru bernama `link_github` pada model project, perubahan tersebut belum langsung membuat kolom baru pada database. Saya perlu menjalankan `makemigrations` terlebih dahulu agar Django membuat file migrasi yang mencatat perubahan tersebut. Setelah itu, saya menjalankan `migrate` agar perubahan tersebut benar-benar diterapkan pada database dan kolom `link_github` dapat digunakan untuk menyimpan data.

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

## Tugas 5

### 1. Apa Itu Debouncing dan Mengapa Penting pada Fitur Pencarian AJAX?

Debouncing adalah teknik untuk menahan eksekusi sebuah fungsi sampai pengguna berhenti melakukan suatu aksi selama jeda waktu tertentu. Pada fitur pencarian, artinya request AJAX tidak langsung dikirim setiap kali pengguna mengetik satu huruf, tetapi baru dikirim setelah pengguna berhenti mengetik, misalnya selama 1 detik.

Tanpa debouncing, setiap ketikan akan langsung memicu request ke server. Sebagai contoh, ketika pengguna mengetik "BUKU", server akan menerima request untuk `B`, `BU`, `BUK`, dan `BUKU` secara beruntun. Jika banyak pengguna melakukan hal yang sama, jumlah request yang masuk bisa menjadi sangat besar dan membuat server kelebihan beban, padahal hasil yang benar-benar dibutuhkan hanya hasil dari kata terakhir.

Selain membebani server, ada juga risiko *race condition*. Request untuk kata yang lebih pendek, misalnya "BUK", bisa saja mengalami delay dan baru mendapat respons setelah request "BUKU" selesai. Akibatnya, tampilan justru diperbarui dengan data yang sudah kedaluwarsa dan tidak sesuai dengan kata yang terakhir diketik pengguna.

Dengan debouncing, request hanya dikirim satu kali menggunakan kata final setelah pengguna benar-benar berhenti mengetik. Dari sini saya memahami bahwa debouncing bukan hanya soal menghemat resource server, tetapi juga membantu memastikan hasil yang ditampilkan di halaman tetap sesuai dengan apa yang pengguna cari.

### 2. Fungsi `await` pada `fetch()` dan Apa yang Terjadi Jika Tidak Digunakan

Mengambil data dari server membutuhkan waktu tempuh, mirip seperti menunggu makanan yang sudah dipesan sampai benar-benar siap. Karena itu, `fetch()` bekerja secara asinkron dan tidak langsung mengembalikan datanya, melainkan sebuah *Promise* yang statusnya masih menunggu.

Fungsi `await` digunakan untuk menjeda eksekusi pada baris tersebut sampai proses `fetch()` selesai dan datanya siap digunakan. Dengan begitu, baris kode di bawahnya, seperti mengubah response menjadi JSON atau merender data ke halaman, baru berjalan setelah data dari server benar-benar tersedia.

Jika `await` tidak digunakan, kode di bawah `fetch()` akan langsung dieksekusi sebelum data dari server tiba. Pada saat itu, yang dimiliki program baru berupa Promise yang berstatus *pending*, bukan data yang sebenarnya. Akibatnya, program bisa mengalami error atau gagal merender karena mencoba mengolah data yang masih kosong.

Dari sini saya memahami bahwa `await` bukan sekadar tambahan penulisan, tetapi bagian penting untuk mengatur urutan proses ketika bekerja dengan data yang tidak langsung tersedia.

### 3. Serangan XSS dan Mengapa Data AJAX/JavaScript Lebih Rentan Dibanding Template Django

XSS (*Cross-Site Scripting*) adalah serangan ketika pihak yang tidak bertanggung jawab memasukkan kode berbahaya, seperti `<script>`, melalui input yang diterima aplikasi, misalnya lewat form yang datanya kemudian tersimpan di database. Ketika browser pengguna lain memuat data tersebut, browser akan mengeksekusi script itu tanpa disadari, sehingga dapat berujung pada pencurian data atau informasi rahasia pengguna.

Template Django relatif lebih aman karena memiliki fitur *auto-escaping* bawaan. Karakter berbahaya seperti `<` dan `>` otomatis diubah menjadi bentuk teks biasa sebelum dirender, sehingga browser hanya menampilkannya sebagai teks dan tidak mengeksekusinya sebagai kode.

Sebaliknya, pada AJAX/JavaScript, data diambil terlebih dahulu dalam bentuk mentah lalu dimasukkan ke dalam DOM oleh JavaScript, misalnya dengan `innerHTML`. Pada proses ini tidak ada auto-escaping, sehingga data disuntikkan apa adanya ke halaman. Jika data tersebut mengandung script berbahaya, browser dapat langsung mengeksekusinya.

Karena itu, developer perlu melakukan escaping atau pembersihan data secara manual sebelum menampilkannya di halaman. Hal ini juga berkaitan dengan pengalaman saya di Tugas 5, ketika saya menggunakan `strip_tags` pada bagian skeleton Experience. Dari sini saya memahami bahwa ketika proses render berpindah dari template Django ke JavaScript, tanggung jawab untuk menjaga keamanan data juga ikut berpindah ke sisi developer.

## Tugas 6

### 1. Pengertian REST, Mengapa JSON Saja Tidak Cukup, serta Perbedaan PUT dan PATCH

REST (*Representational State Transfer*) adalah salah satu cara untuk merancang API dengan memanfaatkan method HTTP. Dalam REST, setiap data memiliki URL masing-masing. Misalnya, `/api/v1/experience/` digunakan untuk mengambil kumpulan data Experience, sedangkan `/api/v1/experience/5/` digunakan untuk mengakses Experience dengan ID 5.

Untuk melakukan operasi pada data tersebut, kita menggunakan method HTTP yang sesuai. `GET` untuk mengambil data, `POST` untuk menambahkan data, `PUT` dan `PATCH` untuk mengubah data, serta `DELETE` untuk menghapus data. Selain itu, server juga mengirimkan status code untuk menunjukkan hasil dari request, misalnya `201 Created` jika data berhasil dibuat atau `404 Not Found` jika data yang dicari tidak ditemukan.

Menurut saya, mengembalikan data dalam bentuk JSON saja belum cukup untuk membuat sebuah API disebut RESTful. JSON hanya merupakan format untuk mengirimkan data. Sebuah API bisa saja menggunakan JSON, tetapi masih menggunakan satu URL untuk semua operasi atau selalu memakai `POST`, termasuk untuk menghapus data. REST menggunakan URL dan method HTTP dengan tujuan yang lebih jelas, sehingga cara client berkomunikasi dengan server menjadi lebih teratur dan mudah dipahami.

Perbedaan `PUT` dan `PATCH` ada pada jumlah data yang ingin diubah. `PUT` digunakan ketika client ingin memperbarui data secara keseluruhan, sehingga biasanya seluruh field yang dibutuhkan dikirim kembali. Sementara itu, `PATCH` digunakan jika hanya beberapa field yang ingin diubah tanpa harus mengirim ulang semua data.

Contohnya, ketika pengguna mengedit Experience melalui halaman edit, seluruh isi form dikirim untuk diperbarui. Ini sesuai dengan penggunaan `PUT`. Namun, jika pengguna hanya ingin mengganti judul, client cukup mengirim `{"title": "Judul Baru"}` menggunakan `PATCH`. Pada implementasi saya, perbedaan keduanya diatur melalui `partial=request.method == "PATCH"` pada serializer.

### 2. Peran Serializer pada Django REST Framework dan Keuntungannya

Serializer digunakan untuk mengubah data dari model Django menjadi format yang bisa dikirim melalui API, seperti JSON. Serializer juga menangani data yang dikirim dari client sebelum data tersebut disimpan ke database. Jadi, serializer tidak hanya bertugas mengubah format data, tetapi juga memeriksa apakah data yang dikirim sudah sesuai dengan aturan yang ditentukan.

Pada `ExperienceSerializer`, saya menentukan field yang boleh dikirim ke client, seperti `id`, `title`, `description`, `category`, `thumbnail`, `year`, dan `status`. Saya juga menggunakan serializer untuk mengatur informasi tambahan seperti jumlah star dan apakah pengguna yang sedang login sudah memberikan star. Untuk data yang masuk, serializer melakukan validasi, misalnya memeriksa judul, kategori, status, dan thumbnail, serta membersihkan HTML menggunakan `strip_tags`.

Dibandingkan membuat dictionary secara manual menggunakan `JsonResponse` seperti yang pernah dilakukan pada tutorial sebelumnya, penggunaan serializer terasa lebih praktis karena beberapa hal:

- **Validasi lebih mudah diatur:** Aturan seperti judul tidak boleh kosong, minimal tiga karakter, dan format thumbnail bisa ditulis di satu tempat. Jadi, saya tidak perlu memeriksa semuanya secara manual di setiap view.
- **Lebih sesuai dengan model:** `ModelSerializer` bisa menggunakan informasi field dan pilihan `choices` yang sudah ada pada model. Jika kategori atau status tidak sesuai, serializer bisa langsung memberikan error.
- **Mengurangi kode berulang:** Saya tidak perlu mengambil setiap atribut model dan memasukkannya satu per satu ke dalam dictionary untuk dijadikan JSON.
- **Field tertentu bisa dibuat read-only:** Informasi seperti `star_count` dan `is_starred` berasal dari hasil perhitungan, sehingga pengguna tidak bisa sembarangan mengubah nilainya melalui request.
- **Lebih mudah mengatur data yang ditampilkan:** Saya bisa menentukan sendiri field apa saja yang boleh dikirim ke client, sehingga data yang tidak diperlukan atau bersifat sensitif tidak ikut ditampilkan.
- **Format error lebih teratur:** Jika ada input yang salah, serializer mengembalikan pesan error berdasarkan field yang bermasalah. Frontend jadi lebih mudah menampilkan pesan tersebut kepada pengguna.

Kalau menggunakan `JsonResponse` secara manual, proses validasi dan penyusunan data tersebut harus dibuat sendiri. Untuk data yang field-nya semakin banyak, cara itu bisa membuat kode menjadi lebih panjang dan lebih sulit dirawat.

### 3. Perbedaan Autentikasi dan Otorisasi serta Mengapa Hak Akses Diperiksa di Server

Autentikasi dan otorisasi merupakan dua hal yang berbeda. Autentikasi digunakan untuk mengetahui siapa pengguna yang sedang mengakses aplikasi. Misalnya, ketika seseorang login menggunakan akun Django, sistem akan mengenali pengguna tersebut melalui session. Jika belum login, pengguna akan dianggap sebagai `AnonymousUser`.

Sementara itu, otorisasi digunakan untuk menentukan apa saja yang boleh dilakukan oleh pengguna tersebut. Jadi, meskipun seseorang sudah berhasil login, belum tentu ia boleh melakukan semua tindakan di aplikasi.

Pada project saya, aturan tersebut diterapkan melalui permission class `IsPortfolioOwnerOrEditorOrReadOnly`. Pengunjung tetap bisa melihat data, tetapi tidak bisa mengubahnya. Pengguna biasa juga tidak diberikan akses untuk menambah, mengedit, atau menghapus Experience. Editor yang memiliki permission `main.change_experience` dapat melakukan perubahan, sedangkan superuser memiliki akses penuh. Untuk fitur star, pengguna harus login terlebih dahulu agar bisa memberikan atau membatalkan star.

Pengecekan hak akses perlu dilakukan di server karena pengguna bisa saja melewati tampilan frontend dan mengirim request secara langsung. Contohnya, tombol Delete mungkin hanya ditampilkan kepada Editor. Namun, pengguna biasa tetap bisa mencoba mengirim request `DELETE` melalui Postman atau DevTools. Jika server tidak memeriksa permission, data tetap berisiko terhapus meskipun tombolnya disembunyikan dari halaman.

Karena itu, menyembunyikan tombol hanya berguna untuk mengatur tampilan yang dilihat pengguna. Server tetap harus memeriksa apakah pengguna tersebut benar-benar memiliki izin untuk melakukan tindakan yang diminta.

### 4. Mengapa CSRF Tetap Diperlukan pada SessionAuthentication dan Mengapa force_authenticate Tidak Cukup

Pada `SessionAuthentication`, Django menggunakan session cookie untuk mengenali pengguna yang sudah login. Masalahnya, browser mengirimkan cookie tersebut secara otomatis ketika mengakses domain yang sesuai. Hal ini bisa dimanfaatkan dalam serangan CSRF (*Cross-Site Request Forgery*), yaitu ketika pengguna tanpa sadar diminta oleh situs lain untuk mengirim request yang mengubah data di aplikasi tempat ia sedang login.

Misalnya, pengguna sedang login ke portfolio saya, lalu membuka situs lain yang mencoba mengirim request untuk menghapus salah satu Experience. Browser bisa saja ikut mengirimkan cookie session pengguna pada request tersebut. Jika tidak ada perlindungan CSRF, server berisiko menganggap request itu benar-benar berasal dari pengguna.

Untuk mencegah hal tersebut, Django menggunakan token CSRF. Pada request yang mengubah data, frontend perlu mengirimkan token melalui header `X-CSRFToken`. Token ini digunakan server untuk memeriksa apakah request tersebut memang berasal dari halaman aplikasi yang sah.

Pada halaman Experience, saya menggunakan `{% csrf_token %}` dan fungsi `getCookie` untuk mengambil token dari cookie `csrftoken`. Token tersebut kemudian dikirim melalui header pada request `POST`, `PATCH`, dan `DELETE`.

Saya juga mempelajari bahwa menggunakan `force_authenticate` saja belum cukup untuk menguji perlindungan CSRF. Alasannya, `force_authenticate` langsung mengatur pengguna pada request untuk kebutuhan testing, sehingga tidak melewati proses login dan autentikasi session seperti yang terjadi ketika pengguna benar-benar mengakses aplikasi melalui browser.

Karena itu, untuk pengujian CSRF saya menggunakan `APIClient(enforce_csrf_checks=True)` dan `.login()`. Dengan cara ini, saya bisa menguji apakah request tanpa token CSRF ditolak dan apakah request dengan token yang benar berhasil diproses. Hasilnya, request `POST` tanpa token mendapatkan status `403`, sedangkan setelah token dikirim melalui header, request berhasil dengan status `201`.

Dari pengujian tersebut, saya jadi lebih memahami bahwa autentikasi menggunakan session saja belum cukup untuk melindungi request yang mengubah data. Perlindungan CSRF tetap diperlukan agar request tersebut tidak bisa dilakukan sembarangan oleh situs lain.