/**
 * 3D Flipbook Okuyucu Kontrolcüsü (reader.js)
 * Taktik Mücadelenin Temelleri - Hayatta Kalma Bakış Açısı
 * Kenan Turan
 */

class EKitapReader {
    constructor() {
        this.pageFlip = null;
        this.totalPages = 0;
        this.currentPage = 0;
        this.savedBookmark = parseInt(localStorage.getItem('ekitap_bookmark') || '-1', 10);
        this.currentTheme = localStorage.getItem('ekitap_theme') || 'cream';
        
        this.initDOM();
    }

    initDOM() {
        document.addEventListener('DOMContentLoaded', () => {
            this.applyTheme(this.currentTheme);
            this.renderPages();
            this.initFlipEngine();
            this.setupUIEvents();
            this.setupKeyboard();
            this.setupInteractiveElements();
            this.updateSoundIcon();
        });
    }

    renderPages() {
        const bookContainer = document.getElementById('flipbook');
        if (!bookContainer || !window.BOOK_PAGES) return;

        bookContainer.innerHTML = '';
        this.totalPages = window.BOOK_PAGES.length;

        window.BOOK_PAGES.forEach((p, idx) => {
            const pageEl = document.createElement('div');
            pageEl.className = `page page-${p.type}`;
            pageEl.setAttribute('data-density', p.density || 'soft');
            pageEl.id = `page-${idx}`;

            let inner = '';
            // Kapak olmayan sayfalara şık üstbilgi ve altbilgi ekle (Klasik edebi mizanpaj)
            if (p.type !== 'cover-front' && p.type !== 'cover-back') {
                const runningTitle = (idx % 2 === 0) 
                    ? 'TAKTİK MÜCADELENİN TEMELLERİ' 
                    : 'HAYATTA KALMA BAKIŞ AÇISI';
                
                if (idx % 2 === 0) {
                    inner += `
                        <div class="page-header">
                            <span class="header-page-num">${idx}</span>
                            <span>${runningTitle}</span>
                            <span>4. BÖLÜM</span>
                        </div>
                    `;
                } else {
                    inner += `
                        <div class="page-header">
                            <span>4. BÖLÜM</span>
                            <span>${runningTitle}</span>
                            <span class="header-page-num">${idx}</span>
                        </div>
                    `;
                }
            }

            inner += p.contentHtml;

            if (p.type !== 'cover-front' && p.type !== 'cover-back') {
                inner += `
                    <div class="page-footer">
                        <span class="page-num-pill">SAYFA ${idx}</span>
                    </div>
                `;
            }

            pageEl.innerHTML = inner;
            bookContainer.appendChild(pageEl);
        });

        this.renderDrawerTOC();
    }

    initFlipEngine() {
        const bookEl = document.getElementById('flipbook');
        if (!bookEl || !window.St || !window.St.PageFlip) {
            console.error('StPageFlip kütüphanesi yüklenemedi.');
            return;
        }

        // Ekran boyutuna göre baz çözünürlük
        const isMobile = window.innerWidth <= 768;

        this.pageFlip = new window.St.PageFlip(bookEl, {
            width: 550,
            height: 750,
            size: 'stretch',
            minWidth: 320,
            maxWidth: 1000,
            minHeight: 440,
            maxHeight: 1350,
            maxShadowOpacity: 0.55,
            showCover: true,
            mobileScrollSupport: false,
            usePortrait: true,
            startPage: 0
        });

        const pagesList = document.querySelectorAll('.page');
        this.pageFlip.loadFromHTML(pagesList);

        // Sayfa Değişimi Olayı
        this.pageFlip.on('flip', (e) => {
            this.currentPage = e.data;
            if (window.bookSound) {
                window.bookSound.playPageFlip();
            }
            this.onPageChanged(this.currentPage);
        });

        // Başlangıçta son kalınan sayfa varsa sor veya oradan başla
        const lastPage = parseInt(localStorage.getItem('ekitap_last_page') || '0', 10);
        if (lastPage > 0 && lastPage < this.totalPages) {
            setTimeout(() => {
                this.pageFlip.turnToPage(lastPage);
            }, 600);
        }

        this.onPageChanged(0);
    }

    onPageChanged(pageIndex) {
        this.currentPage = pageIndex;
        localStorage.setItem('ekitap_last_page', pageIndex);

        // Sayfa Göstergesi Güncelle
        const indicator = document.getElementById('pageIndicator');
        if (indicator) {
            if (pageIndex === 0) {
                indicator.innerText = 'Ön Kapak';
            } else if (pageIndex === this.totalPages - 1) {
                indicator.innerText = 'Arka Kapak';
            } else {
                indicator.innerText = `Sayfa ${pageIndex} / ${this.totalPages - 2}`;
            }
        }

        // İlerleme Çubuğu Güncelle
        const progressFill = document.getElementById('progressBarFill');
        if (progressFill && this.totalPages > 1) {
            const pct = (pageIndex / (this.totalPages - 1)) * 100;
            progressFill.style.width = `${pct}%`;
        }

        // Kitap Ayracı Durumu
        this.updateBookmarkRibbonState();

        // Çekmece TOC Aktif Eleman
        this.updateActiveDrawerItem(pageIndex);
    }

    setupUIEvents() {
        // Alt Dok Kontrolleri
        document.getElementById('btnPrev')?.addEventListener('click', () => this.pageFlip?.flipPrev());
        document.getElementById('btnNext')?.addEventListener('click', () => this.pageFlip?.flipNext());
        document.getElementById('btnFirst')?.addEventListener('click', () => this.pageFlip?.turnToPage(0));
        document.getElementById('btnLast')?.addEventListener('click', () => this.pageFlip?.turnToPage(this.totalPages - 1));

        // Yan Oklar
        document.getElementById('sidePrev')?.addEventListener('click', () => this.pageFlip?.flipPrev());
        document.getElementById('sideNext')?.addEventListener('click', () => this.pageFlip?.flipNext());

        // Üst Bar Butonları
        document.getElementById('btnSound')?.addEventListener('click', () => this.toggleSound());
        document.getElementById('btnTheme')?.addEventListener('click', () => this.cycleTheme());
        document.getElementById('btnFullscreen')?.addEventListener('click', () => this.toggleFullscreen());
        document.getElementById('btnBookmark')?.addEventListener('click', () => this.toggleBookmark());
        document.getElementById('bookmarkRibbon')?.addEventListener('click', () => this.toggleBookmark());
        document.getElementById('btnTOC')?.addEventListener('click', () => this.toggleDrawer(true));
        document.getElementById('drawerClose')?.addEventListener('click', () => this.toggleDrawer(false));
        document.getElementById('drawerBackdrop')?.addEventListener('click', (e) => {
            if (e.target.id === 'drawerBackdrop') this.toggleDrawer(false);
        });

        // İlerleme Çubuğuna Tıklama
        document.getElementById('progressBar')?.addEventListener('click', (e) => {
            const rect = e.currentTarget.getBoundingClientRect();
            const clickX = e.clientX - rect.left;
            const pct = clickX / rect.width;
            const targetPage = Math.round(pct * (this.totalPages - 1));
            this.goToPage(targetPage);
        });

        // Arama Girişi
        document.getElementById('drawerSearch')?.addEventListener('input', (e) => {
            this.filterDrawerTOC(e.target.value.toLowerCase());
        });

        // Lightbox Kapatma
        document.getElementById('lightboxClose')?.addEventListener('click', () => this.closeLightbox());
        document.getElementById('lightboxModal')?.addEventListener('click', (e) => {
            if (e.target.id === 'lightboxModal') this.closeLightbox();
        });
    }

    setupKeyboard() {
        document.addEventListener('keydown', (e) => {
            if (e.key === 'ArrowRight' || e.key === 'PageDown' || e.key === ' ') {
                this.pageFlip?.flipNext();
            } else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {
                this.pageFlip?.flipPrev();
            } else if (e.key === 'Home') {
                this.pageFlip?.turnToPage(0);
            } else if (e.key === 'End') {
                this.pageFlip?.turnToPage(this.totalPages - 1);
            } else if (e.key === 'Escape') {
                this.closeLightbox();
                this.toggleDrawer(false);
            }
        });
    }

    goToPage(index) {
        if (this.pageFlip && index >= 0 && index < this.totalPages) {
            this.pageFlip.turnToPage(index);
            this.toggleDrawer(false);
        }
    }

    toggleSound() {
        if (window.bookSound) {
            const state = window.bookSound.toggle();
            this.updateSoundIcon(state);
        }
    }

    updateSoundIcon(state) {
        const isEnabled = state !== undefined ? state : (localStorage.getItem('ekitap_sound') !== 'false');
        const btn = document.getElementById('btnSound');
        if (btn) {
            btn.classList.toggle('active', isEnabled);
            btn.title = isEnabled ? 'Sesi Kapat' : 'Sesi Aç';
        }
    }

    cycleTheme() {
        const themes = ['cream', 'white', 'dark'];
        const nextIdx = (themes.indexOf(this.currentTheme) + 1) % themes.length;
        this.applyTheme(themes[nextIdx]);
    }

    applyTheme(theme) {
        this.currentTheme = theme;
        localStorage.setItem('ekitap_theme', theme);
        document.body.className = `theme-${theme}`;
        
        const btn = document.getElementById('btnTheme');
        if (btn) {
            btn.title = `Tema: ${theme.toUpperCase()}`;
        }
    }

    toggleBookmark() {
        if (this.savedBookmark === this.currentPage) {
            // Ayracı kaldır
            this.savedBookmark = -1;
            localStorage.removeItem('ekitap_bookmark');
        } else {
            // Ayracı bu sayfaya koy
            this.savedBookmark = this.currentPage;
            localStorage.setItem('ekitap_bookmark', this.currentPage);
        }
        this.updateBookmarkRibbonState();
    }

    updateBookmarkRibbonState() {
        const ribbon = document.getElementById('bookmarkRibbon');
        const btn = document.getElementById('btnBookmark');
        const isSaved = this.savedBookmark === this.currentPage && this.currentPage > 0;

        if (ribbon) ribbon.classList.toggle('saved', isSaved);
        if (btn) btn.classList.toggle('active', isSaved);
    }

    toggleFullscreen() {
        if (!document.fullscreenElement) {
            document.documentElement.requestFullscreen().catch(() => {});
        } else {
            document.exitFullscreen().catch(() => {});
        }
    }

    toggleDrawer(open) {
        const drawer = document.getElementById('drawerBackdrop');
        if (drawer) {
            drawer.classList.toggle('open', open);
            if (open) {
                document.getElementById('drawerSearch')?.focus();
            }
        }
    }

    renderDrawerTOC() {
        const container = document.getElementById('drawerList');
        if (!container || !window.BOOK_PAGES) return;

        container.innerHTML = '';
        window.BOOK_PAGES.forEach((p, idx) => {
            if (p.type === 'cover-front' || p.type === 'cover-back' || p.type === 'inner-title') return;
            
            const item = document.createElement('div');
            item.className = 'drawer-item';
            item.dataset.page = idx;
            item.innerHTML = `
                <span class="drawer-title">${p.header || 'Sayfa ' + idx}</span>
                <span class="drawer-page-num">${idx}</span>
            `;
            item.addEventListener('click', () => this.goToPage(idx));
            container.appendChild(item);
        });
    }

    updateActiveDrawerItem(pageIndex) {
        document.querySelectorAll('.drawer-item').forEach(el => {
            el.classList.toggle('active', parseInt(el.dataset.page, 10) === pageIndex);
        });
    }

    filterDrawerTOC(query) {
        document.querySelectorAll('.drawer-item').forEach(el => {
            const text = el.querySelector('.drawer-title')?.innerText.toLowerCase() || '';
            el.style.display = text.includes(query) ? 'flex' : 'none';
        });
    }

    setupInteractiveElements() {
        // Görseller ve interaktif kartlara tıklanırken sayfanın dönmesini kesinlikle engelle
        const interactives = document.querySelectorAll('.zoomable, .figure-card, .qr-video-box, .toc-list li, .callout-tactical');
        interactives.forEach(el => {
            ['click', 'mousedown', 'pointerdown', 'mouseup'].forEach(evt => {
                el.addEventListener(evt, (e) => {
                    e.stopPropagation();
                });
            });
            el.addEventListener('touchstart', (e) => {
                e.stopPropagation();
            }, { passive: true });
        });

        // Tüm zoomable görsellere tıklandığında güvenli lightbox aç
        document.querySelectorAll('.zoomable').forEach(img => {
            img.addEventListener('click', (e) => {
                e.stopPropagation();
                e.preventDefault();
                this.openLightbox(img.src, e);
            });
        });
    }

    openLightbox(src, event) {
        if (event) {
            if (typeof event.stopPropagation === 'function') event.stopPropagation();
            if (typeof event.preventDefault === 'function') event.preventDefault();
        }
        const modal = document.getElementById('lightboxModal');
        const img = document.getElementById('lightboxImage');
        if (modal && img) {
            img.src = src;
            modal.classList.add('open');
        }
    }

    closeLightbox() {
        const modal = document.getElementById('lightboxModal');
        if (modal) {
            modal.classList.remove('open');
        }
    }
}

window.reader = new EKitapReader();
