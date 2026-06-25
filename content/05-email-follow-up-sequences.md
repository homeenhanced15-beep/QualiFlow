# Email Follow-Up Sequences for Leads QualiFlow

---

## Sequence 1: Cold Lead Nurturing (3-Email Sequence)

> **Trigger**: Lead scores 0–25 (or equivalent for industry) in qualification chatbot
> **Goal**: Warm the lead with value, build trust, re-engage within 30 days
> **Cadence**: Email 1 → Day 0 | Email 2 → Day 4 | Email 3 → Day 12

---

### Email 1: "You caught our attention" (Day 0)

**Subject**: Thanks for stopping by, {{first_name}} 👋

**Body**:

```
Hi {{first_name}},

Thanks for checking us out at {{company_name}}. We noticed you were
looking into our services — and we'd love to help when the time is right.

In the meantime, here's something you might find useful:

👉 [Link to relevant resource — e.g., "5 Signs It's Time to Switch 
   [Service Provider]" / industry guide / ROI calculator]

No pressure — just wanted to share this while it's on my mind.

If anything changes and you'd like to have a quick chat, just hit
reply. I'm here when you're ready.

Best,
{{sender_name}}
{{company_name}}
```

**Metrics**: Open rate target ≥ 40% | Click rate target ≥ 8%

---

### Email 2: "Quick question + more value" (Day 4)

**Subject**: {{first_name}}, we're still here if you need us

**Body**:

```
Hi {{first_name}},

Quick question: what's the #1 challenge you're facing right now with
[their area of interest — e.g., "lead generation" / "finding the
right property" / "financial planning"]?

We've put together a short guide that might help:

📘 [Title of guide relevant to their challenge]
👉 [Link]

Whether you're ready to start today or just getting your bearings,
we've got resources to help you make the right decision.

Talk soon,
{{sender_name}}
```

**Metrics**: Open rate target ≥ 35% | Reply rate target ≥ 5%

---

### Email 3: "Final thought — no hard feelings" (Day 12)

**Subject**: Wrapping this up — unless you have questions?

**Body**:

```
Hi {{first_name}},

I don't want to keep clogging your inbox if the timing isn't right.
This will be my last note unless I hear back from you.

Quick recap of what we offer:

✅ [Key benefit 1]
✅ [Key benefit 2]
✅ [Key benefit 3]

If any of that sounds useful — now or down the road — here's a link
to book a 15-minute chat whenever you're ready:
👉 [Calendar booking link]

If not, no hard feelings at all. You know where to find us.

All the best,
{{sender_name}}
{{company_name}}
```

**Metrics**: Open rate target ≥ 30% | Booking rate target ≥ 3%

---

## Sequence 2: Warm Lead Follow-Up (2-Email Sequence)

> **Trigger**: Lead scores 26–59 (or equivalent) — showed interest, needs a nudge
> **Goal**: Convert to a qualified meeting/call
> **Cadence**: Email 1 → Day 0 (immediate) | Email 2 → Day 2

---

### Email 1: "Thanks for the detail — let's take the next step" (Day 0)

**Subject**: Great talking with you, {{first_name}}! Next steps...

**Body**:

```
Hi {{first_name}},

Thanks so much for the time you spent chatting with us earlier.
You mentioned you were interested in [service/product], with a
timeline of {{timeline}}.

I took a look at what you shared, and I think we can definitely help.

Here's what I'd suggest as a next step:

📅 Let's hop on a 15-minute call to:
   • Confirm your needs
   • Walk through how we'd approach this
   • Answer any questions

Pick a time that works for you:
👉 [Calendar booking link]

Looking forward to connecting!

Best,
{{sender_name}}
{{company_name}}
```

**Metrics**: Open rate target ≥ 55% | Booking rate target ≥ 20%

---

### Email 2: "Still thinking it over? Here's a shortcut" (Day 2)

**Subject**: {{first_name}}, one more thing about {{company_name}}

**Body**:

```
Hi {{first_name}},

Just following up on my last email. I know you're busy — so let me
make this easy.

Here's exactly what a conversation with us looks like:

Step 1: 15-minute call to understand your situation
Step 2: We put together a tailored recommendation
Step 3: You decide if it's right for you (no obligation)

That's it. No sales pitch, no pressure.

Here's that calendar link again:
👉 [Calendar booking link]

Or if you'd rather, just reply with a time that works for you.

Talk soon,
{{sender_name}}
```

**Metrics**: Open rate target ≥ 50% | Booking rate target ≥ 15%

---

## Sequence 3: Hot Lead Instant Handoff (Sales Team Notification)

> **Trigger**: Lead scores ≥ 60+ (or equivalent) — high intent, immediate action needed
> **Goal**: Get the sales rep in front of the lead within 1 hour
> **Delivery**: Not an email to the lead — this is the internal alert to the sales team

---

### Internal Alert Email to Sales Team

**Subject**: 🚀 HOT LEAD: {{first_name}} {{last_name}} — {{company_name}} — Score: {{score}}

**Body**:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  🔥 HOT LEAD ALERT — ACT NOW
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

LEAD DETAILS
───────────────────────────────────────────
  Name:            {{first_name}} {{last_name}}
  Company:         {{company_name}}
  Role:            {{role}}
  Email:           {{email}}
  Phone:           {{phone}}
  Channel:         {{channel}} (at {{timestamp}})

QUALIFICATION SUMMARY
───────────────────────────────────────────
  Lead Score:      {{score}}/100 — "Hot Lead"
  Timeline:        {{timeline}}
  Budget:          {{budget}}
  Authority:       {{decision_role}}
  Pain Points:     {{pain_points_note}}

RECOMMENDED ACTION
───────────────────────────────────────────
  ⏱️ Contact within:  1 hour
  📞 Suggested:       Call first, then email
  🎯 Talking points:  {{key_talking_points}}

FULL TRANSCRIPT
───────────────────────────────────────────
  {{link_to_transcript}}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  This lead was generated by Leads QualiFlow.
  Time-to-first-contact is being tracked.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Distribution**: Email + Slack DM + push notification to assigned rep

---

### Optional: Lead Booking Confirmation Email (to lead)

> This gets sent to the hot lead confirming their submission and setting expectations

**Subject**: {{first_name}}, someone from {{company_name}} will be in touch shortly!

**Body**:

```
Hi {{first_name}},

Thanks for chatting with us! Your information has been received,
and one of our specialists is reviewing it right now.

Here's what to expect:

⏱️ Someone will reach out within 1 business day
📧 We'll use {{email}} to contact you
📞 If you included a phone number, they may call as well

In the meantime, if you have any urgent questions, feel free
to reply to this email.

Talk soon,
The {{company_name}} Team
```

---

## Email Automation Rules

### Sending Rules

| Lead Type | Sequence | Start Trigger | Max Emails |
|---|---|---|---|
| Cold (0–25) | Sequence 1 | 1 hour after chatbot ends | 3 |
| Warm (26–59) | Sequence 2 | 5 minutes after chatbot ends | 2 |
| Hot (60+) | Sequence 3 (internal) + booking confirmation | Instant | 1 (internal) + 1 (lead) |
| Enterprise (85+) | Sequence 3 + direct manual email from senior rep | Instant | 1 (internal) + personalized |

### Opt-Out & Compliance

- Every email must include: "Unsubscribe from these emails" link
- Unsubscribed leads → moved to suppressed list immediately
- CAN-SPAM compliance: valid physical mailing address in every email
- GDPR: separate consent required before sending Sequence 1 (cold nurture)
- CCPA: "Do Not Sell My Information" link in every email footer