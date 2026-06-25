# Multi-Language Script Adaptation Notes

> **Purpose**: Guidelines for adapting the English qualification chatbot scripts into Spanish, French, Mandarin, Hindi, and Arabic
> **Target Scripts**: B2B (Script A), Real Estate (Script B), Financial/Legal (Script C)

---

## General Localization Guidelines

### Cultural Adaptation Principles

| Principle | Description |
|---|---|
| **Localize, don't translate** | Adapt idioms, examples, and references to the target culture |
| **Formality levels** | Spanish/French → formal "you" (usted/vous) for B2B; informal for real estate |
| **Date & number formats** | Use local conventions (dd/mm/yyyy, comma/decimal separators) |
| **Currency** | Localize budget questions to relevant currencies |
| **Legal compliance** | Each country has its own data privacy and lead generation laws |

### Structure to Maintain Across Languages

All scripts share this identical flow structure:

```
Phase 1: Greeting & Intent → Phase 2: Info Collection → Phase 3: Needs Assessment
→ Phase 4: Qualification Deep-Dive → Phase 5: Summary & Handoff → Scoring
```

---

## Spanish (Español) — Adaptation Notes

### Key Settings

| Parameter | Value |
|---|---|
| **Formal/Informal** | Use "usted" (formal) for financial/legal; "tú" for real estate |
| **Common Names** | José, María, Carlos, Ana, Juan, Laura, Miguel |
| **Currency** | MXN (🇲🇽), EUR (🇪🇸), USD (🇺🇸), COP (🇨🇴), ARS (🇦🇷) — detect by domain/IP |
| **Greeting Style** | "¡Hola! Bienvenido/a" — warm, friendly, slightly formal in B2B |
| **Budget Ranges** | Adjust to local purchasing power (e.g., Mexico: 50K-500K MXN for B2B) |

### Cultural Nuances

- **Family first**: Real estate scripts should mention "para su familia" (for your family)
- **Trust signals**: Emphasize "años de experiencia" (years of experience) and "clientes satisfechos" (satisfied clients)
- **Pricing**: Avoid aggressive pricing questions early — build rapport first
- **Phone preference**: Spanish-speaking leads often prefer phone calls over email
- **Time zones**: Be aware of siesta hours in some countries (1–4 PM)

### Specific Script Adjustments

```
Script A (B2B): Add option "Soy dueño de un negocio pequeño" (I own a small business)
Script B (Real Estate): Mention "crédito hipotecario" (mortgage) early
Script C (Financial): Use "asesor financiero" not "agente" (agent has different connotation)
```

---

## French (Français) — Adaptation Notes

### Key Settings

| Parameter | Value |
|---|---|
| **Formal/Informal** | Always "vous" (formal) in all contexts |
| **Common Names** | Jean, Marie, Pierre, Sophie, Thomas, Camille |
| **Currency** | EUR (💶), CAD (🇨🇦), CHF (🇨🇭), XAF/XOF |
| **Greeting Style** | "Bonjour et bienvenue" — formal, elegant |
| **Budget Ranges** | Use EUR amounts; adjust for Canadian market (CAD) |

### Cultural Nuances

- **Formality is key**: French B2B communication demands high formality — avoid all slang
- **Legal phrasing**: French law (RGPD/GDPR) requires explicit consent checkboxes
- **Long responses**: French users tend to give more detailed free-text responses
- **Lunch hours**: Avoid contacting leads 12:30–14:30
- **Summer**: August is vacation month — follow-up cadence should adjust

### Specific Script Adjustments

```
Script A (B2B): Add "PME" (small business) and "grande entreprise" as company size options
Script B (Real Estate): Include "diagnostic de performance énergétique" (energy rating) as priority
Script C (Financial): Use "notaire" for estate planning — distinguishes from "avocat"
```

---

## Mandarin (中文) — Adaptation Notes

### Key Settings

| Parameter | Value |
|---|---|
| **Formal/Informal** | Use 您 (nín, formal) for all business contexts |
| **Common Names** | Wang, Li, Zhang, Liu, Chen, Yang, Huang |
| **Currency** | CNY (¥), SGD, TWD (NT$) |
| **Greeting Style** | "您好，欢迎！" — polite, efficiency-focused |
| **Budget Ranges** | Adjust for Chinese market (e.g., 10K-500K CNY for B2B) |

### Cultural Nuances

- **Face (面子)**: Never directly say a lead's budget is "too low" — use "让我们看看什么方案适合您" (let's see what plan fits you)
- **Guanxi (关系)**: Building relationship matters — add an extra rapport-building turn
- **WeChat**: Integrate WeChat as a channel option for lead capture
- **Authority**: Decision-making is often hierarchical — "我需要和领导讨论" (I need to discuss with leadership) is common
- **Numbers**: Avoid 4 (tetraphobia), favor 8 (auspicious)

### Specific Script Adjustments

```
Script A (B2B): Add "国企" (state-owned enterprise) and "外企" (foreign company) as company types
Script B (Real Estate): Include "学区房" (school district property) as a key search filter
Script C (Financial): Emphasize "资产保值" (wealth preservation) over "增长" (growth)
```

---

## Hindi (हिन्दी) — Adaptation Notes

### Key Settings

| Parameter | Value |
|---|---|
| **Formal/Informal** | Use आप (aap, formal) in all business contexts |
| **Common Names** | Sharma, Verma, Patel, Singh, Gupta, Kumar, Devi |
| **Currency** | INR (₹) |
| **Greeting Style** | "नमस्ते! आपका स्वागत है" — respectful, warm |
| **Budget Ranges** | Adjust for Indian market (₹50K-₹50L for B2B) |

### Cultural Nuances

- **Family involvement**: Extended family often involved in major decisions — ask "और किसको शामिल करना चाहिए?" (who else should be included?)
- **English mix**: Hindi speakers frequently code-switch with English — allow bilingual responses
- **WhatsApp**: Primary business communication channel — integrate WhatsApp as lead capture channel
- **Respect titles**: Use "जी" (ji) suffix after names in conversation
- **Festivals**: Avoid key holidays (Diwali, Holi) for follow-up calls

### Specific Script Adjustments

```
Script A (B2B): Add "परिवार के स्वामित्व वाला व्यवसाय" (family-owned business) option
Script B (Real Estate): Include "फ्लैट" (flat/apartment) as primary property type
Script C (Financial): Mention "PPF" and "ELSS" as common Indian investment products
```

---

## Arabic (العربية) — Adaptation Notes

### Key Settings

| Parameter | Value |
|---|---|
| **Formal/Informal** | Use أنتم (antum, formal plural) for respect |
| **Common Names** | Ahmed, Mohammed, Ali, Fatima, Hassan, Omar, Noor |
| **Currency** | AED (🇦🇪), SAR (🇸🇦), EGP (🇪🇬), QAR (🇶🇦), KWD (🇰🇼) |
| **Greeting Style** | "مرحباً بكم! أهلاً وسهلاً" — warm, generous greeting |
| **Budget Ranges** | Adjust for Gulf states (higher) vs. Egypt/Levant (lower) |

### Cultural Nuances

- **Relationship first**: Extended greeting rituals expected before business — add 2–3 icebreaker exchanges
- **Right-to-left (RTL)**: The interface and script must support RTL rendering
- **Gender sensitivity**: Use masculine default unless lead's gender is known
- **Friday/Saturday**: Weekend in most Arab countries — adjust follow-up timing
- **Ramadan**: Business hours shift dramatically — messages sent after Iftar (sunset) get best response
- **Trust**: Family and personal connections matter more than corporate credentials

### Specific Script Adjustments

```
Script A (B2B): Add "مؤسسة فردية" (sole proprietorship) and "شركة عائلية" (family company)
Script B (Real Estate): Include "فيلا" (villa) and "شقة" (apartment) as key property types
Script C (Financial): Use "تخطيط مالي إسلامي" (Islamic financial planning) as a service option
```

---

## Technical Implementation Notes

### Encoding & Character Support

| Language | Unicode Range | Notes |
|---|---|---|
| Spanish | U+0000–U+00FF (Latin-1 Supplement) | Standard ASCII + accents (é, í, ó, ú, ü, ñ, ¿, ¡) |
| French | U+0000–U+00FF | Additional characters: œ, æ, « », — |
| Mandarin | U+4E00–U+9FFF (CJK Unified) | Requires full CJK font support |
| Hindi | U+0900–U+097F (Devanagari) | Requires Devanagari font support; complex text shaping |
| Arabic | U+0600–U+06FF (Arabic) | RTL support required; contextual letterforms |

### Fallback Strategy

```
If a user's language preference is unknown:
1. Detect browser/settings locale
2. Fallback to English if language not yet supported
3. Display: "Select your language / 选择语言 / Sélectionnez votre langue / हिन्दी / العربية"
```

### Response Time Expectations by Market

| Language | Expected Response Window | Best Send Time |
|---|---|---|
| Spanish | 24 hours | 9 AM–12 PM (local) |
| French | 24–48 hours | 10 AM–12 PM, 2–5 PM |
| Mandarin | 4–12 hours | 9 AM–12 PM, 7–9 PM |
| Hindi | 2–8 hours | 10 AM–1 PM, 4–7 PM |
| Arabic | 4–12 hours | 8 PM–12 AM (after Iftar in Ramadan) |