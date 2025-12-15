# Sistem Validasi Pendaftaran Mata Kuliah Mahasiswa

## Ringkasan Skenario
Sistem ini bertujuan untuk melakukan validasi pendaftaran mata kuliah mahasiswa. Versi awal sistem menggabungkan semua logika validasi (seperti SKS, prasyarat, dll.) dalam satu kelas atau metode menggunakan struktur `if/else`. Pendekatan ini menyebabkan beberapa masalah desain yang signifikan.

---

## Pelanggaran Prinsip Desain

### 1. **Single Responsibility Principle (SRP)**
- **Pelanggaran**: 
  - `ValidatorManager` melakukan terlalu banyak tugas, seperti:
    - Menerima request.
    - Memutuskan aturan validasi.
    - Mengevaluasi SKS.
    - Mengecek prasyarat.
    - Membentuk pesan error.
- **Dampak**:
  - Sulit untuk diuji.
  - Sulit untuk dipelihara.
  - Perubahan aturan validasi memaksa perubahan pada kelas yang sama.

---

### 2. **Open/Closed Principle (OCP)**
- **Pelanggaran**:
  - Untuk menambah aturan validasi baru (misalnya konflik jadwal), developer harus membuka dan memodifikasi metode `validate_all` yang berisi banyak `if/else`.
- **Dampak**:
  - Risiko bug saat menambah fitur baru.
  - Perubahan pada kode yang sudah stabil.

---

### 3. **Dependency Inversion Principle (DIP)**
- **Pelanggaran**:
  - `ValidatorManager` bergantung langsung pada implementasi konkret, seperti memanggil fungsi internal `validate_sks` dan `validate_prasyarat`, bukan pada abstraksi.
- **Dampak**:
  - Sulit untuk mengganti strategi validasi (misalnya untuk pengujian atau variasi aturan) tanpa mengubah `ValidatorManager`.

---

## Tujuan Refactoring

1. **Pisahkan tanggung jawab (SRP)**:
   - Setiap validator hanya memiliki satu tugas.

2. **Terapkan Dependency Inversion Principle (DIP)**:
   - `ValidatorManager` hanya bergantung pada abstraksi `Validator`.

3. **Terapkan Open/Closed Principle (OCP)**:
   - Menambah validator baru tidak memerlukan perubahan pada `ValidatorManager`.