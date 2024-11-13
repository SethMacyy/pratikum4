data_mahasiswa = []

def hitung_nilai_akhir(tugas, uts, uas):
    return (tugas * 0.30) + (uts * 0.35) + (uas * 0.35)

while True:
    print("\nMasukkan data mahasiswa:")
    nim = input("NIM: ")
    nama = input("Nama: ")
    tugas = float(input("Nilai Tugas (0-100): "))
    uts = float(input("Nilai UTS (0-100): "))
    uas = float(input("Nilai UAS (0-100): "))
                
    nilai_akhir = hitung_nilai_akhir(tugas, uts, uas)
    
    data_mahasiswa.append({
        'NIM': nim,
        'Nama': nama,
        'Tugas': tugas,
        'UTS': uts,
        'UAS': uas,
        'Nilai Akhir': nilai_akhir
    })
    
    tambah_data = input("\nApakah ingin menambah data lagi? (y/t): ").lower()
    if tambah_data == 't':
        break

print("\nDaftar Data Mahasiswa:")
print("="*70)
print(f"{'No.':<5} {'NIM':<10} {'Nama':<15} {'Tugas':<10} {'UTS':<10} {'UAS':<10} {'Nilai Akhir':<10}")
print("="*70)

for index, mhs in enumerate(data_mahasiswa, start=1):
    print(f"{index:<5} {mhs['NIM']:<10} {mhs['Nama']:<15} {mhs['Tugas']:<10} {mhs['UTS']:<10} {mhs['UAS']:<10} {mhs['Nilai Akhir']:<10.2f}")

print("="*70)
print("Program selesai.")
