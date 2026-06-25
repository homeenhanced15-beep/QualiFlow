# Script A: General B2B Lead Qualification Chatbot

> **Purpose**: Qualify general B2B leads across industries (SaaS, consulting, professional services, manufacturing, etc.)
> **Channel**: Website embed, SMS, WhatsApp, Facebook Messenger
> **Lead Scoring Range**: 0–100 points
> **Qualified Threshold**: ≥ 60 points

---

## Conversation Flow

### Phase 1: Greeting & Intent Capture

```
[BOT] 👋 Hi! Welcome to [Company Name]. I'm here to help connect you with the right solutions.
       Mind if I ask a few quick questions to see how we can best assist you?

       [Yes, let's go!]  [I'm just browsing]  [I need help now]

[IF "I'm just browsing"]
[BOT] No problem at all! Feel free to look around. If you ever need anything,
      just click the chat bubble. Is there anything specific you're curious about?
      [Yes, I have a question]  [No, thanks — just looking]

[IF "No, thanks"]
[BOT] Sounds good! I'll be here if you change your mind. Have a great day! 👋
[END]
```

### Phase 2: Basic Information

```
[BOT] Great! Let's start simple — what's your name?
[USER] [Enters name]

[BOT] Thanks, {name}! And what's the best email address to reach you at?
[USER] [Enters email]

[BOT] Perfect! And what's the name of your company or organization?
[USER] [Enters company name]

[BOT] Got it — {company}. What's your role there?
      (e.g., Founder, Sales Director, Marketing Manager, etc.)
[USER] [Enters role/title]
```

### Phase 3: Needs Assessment (Scoring Begins)

```
[BOT] Thanks, {name}! Now let's figure out what you need.
      What best describes why you're reaching out today?

      [A] Looking to buy a solution/service
      [B] Researching options for future purchase
      [C] Need pricing information
      [D] Have a technical question
      [E] Something else

Scoring:
  A → +20 points (High intent)
  B → +10 points (Medium intent)
  C → +5 points (Low intent, but signal)
  D → +5 points (Existing customer or technical evaluation)
  E → +0 points (Needs clarification — route to general inquiry)

[IF "E" or needs clarification]
[BOT] Can you tell me a bit more about what you're looking for?
[USER] [Free text]
[Then re-route to appropriate option based on NLP analysis]
```

### Phase 4: Qualification Deep Dive

```
[BOT] Great, thanks! How soon are you looking to make a decision or purchase?

      [A] Immediately — within this week
      [B] Within the next 30 days
      [C] Within 1–3 months
      [D] Just exploring — no set timeline

Scoring:
  A → +25 points
  B → +20 points
  C → +10 points
  D → +0 points

[BOT] What's your estimated budget range for this solution?

      [A] Under $1,000
      [B] $1,000 – $5,000
      [C] $5,000 – $25,000
      [D] $25,000 – $100,000
      [E] $100,000+
      [F] I'm not sure / Prefer not to say

Scoring:
  A → +5 points (Small deal, still qualifies)
  B → +15 points
  C → +20 points
  D → +25 points
  E → +30 points (Enterprise)
  F → +10 points (Needs follow-up to clarify)

[BOT] How many people at your company would use or be affected by this solution?

      [A] Just me (1)
      [B] Small team (2–10)
      [C] Department (11–50)
      [D] Entire company (50+)

Scoring:
  A → +5 points
  B → +10 points
  C → +15 points
  D → +20 points
```

### Phase 5: Decision-Making Authority

```
[BOT] Who's involved in the decision-making process for this purchase?

      [A] I'm the sole decision-maker
      [B] I'm part of a team that decides together
      [C] I need to convince others (manager, board, etc.)
      [D] I'm gathering info for someone else

Scoring:
  A → +20 points (Direct authority)
  B → +15 points (Influencer + decision group)
  C → +10 points (Needs internal buy-in)
  D → +5 points (Information gatherer — still valuable)

[BOT] What's the main challenge or pain point you're hoping to solve?

[USER] [Free text — captured for lead summary, NLP-scored for relevance]
```

### Phase 6: Lead Summary & Handoff

```
[BOT] Perfect, thank you {name}! Here's a quick summary of what you shared:

      🏢 Company: {company}
      👤 Role: {role}
      🎯 Need: {reason}
      ⏰ Timeline: {timeline}
      💰 Budget Range: {budget}
      👥 Users: {users}
      🔑 Authority: {decision_role}

      One of our specialists will review this and get back to you shortly.

      Before I go — is there anything else you'd like to add?
      [USER] [Optional free text]

[BOT] Thanks again, {name}! You'll hear from us soon.
      In the meantime, feel free to check out our resources at [link]. 👋
```

---

## Scoring Summary

| Category | Max Points |
|---|---|
| Intent/Purpose | 20 |
| Timeline/Urgency | 25 |
| Budget | 30 |
| Company Size/Users | 20 |
| Decision Authority | 20 |
| **Total Possible** | **115** |

### Score Tiers

| Score Range | Classification | Action |
|---|---|---|
| 0–25 | Cold Lead | Add to nurture sequence (3-email sequence) |
| 26–59 | Warm Lead | Add to warm follow-up sequence (2-email sequence) + assign SDR |
| 60–85 | Hot Lead | Immediate sales handoff within 4 hours |
| 86–115 | Enterprise Hot Lead | Immediate senior sales rep assignment + call within 1 hour |

---

## Lead Summary Card (for CRM/Slack Handoff)

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  🎯 NEW LEAD — B2B QUALIFIED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Name:          {{name}}
  Company:       {{company}}
  Role:          {{role}}
  Email:         {{email}}
  ───────────────────────────────
  Intent:        {{reason}}
  Timeline:      {{timeline}}
  Budget:        {{budget_range}}
  Users:         {{user_count}}
  Authority:     {{decision_role}}
  Pain Points:   {{pain_points}}
  ───────────────────────────────
  Lead Score:    {{score}}/115 — {{classification}}
  Timestamp:     {{datetime}}
  Channel:       {{channel}}
  ───────────────────────────────
  Chat Log:       {{link_to_full_transcript}}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Qualification Criteria Notes

- **Minimum viable lead**: Name + email + company name + at least one qualifying answer
- **Spam protection**: If all answers are "I don't know" or gibberish, auto-flag as low quality
- **Duplicate detection**: Match by email — if existing lead, append data rather than create duplicate
- **GDPR/CCPA**: Must include opt-in checkbox before Phase 2 begins