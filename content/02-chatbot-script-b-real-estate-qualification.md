# Script B: Real Estate / Agency Lead Qualification Chatbot

> **Purpose**: Qualify real estate leads — buyers, sellers, renters, and investors
> **Channel**: Real estate website, Zillow/Realtor.com integration, SMS, social media DM
> **Lead Scoring Range**: 0–100 points
> **Qualified Threshold**: ≥ 55 points

---

## Conversation Flow

### Phase 1: Greeting & Property Intent

```
[BOT] 🏠 Hi there! Welcome to [Agency Name].
       Looking for a property, or thinking of selling?

       [I'm looking to BUY]  [I'm looking to SELL]  [I want to RENT]
       [I'm an INVESTOR]  [Just browsing]

Scoring (intent):
  BUY    → +10 points (High-value buyer intent)
  SELL   → +10 points (High-value seller intent)
  RENT   → +5 points (Lower value but possible future buyer)
  INVEST → +15 points (Repeat business potential)
  BROWSE → +0 points (Nurture)

[IF "I want to SELL"]
[BOT] Excellent! Let's find out what your property is worth.
      What type of property are you selling?
      [Single Family Home]  [Condo/Apartment]  [Townhouse]
      [Multi-Unit/Commercial]  [Land/Lot]

[IF "I'm looking to BUY" or "RENT"]
[BOT] Great! What type of property are you looking for?
      [Single Family Home]  [Condo/Apartment]  [Townhouse]
      [Multi-Unit]  [Commercial/Retail]
```

### Phase 2: Contact Information

```
[BOT] What's your full name?
[USER] [Enters name]

[BOT] Thanks, {name}! What's the best email to reach you at?
[USER] [Enters email]

[BOT] And a phone number where we can text or call you?
[USER] [Enters phone]

[BOT] What city or neighborhood are you interested in?
      (Or — if selling — where is the property located?)
[USER] [Enters city/neighborhood/zip]

Scoring: +5 points for providing phone number
```

### Phase 3: Timeline & Urgency

```
[BOT] When are you hoping to make a move?

      [A] ASAP — within 2 weeks
      [B] Within 1 month
      [C] Within 3 months
      [D] Within 6 months
      [E] Just exploring — no rush

Scoring:
  A → +25 points
  B → +20 points
  C → +15 points
  D → +10 points
  E → +0 points

[BOT] Have you already been pre-approved for a mortgage?
      [Only show if intent = BUY]

      [A] Yes — I have a pre-approval letter
      [B] I'm working on it now
      [C] Not yet — I need recommendations
      [D] I'm paying cash

Scoring:
  A → +20 points (Serious buyer)
  D → +20 points (Cash buyer — premium lead)
  B → +10 points (In progress)
  C → +5 points (Needs handholding)

[IF selling]
[BOT] Have you already purchased your next home?

      [A] Yes — I need to sell my current home
      [B] No — I want to sell first, then buy
      [C] I'm not sure yet on the timing

Scoring:
  A → +20 points (Motivated seller — carrying two properties)
  B → +15 points (Ready to move)
  C → +5 points (Casual seller)
```

### Phase 4: Property Details & Preferences

```
[BOT] What's your budget range?

      [A] Under $200,000
      [B] $200,000 – $400,000
      [C] $400,000 – $700,000
      [D] $700,000 – $1,000,000
      [E] $1,000,000+

Scoring:
  A → +5 points
  B → +10 points
  C → +15 points
  D → +20 points
  E → +25 points (High-value lead)

[BOT] What are your top priorities? (Select all that apply)

      [ ] Location/Neighborhood
      [ ] Price/Value
      [ ] Square footage / Lot size
      [ ] Number of bedrooms/bathrooms
      [ ] School district
      [ ] Commute time
      [ ] New construction
      [ ] Move-in ready condition
      [ ] Yard/Outdoor space
      [ ] Garage/Parking

Scoring: +2 points per selection (max +14 points)

[BOT] How many bedrooms do you need?

      [Studio/Loft]  [1 bedroom]  [2 bedrooms]
      [3 bedrooms]  [4 bedrooms]  [5+ bedrooms]

[IF SELLING]
[BOT] Tell us about your property:

      - Property type: [Single Family / Condo / Townhouse / Multi-Unit / Land]
      - Bedrooms: [#]
      - Bathrooms: [#]
      - Approximate square footage: [#]
      - Year built: [year]
      - Any renovations in the last 5 years? [Yes / No]
        [IF Yes]: What kind? [Free text]

      +5 points if property is well-maintained or recently renovated
```

### Phase 5: Lead Summary & Handoff

```
[BOT] Thanks, {name}! Here's what I've noted:

      🏠 Intent: {buy/sell/rent/invest}
      📍 Area: {city/neighborhood}
      💰 Budget/Price: {budget}
      ⏰ Timeline: {timeline}
      🏡 Property Type: {property_type}
      🛏️ Bedrooms: {bedrooms}
      📋 Top Priorities: {priorities}

      One of our top agents will be in touch shortly!

[BOT] Any questions before I hand you off?
[USER] [Optional free text]

[BOT] You're all set! Keep an eye on your phone/email — {agent_name}
      will reach out soon. Have a great day! 🏡👋
```

---

## Scoring Summary

| Category | Max Points |
|---|---|
| Intent | 15 |
| Contact Provided (phone) | 5 |
| Timeline/Urgency | 25 |
| Financial Readiness (pre-approval/cash/seller motivation) | 20 |
| Budget Range | 25 |
| Preferences & Specificity | 14 |
| Property Condition (selling) | 5 |
| **Total Possible** | **109** |

### Score Tiers

| Score Range | Classification | Action |
|---|---|---|
| 0–25 | Cold / Browsing | Add to monthly newsletter + drip campaign |
| 26–54 | Warm Lead | Send to inside sales agent for follow-up within 24 hrs |
| 55–79 | Hot Buyer/Seller | Assign to top agent — contact within 4 hours |
| 80+ | Premium Lead | Immediate agent assignment + text/call within 1 hour |

---

## Lead Summary Card (for CRM/Slack Handoff)

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  🏠 NEW LEAD — REAL ESTATE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Name:          {{name}}
  Email:         {{email}}
  Phone:         {{phone}}
  Intent:        {{buy/sell/rent/invest}}
  Area:          {{city/neighborhood}}
  Budget:        {{budget_range}}
  Timeline:      {{timeline}}
  ───────────────────────────────
  Property Type: {{property_type}}
  Bedrooms:      {{bedrooms}}
  Priorities:    {{priorities}}
  ───────────────────────────────
  Pre-Approved:  {{yes/no/in progress/cash}}
  Lead Score:    {{score}}/109 — {{classification}}
  Timestamp:     {{datetime}}
  Channel:       {{channel}}
  ───────────────────────────────
  Chat Log:       {{link_to_full_transcript}}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Qualification Criteria Notes

- **Minimum viable lead**: Name + email + phone + property intent + city/neighborhood
- **Duplicate detection**: Match by email AND phone — real estate leads frequently search from multiple devices
- **Priority rules**: Cash buyers and pre-approved buyers skip the queue
- **Seller leads**: Always flag for immediate call — sellers often interview multiple agents the same day
- **Fair Housing Compliance**: Do NOT ask about race, religion, gender, familial status, disability, or national origin