# Laporan Praktikum 1: Big Data Technology

**Setup Environment & Git Workflow (Spark + Cloud Industry Ready)** 

## Identitas Mahasiswa

* **Nama:** Achmad Fauzil ‘Adhim
* **NIM:** 230104040222
* **Kelas:** Teknologi Informasi - Semester 5 
* **Dosen Pengampu:** Muhayat, M.IT 

## Deskripsi Singkat

Praktikum ini bertujuan untuk membangun fondasi lingkungan kerja seorang *Data Engineer* dengan menggunakan stack teknologi modern seperti PySpark untuk pengolahan data terdistribusi, MongoDB Atlas sebagai database cloud, dan Git untuk version control.

## Technology Stack
* **Editor:** VS Code 
* **Terminal:** PowerShell 
* **Bahasa:** Python 3.10+ 
* **Engine:** PySpark 
* **Database:** MongoDB Atlas (Cloud) 
* **Version Control:** Git & GitHub 

## Struktur Project

```text
bigdata-project/
├── data/           # Penyimpanan data lokal
├── cloud_storage/  # Simulasi penyimpanan cloud
├── scripts/        # Script Python (test_mongo.py, simple_job.py)
├── notebooks/      # Eksperimen data
├── reports/        # Dokumentasi laporan
├── requirements.txt
└── README.md

```
## Bukti Hasil Praktikum (Screenshots)


### 1. Inisialisasi PySpark

Menampilkan keberhasilan pembuatan `SparkSession` di terminal VS Code tanpa error.

![Inisialisasi PySpark](https://github.com/user-attachments/assets/e196524f-65b1-49ca-99e2-707682521edd)

### 2. MongoDB Atlas Cluster

Menampilkan status cluster MongoDB Atlas yang sudah **ACTIVE** pada Tier M0 (Free) di region Singapore.

![Mongodb Atlas](https://github.com/user-attachments/assets/7760bc8b-04f1-4159-a6f4-f9eb6670d70f)

### 3. GitHub Repository

Menampilkan repositori GitHub yang sudah bersifat publik dengan struktur folder yang lengkap.

![Github Repository](https://github.com/user-attachments/assets/ad0148a1-1bf5-4d96-b0b3-abfded7c88a5)

### 4. Script simple_job.py

Menampilkan kode lengkap script PySpark untuk melakukan agregasi data sederhana.

![simple job](https://github.com/user-attachments/assets/6225337d-fccd-421f-ab2b-e49aea2047d8)

### 5. Hasil Eksekusi Spark Job

Menampilkan output tabel agregasi `sum(value)` berdasarkan kategori yang dijalankan melalui terminal.

![Eksekusi Spark](https://github.com/user-attachments/assets/541416a6-2883-4d76-b230-c8d59e608f41)

## Kesimpulan

Melalui praktikum ini, lingkungan kerja *Data Engineer* telah berhasil disiapkan. Hal ini mencakup kesiapan *reproducibility environment*, konektivitas *cloud*, serta alur kerja profesional menggunakan Git sebagai persiapan untuk tahap ETL dan *data ingestion* selanjutnya.

