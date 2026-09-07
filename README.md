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

## Pengungkapan Penggunaan AI (AI Disclosure) & Catatan Pengerjaan

### Pesan Singkat untuk Kak Asdos

Halo Kak! Sebelumnya saya ingin meminta maaf dan jujur bahwa untuk eksekusi kode pada tugas kali ini, saya **SANGAT banyak menggunakan pendekatan vibecoding** (mengandalkan AI untuk merakit syntax HTML/CSS) karena saya deadline. Saya sangat minta maaf untuk itu TT. Saya berjanji ke depannya akan belajar lebih dalam mengenai penulisan syntax secara mandiri dan memperbaiki kualitas kode saya. Terima kasih atas pengertiannya Kak!

### Pembagian Pengerjaan

Untuk Tugas 1 ini, desain awal yaitu, layout, palet warna, gaya *Neo-Brutalism*, sampai hierarki informasinya saya rancang sendiri dulu di Figma. Setelah itu, untuk menerjemahkan rancangan tersebut ke HTML dan CSS, saya banyak menggunakan AI dengan pendekatan vibecoding. Saya menggunakan beberapa AI, yaitu Claude, Gemini, dan OpenAI, karena beberapa bagian membutuhkan beberapa kali percobaan sampai hasilnya sesuai dengan desain yang saya inginkan.

Cara kerja saya biasanya seperti ini: saya memberikan konteks mengenai desain dan bagian yang ingin dibuat, kemudian AI menghasilkan kodenya. Setelah melihat hasilnya, saya mengecek apakah tampilannya sudah sesuai dengan rancangan saya. Kalau ada yang belum pas atau malah rusak, saya memberikan prompt lanjutan yang lebih spesifik untuk menjelaskan masalah dan perubahan yang saya inginkan.

Hal ini paling sering terjadi pada tampilan *mobile*. Beberapa elemen sempat terlalu sempit atau bertabrakan, misalnya deskripsi yang menutupi foto *background* utama. Untuk memperbaikinya, saya memberikan instruksi yang lebih detail kepada AI, seperti meminta perubahan ukuran *card project*, posisi elemen, `z-index`, serta mengubah susunan *layout* dari horizontal menjadi vertikal pada ukuran layar tertentu.

Selain masalah pada tampilan, saya juga sempat mengalami kendala ketika melakukan push ke PWS karena ada file gambar yang ukurannya terlalu besar dan membuat prosesnya bermasalah. Untuk bagian tersebut, saya juga menggunakan bantuan AI untuk mencari tahu penyebabnya dan membantu membenahinya.

Jadi, keputusan mengenai desain dan tampilan website tetap berasal dari saya, sedangkan proses penulisan dan perbaikan syntax banyak dibantu oleh AI. Prosesnya juga bukan hanya sekali *generate* lalu selesai, tetapi melalui beberapa kali coba, evaluasi hasil, dan pemberian prompt lanjutan.

### Strategi Penggunaan AI

Saya menggunakan AI terutama untuk membantu menerjemahkan desain yang sudah saya buat di Figma menjadi implementasi HTML dan CSS. Saya tidak langsung memberikan satu prompt untuk membuat semuanya sekaligus, tetapi biasanya membaginya menjadi beberapa bagian dan melakukan perbaikan berdasarkan hasil yang diberikan.

Strategi yang paling sering saya gunakan adalah memberikan konteks desain terlebih dahulu, kemudian mengecek hasil implementasinya. Kalau ada bagian yang tidak sesuai, saya mencoba menjelaskan masalahnya secara lebih spesifik pada prompt berikutnya. Semakin jelas masalah yang saya jelaskan, biasanya hasil perbaikannya juga semakin sesuai.

AI saya gunakan untuk membantu beberapa hal, seperti:

* Menyusun struktur HTML berdasarkan rancangan halaman.
* Menerjemahkan desain visual dari Figma ke CSS.
* Membantu membuat *responsive layout* untuk ukuran layar yang berbeda.
* Memperbaiki posisi dan ukuran elemen yang bermasalah.
* Membantu mencari penyebab error saat proses pengerjaan dan deployment.
* Membantu merapikan format dan struktur penulisan `README.md`.

Sementara itu, keputusan mengenai tampilan website, seperti struktur halaman, *layout*, gaya *Neo-Brutalism*, palet warna, komposisi elemen, dan hierarki informasi, saya tentukan sendiri melalui proses perancangan di Figma.

### Evaluasi Penggunaan AI

Selama menggunakan AI, saya menyadari bahwa hasil yang diberikan tidak selalu langsung sesuai dengan yang saya inginkan. AI memang sangat membantu mempercepat proses penulisan kode, tetapi AI tidak selalu bisa memahami desain yang saya bayangkan hanya dari satu instruksi.

Masalah yang paling terasa ada pada tampilan *mobile*. Pada awalnya, beberapa elemen menjadi terlalu sempit atau saling bertabrakan. Salah satu contohnya adalah deskripsi yang sempat menutupi foto *background* utama. Ada juga beberapa *card*, gambar, dan tombol yang perlu disesuaikan kembali supaya tetap nyaman dilihat pada layar yang lebih kecil.

Dari situ saya belajar bahwa menggunakan AI untuk coding tetap membutuhkan proses pengecekan. Saya tidak bisa hanya menerima hasil *generate* begitu saja. Saya perlu melihat hasilnya, menemukan bagian yang tidak sesuai, lalu menjelaskan masalah tersebut melalui prompt berikutnya.

Menurut saya, bagian yang paling penting dari proses vibecoding bukan hanya bagaimana mendapatkan kode dengan cepat, tetapi bagaimana saya bisa mengevaluasi hasilnya dan memberikan instruksi yang tepat ketika hasil tersebut belum sesuai.

### Proses Pengerjaan

Secara umum, proses pengerjaan website saya lakukan melalui beberapa tahap:

1. **Perancangan UI/UX**

   Saya terlebih dahulu membuat rancangan website menggunakan Figma. Pada tahap ini saya menentukan struktur halaman, *layout*, warna, tipografi, komponen, serta gaya visual yang ingin digunakan.

2. **Implementasi Awal**

   Setelah rancangan selesai, saya menggunakan AI untuk membantu menerjemahkan desain tersebut menjadi struktur HTML dan styling CSS.

3. **Evaluasi Tampilan**

   Setelah implementasi awal selesai, saya melihat hasilnya dan membandingkannya dengan rancangan yang sudah saya buat. Saya mengecek tampilan pada *desktop* maupun *mobile* untuk melihat apakah ada elemen yang terlalu besar, terlalu kecil, bertabrakan, atau tidak berada di posisi yang seharusnya.

4. **Iterasi Prompt**

   Jika menemukan masalah, saya memberikan prompt lanjutan kepada AI dengan menjelaskan bagian yang bermasalah dan hasil seperti apa yang saya inginkan. Misalnya, ketika beberapa elemen bertabrakan pada layar *mobile*, saya meminta AI menyesuaikan ukuran *card*, posisi elemen, dan susunan *layout* agar dapat beradaptasi dengan ukuran layar yang lebih kecil.

5. **Perbaikan dan Finalisasi**

   Proses evaluasi dan pemberian prompt dilakukan beberapa kali sampai hasil implementasinya sudah lebih mendekati desain yang saya buat dan dapat ditampilkan dengan baik pada ukuran layar yang berbeda.

Dari keseluruhan proses ini, saya menyadari bahwa AI memang sangat membantu mempercepat proses implementasi, tetapi hasilnya tetap perlu diperiksa dan diarahkan. Saya juga jadi lebih memahami bahwa desain UI/UX yang terlihat sederhana di Figma belum tentu bisa langsung diterapkan begitu saja ke semua ukuran layar. Ada banyak hal yang perlu dipikirkan kembali ketika desain tersebut diimplementasikan menjadi website yang *responsive*.

### Styling README.md

Saya juga menggunakan AI untuk membantu merapikan format dan struktur penulisan `README.md` ini agar lebih mudah dibaca. Isi dan pengalaman yang dituliskan tetap berdasarkan proses pengerjaan yang saya lakukan sendiri.

### Log Obrolan AI

1. [Link Chat 1](https://share.gemini.google/0Gzb6xhpXxTz)
2. [Link Chat 2](https://claude.ai/share/4fc6e0a6-b626-42b8-9c4b-ee7bf4abcb6a)
3. [Link Chat 3](https://opncd.ai/share/B04zqg7p)

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