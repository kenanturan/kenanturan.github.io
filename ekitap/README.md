# Taktik Mücadelenin Temelleri — 3D İnteraktif E-Kitap

Bu proje, **Kenan Turan**'ın *"Taktik Mücadelenin Temelleri - Hayatta Kalma Bakış Açısı"* adlı eserini modern web teknolojileriyle, gerçekçi **3D sayfa çevirme (Flipbook)** efekti ve zengin multimedya (görseller + video QR kodları) ile sunan bir web sitesidir.

Tamamen statik (HTML5, CSS3, StPageFlip Canvas ve modern JavaScript) mimaride geliştirilmiş olup **GitHub Pages** üzerinde $0 maliyetle, ömür boyu ücretsiz SSL sertifikasıyla çalışacak şekilde tasarlanmıştır.

---

## 🌟 Öne Çıkan Özellikler

- **Gerçekçi 3D Sayfa Çevirme:** Dokunmatik ekranlarda ve masaüstünde fareyle sayfayı köşesinden tutup çevirme, sayfa kıvrılma fiziği ve dinamik gölgeler.
- **Doğal Sayfa Çevirme Sesi:** Harici dosya indirmeden Web Audio API ile saf sentezlenen sayfa hışırtısı (isteğe bağlı açma/kapatma).
- **Lüks Sert Kapak (Hardcover):** Altın varak detaylar ve prestijli tipografi (*Playfair Display*, *Cinzel*, *Merriweather*).
- **Akıllı Yer İmi (Bookmark):** Kırmızı saten kitap ayracı; okuyucunun kaldığı sayfayı otomatik hatırlar.
- **İçindekiler (Fihrist) Çekmecesi:** Bölümlere tek tıkla zıplama ve anlık metin arama filtresi.
- **Okuma Temaları:** Klasik Krem Kağıt, Beyaz Kağıt ve Gece (Koyu) Kağıt modları.
- **Büyüteç (Lightbox Zoom):** Taktik şema ve görsellere tıklandığında tam ekran yüksek çözünürlüklü inceleme.
- **Mobil Uyum:** Telefonlarda otomatik tek sayfa, tablet ve bilgisayarlarda çift sayfa görünümü.

---

## 🚀 Bilgisayarda Yerel Olarak Çalıştırma

Projeyi tarayıcınızda test etmek için terminalde şu komutu çalıştırabilirsiniz:

```bash
cd /Users/kenanturan/Desktop/ekitap
python3 -m http.server 8000
```
Ardından tarayıcınızda [http://localhost:8000](http://localhost:8000) adresine gitmeniz yeterlidir.

---

## 🌐 GitHub Pages ile İnternette Yayınlama

Sitenizi GitHub Pages üzerinden dünyayla paylaşmak için şu adımları izleyin:

1. **GitHub'da Yeni Bir Depo (Repository) Oluşturun:**
   - GitHub hesabınıza girip `ekitap` adında boş (Public) bir repository açın.

2. **Terminalden Projeyi Yükleyin:**
   ```bash
   cd /Users/kenanturan/Desktop/ekitap
   git init
   git add .
   git commit -m "İlk sürüm: 3D Flipbook E-Kitap"
   git branch -M main
   git remote add origin https://github.com/KULLANICI_ADINIZ/ekitap.git
   git push -u origin main
   ```

3. **GitHub Pages'i Açın:**
   - Repository sayfanızda **Settings > Pages** bölümüne gidin.
   - **Branch:** `main` seçip **Save** deyin.
   - 1-2 dakika içinde siteniz `https://kullaniciadiniz.github.io/ekitap/` adresinde yayına girecektir.

4. **Kendi Özel Alan Adınızı (Domain) Bağlama:**
   - Proje ana dizinindeki `CNAME` dosyasına alan adınızı yazın (örn: `kitap.alanadiniz.com`).
   - Domain firmanızın DNS yönetim panelinden:
     - Alt alan adı için (`kitap.alanadiniz.com`): Bir **CNAME** kaydı açıp değerine `kullaniciadiniz.github.io` yazın.
     - Ana alan adı için (`alanadiniz.com`): GitHub Pages IP adreslerine (A kayıtları) yönlendirin:
       ```
       185.199.108.153
       185.199.109.153
       185.199.110.153
       185.199.111.153
       ```
   - GitHub Settings > Pages altında **Enforce HTTPS** kutucuğunu işaretleyin (Ücretsiz SSL sertifikanız dakikalar içinde aktifleşir).

---

## 📝 Kitabı İleride Nasıl Güncellersiniz?

Kitapta bir metni, başlığı veya görselleri güncellemek istediğinizde:

1. Word dosyanızı (`DÖRDÜNCÜ BÖLÜM.docx` veya yeni bölümleri) normal Word programıyla düzenleyip kaydedin.
2. Terminalde tek bir komut çalıştırın:
   ```bash
   python3 convert.py
   ```
   *(Sistem görselleri çıkarır, sayfaları yeniden mizanpaj yapar ve `js/book-data.js` dosyasını otomatik yeniler.)*
3. Değişiklikleri GitHub'a gönderin:
   ```bash
   git commit -am "İçerik güncellendi"
   git push
   ```
   Web siteniz 30 saniye içinde internette yeni haliyle güncellenecektir!
