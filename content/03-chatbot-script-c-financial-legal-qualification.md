# Script C: Financial & Legal Services Lead Qualification Chatbot

> **Purpose**: Qualify leads for financial advisors, wealth managers, law firms, accountants, and tax professionals
> **Channel**: Website embed, SMS, WhatsApp, secure portal
> **Lead Scoring Range**: 0–100 points
> **Qualified Threshold**: ≥ 55 points
> **Compliance Note**: Must include disclaimers — this chatbot does not provide financial or legal advice

---

## Conversation Flow

### Phase 1: Greeting & Service Selection

```
[BOT] ⚖️ Welcome to [Firm Name]. I'm here to help connect you with the right
       professional for your needs. How can we assist you today?

      [Financial Planning / Wealth Management]
      [Tax Preparation / Planning]
      [Estate Planning / Wills]
      [Business Formation / Contracts]
      [Real Estate Law / Closing]
      [Family Law / Divorce]
      [Insurance / Annuities]
      [Something Else]

[IF "Something Else"]
[BOT] Please tell us a bit more about what you need:
[USER] [Free text — NLP routing to appropriate service]

Scoring:
  High-value services (Estate Planning, Wealth Management, Business Formation) → +10 points
  Mid-value services (Tax, Real Estate Law) → +5 points
  Low-value/commodity → +3 points
```

### Phase 2: Contact & Identity Verification

```
[BOT] Let's start with some basic information.
      What's your full name?
[USER] [Enters name]

[BOT] Thanks, {name}. What's your email address?
[USER] [Enters email]

[BOT] And your phone number?
[USER] [Enters phone]

[BOT] Are you inquiring for yourself, or on behalf of:
      [Myself]  [My family]  [My business/organization]  [Someone else]

Scoring:
  Myself → +5 points
  Family → +5 points (multiple services needed)
  Business → +10 points (higher-value engagements)
  Someone else → +3 points (gatekeeper — needs qualifier)
```

### Phase 3: Needs Assessment & Complexity

```
[BOT] Thanks, {name}. Let's get a clearer picture of what you need.

      What best describes your current situation?

      [A] I have a specific issue I need resolved
      [B] I need ongoing advisory/planning services
      [C] I want a second opinion on my current plan
      [D] I'm just exploring what services you offer

Scoring:
  A → +15 points (Immediate need)
  B → +20 points (Long-term client potential)
  C → +10 points (Already engaged — comparison shopper)
  D → +0 points (Education/nurture)

[IF Financial Planning / Wealth Management]
[BOT] What area of financial planning are you most focused on?

      [A] Retirement planning
      [B] Investment management
      [C] Debt reduction / Financial wellness
      [D] College/Education savings
      [E] Tax optimization strategies
      [F] Insurance / Risk management
      [G] All of the above

[BOT] What's your approximate investable asset level?

      [A] Under $50,000
      [B] $50,000 – $250,000
      [C] $250,000 – $500,000
      [D] $500,000 – $1,000,000
      [E] $1,000,000 – $5,000,000
      [F] $5,000,000+
      [Prefer not to say]

Scoring:
  A → +3 points
  B → +8 points
  C → +15 points
  D → +20 points
  E → +25 points
  F → +30 points
  Prefer not to say → +5 points
```

### Phase 4: Urgency & Decision Authority

```
[BOT] When are you looking to get started?

      [A] Immediately — this week
      [B] Within 30 days
      [C] Within 90 days
      [D] This year — no specific deadline
      [E] Not sure yet

Scoring:
  A → +25 points
  B → +20 points
  C → +10 points
  D → +5 points
  E → +0 points

[BOT] Who will be involved in making the final decision?

      [A] Just me
      [B] Me and my spouse/partner
      [C] Me and my business partners
      [D] I'm gathering info for the decision-maker(s)
      [E] I need to check with someone else first

Scoring:
  A → +15 points (Sole decision-maker)
  B → +10 points (Joint decision — need both engaged)
  C → +10 points (Business decision — multiple stakeholders)
  D → +5 points (Information gatherer)
  E → +3 points (Needs buy-in)

[IF Legal Service]
[BOT] Is this matter time-sensitive or urgent? (e.g., court date, filing deadline, statute of limitations)

      [A] Yes — very urgent
      [B] Somewhat urgent
      [C] Not urgent — gathering information

Scoring:
  A → +20 points
  B → +10 points
  C → +0 points
```

### Phase 5: Budget & Engagement Scope

```
[BOT] Do you have a budget range in mind for this engagement?

      [A] Under $500
      [B] $500 – $2,000
      [C] $2,000 – $5,000
      [D] $5,000 – $15,000
      [E] $15,000+
      [F] I'm not sure / I'd like a consultation first

Scoring:
  A → +3 points
  B → +8 points
  C → +15 points
  D → +20 points
  E → +25 points
  F → +5 points

[BOT] Is there anything specific we should know about your situation?
      (Briefly describe your situation — this helps us prepare for our conversation)

[USER] [Free text — captured for lead summary]
```

### Phase 6: Lead Summary & Handoff

```
[BOT] Thank you, {name}! Here's a summary of what you shared:

      ⚖️ Service: {service_type}
      📋 Situation: {situation}
      ⏰ Timeline: {timeline}
      💰 Budget: {budget_range}
      👥 Decision Role: {decision_role}
      🔑 Details: {free_text_note}

      One of our specialists will review this and reach out to you
      at {email} or {phone} shortly.

[BOT] DISCLAIMER: This chat is for informational purposes only and
      does not constitute financial or legal advice. No attorney-client
      or advisor-client relationship is formed by this conversation.
      Our team will review your information and contact you to discuss
      next steps.

[BOT] Any final questions before I hand you off?
[USER] [Optional free text]

[BOT] You'll hear from us soon. Have a great day! ⚖️👋
```

---

## Scoring Summary

| Category | Max Points |
|---|---|
| Service Selection (value tier) | 10 |
| Contact Role (self/business/other) | 10 |
| Situation / Need Type | 20 |
| Financial Assets (wealth management) | 30 |
| Timeline / Urgency | 25 |
| Decision Authority | 15 |
| Legal Urgency (if applicable) | 20 |
| Budget Range | 25 |
| **Total Possible** | **130 (financial) / 120 (legal)** |

### Score Tiers

| Score Range | Classification | Action |
|---|---|---|
| 0–25 | Cold Lead | Add to education/nurture newsletter sequence |
| 26–54 | Warm Lead | Assign to junior advisor/associate for initial call within 24 hrs |
| 55–79 | Hot Lead | Assign to senior advisor/partner — contact within 4 hours |
| 80+ | Premium Lead | Immediate partner assignment + call within 1 hour |

---

## Lead Summary Card (for CRM/Slack Handoff)

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ⚖️ NEW LEAD — FINANCIAL / LEGAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Name:          {{name}}
  Email:         {{email}}
  Phone:         {{phone}}
  Service:       {{service_type}}
  Inquiry For:   {{self/family/business}}
  ───────────────────────────────
  Situation:     {{situation}}
  Assets:        {{asset_level}}
  Timeline:      {{timeline}}
  Budget:        {{budget_range}}
  Decision Role: {{decision_role}}
  ───────────────────────────────
  Lead Score:    {{score}}/130 — {{classification}}
  Timestamp:     {{datetime}}
  Channel:       {{channel}}
  ───────────────────────────────
  Chat Log:       {{link_to_full_transcript}}
  ⚠️ DISCLAIMER: This lead was informed this chat is not
     legal/financial advice and no relationship was formed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Qualification Criteria Notes

- **Minimum viable lead**: Name + email + phone + service selection + situation description
- **Compliance**: Must display disclaimer BEFORE information collection begins and at handoff
- **Regulated industries**: For financial services (SEC/FINRA), legal (state bar rules), tax (IRS Circular 230)
- **Sensitive data**: Never ask for SSN, account numbers, or case-specific legal details in chat
- **Conflict check**: For law firms — flag if lead mentions an existing client name as an opposing party
- **Duplicate detection**: Match by email + phone — financial/legal leads often reach out through multiple channels