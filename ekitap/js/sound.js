/**
 * Web Audio API ile Gerçekçi Sayfa Çevirme Sesi Sentezleyici
 * Dış ses dosyası indirmeye gerek kalmadan tarayıcı içinde saf fiziksel ses üretir.
 */

class BookAudioSynthesizer {
    constructor() {
        this.ctx = null;
        this.enabled = localStorage.getItem('ekitap_sound') !== 'false';
    }

    init() {
        if (!this.ctx) {
            const AudioCtx = window.AudioContext || window.webkitAudioContext;
            if (AudioCtx) {
                this.ctx = new AudioCtx();
            }
        }
        if (this.ctx && this.ctx.state === 'suspended') {
            this.ctx.resume();
        }
    }

    toggle() {
        this.enabled = !this.enabled;
        localStorage.setItem('ekitap_sound', this.enabled);
        return this.enabled;
    }

    playPageFlip() {
        if (!this.enabled) return;
        this.init();
        if (!this.ctx) return;

        const now = this.ctx.currentTime;
        const duration = 0.22;

        // 1. Sayfa Hışırtısı (Filtrelenmiş Beyaz/Pembe Gürültü)
        const bufferSize = this.ctx.sampleRate * duration;
        const buffer = this.ctx.createBuffer(1, bufferSize, this.ctx.sampleRate);
        const data = buffer.getChannelData(0);
        let lastOut = 0.0;
        for (let i = 0; i < bufferSize; i++) {
            const white = Math.random() * 2 - 1;
            // Pembe gürültü yumuşatması
            lastOut = (lastOut * 0.7) + (white * 0.3);
            data[i] = lastOut;
        }

        const noise = this.ctx.createBufferSource();
        noise.buffer = buffer;

        // Dinamik Frekans Kaydırması (Sayfanın kıvrılıp açılması)
        const filter = this.ctx.createBiquadFilter();
        filter.type = 'bandpass';
        filter.frequency.setValueAtTime(1400, now);
        filter.frequency.exponentialRampToValueAtTime(320, now + duration);
        filter.Q.setValueAtTime(2.2, now);

        // Ses Seviyesi Zarfı (Envelope)
        const gainNode = this.ctx.createGain();
        gainNode.gain.setValueAtTime(0.001, now);
        gainNode.gain.linearRampToValueAtTime(0.28, now + 0.03);
        gainNode.gain.exponentialRampToValueAtTime(0.001, now + duration);

        noise.connect(filter);
        filter.connect(gainNode);
        gainNode.connect(this.ctx.destination);

        noise.start(now);
        noise.stop(now + duration);

        // 2. Sayfanın Yerine Oturma Hafif Tok Sesi (Düşük Frekans)
        const thudOsc = this.ctx.createOscillator();
        const thudGain = this.ctx.createGain();
        thudOsc.type = 'sine';
        thudOsc.frequency.setValueAtTime(120, now + 0.08);
        thudOsc.frequency.exponentialRampToValueAtTime(45, now + 0.2);

        thudGain.gain.setValueAtTime(0.001, now + 0.08);
        thudGain.gain.linearRampToValueAtTime(0.08, now + 0.11);
        thudGain.gain.exponentialRampToValueAtTime(0.001, now + 0.22);

        thudOsc.connect(thudGain);
        thudGain.connect(this.ctx.destination);

        thudOsc.start(now + 0.08);
        thudOsc.stop(now + 0.22);
    }
}

window.bookSound = new BookAudioSynthesizer();
