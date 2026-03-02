import cv2
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

def ekstrak_fitur(image_path):
    """
    Ekstraksi fitur warna HSV dari gambar mangga.

    Args:
        image_path (str): Path ke file gambar.

    Returns:
        list: Rata-rata nilai H, S, dan V dari gambar.
    """
    # Membaca gambar
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Gambar tidak ditemukan atau tidak dapat dibaca: {image_path}")

    # Konversi ke ruang warna HSV
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Hitung rata-rata nilai H, S, dan V
    h_mean = np.mean(hsv_image[:, :, 0])  # Hue
    s_mean = np.mean(hsv_image[:, :, 1])  # Saturation
    v_mean = np.mean(hsv_image[:, :, 2])  # Value

    return [h_mean, s_mean, v_mean]

# Dataset pelatihan (gambar dan label)
train_data = [
    ('manggabusuk2.jpg', 'Busuk'),
    ('manggabusuk3.jpg', 'Busuk'),
    ('manggabusuk4.jpg', 'Busuk'),
    ('manggabusuk5.jpg', 'Busuk'),
    ('manggasegar2.jpg', 'Segar'),
    ('manggasegar3.jpg', 'Segar'),
    ('manggasegar4.jpg', 'Segar'),
    ('manggasegar5.jpg', 'Segar'),
    ('manggabusuk6.jpg', 'Busuk'),
]

# Ekstrak fitur dan label untuk pelatihan
X_train = []  # Fitur
y_train = []  # Label

for img_path, label in train_data:
    try:
        features = ekstrak_fitur(img_path)
        X_train.append(features)
        y_train.append(label)
    except Exception as e:
        print(f"Gagal memproses {img_path}: {e}")

# Inisialisasi model KNN
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# Hitung akurasi model
accuracy = knn.score(X_train, y_train) * 100

# Dataset uji
test_data = [
    'manggabusuk1.jpg', 'manggasegar1.jpg'
]

# Proses pengujian
for i, test_img in enumerate(test_data):
    try:
        # Ekstrak fitur dari gambar uji
        test_features = ekstrak_fitur(test_img)

        # Prediksi status kesegaran
        prediction = knn.predict([test_features])[0]
        print(f"Objek {i+1}: Status = {prediction}")

        # Tampilkan gambar asli dengan label prediksi
        image = cv2.imread(test_img)
        plt.figure(figsize=(6, 5))
        
        # Tambahkan background kuning
        plt.gcf().patch.set_facecolor('yellow')
        
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        plt.title(f"Menguji Kesegaran Buah Mangga\nMetode: KNN", fontsize=16, fontweight='bold')

        # Menambahkan status dan akurasi di kiri bawah
        plt.text(10, image.shape[0] - 30, f"Status: {prediction}\nAkurasi: {accuracy:.2f}%", 
                 fontsize=12, color='blue', ha='left', va='bottom', fontweight='bold', 
                 bbox=dict(facecolor='white', alpha=0.7, edgecolor='blue', boxstyle='round,pad=0.5'))

        plt.axis('off')
        plt.show()

    except Exception as e:
        print(f"Gagal memproses {test_img}: {e}")
