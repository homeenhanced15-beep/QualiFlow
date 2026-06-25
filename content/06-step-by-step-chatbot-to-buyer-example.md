# How a Lead Goes from Chatbot to Qualified Buyer

> **Scenario**: A mid-sized B2B SaaS company uses Leads QualiFlow to qualify leads on their website
> **Client**: Acme Software Solutions (fictional) — sells project management software to enterprises
> **Lead**: Sarah Chen — VP of Operations at a 200-person logistics company

---

## The Full Journey — Step by Step

### Step 1: Lead Encounters the Chatbot

**Sarah** visits Acme's website after searching "enterprise project management software."
She sees the chat bubble in the bottom right corner.

```
🟢 "Hi! I'm here to help. Got a quick question?"
```

**Sarah clicks the bubble.** The chatbot activates.

**Channel**: Website embed → Desktop
**Timestamp**: Tuesday, 10:34 AM EST

---

### Step 2: Chatbot Qualifies the Lead

The chat proceeds through the B2B qualification flow (Script A):

```
BOT: Welcome to Acme Software! Mind if I ask a few quick questions?

SARAH: Sure, go ahead.

BOT: What's your name?
SARAH: Sarah Chen

BOT: Thanks Sarah! What's the best email to reach you?
SARAH: sarah.chen@logico.com

BOT: And your company name?
SARAH: LogiCo Logistics

BOT: Got it! What's your role at LogiCo?
SARAH: VP of Operations

BOT: What brings you here today?
SARAH: We're evaluating project management tools. [→ +20 pts]

BOT: How soon are you looking to decide?
SARAH: Within 30 days. [→ +20 pts]

BOT: What's your budget range?
SARAH: $25,000–$100,000. [→ +25 pts]

BOT: How many users would this affect?
SARAH: Our whole operations team — about 50 people. [→ +15 pts]

BOT: Who's involved in the decision?
SARAH: I'll make the final call after input from my team. [→ +15 pts]

BOT: What's the main challenge you're solving?
SARAH: We're managing projects across 12 warehouses with spreadsheets.
      It's chaos. We need real-time visibility.
```

---

### Step 3: Lead Score Calculated

| Criterion | Sarah's Answer | Points |
|---|---|---|
| Intent | Evaluating solutions | 20 |
| Timeline | Within 30 days | 20 |
| Budget | $25K–$100K | 25 |
| Team Size | 50 users | 15 |
| Authority | Final decision-maker | 15 |
| **Total** | | **95/115** |

**Classification**: 🔥 **Enterprise Hot Lead** (Score 86–115)

**Action triggered**: Instant sales team notification

---

### Step 4: Lead Gets a Confirmation

```
BOT: Thanks Sarah! Here's your summary:

      🏢 LogiCo Logistics  |  VP of Operations
      🎯 Evaluating PM tools  |  Timeline: 30 days
      💰 $25K–$100K  |  50 users
      🔑 You're the decision-maker

      One of our specialists will reach out shortly!

SARAH: Great, thanks!

BOT: Have a great day! 👋
```

---

### Step 5: Internal Hot Lead Alert Fires

**Within 30 seconds**, the sales team receives:

Slack DM to #hot-leads channel:

```
🔥 HOT LEAD — Score: 95/115
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Sarah Chen | VP Ops | LogiCo Logistics
sarah.chen@logico.com | (555) 123-4567
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Want: PM software for 50 users
Budget: $25K-$100K | Timeline: 30 days
Decision-maker: YES
Pain: Managing 12 warehouses with spreadsheets
━━━━━━━━━━━━━━━━━━━━━━━━━━━
⏱️ PICK UP WITHIN 60 MINUTES
Full transcript: [link]
━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

Email alert sent to assigned sales rep **Mike Torres**:

```
🚀 HOT LEAD: Sarah Chen — LogiCo Logistics
Contact within 1 hour. Transcript attached.
```

---

### Step 6: Sales Rep Follows Up (Within 50 Minutes)

**Mike calls Sarah** at 11:24 AM — 50 minutes after her chat.

```
MIKE: Hi Sarah, this is Mike Torres from Acme Software.
      I saw you were checking out our platform — sounds like
      LogiCo is scaling fast with those 12 warehouses.

SARAH: [Laughs] That's one way to put it! Yes, the spreadsheets
       are becoming unmanageable.

MIKE: Totally understand. I'd love to show you how we've helped
      similar logistics companies get real-time visibility.
      Could we set up a 30-minute demo for later this week?

SARAH: Thursday at 2 PM works. Can you include a scenario
       with multi-location reporting?

MIKE: Absolutely. I'll send you a calendar invite right now.
```

**Demo booked**: Thursday at 2:00 PM

---

### Step 7: Demo & Proposal

**Thursday**: Mike delivers a tailored demo showing multi-location reporting.
Sarah brings her operations team lead.

**Friday**: Mike sends a proposal — $48,000/year for 55 licenses, including onboarding.

---

### Step 8: Deal Closed

**Two weeks later**: Sarah signs the contract.

**Annual value**: $48,000 MRR → $48,000 ARR

**Time from chatbot to closed deal**: 19 days

**QualiFlow metrics contributed to this win**:

| Metric | Value |
|---|---|
| Time-to-first-contact | 50 minutes |
| Lead score accuracy | 95 — correctly identified as hot |
| Qualification cost | $0 (chatbot automation) |
| Sales rep time saved | ~3 hours (manual qualification avoided) |

---

## Key Takeaways

### What Made This Lead Successful?

1. **Quick response time** — 50 minutes to first contact (vs. industry avg of 21 hours)
2. **Accurate scoring** — The chatbot correctly identified high intent from Sarah's specific pain point
3. **Personalized handoff** — Mike used the chatbot transcript to reference Sarah's exact situation
4. **Right channel** — Sarah preferred phone, which the lead card captured

### What If Sarah Had Scored Lower?

| Score Range | What Would Happen |
|---|---|
| 0–25 (Cold) | Enter nurture sequence. Not called unless she re-engages. |
| 26–59 (Warm) | Assigned to SDR for follow-up in 24 hours. |
| 60–85 (Hot) | Assigned to rep within 4 hours. |
| 86+ (Enterprise Hot) | Senior rep within 1 hour — which is what happened. |

### ROI for Acme Software

| Metric | Before QualiFlow | After QualiFlow |
|---|---|---|
| Sales calls per qualified lead | 8 | 2 |
| Time qualifying leads per week (per rep) | 12 hours | 2 hours |
| Leads that were "not ready" when called | 60% | 15% |
| Close rate on qualified leads | 12% | 34% |