# Naufal Store - Website Katalog Produk Django

Nama : Naufal Farrel Syafilan  
NIM : 2308107010058

## Penjelasan Singkat Program

Naufal Store adalah website katalog produk sederhana berbasis Django. Website ini memiliki halaman beranda, katalog produk, detail produk berdasarkan ID, dan halaman kontak.

Data produk disimpan langsung di `katalog/views.py`, sehingga aplikasi dapat berjalan tanpa konfigurasi database. Tampilan halaman menggunakan template Django dan CSS lokal agar terlihat seperti katalog produk yang rapi dan siap digunakan.

## Fitur

- Beranda: `/`
- Katalog produk: `/produk/`
- Detail produk: `/produk/<id>/`
- Kontak: `/kontak/`
- Minimal 3 produk, pada project ini tersedia 6 produk
- Halaman detail menampilkan produk sesuai ID
- Routing menggunakan `urls.py`
- Tampilan halaman menggunakan Django Template

## Struktur Folder

```text
katalog-sederhana-django-naufal/
├── manage.py
├── requirements.txt
├── README.md
├── katalog_sederhana/
│   ├── settings.py
│   └── urls.py
└── katalog/
    ├── urls.py
    ├── views.py
    ├── templates/katalog/
    └── static/katalog/css/style.css
```

## Cara Menjalankan

1. Buat virtual environment.

```bash
python -m venv venv
```

2. Aktifkan virtual environment.

Windows:

```bash
venv\Scripts\activate
```

Linux atau macOS:

```bash
source venv/bin/activate
```

3. Install dependency.

```bash
pip install -r requirements.txt
```

4. Jalankan server.

```bash
python manage.py runserver
```

5. Buka website di browser.

```text
http://127.0.0.1:8000/
```

## URL yang Tersedia

| Halaman | URL |
| --- | --- |
| Beranda | `/` |
| Katalog produk | `/produk/` |
| Detail produk | `/produk/1/`, `/produk/2/`, dan seterusnya |
| Kontak | `/kontak/` |
