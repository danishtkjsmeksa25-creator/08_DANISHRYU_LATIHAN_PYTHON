import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
from getpass import getpass

scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

creds = Credentials.from_service_account_file(
    "credentials.json",
    scopes=scope
)

client = gspread.authorize(creds)

sheet = client.open_by_key(
    "1fxLqnc52wMJm7k9yuUt3lx4hmgqu5JW2TrkbbKvtdTI"
).sheet1

# Membuat judul kolom jika masih kosong
if sheet.cell(1, 1).value is None:
    sheet.append_row(["Username", "Kode", "Timer"])

# Input data
username = input("Masukkan username : ")
kode = getpass("Masukkan kode     : ")

# Waktu saat data dimasukkan
timer = datetime.now().strftime("%H:%M:%S")

# Masukkan ke Google Sheets
sheet.append_row([username, kode, timer])

print("\nData berhasil disimpan!")
print("Username :", username)
print("Kode     : ********")
print("Timer    :", timer)
