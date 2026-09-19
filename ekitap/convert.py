#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
E-Kitap Dönüştürücü (Word .docx -> 3D Flipbook Sayfa Mimarisi)
Taktik Mücadelenin Temelleri - Hayatta Kalma Bakış Açısı
Yazar: Kenan Turan
28 Sayfalık Ferah, Yüksek Çözünürlüklü ve Tam En-Boy Uyumlu Kitap Düzeni
"""

import os
import sys
import json
import zipfile
import xml.etree.ElementTree as ET

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOCX_PATH = os.path.join(BASE_DIR, "DÖRDÜNCÜ BÖLÜM.docx")
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
IMAGES_DIR = os.path.join(ASSETS_DIR, "images")
JS_DIR = os.path.join(BASE_DIR, "js")

os.makedirs(IMAGES_DIR, exist_ok=True)
os.makedirs(JS_DIR, exist_ok=True)

def extract_media(docx_path):
    with zipfile.ZipFile(docx_path) as z:
        for f in z.namelist():
            if f.startswith('word/media/'):
                fname = os.path.basename(f)
                out_path = os.path.join(IMAGES_DIR, fname)
                with open(out_path, 'wb') as out_f:
                    out_f.write(z.read(f))
    print(f"Görseller başarıyla çıkarıldı: {IMAGES_DIR}")

def build_book_data():
    pages = []

    # -------------------------------------------------------------
    # SAYFA 0: Sert Ön Kapak (Hardcover)
    # -------------------------------------------------------------
    pages.append({
        "type": "cover-front",
        "density": "hard",
        "pageNumber": 0,
        "title": "HAYATTA KALMA BAKIŞ AÇISI",
        "bookTitle": "TAKTİK MÜCADELENİN TEMELLERİ",
        "author": "KENAN TURAN",
        "subtitle": "Taktik Farkındalık, Zihinsel Hazırlık ve Hayatta Kalma Prensipleri",
        "badge": "4. BÖLÜM",
        "contentHtml": """
        <div class="cover-content">
            <div class="cover-ornament top-ornament"></div>
            <div class="cover-series">TAKTİK MÜCADELENİN TEMELLERİ</div>
            <div class="cover-divider-line"></div>
            <h1 class="cover-title">HAYATTA KALMA<br><span class="gold-text">BAKIŞ AÇISI</span></h1>
            <p class="cover-chapter-badge">4. BÖLÜM</p>
            <p class="cover-subtitle">Kritik Anlarda Doğru Karar, Taktik Durum Farkındalığı ve Hayatta Kalma Prensipleri</p>
            <div class="cover-crest">
                <svg viewBox="0 0 100 100" class="crest-svg">
                    <polygon points="50,5 90,25 90,65 50,95 10,65 10,25" fill="none" stroke="#d4af37" stroke-width="2.5" />
                    <polygon points="50,15 80,30 80,60 50,85 20,60 20,30" fill="none" stroke="#d4af37" stroke-width="1" stroke-dasharray="3,3" />
                    <circle cx="50" cy="50" r="14" fill="#d4af37" fill-opacity="0.2" stroke="#d4af37" stroke-width="1.5"/>
                    <path d="M50 38 L50 62 M38 50 L62 50" stroke="#d4af37" stroke-width="2"/>
                </svg>
            </div>
            <div class="cover-author">
                <span class="author-label">YAZAR</span>
                <span class="author-name">KENAN TURAN</span>
            </div>
            <div class="cover-ornament bottom-ornament"></div>
        </div>
        """
    })

    # -------------------------------------------------------------
    # SAYFA 1: Jenerik & İç Kapak
    # -------------------------------------------------------------
    pages.append({
        "type": "inner-title",
        "density": "soft",
        "pageNumber": 1,
        "header": "TAKTİK MÜCADELENİN TEMELLERİ",
        "footer": "1",
        "contentHtml": """
        <div class="inner-title-wrapper">
            <div class="edition-tag">DİJİTAL VE İNTERAKTİF E-KİTAP SÜRÜMÜ</div>
            <h2 class="book-main-title">TAKTİK MÜCADELENİN TEMELLERİ</h2>
            <div class="small-divider"></div>
            <h3 class="chapter-sub-title">DÖRDÜNCÜ BÖLÜM<br><strong>HAYATTA KALMA BAKIŞ AÇISI</strong></h3>
            <p class="author-sub">Kenan Turan</p>
            <div class="colophon-box">
                <p><strong>Yayın ve Telif Bilgileri</strong></p>
                <p>Bu eserin tüm hakları saklıdır. Yazarın izni olmaksızın elektronik, mekanik, fotokopi veya herhangi bir kayıt sistemiyle kısmen veya tamamen çoğaltılamaz.</p>
                <div class="colophon-meta">
                    <span><strong>Tür:</strong> Güvenlik, Taktik Eğitim, Durum Farkındalığı</span>
                    <span><strong>Format:</strong> Zengin Medya Destekli İnteraktif E-Kitap</span>
                    <span><strong>Güncelleme:</strong> 2026</span>
                </div>
            </div>
        </div>
        """
    })

    # -------------------------------------------------------------
    # SAYFA 2: İçindekiler Tablosu (Fihrist)
    # -------------------------------------------------------------
    pages.append({
        "type": "toc",
        "density": "soft",
        "pageNumber": 2,
        "header": "İÇİNDEKİLER",
        "footer": "2",
        "contentHtml": """
        <div class="toc-page-container">
            <h2 class="section-heading-classic">BÖLÜM İÇİNDEKİLER</h2>
            <div class="heading-gold-line"></div>
            <ul class="toc-list">
                <li onclick="window.reader.goToPage(3)"><span class="toc-title">GİRİŞ & Oscar Wilde Alıntısı</span><span class="toc-dots"></span><span class="toc-page">3</span></li>
                <li onclick="window.reader.goToPage(4)"><span class="toc-title">4.1. Hayatta Kalma Bakış Açısı</span><span class="toc-dots"></span><span class="toc-page">4</span></li>
                <li onclick="window.reader.goToPage(5)"><span class="toc-title">4.2. Temel Prensipler Özeti (1-22)</span><span class="toc-dots"></span><span class="toc-page">5-7</span></li>
                <li onclick="window.reader.goToPage(8)"><span class="toc-title">4.2.1. Duyarsızlık, Kayıtsızlık ve Tedbirsizlik</span><span class="toc-dots"></span><span class="toc-page">8</span></li>
                <li onclick="window.reader.goToPage(9)"><span class="toc-title">4.2.2. Empati Kurun ve İletişimi Sürdürün</span><span class="toc-dots"></span><span class="toc-page">9</span></li>
                <li onclick="window.reader.goToPage(10)"><span class="toc-title">4.2.3. Duyuları Etkin Kullanın ve Anormallikler</span><span class="toc-dots"></span><span class="toc-page">10</span></li>
                <li onclick="window.reader.goToPage(11)"><span class="toc-title">4.2.3. Aydınlatma ve Düşük Işık Taktikleri</span><span class="toc-dots"></span><span class="toc-page">11</span></li>
                <li onclick="window.reader.goToPage(12)"><span class="toc-title">4.2.4. Müdahale Yönteminizi Şartlara Göre Değiştirin</span><span class="toc-dots"></span><span class="toc-page">12</span></li>
                <li onclick="window.reader.goToPage(13)"><span class="toc-title">4.2.5. Her Sorun Kendine Özgü Yöntemle Çözülür</span><span class="toc-dots"></span><span class="toc-page">13</span></li>
                <li onclick="window.reader.goToPage(14)"><span class="toc-title">4.2.6. Doğru Bir Teknikle Nefes Alıp Verin</span><span class="toc-dots"></span><span class="toc-page">14</span></li>
                <li onclick="window.reader.goToPage(15)"><span class="toc-title">4.2.7. & 4.2.8. Saldırı Cisimleri & Ortamı Silahlandırma</span><span class="toc-dots"></span><span class="toc-page">15</span></li>
                <li onclick="window.reader.goToPage(16)"><span class="toc-title">4.2.9. Saldırganın Fiziksel Analizi</span><span class="toc-dots"></span><span class="toc-page">16</span></li>
                <li onclick="window.reader.goToPage(17)"><span class="toc-title">4.2.10. Saldırgan Sayısı ve Konumlanma</span><span class="toc-dots"></span><span class="toc-page">17</span></li>
                <li onclick="window.reader.goToPage(18)"><span class="toc-title">4.2.11. & 4.2.12. Çevreye Duyurma & Hâkim Konum</span><span class="toc-dots"></span><span class="toc-page">18</span></li>
                <li onclick="window.reader.goToPage(19)"><span class="toc-title">4.2.13. Saldırganı Bütün Olarak Değerlendirin</span><span class="toc-dots"></span><span class="toc-page">19</span></li>
                <li onclick="window.reader.goToPage(20)"><span class="toc-title">4.2.14. & 4.2.15. Öz Güven & Doğru Konumlanma</span><span class="toc-dots"></span><span class="toc-page">20</span></li>
                <li onclick="window.reader.goToPage(21)"><span class="toc-title">4.2.16. & 4.2.17. Güvenli Yaklaşım & Uygun Zaman</span><span class="toc-dots"></span><span class="toc-page">21</span></li>
                <li onclick="window.reader.goToPage(22)"><span class="toc-title">4.2.18. Güven Veren Tavırlar Karşısında Rehavet</span><span class="toc-dots"></span><span class="toc-page">22</span></li>
                <li onclick="window.reader.goToPage(23)"><span class="toc-title">4.2.19. En Az Bir Saldırgan Daha Olabileceği</span><span class="toc-dots"></span><span class="toc-page">23</span></li>
                <li onclick="window.reader.goToPage(24)"><span class="toc-title">4.2.20. İkinci Silah İhtimali (+1 Kuralı)</span><span class="toc-dots"></span><span class="toc-page">24</span></li>
                <li onclick="window.reader.goToPage(25)"><span class="toc-title">4.2.21. & 4.2.22. Yaralanma & Güvenlik Güçleri</span><span class="toc-dots"></span><span class="toc-page">25</span></li>
                <li onclick="window.reader.goToPage(26)"><span class="toc-title">Bölüm Özeti & Taktik Kontrol Listesi</span><span class="toc-dots"></span><span class="toc-page">26</span></li>
            </ul>
        </div>
        """
    })

    # -------------------------------------------------------------
    # SAYFA 3: Giriş & Oscar Wilde
    # -------------------------------------------------------------
    pages.append({
        "type": "chapter-start",
        "density": "soft",
        "pageNumber": 3,
        "header": "DÖRDÜNCÜ BÖLÜM: HAYATTA KALMA BAKIŞ AÇISI",
        "footer": "3",
        "contentHtml": """
        <div class="page-content-wrapper">
            <div class="chapter-eyebrow">DÖRDÜNCÜ BÖLÜM</div>
            <h1 class="chapter-head-title">HAYATTA KALMA BAKIŞ AÇISI</h1>
            
            <div class="quote-card-luxury">
                <span class="quote-mark">“</span>
                <p class="quote-text">Düşen bir çığda hiçbir kar tanesi kendisini sorumlu tutmaz. Sizin de bakış açınız olayları üstlenme veya kaçınma yönünüzü belirler.</p>
                <div class="quote-author">— Oscar Wilde</div>
            </div>

            <h3 class="sub-section-title">GİRİŞ</h3>
            <p><span class="drop-cap">İ</span>nsanlar; karşılaştıkları veya kendilerine yönelen bir tehlikenin muhtemel sonuçlarının farkında olsalardı adımlarını karşılaştıkları veya karşılaşabilecekleri durumun vahametine göre atarlardı. Yaşanabilecek olayların sonucunu önceden öngörebilmek ancak olaylara doğru bir bakış açısıyla yaklaşmakla mümkündür.</p>
            <p>Gerçek hayatta yaşanan olaylar göstermektedir ki birçok mücadelenin ardından telafisi mümkün olmayan ve sadece pişmanlık duyulan sonuçlar ortaya çıkmaktadır. Yaşanan kayıpların önemli bir kısmının temel nedeni, olaya müdahale edenlerin gerekli taktik ve teknik donanıma veya teçhizata sahip olmamaları değildir.</p>
            <p>Buradan anlaşılacağı üzere, alınan eğitim ile sahip olunan silah veya teçhizat hayatta kalmak için tek başına yeterli olmamaktadır. Sahip olunan fiziksel ve zihinsel potansiyeli harekete geçirecek, olaylara yön verecek ve doğru kararların alınmasını sağlayacak bir vizyona ihtiyaç vardır.</p>
        </div>
        """
    })

    # -------------------------------------------------------------
    # SAYFA 4: 4.1. Hayatta Kalma Bakış Açısı
    # -------------------------------------------------------------
    pages.append({
        "type": "body",
        "density": "soft",
        "pageNumber": 4,
        "header": "4.1. HAYATTA KALMA BAKIŞ AÇISI",
        "footer": "4",
        "contentHtml": """
        <div class="page-content-wrapper">
            <h2 class="sub-section-title">4.1. Hayatta Kalma Bakış Açısı</h2>
            <p>“Hayatta kalma bakış açısı” olarak nitelendireceğimiz bu vizyon ise ihtiyaç duyulan donanım, teçhizat, taktik ve tekniği organize eden bir yapıdır. Bu bakış açısı, bireyin tehlikeyi henüz ortaya çıkmadan sezmesini, başladığı anda doğru okumasını ve sonrasında en etkili kararı uygulamasını sağlar.</p>
            
            <div class="callout-tactical">
                <div class="callout-tactical-header">
                    <span class="callout-icon">⚡</span>
                    <strong>Taktik Vizyonun Önemi</strong>
                </div>
                <p>Bir silah ya da teçhizat, ancak onu kullanan zihnin vizyonu ve durum farkındalığı kadar etkilidir. Taktik bakış açısı gelişmemiş bir kişi, en modern ekipmana sahip olsa bile rehavetin ve paniğin kurbanı olabilir.</p>
            </div>

            <p>Bu bakış açısını içselleştiren bireyler, kriz anlarında paniğe kapılmak yerine durumu soğukkanlılıkla analiz eder, tehdidin niteliğini belirler ve refleksler yerine stratejik hamlelerle hareket ederler.</p>
            <p>Hayatta kalma bakış açısının temelinde sürekli uyanık bir durum farkındalığı, riskleri minimize etme becerisi ve şartlara göre esneyebilen dinamik karar verme yeteneği yer alır.</p>
        </div>
        """
    })

    # -------------------------------------------------------------
    # SAYFA 5: 4.2. Temel Prensipler Özeti (1-7)
    # -------------------------------------------------------------
    pages.append({
        "type": "body",
        "density": "soft",
        "pageNumber": 5,
        "header": "4.2. TEMEL PRENSİPLER (1-7)",
        "footer": "5",
        "contentHtml": """
        <div class="page-content-wrapper">
            <h2 class="sub-section-title">4.2. Hayatta Kalma Bakış Açısının Temel Prensipleri</h2>
            <p class="lead-text">Hayatta kalma bakış açısını oluşturmak, geliştirmek ve sürdürmek için aşağıda belirtilen temel prensiplere uyulmalıdır:</p>
            
            <div class="principles-grid">
                <div class="principle-card">
                    <span class="p-num">1</span>
                    <div class="p-body">
                        <strong>Duyarsızlık, Kayıtsızlık ve Tedbirsizlik Katilinizdir:</strong> Rehavet ve aşırı güven en büyük zafiyettir.
                    </div>
                </div>
                <div class="principle-card">
                    <span class="p-num">2</span>
                    <div class="p-body">
                        <strong>Empati Kurun ve İletişimi Sürdürün:</strong> Saldırganın ruh halini okumak, çatışmayı büyümeden önlemenin ilk adımıdır.
                    </div>
                </div>
                <div class="principle-card">
                    <span class="p-num">3</span>
                    <div class="p-body">
                        <strong>Duyuları Etkin Kullanın ve Anormallikleri Fark Edin:</strong> Çevredeki en küçük ses, gölge veya hareket erken uyarıdır.
                    </div>
                </div>
                <div class="principle-card">
                    <span class="p-num">4</span>
                    <div class="p-body">
                        <strong>Müdahale Yönteminizi Şartlara Göre Değiştirin:</strong> Sabit şablonlar krizde iflas eder; duruma adapte olun.
                    </div>
                </div>
                <div class="principle-card">
                    <span class="p-num">5</span>
                    <div class="p-body">
                        <strong>Her Sorun Kendine Özgü Yöntemle Çözülür:</strong> Her tehdit özgündür, genel geçer çözümler hata yaptırır.
                    </div>
                </div>
                <div class="principle-card">
                    <span class="p-num">6</span>
                    <div class="p-body">
                        <strong>Doğru Bir Teknikle Nefes Alıp Verin:</strong> Kalp ritmini ve tünel görüşünü kontrol altına alan tek biyolojik anahtar nefestir.
                    </div>
                </div>
                <div class="principle-card">
                    <span class="p-num">7</span>
                    <div class="p-body">
                        <strong>Saldırıda Kullanılabilecek Cisimleri Belirleyin:</strong> Çevrenizdeki her nesne bir silaha veya kalkana dönüşebilir.
                    </div>
                </div>
            </div>
        </div>
        """
    })

    # -------------------------------------------------------------
    # SAYFA 6: 4.2. Temel Prensipler Özeti (8-14)
    # -------------------------------------------------------------
    pages.append({
        "type": "body",
        "density": "soft",
        "pageNumber": 6,
        "header": "4.2. TEMEL PRENSİPLER (8-14)",
        "footer": "6",
        "contentHtml": """
        <div class="page-content-wrapper">
            <h2 class="sub-section-title">Temel Prensipler (Devamı)</h2>
            
            <div class="principles-grid">
                <div class="principle-card">
                    <span class="p-num">8</span>
                    <div class="p-body">
                        <strong>Taşıdığınız Silah Ortamı Silahlandırır:</strong> Silahınız size karşı da kullanılabilir; silah emniyetine azami dikkat gerekir.
                    </div>
                </div>
                <div class="principle-card">
                    <span class="p-num">9</span>
                    <div class="p-body">
                        <strong>Saldırganın Avantaj ve Dezavantajlarını Belirleyin:</strong> Boy, kilo, hız, zemin ve psikolojik durum analizi yapın.
                    </div>
                </div>
                <div class="principle-card">
                    <span class="p-num">10</span>
                    <div class="p-body">
                        <strong>Saldırgan Sayısı ve Yönleriyle İlgili Çıkarımda Bulunun:</strong> Saldırgan asla tek başına olmayabilir.
                    </div>
                </div>
                <div class="principle-card">
                    <span class="p-num">11</span>
                    <div class="p-body">
                        <strong>Tehlikeyi Çevredekilere Duyurup Dikkat Çekin:</strong> Uyarı bağırışı şüphelinin dikkatini dağıtır ve şahit oluşturur.
                    </div>
                </div>
                <div class="principle-card">
                    <span class="p-num">12</span>
                    <div class="p-body">
                        <strong>Saldırı Yönüne Dönün ve Hâkim Yere Geçin:</strong> Sırtınızı açıkta bırakmayın; sütre ve mevzi arayın.
                    </div>
                </div>
                <div class="principle-card">
                    <span class="p-num">13</span>
                    <div class="p-body">
                        <strong>Saldırganı Bir Bütün Olarak Değerlendirin:</strong> Sadece ellerine değil, beden diline, gözlerine ve çevresine bakın.
                    </div>
                </div>
                <div class="principle-card">
                    <span class="p-num">14</span>
                    <div class="p-body">
                        <strong>Aşırı Öz Güven ve İspatlama Hata Yaptırır:</strong> Kahramanlık peşinde koşmak taktiksel bir intihardır.
                    </div>
                </div>
            </div>
        </div>
        """
    })

    # -------------------------------------------------------------
    # SAYFA 7: 4.2. Temel Prensipler Özeti (15-22)
    # -------------------------------------------------------------
    pages.append({
        "type": "body",
        "density": "soft",
        "pageNumber": 7,
        "header": "4.2. TEMEL PRENSİPLER (15-22)",
        "footer": "7",
        "contentHtml": """
        <div class="page-content-wrapper">
            <h2 class="sub-section-title">Temel Prensipler (Devamı)</h2>
            
            <div class="principles-grid">
                <div class="principle-card">
                    <span class="p-num">15</span>
                    <div class="p-body">
                        <strong>Doğru Yerde Konumlanın:</strong> Kaçış rotanız açık, siperiniz sağlam ve görüş açınız geniş olmalıdır.
                    </div>
                </div>
                <div class="principle-card">
                    <span class="p-num">16</span>
                    <div class="p-body">
                        <strong>Müdahale Ederken Güvenli Şekilde Yaklaşın:</strong> Kör noktalardan, mesafeyi koruyarak ve tetikte yaklaşın.
                    </div>
                </div>
                <div class="principle-card">
                    <span class="p-num">17</span>
                    <div class="p-body">
                        <strong>Uygun Zamanda Müdahale Edin:</strong> Erken veya geç müdahale facia getirir; doğru anı kollayın.
                    </div>
                </div>
                <div class="principle-card">
                    <span class="p-num">18</span>
                    <div class="p-body">
                        <strong>Güven Veren Tavırlar Karşısında Rehavete Kapılmayın:</strong> Saldırgan teslim oluyor gibi yapıp aniden saldırabilir.
                    </div>
                </div>
                <div class="principle-card">
                    <span class="p-num">19</span>
                    <div class="p-body">
                        <strong>En Az Bir Saldırganın Daha Olabileceğini Unutmayın:</strong> Birincil hedefe odaklanırken pusuya düşmeyin (Artçı tehdit).
                    </div>
                </div>
                <div class="principle-card">
                    <span class="p-num">20</span>
                    <div class="p-body">
                        <strong>Saldırganda "En Az Bir Tane Daha" Silah Olabilir:</strong> İlk silahı etkisiz kılmak tehdidin bittiği anlamına gelmez.
                    </div>
                </div>
                <div class="principle-card">
                    <span class="p-num">21</span>
                    <div class="p-body">
                        <strong>Yaralanma Halinde Sakin Kalıp Müdahale Edin:</strong> İlk yardım önceliklerini bilin; kanamayı derhal durdurun.
                    </div>
                </div>
                <div class="principle-card">
                    <span class="p-num">22</span>
                    <div class="p-body">
                        <strong>Güvenlik Güçlerine Tam ve Doğru Bilgi Verin:</strong> Eşkâl, konum, silah türü ve yön bilgilerini net aktarın.
                    </div>
                </div>
            </div>
        </div>
        """
    })

    # -------------------------------------------------------------
    # SAYFA 8: 4.2.1. Duyarsızlık, Kayıtsızlık ve Tedbirsizlik
    # -------------------------------------------------------------
    pages.append({
        "type": "body",
        "density": "soft",
        "pageNumber": 8,
        "header": "4.2.1. DUYARSIZLIK VE TEDBİRSİZLİK",
        "footer": "8",
        "contentHtml": """
        <div class="page-content-wrapper">
            <h2 class="sub-section-title">4.2.1. Duyarsızlık, Kayıtsızlık ve Tedbirsizlik Katilinizdir</h2>
            <p>Psikolojik ve fiziksel yorgunluk, görevin içerdiği risklere dair bilinç düzeyi, rutinleşen iş süreçleri veya uzun süre olaysız geçen çalışma dönemleri; bireylerde tehlikelere karşı duyarsızlık, kayıtsızlık ve tedbirsizlik durumunun ortaya çıkmasına yol açabilmektedir.</p>
            
            <div class="figure-card">
                <img src="assets/images/image1.jpeg" alt="Tedbirsizlik ve Yorgunluk Analizi" class="book-img zoomable" onclick="event.stopPropagation(); window.reader.openLightbox(this.src, event);">
                <div class="figure-caption">Görsel 4.1: Rutinleşme ve yorgunluğun taktik farkındalık üzerindeki olumsuz etkisi.</div>
            </div>

            <div class="qr-video-box">
                <img src="assets/images/image2.png" alt="QR Kod Video" class="qr-img zoomable" onclick="event.stopPropagation(); window.reader.openLightbox(this.src, event);">
                <div class="qr-info">
                    <span class="qr-badge">VİDEO MATERYALİ</span>
                    <p class="qr-text">Örnek videoyu izlemek için QR kodunu okutup, listedeki <strong>4.2.1.</strong> numaralı videoyu tıklayınız.</p>
                </div>
            </div>
        </div>
        """
    })

    # -------------------------------------------------------------
    # SAYFA 9: 4.2.2. Empati Kurun ve İletişimi Sürdürün
    # -------------------------------------------------------------
    pages.append({
        "type": "body",
        "density": "soft",
        "pageNumber": 9,
        "header": "4.2.2. EMPATİ VE İLETİŞİM",
        "footer": "9",
        "contentHtml": """
        <div class="page-content-wrapper">
            <h2 class="sub-section-title">4.2.2. Empati Kurun ve İletişimi Sürdürün</h2>
            <p>Karşıdaki kişinin öfkesini, korkusunu ya da panik düzeyini doğru analiz etmek, krizi fiziksel çatışmaya dönüşmeden çözmenin anahtarıdır. Saldırganla göz teması kurmak ve kararlı bir ses tonu kullanmak durumu kontrol altına almayı sağlar.</p>
            
            <div class="figure-card">
                <img src="assets/images/image3.jpeg" alt="Taktik İletişim ve Empati" class="book-img zoomable" onclick="event.stopPropagation(); window.reader.openLightbox(this.src, event);">
                <div class="figure-caption">Görsel 4.2: Kriz esnasında mesafe koruma ve kararlı beden dili ile iletişim.</div>
            </div>

            <div class="qr-video-box">
                <img src="assets/images/image2.png" alt="QR Kod Video" class="qr-img zoomable" onclick="event.stopPropagation(); window.reader.openLightbox(this.src, event);">
                <div class="qr-info">
                    <span class="qr-badge">VİDEO MATERYALİ</span>
                    <p class="qr-text">Örnek videoyu izlemek için QR kodunu okutup, listedeki <strong>4.2.2.</strong> numaralı videoyu tıklayınız.</p>
                </div>
            </div>
        </div>
        """
    })

    # -------------------------------------------------------------
    # SAYFA 10: 4.2.3. Duyuları Etkin Kullanın (Görsel 4)
    # -------------------------------------------------------------
    pages.append({
        "type": "body",
        "density": "soft",
        "pageNumber": 10,
        "header": "4.2.3. DUYULARI ETKİN KULLANIN",
        "footer": "10",
        "contentHtml": """
        <div class="page-content-wrapper">
            <h2 class="sub-section-title">4.2.3. Duyuları Etkin Kullanın ve Anormallikleri Fark Edin</h2>
            <p>İnsan beyni, alışık olduğu çevreye dair kalıplar geliştirir. Rutinin dışına çıkan her unsur (anormal bir ses, mevsim normallerine uymayan giyim tarzı veya tedirgin bakışlar) potansiyel tehlike habercisidir.</p>
            
            <div class="figure-card">
                <img src="assets/images/image4.jpeg" alt="Çevre Taraması ve Durum Farkındalığı" class="book-img zoomable" onclick="event.stopPropagation(); window.reader.openLightbox(this.src, event);">
                <div class="figure-caption">Görsel 4.3: Görsel tarama teknikleri ve şüpheli hareketlerin tespiti.</div>
            </div>

            <div class="qr-video-box">
                <img src="assets/images/image2.png" alt="QR Kod Video" class="qr-img zoomable" onclick="event.stopPropagation(); window.reader.openLightbox(this.src, event);">
                <div class="qr-info">
                    <span class="qr-badge">VİDEO MATERYALİ</span>
                    <p class="qr-text">Örnek videoyu izlemek için QR kodunu okutup, listedeki <strong>4.2.3.1</strong> numaralı videoyu tıklayınız.</p>
                </div>
            </div>
        </div>
        """
    })

    # -------------------------------------------------------------
    # SAYFA 11: 4.2.3. Aydınlatma ve Düşük Işık Taktikleri (Görsel 5)
    # -------------------------------------------------------------
    pages.append({
        "type": "body",
        "density": "soft",
        "pageNumber": 11,
        "header": "4.2.3. AYDINLATMA VE DUYU YÖNETİMİ",
        "footer": "11",
        "contentHtml": """
        <div class="page-content-wrapper">
            <h2 class="sub-section-title">Karanlık Ortamlar ve Aydınlatma Taktikleri</h2>
            <p>Örneğin, karanlık ortamlarda el feneri kullanmak, duymayı engelleyecek düzeydeki gürültülü alanlarda ekstra dikkatli olmak duyuların sınırlarını bilmek açısından elzemdir. 'Yak-bak-söndür-yer değiştir' taktiği siluetinizi gizler.</p>
            
            <div class="figure-card">
                <img src="assets/images/image5.jpeg" alt="Düşük Işıkta Mücadele" class="book-img zoomable" onclick="event.stopPropagation(); window.reader.openLightbox(this.src, event);">
                <div class="figure-caption">Görsel 4.4: Düşük ışık koşullarında fener kullanımı ve hedef siluetini gizleme.</div>
            </div>

            <div class="qr-video-box">
                <img src="assets/images/image2.png" alt="QR Kod Video" class="qr-img zoomable" onclick="event.stopPropagation(); window.reader.openLightbox(this.src, event);">
                <div class="qr-info">
                    <span class="qr-badge">VİDEO MATERYALİ</span>
                    <p class="qr-text">Örnek videoyu izlemek için QR kodunu okutup, listedeki <strong>4.2.3.2</strong> numaralı videoyu tıklayınız.</p>
                </div>
            </div>
        </div>
        """
    })

    # -------------------------------------------------------------
    # SAYFA 12: 4.2.4. Müdahale Yöntemini Şartlara Göre Değiştirin (Görsel 6)
    # -------------------------------------------------------------
    pages.append({
        "type": "body",
        "density": "soft",
        "pageNumber": 12,
        "header": "4.2.4. ŞARTLARA GÖRE MÜDAHALE",
        "footer": "12",
        "contentHtml": """
        <div class="page-content-wrapper">
            <h2 class="sub-section-title">4.2.4. Müdahale Yönteminizi Şartlara Göre Değiştirin</h2>
            <p>Örneğin, ilk karşılaşmada elinde herhangi bir silah bulunmayan şüphelinin, aniden cebinden veya belinden bir kesici alet ya da ateşli silah çıkarması durumunda kullanılan taktik derhal revize edilmeli ve güvenli mesafeye çıkılmalıdır.</p>
            
            <div class="figure-card">
                <img src="assets/images/image6.jpeg" alt="Dinamik Müdahale Yöntemleri" class="book-img zoomable" onclick="event.stopPropagation(); window.reader.openLightbox(this.src, event);">
                <div class="figure-caption">Görsel 4.5: Tehdit seviyesi yükseldiğinde orantılı ve güvenli karşılık verme.</div>
            </div>

            <div class="qr-video-box">
                <img src="assets/images/image2.png" alt="QR Kod Video" class="qr-img zoomable" onclick="event.stopPropagation(); window.reader.openLightbox(this.src, event);">
                <div class="qr-info">
                    <span class="qr-badge">VİDEO MATERYALİ</span>
                    <p class="qr-text">Örnek videoyu izlemek için QR kodunu okutup listedeki <strong>4.2.4</strong> numaralı videoyu tıklayınız.</p>
                </div>
            </div>
        </div>
        """
    })

    # -------------------------------------------------------------
    # SAYFA 13: 4.2.5. Her Sorun Kendine Özgü Yöntemle Çözülür
    # -------------------------------------------------------------
    pages.append({
        "type": "body",
        "density": "soft",
        "pageNumber": 13,
        "header": "4.2.5. ÖZGÜN ÇÖZÜMLER",
        "footer": "13",
        "contentHtml": """
        <div class="page-content-wrapper">
            <h2 class="sub-section-title">4.2.5. Her Sorun Kendine Özgü Yöntemle Çözülür</h2>
            <p>Her krizin kendine ait dinamikleri, mekânsal kısıtlamaları ve insan faktörleri vardır. Ezberlenmiş tek tip hareket kalıpları beklenmedik durumlarda felakete yol açar. Çözüm, o anki şartların mantığına uygun üretilmelidir.</p>
            
            <div class="callout-tactical">
                <div class="callout-tactical-header">
                    <span class="callout-icon">💡</span>
                    <strong>Esnek Taktik Yaklaşım</strong>
                </div>
                <p>Bir önceki operasyonda veya olayda başarılı olmuş bir yöntem, farklı bir coğrafyada ya da farklı bir psikolojik ortamda ölümcül bir tuzağa dönüşebilir. Taktik zihin kalıplara değil, anın dinamiklerine odaklanır.</p>
            </div>

            <div class="qr-video-box">
                <img src="assets/images/image2.png" alt="QR Kod Video" class="qr-img zoomable" onclick="event.stopPropagation(); window.reader.openLightbox(this.src, event);">
                <div class="qr-info">
                    <span class="qr-badge">VİDEO MATERYALİ</span>
                    <p class="qr-text">Örnek videoyu izlemek için QR kodunu okutup listedeki <strong>4.2.5</strong> numaralı videoyu tıklayınız.</p>
                </div>
            </div>
        </div>
        """
    })

    # -------------------------------------------------------------
    # SAYFA 14: 4.2.6. Doğru Teknikle Nefes Alıp Verin (Görsel 7)
    # -------------------------------------------------------------
    pages.append({
        "type": "body",
        "density": "soft",
        "pageNumber": 14,
        "header": "4.2.6. TAKTİK NEFES KONTROLÜ",
        "footer": "14",
        "contentHtml": """
        <div class="page-content-wrapper">
            <h2 class="sub-section-title">4.2.6. Doğru Bir Teknikle Nefes Alıp Verin</h2>
            <p>Yoğun stres ve hayati tehdit anında kalp atış hızının aşırı yükselmesi ince motor becerileri köreltir ve tünel görüşüne sebep olur. Bu fizyolojik kilitlenmeyi aşmanın tek yolu kontrollü diyafram nefesidir.</p>

            <div class="figure-card">
                <img src="assets/images/image7.jpeg" alt="Taktik Nefes Egzersizi" class="book-img zoomable" onclick="event.stopPropagation(); window.reader.openLightbox(this.src, event);">
                <div class="figure-caption">Görsel 4.6: 4 saniye nefes al, 4 saniye tut, 4 saniye ver, 4 saniye bekle döngüsü.</div>
            </div>

            <div class="qr-video-box">
                <img src="assets/images/image2.png" alt="QR Kod Video" class="qr-img zoomable" onclick="event.stopPropagation(); window.reader.openLightbox(this.src, event);">
                <div class="qr-info">
                    <span class="qr-badge">VİDEO MATERYALİ</span>
                    <p class="qr-text">Örnek videoyu izlemek için QR kodunu okutup listedeki <strong>4.2.6</strong> numaralı videoyu tıklayınız.</p>
                </div>
            </div>
        </div>
        """
    })

    # -------------------------------------------------------------
    # SAYFA 15: 4.2.7 & 4.2.8 Cisimler & Ortamı Silahlandırma
    # -------------------------------------------------------------
    pages.append({
        "type": "body",
        "density": "soft",
        "pageNumber": 15,
        "header": "4.2.7. & 4.2.8. SİLAH VE ÇEVRE ANALİZİ",
        "footer": "15",
        "contentHtml": """
        <div class="page-content-wrapper">
            <h2 class="sub-section-title">4.2.7. Saldırıda Kullanılabilecek Cisimleri Belirleyin</h2>
            <p>Mücadele ortamında bulunan sandalyeler, şişeler, yangın tüpleri veya kemerler; hem saldırgan için silaha hem de savunma yapan kişi için etkili bir kalkan veya caydırıcıya dönüşebilir.</p>
            
            <div class="qr-video-box">
                <img src="assets/images/image2.png" alt="QR Kod Video" class="qr-img zoomable" onclick="event.stopPropagation(); window.reader.openLightbox(this.src, event);">
                <div class="qr-info">
                    <span class="qr-badge">VİDEO MATERYALİ</span>
                    <p class="qr-text">Örnek videoyu izlemek için QR kodunu okutup listedeki <strong>4.2.7</strong> numaralı videoyu tıklayınız.</p>
                </div>
            </div>

            <h2 class="sub-section-title" style="margin-top: 15px;">4.2.8. Taşıdığınız Silah Ortamı Silahlandırır</h2>
            <p>Üzerinizdeki silah, yalnızca sizin gücünüz değildir; yakın temas boğuşmalarında saldırganın eline geçebilecek ölümcül bir tehdittir. Kılıf emniyeti ve güvenli mesafe kuralı hayati önem taşır.</p>

            <div class="qr-video-box">
                <img src="assets/images/image2.png" alt="QR Kod Video" class="qr-img zoomable" onclick="event.stopPropagation(); window.reader.openLightbox(this.src, event);">
                <div class="qr-info">
                    <span class="qr-badge">VİDEO MATERYALİ</span>
                    <p class="qr-text">Örnek videoyu izlemek için QR kodunu okutup listedeki <strong>4.2.8</strong> numaralı videoyu tıklayınız.</p>
                </div>
            </div>
        </div>
        """
    })

    # -------------------------------------------------------------
    # SAYFA 16: 4.2.9. Saldırganın Fiziksel Analizi
    # -------------------------------------------------------------
    pages.append({
        "type": "body",
        "density": "soft",
        "pageNumber": 16,
        "header": "4.2.9. SALDIRGANIN FİZİKSEL ANALİZİ",
        "footer": "16",
        "contentHtml": """
        <div class="page-content-wrapper">
            <h2 class="sub-section-title">4.2.9. Saldırganın Fiziksel Avantaj ve Dezavantajlarını Belirleyin</h2>
            <p>Saldırganın boyu, kilosu, çevikliği ve kullandığı el doğrudan mücadele stratejisini belirler. Sizden iri birine kaba kuvvetle karşılık vermek yerine kaldıraç prensipleri ve denge bozma taktikleri uygulanmalıdır.</p>

            <div class="callout-tactical">
                <div class="callout-tactical-header">
                    <span class="callout-icon">🎯</span>
                    <strong>Taktik Analiz Kriterleri</strong>
                </div>
                <ul>
                    <li><strong>Menzil:</strong> Saldırganın kol ve bacak erişim mesafesi.</li>
                    <li><strong>Denge Merkezi:</strong> Ayak basış pozisyonu ve ağırlık dağılımı.</li>
                    <li><strong>Zayıf Noktalar:</strong> Gözler, boğaz, kasık ve diz eklemleri.</li>
                </ul>
            </div>

            <div class="qr-video-box">
                <img src="assets/images/image2.png" alt="QR Kod Video" class="qr-img zoomable" onclick="event.stopPropagation(); window.reader.openLightbox(this.src, event);">
                <div class="qr-info">
                    <span class="qr-badge">VİDEO MATERYALİ</span>
                    <p class="qr-text">Örnek videoyu izlemek için QR kodunu okutup listedeki <strong>4.2.9</strong> numaralı videoyu tıklayınız.</p>
                </div>
            </div>
        </div>
        """
    })

    # -------------------------------------------------------------
    # SAYFA 17: 4.2.10. Saldırgan Sayısı ve Konumlanma (Görsel 8)
    # -------------------------------------------------------------
    pages.append({
        "type": "body",
        "density": "soft",
        "pageNumber": 17,
        "header": "4.2.10. SALDIRGAN SAYISI VE KONUMLANMA",
        "footer": "17",
        "contentHtml": """
        <div class="page-content-wrapper">
            <h2 class="sub-section-title">4.2.10. Saldırgan Sayısı ve Saldırı Yönleriyle İlgili Çıkarımda Bulunun</h2>
            <p>Birden fazla saldırganın varlığında çevrelenmemek hayatta kalmanın birinci kuralıdır. Saldırganları bir hizada tutacak açılı adımlar atılmalı, biri diğerine kalkan yapılmalıdır.</p>

            <div class="figure-card">
                <img src="assets/images/image8.jpeg" alt="Çoklu Tehdit Konumlanması" class="book-img zoomable" onclick="event.stopPropagation(); window.reader.openLightbox(this.src, event);">
                <div class="figure-caption">Görsel 4.7: Çoklu saldırgan karşısında hat oluşturma ve açı yönetimi.</div>
            </div>

            <div class="qr-video-box">
                <img src="assets/images/image2.png" alt="QR Kod Video" class="qr-img zoomable" onclick="event.stopPropagation(); window.reader.openLightbox(this.src, event);">
                <div class="qr-info">
                    <span class="qr-badge">VİDEO MATERYALİ</span>
                    <p class="qr-text">Örnek videoyu izlemek için QR kodunu okutup listedeki <strong>4.2.10</strong> numaralı videoyu tıklayınız.</p>
                </div>
            </div>
        </div>
        """
    })

    # -------------------------------------------------------------
    # SAYFA 18: 4.2.11 & 4.2.12 Çevreye Duyurma & Hâkim Konum
    # -------------------------------------------------------------
    pages.append({
        "type": "body",
        "density": "soft",
        "pageNumber": 18,
        "header": "4.2.11. & 4.2.12. ERKEN UYARI VE HÂKİMİYET",
        "footer": "18",
        "contentHtml": """
        <div class="page-content-wrapper">
            <h2 class="sub-section-title">4.2.11. Tehlikenin Varlığını Çevredekilere Duyurun</h2>
            <p>Yüksek sesle bağırmak ("Bıçak var!", "Silahı bırak!"), çevredekilerin kaçmasını sağlarken saldırganın gizlilik avantajını yok eder ve onu psikolojik baskı altına sokar.</p>
            
            <div class="qr-video-box">
                <img src="assets/images/image2.png" alt="QR Kod Video" class="qr-img zoomable" onclick="event.stopPropagation(); window.reader.openLightbox(this.src, event);">
                <div class="qr-info">
                    <span class="qr-badge">VİDEO MATERYALİ</span>
                    <p class="qr-text">Örnek videoyu izlemek için QR kodunu okutup listedeki <strong>4.2.11</strong> numaralı videoyu tıklayınız.</p>
                </div>
            </div>

            <h2 class="sub-section-title" style="margin-top: 15px;">4.2.12. Saldırının Geldiği Yöne Dönün ve Hâkim Yere Geçin</h2>
            <p>Sırtınızı tehdide dönerek kontrolsüzce kaçmak savunmasız bırakır. Tehdide dönmeli, güvenli mesafeye çekilmeli ve arkasında katı bir sütre bulunan hâkim noktaya yerleşilmelidir.</p>

            <div class="qr-video-box">
                <img src="assets/images/image2.png" alt="QR Kod Video" class="qr-img zoomable" onclick="event.stopPropagation(); window.reader.openLightbox(this.src, event);">
                <div class="qr-info">
                    <span class="qr-badge">VİDEO MATERYALİ</span>
                    <p class="qr-text">Örnek videoyu izlemek için QR kodunu okutup listedeki <strong>4.2.12</strong> numaralı videoyu tıklayınız.</p>
                </div>
            </div>
        </div>
        """
    })

    # -------------------------------------------------------------
    # SAYFA 19: 4.2.13. Saldırganı Bütün Olarak Değerlendirin (Görsel 9)
    # -------------------------------------------------------------
    pages.append({
        "type": "body",
        "density": "soft",
        "pageNumber": 19,
        "header": "4.2.13. BÜTÜNCÜL TEHDİT ANALİZİ",
        "footer": "19",
        "contentHtml": """
        <div class="page-content-wrapper">
            <h2 class="sub-section-title">4.2.13. Saldırgan Sadece Gördüğünüz Kesit Değildir</h2>
            <p>Saldırganı sadece elindeki aletle değerlendirmek yanılgıdır. Beden dili, ceplerindeki kabarıklıklar, duruş açısı ve kaçış rotası bir bütün olarak analiz edilmelidir.</p>

            <div class="figure-card">
                <img src="assets/images/image9.jpeg" alt="Saldırgan Analizi ve Bütüncül Bakış" class="book-img zoomable" onclick="event.stopPropagation(); window.reader.openLightbox(this.src, event);">
                <div class="figure-caption">Görsel 4.8: Beden dili analizi, saklanan eller ve duruş açısı.</div>
            </div>

            <div class="qr-video-box">
                <img src="assets/images/image2.png" alt="QR Kod Video" class="qr-img zoomable" onclick="event.stopPropagation(); window.reader.openLightbox(this.src, event);">
                <div class="qr-info">
                    <span class="qr-badge">VİDEO MATERYALİ</span>
                    <p class="qr-text">Örnek videoyu izlemek için QR kodunu okutup listedeki <strong>4.2.13</strong> numaralı videoyu tıklayınız.</p>
                </div>
            </div>
        </div>
        """
    })

    # -------------------------------------------------------------
    # SAYFA 20: 4.2.14 & 4.2.15 Öz Güven & Doğru Konumlanma
    # -------------------------------------------------------------
    pages.append({
        "type": "body",
        "density": "soft",
        "pageNumber": 20,
        "header": "4.2.14. & 4.2.15. ÖZ GÜVEN VE KONUMLANMA",
        "footer": "20",
        "contentHtml": """
        <div class="page-content-wrapper">
            <h2 class="sub-section-title">4.2.14. Aşırı Öz Güven ve Kendini İspatlama Hata Yaptırır</h2>
            <p>"Bana bir şey olmaz", "Ben bunu kolayca alt ederim" yanılgısı ölümcül hataların başlangıcıdır. Profesyonellik, tehdidi asla hafife almamaktır.</p>
            
            <div class="qr-video-box">
                <img src="assets/images/image2.png" alt="QR Kod Video" class="qr-img zoomable" onclick="event.stopPropagation(); window.reader.openLightbox(this.src, event);">
                <div class="qr-info">
                    <span class="qr-badge">VİDEO MATERYALİ</span>
                    <p class="qr-text">Örnek videoyu izlemek için QR kodunu okutup listedeki <strong>4.2.14</strong> numaralı videoyu tıklayınız.</p>
                </div>
            </div>

            <h2 class="sub-section-title" style="margin-top: 15px;">4.2.15. Doğru Yerde Konumlanın</h2>
            <p>Doğru konumlanma; saldırganın hücum açısını daraltan, size kaçış ve manevra alanı tanıyan, arkadan gelebilecek tehditleri görmenizi sağlayan geometrik üstünlüktür.</p>

            <div class="qr-video-box">
                <img src="assets/images/image2.png" alt="QR Kod Video" class="qr-img zoomable" onclick="event.stopPropagation(); window.reader.openLightbox(this.src, event);">
                <div class="qr-info">
                    <span class="qr-badge">VİDEO MATERYALİ</span>
                    <p class="qr-text">Örnek videoyu izlemek için QR kodunu okutup listedeki <strong>4.2.15</strong> numaralı videoyu tıklayınız.</p>
                </div>
            </div>
        </div>
        """
    })

    # -------------------------------------------------------------
    # SAYFA 21: 4.2.16 & 4.2.17 Güvenli Yaklaşım & Uygun Zaman (Görsel 10)
    # -------------------------------------------------------------
    pages.append({
        "type": "body",
        "density": "soft",
        "pageNumber": 21,
        "header": "4.2.16. & 4.2.17. YAKLAŞIM VE MÜDAHALE ANI",
        "footer": "21",
        "contentHtml": """
        <div class="page-content-wrapper">
            <h2 class="sub-section-title">4.2.16. & 4.2.17. Güvenli Yaklaşım ve Uygun Müdahale Zamanı</h2>
            <p>Şüpheliye doğrudan cepheden değil, açılı yaklaşılmalıdır. Tehdit sonlandırıldığı anda güç kullanımı durdurulmalı ve kontrol prosedürüne geçilmelidir.</p>

            <div class="figure-card">
                <img src="assets/images/image10.jpeg" alt="Zamanlama ve Müdahale Kontrolü" class="book-img zoomable" onclick="event.stopPropagation(); window.reader.openLightbox(this.src, event);">
                <div class="figure-caption">Görsel 4.9: Kontrol altına alma ve müdahalenin hukuki/taktiksel sınırları.</div>
            </div>

            <div class="qr-video-box">
                <img src="assets/images/image2.png" alt="QR Kod Video" class="qr-img zoomable" onclick="event.stopPropagation(); window.reader.openLightbox(this.src, event);">
                <div class="qr-info">
                    <span class="qr-badge">VİDEO MATERYALİ</span>
                    <p class="qr-text">Örnek videoyu izlemek için QR kodunu okutup listedeki <strong>4.2.17</strong> numaralı videoyu tıklayınız.</p>
                </div>
            </div>
        </div>
        """
    })

    # -------------------------------------------------------------
    # SAYFA 22: 4.2.18. Rehavete Kapılmayın (Görsel 11)
    # -------------------------------------------------------------
    pages.append({
        "type": "body",
        "density": "soft",
        "pageNumber": 22,
        "header": "4.2.18. REHAVETE KAPILMAYIN",
        "footer": "22",
        "contentHtml": """
        <div class="page-content-wrapper">
            <h2 class="sub-section-title">4.2.18. Güven Veren Tavırlar Karşısında Rehavete Kapılmayın</h2>
            <p>Bazı saldırganlar kaçmak veya aniden saldırmak için 'sahte itaat' gösterirler. Şüpheli teslim oluyor gibi görünse dahi arama tamamlanana kadar tetikte kalınmalıdır.</p>

            <div class="figure-card">
                <img src="assets/images/image11.jpeg" alt="Sahte İtaat ve Taktik Tetiktelik" class="book-img zoomable" onclick="event.stopPropagation(); window.reader.openLightbox(this.src, event);">
                <div class="figure-caption">Görsel 4.10: Teslim olma anında dahi mesafeyi koruma ve kontrol prosedürü.</div>
            </div>

            <div class="qr-video-box">
                <img src="assets/images/image2.png" alt="QR Kod Video" class="qr-img zoomable" onclick="event.stopPropagation(); window.reader.openLightbox(this.src, event);">
                <div class="qr-info">
                    <span class="qr-badge">VİDEO MATERYALİ</span>
                    <p class="qr-text">Örnek videoyu izlemek için QR kodunu okutup listedeki <strong>4.2.18</strong> numaralı videoyu tıklayınız.</p>
                </div>
            </div>
        </div>
        """
    })

    # -------------------------------------------------------------
    # SAYFA 23: 4.2.19. Artçı Saldırgan İhtimali (Görsel 12)
    # -------------------------------------------------------------
    pages.append({
        "type": "body",
        "density": "soft",
        "pageNumber": 23,
        "header": "4.2.19. ARTÇI SALDIRGAN İHTİMALİ",
        "footer": "23",
        "contentHtml": """
        <div class="page-content-wrapper">
            <h2 class="sub-section-title">4.2.19. En Az Bir Saldırganın Daha Olabileceğini Unutmayın</h2>
            <p>Kaçan şüphelinin peşinden körü körüne koşmak pusuya düşmektir. Birincil tehdit etkisiz hale geldiğinde derhal 360 derece çevre taraması yapılmalıdır.</p>

            <div class="figure-card">
                <img src="assets/images/image12.jpeg" alt="Artçı Tehdit ve Pusu Analizi" class="book-img zoomable" onclick="event.stopPropagation(); window.reader.openLightbox(this.src, event);">
                <div class="figure-caption">Görsel 4.11: Takip esnasında pusu riskleri ve çevre emniyeti.</div>
            </div>

            <div class="qr-video-box">
                <img src="assets/images/image2.png" alt="QR Kod Video" class="qr-img zoomable" onclick="event.stopPropagation(); window.reader.openLightbox(this.src, event);">
                <div class="qr-info">
                    <span class="qr-badge">VİDEO MATERYALİ</span>
                    <p class="qr-text">Örnek videoyu izlemek için QR kodunu okutup listedeki <strong>4.2.19</strong> numaralı videoyu tıklayınız.</p>
                </div>
            </div>
        </div>
        """
    })

    # -------------------------------------------------------------
    # SAYFA 24: 4.2.20. İkinci Silah İhtimali (Görsel 13)
    # -------------------------------------------------------------
    pages.append({
        "type": "body",
        "density": "soft",
        "pageNumber": 24,
        "header": "4.2.20. İKİNCİ SİLAH İHTİMALİ",
        "footer": "24",
        "contentHtml": """
        <div class="page-content-wrapper">
            <h2 class="sub-section-title">4.2.20. Saldırganda Silah Varsa Bir Tane Daha Olabileceğini Unutmayın</h2>
            <p>Taktik literatürde <strong>"+1 Kuralı"</strong> esastır: Her zaman gizlenmiş bir ikincil silah veya ek bir saldırgan daha varmış gibi hareket edilir.</p>

            <div class="figure-card">
                <img src="assets/images/image13.jpeg" alt="+1 Kuralı ve İkincil Silahlar" class="book-img zoomable" onclick="event.stopPropagation(); window.reader.openLightbox(this.src, event);">
                <div class="figure-caption">Görsel 4.12: Gizlenmiş ikincil silahlar ve detaylı üst arama protokolü.</div>
            </div>

            <div class="qr-video-box">
                <img src="assets/images/image2.png" alt="QR Kod Video" class="qr-img zoomable" onclick="event.stopPropagation(); window.reader.openLightbox(this.src, event);">
                <div class="qr-info">
                    <span class="qr-badge">VİDEO MATERYALİ</span>
                    <p class="qr-text">Örnek videoyu izlemek için QR kodunu okutup listedeki <strong>4.2.20</strong> numaralı videoyu tıklayınız.</p>
                </div>
            </div>
        </div>
        """
    })

    # -------------------------------------------------------------
    # SAYFA 25: 4.2.21 & 4.2.22 Yaralanma & Güvenlik Güçleri
    # -------------------------------------------------------------
    pages.append({
        "type": "body",
        "density": "soft",
        "pageNumber": 25,
        "header": "4.2.21. & 4.2.22. MÜDAHALE VE YARDIM",
        "footer": "25",
        "contentHtml": """
        <div class="page-content-wrapper">
            <h2 class="sub-section-title">4.2.21. Yaralanma veya Ölüm Meydana Gelirse</h2>
            <p>Öncelik kendi vücudunuzu kontrol etmektir (Adrenalin nedeniyle yara fark edilmeyebilir). Ardından ekip arkadaşları kontrol edilir ve acil kanama tamponu uygulanır.</p>
            
            <div class="qr-video-box">
                <img src="assets/images/image2.png" alt="QR Kod Video" class="qr-img zoomable" onclick="event.stopPropagation(); window.reader.openLightbox(this.src, event);">
                <div class="qr-info">
                    <span class="qr-badge">VİDEO MATERYALİ</span>
                    <p class="qr-text">Örnek videoyu izlemek için QR kodunu okutup listedeki <strong>4.2.21</strong> numaralı videoyu tıklayınız.</p>
                </div>
            </div>

            <h2 class="sub-section-title" style="margin-top: 15px;">4.2.22. Güvenlik Güçlerine Tam ve Doğru Bilgi Verin</h2>
            <p>112 acil çağrı merkezine olay yeri adresi, yaralı sayısı, eşkâl, kaçış yönü ve silah türü net olarak bildirilmelidir.</p>

            <div class="qr-video-box">
                <img src="assets/images/image2.png" alt="QR Kod Video" class="qr-img zoomable" onclick="event.stopPropagation(); window.reader.openLightbox(this.src, event);">
                <div class="qr-info">
                    <span class="qr-badge">VİDEO MATERYALİ</span>
                    <p class="qr-text">Örnek videoyu izlemek için QR kodunu okutup listedeki <strong>4.2.22</strong> numaralı videoyu tıklayınız.</p>
                </div>
            </div>
        </div>
        """
    })

    # -------------------------------------------------------------
    # SAYFA 26: Bölüm Değerlendirmesi & Taktik Kontrol Listesi
    # -------------------------------------------------------------
    pages.append({
        "type": "body",
        "density": "soft",
        "pageNumber": 26,
        "header": "BÖLÜM ÖZETİ VE KONTROL LİSTESİ",
        "footer": "26",
        "contentHtml": """
        <div class="page-content-wrapper">
            <h2 class="sub-section-title">4. Bölüm Özeti: Hayatta Kalma Kontrol Listesi</h2>
            <p class="lead-text">Kritik bir tehdit karşısında saniyeler içinde hatırlanması gereken altın kurallar:</p>

            <div class="callout-tactical">
                <div class="callout-tactical-header">
                    <span class="callout-icon">📋</span>
                    <strong>Taktik Kontrol Maddeleri</strong>
                </div>
                <ul>
                    <li><strong>Zihinsel Hazırlık:</strong> Rehaveti bırakın, tehlikenin heran çıkabileceğini kabul edin.</li>
                    <li><strong>Biyolojik Kontrol:</strong> Taktik nefes (4x4 kutu nefesi) ile nabzınızı dengede tutun.</li>
                    <li><strong>360° Farkındalık:</strong> Sadece birincil saldırgana değil, arka plana ve olası ikinci saldırgana dikkat edin (+1 Kuralı).</li>
                    <li><strong>Geometrik Üstünlük:</strong> Açılı hareket edin, sütre gerisinde durun ve kaçış koridorunuzu açık tutun.</li>
                    <li><strong>Soğukkanlı Müdahale:</strong> Tehdit sona erdiği anda güç kullanımını kesin ve çevre güvenliğini alın.</li>
                </ul>
            </div>

            <p style="margin-top: 15px; font-style: italic; color: var(--paper-text-muted); text-align: center;">
                "Hazırlıksız yakalanan taktik personel yoktur; durum farkındalığını kaybetmiş zihin vardır."
            </p>
        </div>
        """
    })

    # -------------------------------------------------------------
    # SAYFA 27: Sert Arka Kapak (Hardcover Back)
    # -------------------------------------------------------------
    pages.append({
        "type": "cover-back",
        "density": "hard",
        "pageNumber": 27,
        "contentHtml": """
        <div class="back-cover-content">
            <div class="cover-ornament top-ornament"></div>
            <div class="back-quote-box">
                <p class="back-quote-text">“Bir mücadelede hayatta kalmak; sadece sahip olduğunuz teçhizatla değil, tehdidi doğmadan sezen ve kriz anında doğru kararları alan zihinsel hazırlığınızla mümkündür.”</p>
                <div class="back-author-quote">— Kenan Turan</div>
            </div>
            <div class="back-blurb">
                <p><strong>TAKTİK MÜCADELENİN TEMELLERİ</strong> serisinin bu dördüncü bölümü; hayati kriz anlarında soğukkanlılığı koruma, tehdit analizi yapma, nefes kontrolü ve doğru taktik konumlanma prensiplerini zengin görsel ve video materyalleriyle okuyucuya sunmaktadır.</p>
            </div>
            <div class="back-barcode-box">
                <div class="barcode-lines">
                    <span class="b-line b-1"></span><span class="b-line b-2"></span><span class="b-line b-1"></span>
                    <span class="b-line b-3"></span><span class="b-line b-2"></span><span class="b-line b-1"></span>
                    <span class="b-line b-3"></span><span class="b-line b-2"></span><span class="b-line b-1"></span>
                    <span class="b-line b-1"></span><span class="b-line b-3"></span><span class="b-line b-2"></span>
                </div>
                <div class="barcode-isbn">ISBN 978-605-0000-04-0</div>
            </div>
            <div class="cover-ornament bottom-ornament"></div>
        </div>
        """
    })

    output_js_path = os.path.join(JS_DIR, "book-data.js")
    with open(output_js_path, 'w', encoding='utf-8') as f:
        f.write("/**\n * Otomatik Oluşturulmuş Kitap Verisi (28 Sayfalık Ferah Mizanpaj)\n * Taktik Mücadelenin Temelleri - Kenan Turan\n */\n")
        f.write("window.BOOK_PAGES = ")
        json.dump(pages, f, ensure_ascii=False, indent=2)
        f.write(";\n")
    
    print(f"Başarıyla {len(pages)} sayfalık kitap verisi üretildi: {output_js_path}")

if __name__ == "__main__":
    extract_media(DOCX_PATH)
    build_book_data()
