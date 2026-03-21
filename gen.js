const crypto = require('crypto');

async function hashString(str) {
    const encoder = new TextEncoder();
    const data = encoder.encode(str);
    const hashBuffer = await crypto.webcrypto.subtle.digest('SHA-256', data);
    const hashArray = Array.from(new Uint8Array(hashBuffer));
    return hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
}

async function deriveKey(password) {
    const enc = new TextEncoder();
    const passHash = await crypto.webcrypto.subtle.digest('SHA-256', enc.encode(password));
    return await crypto.webcrypto.subtle.importKey("raw", passHash, {name: "AES-GCM"}, false, ["encrypt", "decrypt"]);
}

async function encryptData(secretData, password) {
    const key = await deriveKey(password);
    const iv = crypto.webcrypto.getRandomValues(new Uint8Array(12));
    const enc = new TextEncoder();
    const encrypted = await crypto.webcrypto.subtle.encrypt({ name: "AES-GCM", iv: iv }, key, enc.encode(JSON.stringify(secretData)));

    const ivHex = Array.from(iv).map(b => b.toString(16).padStart(2, '0')).join('');
    const encHex = Array.from(new Uint8Array(encrypted)).map(b => b.toString(16).padStart(2, '0')).join('');
    return `${ivHex}.${encHex}`;
}

(async () => {
    const certId = "TA-2026-001";
    const hashedId = await hashString(certId);
    const payload = { name: "K**** T****", course: "Taktik Atış ve İleri Düzey Silah Kullanımı", date: "2026-03-24" };
    const encryptedPayload = await encryptData(payload, certId);
    console.log(`{\n  "${hashedId}": "${encryptedPayload}"\n}`);
})();
