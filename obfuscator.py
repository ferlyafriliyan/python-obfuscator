# __author : Ferly Afriliyan
# Do not change the original author's name 

from colorama import Fore, init
import subprocess
import importlib
import os, sys

# Warna teks
k = Fore.YELLOW  # Warna Kuning
a = Fore.LIGHTBLACK_EX  # Warna Abu-Abu
m = Fore.RED  # Warna Merah
h = Fore.GREEN  # Warna Hijau
p = Fore.WHITE  # Warna Putih
b = Fore.BLUE  # Warna Biru
v = Fore.MAGENTA  # Warna Violet
u = Fore.CYAN  # Warna Ungu
j = Fore.LIGHTWHITE_EX  # Warna Jingga


# Clear Terminal
def clear():
    if 'linux' in sys.platform.lower():os.system('clear')
    elif 'win' in sys.platform.lower():os.system('cls')

# Memeriksa apakah modul python_obfuscator terinstal
try:
    clear()
    importlib.import_module('python_obfuscator')
    python_obfuscator_module_installed = True
except ImportError:
    python_obfuscator_module_installed = False

# Cek apakah modul python_obfuscator terinstal
if not python_obfuscator_module_installed:
    clear()
    print(f"{h}[{a}•{h}] {p}Modul Obfuscate belum terinstal. Anda perlu menginstal modul berikut {a}:")
    print(f"  {a}- {p}python_obfuscator (pyobfuscate)")
    print(f"{h}[{a}•{h}] {p}Ketik perintah: pip install {a}python_obfuscator {p}")
    exit()

# Meminta pengguna untuk memasukkan nama file input
clear()
print(f"{p}█ ▄▄ ▀▄    ▄   ▄▄▄▄▀ ▄  █ ████▄    ▄   ████▄ ███   ▄████ ▄      ▄▄▄▄▄   ▄█▄    ██     ▄▄▄▄▀ ████▄ █▄▄▄▄ ")
print(f"{p}█   █  █  █ ▀▀▀ █   █   █ █   █     █  █   █ █  █  █▀   ▀ █    █     ▀▄ █▀ ▀▄  █ █ ▀▀▀ █    █   █ █  ▄▀ ")
print(f"{p}█▀▀▀    ▀█      █   ██▀▀█ █   █ ██   █ █   █ █ ▀ ▄ █▀▀ █   █ ▄  ▀▀▀▀▄   █   ▀  █▄▄█    █    █   █ █▀▀▌  ")
print(f"{p}█       █      █    █   █ ▀████ █ █  █ ▀████ █  ▄▀ █   █   █  ▀▄▄▄▄▀    █▄  ▄▀ █  █   █     ▀████ █  █  ")
print(f"{p} █    ▄▀      ▀        █        █  █ █       ███    █  █▄ ▄█            ▀███▀     █  ▀              █   ")
print(f"{p}  ▀                   ▀         █   ██               ▀  ▀▀▀                      █                 ▀    ")
print(f"{p}                                                                                ▀                      ")
input_file = input(f"{h}[{a}•{h}] {p}Masukkan nama file Input {a}: {p}")
if not input_file:
    print(f"{m}[{a}!{m}] {p}File '{input_file}' tidak ditemukan.")
    exit()
    input_text = None
elif not input_file.endswith(".py"):
    print(f"{m}[{a}!{m}] {p}File harus memiliki ekstensi .py {p}")
    exit()



# Meminta pengguna untuk memasukkan nama file output
output_file = input(f"{h}[{a}•{h}] {p}Masukkan nama file Output {a}: {p}")
if not output_file:
    print(f"{m}[{a}!{m}] {p}Isi dengan benar {m}! {p}")
    exit()
elif not output_file.endswith(".py"):
    print(f"{m}[{a}!{m}] {p}File output harus memiliki ekstensi .py {p}")
    exit()

# Inisialisasi variabel result
result = None

# Jalankan perintah pyobfuscate untuk mengobfuscate file input dan tangkap output
try:
    result = subprocess.check_output(f'pyobfuscate -i {input_file}', shell=True, text=True)
    print(f"File {input_file} telah dienkripsi. Dan tersimpan di {output_file}")
except subprocess.CalledProcessError:
    print("Terjadi kesalahan dalam mengenkripsi file.")
    exit()

# Simpan hasil obfuscation ke dalam file output jika result tidak None
if result is not None:
    with open(output_file, "w", encoding="utf-8") as output_f:
        output_f.write(result)
