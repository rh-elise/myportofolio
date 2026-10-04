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

### 7. Buat Grup Editor (via Admin)

```bash
    python manage.py createsuperuser

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

Halo Kak! Di Tugas 5 saya masih menggunakan AI, saya mengerjakan atau menentukan arahnya terlebih dahulu, lalu memberikan kode, traceback, atau screenshot yang memang sedang saya hadapi kepada AI untuk didiskusikan.

Di tugas ini AI paling banyak saya gunakan untuk debugging, membantu menerjemahkan rancangan UI ke CSS/JavaScript, dan melakukan review terhadap implementasi serta test. Saya tetap mengecek hasilnya di project karena beberapa saran AI ternyata tidak langsung cocok dengan struktur kode yang saya gunakan.

### Kapan dan Bagaimana Saya Menggunakan AI di Tugas Ini?

**Tools & Strategi Prompting**

Tool AI yang saya gunakan adalah OpenCode. Cara saya memberikan prompt juga lebih spesifik dibanding sekadar meminta kode. Untuk debugging, saya memberikan traceback dan bagian kode yang berkaitan, kemudian meminta AI mencari kemungkinan penyebabnya. Untuk styling, saya memberikan screenshot hasil implementasi beserta CSS yang sedang digunakan agar masalahnya bisa dilihat berdasarkan kondisi yang sebenarnya.

Saya juga menggunakan AI untuk review setelah suatu bagian selesai, misalnya meminta pengecekan test, konsistensi JSON dengan template, atau mencari sisa `TODO` dan bahasa Indonesia. Jadi, prompt yang saya gunakan lebih banyak berbentuk **"ini yang saya punya, kenapa hasilnya seperti ini?"** atau **"tolong review bagian ini"**.

**Debugging**

AI paling banyak membantu ketika saya menemukan error yang sulit dilacak. Saya memberikan traceback yang saya dapatkan setelah menjalankan project, misalnya `ImportError require_POST`, `TemplateDoesNotExist`, dan `NoReverseMatch`.

Namun, saya tetap mengecek file dan baris yang disebutkan, lalu menjalankan ulang project setelah melakukan perubahan. Dalam beberapa kasus, penyebab error memang sesuai dengan penjelasan AI, tetapi saya tetap perlu menyesuaikan solusi dengan kode saya sendiri.

Menurut saya, bagian ini menjadi salah satu penggunaan AI yang paling membantu karena saya mendapatkan arah untuk mencari masalah tanpa harus menyerahkan seluruh proses debugging kepada AI.

**CSS & JavaScript**

Untuk UI, saya memberikan rancangan dan screenshot kepada AI lalu meminta bantuan untuk menerjemahkannya ke CSS atau JavaScript. Hasil pertama tidak selalu benar. Contohnya, aturan `.button` sempat ikut memengaruhi badge star sehingga tampilannya berubah menjadi merah, dan search sempat berubah menjadi input yang terlalu sederhana dibandingkan desain yang saya inginkan.

Pada kondisi seperti ini, saya tidak hanya meminta AI mengganti CSS sampai terlihat benar. Saya mencoba memahami selector atau aturan yang menyebabkan konflik, kemudian mengecek kembali perubahan yang diberikan. Beberapa bagian juga saya tulis terlebih dahulu sendiri, termasuk skeleton Experience dan penggunaan `strip_tags`, kemudian AI saya gunakan sebagai reviewer.

**Testing & Review**

Setelah melakukan perubahan, saya menggunakan AI untuk membantu melakukan pengecekan tambahan, salah satunya dengan meminta AI memeriksa test yang gagal dan mencari kemungkinan masalah pada implementasi.

Saya juga menggunakan AI untuk pengecekan yang lebih sederhana, seperti mencari sisa `TODO`, bahasa Indonesia yang masih tertinggal, file modal yang terduplikasi, dan ketidakkonsistenan antara JSON dengan template. Hasil akhirnya saya verifikasi kembali melalui project dan test.

### Keterbatasan AI yang Saya Temui

Keterbatasan AI yang saya temui di Tugas 5 adalah meskipun menggunakan agentic AI yang dapat memahami konteks beberapa file dalam project, hasilnya tetap tidak selalu sesuai dengan kondisi dan rancangan project saya. Misalnya, AI memberikan perubahan CSS yang secara teknis benar, tetapi dapat bertabrakan dengan aturan yang sudah ada. AI juga sempat menyarankan perubahan pada test yang kurang sesuai setelah cara rendering data berubah karena penggunaan skeleton.

Karena itu, saya tetap perlu mengecek hasilnya dengan menjalankan project, melihat tampilan di browser, membaca error atau traceback, dan memastikan perubahan tersebut sesuai dengan kebutuhan saya. Dari sini saya memahami bahwa AI dapat membantu mengerjakan dan menemukan solusi, tetapi hasilnya tetap perlu saya validasi.

### Perbaikan Manual yang Saya Lakukan

Beberapa hasil dari AI tidak langsung saya gunakan. Saya melakukan penyesuaian sendiri ketika hasilnya tidak sesuai dengan struktur project atau desain.

- **Styling:** saya memperbaiki kembali selector yang terlalu umum agar tidak memengaruhi komponen lain.
- **Template & modal:** saya memastikan sendiri posisi `{% include %}` berada pada struktur template yang benar.
- **Test:** saya menyesuaikan kembali asersi dengan cara data sebenarnya dikembalikan oleh endpoint setelah menggunakan skeleton.

Selain itu, keputusan mengenai arsitektur, struktur folder, desain UI, dan cara fitur tersebut seharusnya bekerja tetap saya tentukan sendiri. AI lebih banyak membantu pada tahap implementasi, pencarian masalah, dan review.

### Refleksi Diri

Dari Tugas 5, saya merasa penggunaan AI saya belum bisa dibilang sedikit. Saya masih cukup bergantung pada AI ketika menemukan error yang belum saya pahami, terutama pada bagian JavaScript, AJAX, dan CSS.

Hal yang paling saya rasakan adalah AI tidak selalu menghasilkan solusi yang langsung bisa dipakai. Saya tetap perlu membaca kode, menjalankan test, melihat hasil di browser, dan kadang membatalkan atau mengubah saran AI karena tidak cocok dengan project saya. Dari situ saya mulai melihat AI lebih sebagai alat bantu debugging dan diskusi daripada sebagai orang yang mengerjakan project saya.

Saya masih perlu mengurangi ketergantungan ini pada tugas berikutnya. Terutama untuk bagian yang sudah pernah saya pelajari, saya ingin mencoba menyelesaikan masalahnya sendiri terlebih dahulu sebelum membuka AI. Dengan begitu, AI bisa lebih berfungsi sebagai alat untuk memeriksa pemahaman saya daripada menjadi langkah pertama setiap kali saya menemukan masalah.

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