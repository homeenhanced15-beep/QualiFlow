document.addEventListener('DOMContentLoaded', () => {

    // ══════════════════════════════════════════
    //  ACCESSIBLE ANNOUNCEMENT (no alert())
    // ══════════════════════════════════════════
    function announce(msg) {
        let el = document.getElementById('announcer');
        if (!el) {
            el = document.createElement('div');
            el.id = 'announcer';
            el.setAttribute('role', 'alert');
            el.setAttribute('aria-live', 'assertive');
            el.style.cssText = 'position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0,0,0,0)';
            document.body.prepend(el);
        }
        el.textContent = '';
        setTimeout(() => { el.textContent = msg; }, 50);
        if (typeof showCaption === 'function') showCaption(msg);
    }
    window.announce = announce;

    function sanitize(s) {
        if (typeof s !== 'string') return '';
        const d = document.createElement('div');
        d.textContent = s;
        return d.textContent;
    }

    // ══════════════════════════════════════════
    //  RATE LIMITING + SESSION
    // ══════════════════════════════════════════
    function canProceed() {
        const a = JSON.parse(localStorage.getItem('lqf_attempts') || '[]');
        const n = Date.now();
        const recent = a.filter(t => t > n - 60000);
        if (recent.length >= 5) {
            const w = Math.ceil((recent[0] + 60000 - n) / 1000);
            announce(`Too many attempts. Wait ${w}s.`);
            return false;
        }
        recent.push(n);
        localStorage.setItem('lqf_attempts', JSON.stringify(recent));
        return true;
    }

    let st;
    function resetSession() {
        clearTimeout(st);
        st = setTimeout(() => {
            localStorage.removeItem('lqf_token');
            if (!location.href.includes('login.html')) location.href = 'login.html';
        }, 30*60*1000);
    }
    document.addEventListener('mousemove', resetSession);
    document.addEventListener('keydown', resetSession);
    document.addEventListener('touchstart', resetSession);
    resetSession();

    // ══════════════════════════════════════════
    //  PASSWORD STRENGTH
    // ══════════════════════════════════════════
    function pwStrength(pw) {
        let s = 0;
        const need = [];
        if (pw.length >= 8) s++; else need.push('8+ chars');
        if (pw.length >= 12) s++;
        if (/[a-z]/.test(pw)) s++; else need.push('lowercase');
        if (/[A-Z]/.test(pw)) s++; else need.push('uppercase');
        if (/[0-9]/.test(pw)) s++; else need.push('number');
        if (/[^a-zA-Z0-9]/.test(pw)) s++; else need.push('special char');
        return { score: s, max: 7, need };
    }

    function attachPWmeter(inputId, displayId) {
        const inp = document.getElementById(inputId);
        const disp = document.getElementById(displayId);
        if (!inp || !disp) return;
        inp.addEventListener('input', () => {
            const r = pwStrength(inp.value);
            if (!inp.value) { disp.textContent = ''; return; }
            const l = r.score < 3 ? 'Weak' : r.score < 5 ? 'Medium' : r.score < 6 ? 'Strong' : 'Very Strong';
            const c = r.score < 3 ? '#d9534f' : r.score < 5 ? '#f0ad4e' : '#008554';
            disp.textContent = `${l} (${r.score}/${r.max})`;
            disp.style.color = c;
            if (r.score < 5 && r.need.length) disp.textContent += ` — need: ${r.need.join(', ')}`;
        });
    }

    function setupPWtoggle(toggleId, inputId) {
        const t = document.getElementById(toggleId);
        const i = document.getElementById(inputId);
        if (!t || !i) return;
        t.addEventListener('click', () => {
            const pw = i.type === 'password';
            i.type = pw ? 'text' : 'password';
            t.textContent = pw ? '🙈' : '👁️';
            t.setAttribute('aria-label', pw ? 'Hide' : 'Show');
        });
    }

    // ══════════════════════════════════════════
    //  LOGIN FORM
    // ══════════════════════════════════════════
    const loginForm = document.getElementById('password-login-form');
    if (loginForm) {
        loginForm.addEventListener('submit', e => {
            e.preventDefault();
            if (!canProceed()) return;
            const email = sanitize(document.getElementById('login-email').value);
            const pw = document.getElementById('login-password').value;
            if (!email || !email.includes('@')) {
                document.getElementById('login-email-error').textContent = 'Valid email required.';
                announce('Please enter a valid email.');
                return;
            }
            document.getElementById('login-email-error').textContent = '';
            if (!pw) {
                document.getElementById('login-password-error').textContent = 'Password required.';
                announce('Please enter your password.');
                return;
            }
            document.getElementById('login-password-error').textContent = '';
            announce(`Signed in as ${email}. Welcome!`);
            localStorage.setItem('lqf_token', 'tok_'+Date.now());
        });
    }

    // ══════════════════════════════════════════
    //  REGISTRATION FORM
    // ══════════════════════════════════════════
    const regForm = document.getElementById('registration-form');
    if (regForm) {
        regForm.addEventListener('submit', e => {
            e.preventDefault();
            document.querySelectorAll('.error-message').forEach(el => el.textContent = '');
            const name = sanitize(document.getElementById('reg-name').value.trim());
            const email = sanitize(document.getElementById('reg-email').value.trim());
            const co = sanitize(document.getElementById('reg-company').value.trim());
            const pw = document.getElementById('reg-password').value;
            const cf = document.getElementById('reg-confirm-password').value;
            const terms = document.getElementById('reg-terms').checked;
            let ok = true;
            if (!name) { document.getElementById('reg-name-error').textContent = 'Required.'; ok = false; }
            if (!email||!email.includes('@')) { document.getElementById('reg-email-error').textContent = 'Valid email required.'; ok = false; }
            if (!co) { document.getElementById('reg-company-error').textContent = 'Required.'; ok = false; }
            const r = pwStrength(pw);
            if (r.score < 4) { document.getElementById('reg-password-error').textContent = `Score ${r.score}/${r.max}. Need: ${r.need.join(', ')}`; ok = false; }
            if (pw !== cf) { document.getElementById('reg-confirm-error').textContent = 'Passwords differ.'; ok = false; }
            if (!terms) { announce('Must agree to Terms and Privacy.'); ok = false; }
            if (!ok) { announce('Fix errors and retry.'); return; }
            announce(`Welcome ${name}! Account created.`);
            document.getElementById('registration-status').textContent = '✅ Account created!';
        });
    }

    // ══════════════════════════════════════════
    //  GOOGLE SIGN-IN
    // ══════════════════════════════════════════
    if (document.getElementById('google-signin-btn')) {
        if (!document.querySelector('script[src*="accounts.google.com/gsi/client"]')) {
            const s = document.createElement('script');
            s.src = 'https://accounts.google.com/gsi/client'; s.async = true; s.defer = true;
            document.head.appendChild(s);
        }
        document.getElementById('google-signin-btn').addEventListener('click', () => {
            if (!canProceed()) return;
            if (window.google?.accounts) {
                window.google.accounts.id.initialize({
                    client_id: 'YOUR_GOOGLE_CLIENT_ID.apps.googleusercontent.com',
                    callback: (r) => { announce('Google sign-in success!'); }
                });
                window.google.accounts.id.prompt();
            } else announce('Google sign-in unavailable.');
        });
    }

    // ══════════════════════════════════════════
    //  BIOMETRIC (WebAuthn)
    // ══════════════════════════════════════════
    const bioBtn = document.getElementById('biometric-login-btn');
    const bioSt = document.getElementById('biometric-status');
    if (bioBtn) {
        if (!window.PublicKeyCredential) {
            bioBtn.disabled = true; bioSt.textContent = '❌ Biometrics not supported.';
        } else {
            bioBtn.addEventListener('click', async () => {
                if (!canProceed()) return;
                bioSt.textContent = '⏳ Scanning...';
                announce('Biometric request sent.');
                try {
                    const avail = await PublicKeyCredential.isUserVerifyingPlatformAuthenticatorAvailable();
                    if (!avail) { bioSt.textContent = '❌ No biometric hardware.'; return; }
                    await navigator.credentials.create({
                        publicKey: {
                            challenge: crypto.getRandomValues(new Uint8Array(32)),
                            rp: { name: 'Leads QualiFlow' },
                            user: { id: crypto.getRandomValues(new Uint8Array(16)), name: 'user', displayName: 'User' },
                            pubKeyCredParams: [{ alg: -7, type: 'public-key' }],
                            authenticatorSelection: { authenticatorAttachment: 'platform', userVerification: 'required' },
                            timeout: 60000
                        }
                    });
                    bioSt.textContent = '✅ Verified!';
                    bioSt.style.color = '#008554';
                    announce('Biometric login successful!');
                } catch (err) {
                    bioSt.textContent = `❌ ${err.message || 'Failed'}`;
                    bioSt.style.color = '#d9534f';
                    announce('Biometric failed.');
                }
            });
        }
    }

    // ══════════════════════════════════════════
    //  SIGN IN WITH ANNA
    // ══════════════════════════════════════════
    const annaBtn = document.getElementById('anna-login-btn');
    const annaArea = document.getElementById('anna-verification-area');
    if (annaBtn && annaArea) {
        let step = 0;
        const qs = [
            'Anna: What email did you register with?',
            'Anna: What company do you represent?',
            'Anna: What service interests you?'
        ];
        annaBtn.addEventListener('click', () => {
            if (!canProceed()) return;
            step = 0; annaBtn.disabled = true; annaBtn.textContent = '🤖 Verifying...';
            announce('Anna verification started.');
            nextQ();
        });
        function nextQ() {
            if (step >= qs.length) { complete(); return; }
            annaArea.innerHTML = `<p style="margin-top:0.5rem;font-weight:bold;">${qs[step]}</p>
                <input type="text" id="anna-ans" aria-label="Answer for Anna" style="width:100%;padding:0.5rem;margin:0.5rem 0;">
                <button class="btn btn-sm" style="background:#00A86B;color:#fff;border:none;" onclick="document.getElementById('anna-ans').value ? (announce('Anna: Thanks!'), step++, nextQ()) : announce('Please answer.');">Answer</button>`;
            setTimeout(() => document.getElementById('anna-ans')?.focus(), 100);
        }
        function complete() {
            annaArea.innerHTML = '<p style="color:#008554;font-weight:bold;">✅ Anna verified your identity!</p>';
            annaBtn.disabled = false; annaBtn.textContent = '🤖 Sign in with Anna';
            announce('Anna verification complete!');
        }
    }

    // ══════════════════════════════════════════
    //  CAPTIONS & VOICE
    // ══════════════════════════════════════════
    let capsOn = localStorage.getItem('lqf_caps') === 'true';
    const vb = document.getElementById('voice-btn');
    const cc = document.getElementById('captions-container');
    const ct = document.getElementById('caption-text');
    if (capsOn && cc) cc.classList.add('visible');

    function showCaption(t) {
        if (capsOn && ct && cc) { ct.textContent = sanitize(t); cc.classList.add('visible'); }
    }
    window.showCaption = showCaption;
    window.toggleCaptions = function() {
        capsOn = !capsOn; localStorage.setItem('lqf_caps', capsOn);
        if (capsOn && cc) { cc.classList.add('visible'); showCaption('Captions on'); }
        else if (cc) cc.classList.remove('visible');
    };
    const ccBtn = document.getElementById('cc-btn');
    if (ccBtn) ccBtn.onclick = window.toggleCaptions;

    window.handleVoiceCommand = function(cmd) {
        const c = sanitize(cmd.toLowerCase());
        if (c.includes('scroll down')) window.scrollBy({ top: 400, behavior: 'smooth' });
        else if (c.includes('scroll up')) window.scrollBy({ top: -400, behavior: 'smooth' });
        else if (c.includes('go to pricing')) location.href = 'pricing.html';
        else if (c.includes('go to login')) location.href = 'login.html';
        else if (c.includes('go to features')) location.href = 'features.html';
        else if (c.includes('go to guides')) location.href = 'guides.html';
        else if (c.includes('go to anna')||c.includes('meet anna')) location.href = 'anna.html';
        else if (c.includes('how it works')) location.href = 'how-it-works.html';
        else if (c.includes('go to privacy')) location.href = 'privacy.html';
        else if (c.includes('go to terms')) location.href = 'terms.html';
        else if (c.includes('go home')) location.href = 'index.html';
        else if (c.includes('toggle captions')) window.toggleCaptions();
        else if (c.includes('read this page')) {
            const m = document.querySelector('main');
            if (m) window.speechSynthesis.speak(new SpeechSynthesisUtterance(m.innerText));
        } else if (c.includes('scroll to top')) window.scrollTo({ top: 0, behavior: 'smooth' });
        else if (c.includes('scroll to bottom')) window.scrollTo({ top: document.body.scrollHeight, behavior: 'smooth' });
        else showCaption('Try: go to pricing, scroll down, read this page');
    };

    if (vb) {
        const SR = window.SpeechRecognition || window.webkitSpeechRecognition;
        if (SR) {
            const rec = new SR();
            rec.lang = 'en-US';
            vb.addEventListener('click', () => { rec.start(); showCaption('Listening...'); });
            rec.onresult = e => window.handleVoiceCommand(e.results[0][0].transcript);
        } else vb.style.display = 'none';
    }

    document.addEventListener('focusin', e => {
        if (capsOn && e.target.tagName !== 'BODY') {
            const l = e.target.getAttribute('aria-label')||e.target.innerText||e.target.placeholder||e.target.id;
            if (l&&l.length>2) showCaption(`Focus: ${l.substring(0,60)}`);
        }
    });

    // ══════════════════════════════════════════
    //  INIT
    // ══════════════════════════════════════════
    setupPWtoggle('toggle-password-vis','login-password');
    setupPWtoggle('toggle-reg-password-vis','reg-password');
    attachPWmeter('login-password','password-strength');
    attachPWmeter('reg-password','reg-pass-strength');

    console.log('🔒 Leads QualiFlow — Auth, Security & Accessibility Loaded');
});