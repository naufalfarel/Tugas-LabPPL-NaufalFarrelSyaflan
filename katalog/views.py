from django.http import Http404
from django.shortcuts import render


PRODUK_DATA = [
    {
        'id': 1,
        'nama': 'Notebook Orion Slim 14',
        'kategori': 'Perangkat Digital',
        'kode': 'OR',
        'harga': 8799000,
        'stok': 9,
        'rating': '4.8',
        'aksen': 'tone-blue',
        'deskripsi_singkat': 'Notebook ringan untuk produktivitas harian dan mobilitas tinggi.',
        'deskripsi': (
            'Notebook Orion Slim 14 hadir dengan desain tipis, bobot ringan, dan performa '
            'stabil untuk kebutuhan kerja, belajar, browsing, presentasi, hingga pengelolaan '
            'dokumen harian.'
        ),
        'fitur': [
            'Layar 14 inci Full HD',
            'Baterai tahan sampai 10 jam',
            'Bobot ringan untuk dibawa bepergian',
        ],
    },
    {
        'id': 2,
        'nama': 'Keyboard NeoKeys 75',
        'kategori': 'Aksesoris Komputer',
        'kode': 'NK',
        'harga': 699000,
        'stok': 24,
        'rating': '4.7',
        'aksen': 'tone-purple',
        'deskripsi_singkat': 'Keyboard compact dengan feel mengetik nyaman dan suara halus.',
        'deskripsi': (
            'NeoKeys 75 menggunakan layout ringkas yang hemat ruang, sehingga area kerja '
            'terlihat lebih bersih. Keyboard ini cocok untuk mengetik panjang, membuat dokumen, '
            'dan penggunaan harian.'
        ),
        'fitur': [
            'Layout 75 persen yang ringkas',
            'Kabel USB-C detachable',
            'Backlight lembut untuk malam hari',
        ],
    },
    {
        'id': 3,
        'nama': 'AeroFold Laptop Stand',
        'kategori': 'Perlengkapan Meja',
        'kode': 'AF',
        'harga': 185000,
        'stok': 37,
        'rating': '4.6',
        'aksen': 'tone-green',
        'deskripsi_singkat': 'Stand lipat untuk posisi laptop yang lebih ergonomis.',
        'deskripsi': (
            'AeroFold Laptop Stand membantu menaikkan posisi layar laptop agar postur tubuh '
            'lebih nyaman saat bekerja dalam waktu lama. Desainnya dapat dilipat dan mudah '
            'dibawa ke mana saja.'
        ),
        'fitur': [
            'Bahan aluminium ringan',
            'Tinggi dapat diatur',
            'Mudah dilipat dan dibawa',
        ],
    },
    {
        'id': 4,
        'nama': 'Tumbler Orbit 600ml',
        'kategori': 'Lifestyle',
        'kode': 'OB',
        'harga': 129000,
        'stok': 45,
        'rating': '4.9',
        'aksen': 'tone-orange',
        'deskripsi_singkat': 'Tumbler stainless stylish untuk menemani aktivitas seharian.',
        'deskripsi': (
            'Tumbler Orbit dirancang untuk membawa minuman dengan lebih praktis. Bentuknya '
            'minimalis, mudah dibersihkan, dan nyaman digunakan untuk aktivitas harian.'
        ),
        'fitur': [
            'Kapasitas 600 ml',
            'Material stainless steel',
            'Tutup anti bocor',
        ],
    },
    {
        'id': 5,
        'nama': 'Nova Modular Backpack',
        'kategori': 'Tas Harian',
        'kode': 'NV',
        'harga': 349000,
        'stok': 16,
        'rating': '4.8',
        'aksen': 'tone-red',
        'deskripsi_singkat': 'Tas ransel dengan banyak kompartemen untuk perangkat dan barang harian.',
        'deskripsi': (
            'Nova Modular Backpack memiliki kompartemen laptop, ruang dokumen, dan kantong '
            'kecil untuk menyimpan barang penting dengan lebih rapi. Cocok untuk mobilitas '
            'harian yang padat.'
        ),
        'fitur': [
            'Slot laptop sampai 15 inci',
            'Bahan tahan cipratan air',
            'Banyak kantong penyimpanan',
        ],
    },
    {
        'id': 6,
        'nama': 'Pulse Wireless Earbuds',
        'kategori': 'Audio',
        'kode': 'PL',
        'harga': 259000,
        'stok': 28,
        'rating': '4.5',
        'aksen': 'tone-dark',
        'deskripsi_singkat': 'Earbuds ringkas untuk musik, panggilan, dan aktivitas mobile.',
        'deskripsi': (
            'Pulse Wireless Earbuds menawarkan suara jernih dalam ukuran kecil. Produk ini '
            'nyaman digunakan untuk mendengarkan musik, menerima panggilan, dan menemani '
            'aktivitas saat bepergian.'
        ),
        'fitur': [
            'Koneksi Bluetooth stabil',
            'Charging case ringkas',
            'Mode panggilan dengan mikrofon',
        ],
    },
]


def format_rupiah(nilai):
    return 'Rp {:,}'.format(nilai).replace(',', '.')


def lengkapkan_produk(produk):
    data = produk.copy()
    data['harga_label'] = format_rupiah(data['harga'])
    return data


def semua_produk():
    return [lengkapkan_produk(produk) for produk in PRODUK_DATA]


def home(request):
    context = {
        'produk_unggulan': semua_produk()[:3],
        'total_produk': len(PRODUK_DATA),
    }
    return render(request, 'katalog/home.html', context)


def produk_list(request):
    context = {
        'produk_list': semua_produk(),
    }
    return render(request, 'katalog/produk_list.html', context)


def produk_detail(request, id):
    produk = next((item for item in PRODUK_DATA if item['id'] == id), None)
    if produk is None:
        raise Http404('Produk tidak ditemukan')

    context = {
        'produk': lengkapkan_produk(produk),
        'produk_lain': [item for item in semua_produk() if item['id'] != id][:3],
    }
    return render(request, 'katalog/produk_detail.html', context)


def kontak(request):
    context = {
        'nama_toko': 'Naufal Store',
        'email': 'support@naufalstore.id',
        'telepon': '+62 812-0000-7001',
        'alamat': 'Banda Aceh, Indonesia',
    }
    return render(request, 'katalog/kontak.html', context)
