from api_autoresbot import ApiAutoresbot

api = ApiAutoresbot('YOUR_APIKEY')

# Metode Get
"""
try:
    response = api.get('/api/game/family100')
    print(response)
except Exception as error:
    print(f'Gagal mengambil data: {error}')
"""

# Metode Get With Param
"""
try:
    response = api.get('/api/stalker/whatsapp-group', {
        'url': 'https://chat.whatsapp.com/KJD2nB7j7lfHux9AVQCra4'
    })
    print(response)
except Exception as error:
    print(f'Gagal mengambil data: {error}')
"""

# Get Buffer
"""
try:
    response = api.get_buffer('/api/maker/welcome1', {
        'pp': 'http://localhost:3000/api/maker/pp-default',
        'name': 'Azhari Creative',
        'gcname': 'autoresbot',
        'member': '20',
        'ppgc': 'http://localhost:3000/api/maker/ppgc-default'
    })

    # response sekarang adalah bytes
    with open('welcome.jpg', 'wb') as file:
        file.write(response)
    print('Gambar berhasil disimpan ke welcome.jpg')
except Exception as error:
    print(f'Gagal mengambil data: {error}')
"""

# Upload File 
# Notes: File uploader di autoresbot bisa di upload dari situs resmi autoresbot.com, 
# hasil file ini akan expired selama 1 minggu setelah upload, namun setiap kali di akses 
# masa expired akan selalu di perbarui untuk 1 minggu kedepan
"""
try:
    response = api.tmp_upload('./welcome.jpg')
    print(f"Gambar berhasil diupload ke server: {response}")
except Exception as error:
    print(f'Gagal mengambil data: {error}')
"""
