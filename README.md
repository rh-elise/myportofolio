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

## Pengungkapan Penggunaan AI (AI Disclosure) & Catatan Pengerjaan

### Pesan Singkat untuk Kak Asdos

Halo Kak! Melanjutkan progres dari Tugas 3, di Tugas 4 ini saya masih berusaha mengurangi kebiasaan *vibecoding*. Saya mencoba mengerjakan bagian yang saya pahami terlebih dahulu, kemudian menggunakan AI ketika menemukan error atau bagian yang belum saya mengerti. Di Tugas 4 ini, AI paling banyak saya gunakan untuk membantu debugging, memahami permission, dan menerjemahkan rancangan tampilan yang saya inginkan ke dalam CSS.

### Kapan dan Bagaimana Saya Menggunakan AI di Tugas Ini?

**Superuser & Login**

Saya menggunakan AI untuk memahami cara membuat superuser dan perbedaan ketika menjalankan perintah secara lokal dan melalui Terminal PWS karena keduanya menggunakan database yang berbeda. Saya juga menanyakan arti `is_superuser` serta cara mengisi prompt ketika menjalankan `createsuperuser`.

**Debug Star (NoReverseMatch)**

Ketika halaman `/projects/` mengalami error `NoReverseMatch`, saya memberikan traceback kepada AI untuk membantu mencari penyebabnya. Dari proses debugging tersebut ditemukan dua masalah: URL `toggle_star` masih menggunakan `<uuid:...>`, sedangkan ID pada model saya menggunakan `int`, dan pada `{% include ... with project=project %}` nama variabel yang digunakan tidak sesuai dengan variabel loop, yaitu `proj`.

Saya kemudian mengecek kembali view dan model untuk memastikan bagian tersebut memang sesuai dengan struktur project saya. Setelah itu, saya memperbaiki bagian yang bermasalah berdasarkan hasil pengecekan tersebut.

**Styling Star & Navbar**

Untuk tampilan, saya menentukan sendiri desain yang ingin digunakan. Misalnya, badge star menggunakan `☆/★` dan jumlah star diletakkan di pojok mini card, tombol pada hero berubah dari putih menjadi merah, serta sapaan `Hi! username` diletakkan di bagian kiri navbar tanpa latar merah.

Saya menggunakan AI untuk membantu menerjemahkan rancangan tersebut ke dalam CSS. Ketika hasilnya tidak sesuai, saya memberikan screenshot dan kode yang sedang digunakan agar AI membantu mencari penyebabnya. Salah satu contohnya adalah ketika badge mini card ikut berubah menjadi merah karena aturan `.button` menimpa `.button-star`, atau ketika tampilan search berubah menjadi input yang terlalu polos.

Dari proses ini, saya tidak hanya meminta CSS baru, tetapi juga mencoba memahami selector mana yang menyebabkan konflik dan mengapa perubahan pada satu class dapat memengaruhi elemen lain.

**Pembagian Peran Editor**

Pada bagian permission Editor, saya menggunakan AI sebagai teman diskusi untuk menentukan pembagian akses yang sesuai dengan kebutuhan tugas. Saya meminta AI membantu membandingkan penggunaan `has_perm("main.change_projects")` dengan pengecekan group secara langsung.

Dari diskusi tersebut, saya memahami bahwa Editor seharusnya memiliki akses untuk melakukan update, tetapi tidak memiliki akses untuk create atau delete. Setelah memahami pembagiannya, saya sendiri yang menerapkan perubahan pada `views.py` dan template.

Saya kemudian menggunakan AI untuk memeriksa kembali apakah pembatasan tersebut sudah konsisten, misalnya `update_*` dapat dilakukan Editor, sedangkan `create_*` dan `delete_*` tetap dibatasi untuk Owner.

**Test Peran Editor**

Saya menggunakan AI untuk membantu menuliskan test untuk permission Editor dengan mengikuti pola test 403 yang sudah saya buat sebelumnya. Saya memberikan struktur test lama tersebut dan meminta AI menyesuaikannya untuk beberapa kondisi baru, yaitu Editor tidak dapat membuka halaman tambah, tidak dapat melakukan create, dapat melakukan update, dan tidak dapat melakukan delete experience.

AI membantu menyesuaikan struktur test dan helper `login_as_editor`, sedangkan saya menjalankan test tersebut pada project untuk memastikan hasilnya sesuai. Hasil akhirnya adalah `29/29 OK`.

### Refleksi Diri

### Refleksi Diri

Pada tugas 4 beberapa masalah yang muncul tidak terlihat dari bagian kode yang sedang saya kerjakan. Misalnya, error pada `toggle_star` ternyata berkaitan dengan tipe ID yang digunakan, sedangkan masalah pada template disebabkan oleh nama variabel yang berbeda.

Untuk bagian styling, saya juga beberapa kali mendapatkan hasil yang tidak sesuai dengan yang saya bayangkan. Ketika menggunakan AI untuk membantu memperbaiki tampilan, saya tetap perlu melihat kembali CSS yang sudah ada dan menyesuaikannya dengan struktur project saya.

Saya masih cukup sering menggunakan AI selama pengerjaan Tugas 4, terutama ketika menemui error atau ketika saya belum tahu cara menerapkan sesuatu. Bedanya, sekarang saya lebih sering memberikan kode atau error yang memang sedang saya hadapi daripada meminta seluruh bagian dibuat dari awal.

Saya rasa cara ini masih belum membuat saya sepenuhnya lepas dari bantuan AI, tetapi setidaknya saya jadi lebih terbiasa membaca error, mencari bagian yang bermasalah, dan memahami perubahan yang saya lakukan pada project.


### Styling README.md

Saya juga menggunakan AI untuk membantu merapikan format dan struktur penulisan `README.md` ini agar lebih mudah dibaca. Isi dan pengalaman yang dituliskan tetap berdasarkan proses pengerjaan yang saya lakukan sendiri.

### Log Obrolan AI

1. [Link Chat 1](https://opncd.ai/share/0BwNh7SM)


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

### 2. Mengapa Data (Model dan Temoplate) Dipisahkan?

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