# How-to Guide: Using the Leads QualiFlow Client Dashboard

> **Audience**: New clients who purchased a Lead Package
> **Goal**: Navigate the dashboard, review leads, manage settings, and download lead data

---

## 1. Logging In

### Step 1: Access the Dashboard

1. Go to **app.leadsqualiflow.com** (or your custom subdomain)
2. Click **"Client Login"** in the top-right corner
3. Enter your **email** and **password** (sent in your welcome email)
4. Click **"Sign In"**

> **First time?** Check your inbox for an email from `hello@leadsqualiflow.com` with subject *"Welcome to Leads QualiFlow — Your Dashboard Awaits"*

### Step 2: Two-Factor Authentication (if enabled)

1. Enter the 6-digit code from your authenticator app
2. Click **"Verify"**

### Step 3: Accessibility Options

Once logged in, you'll see the accessibility toolbar at the top:

```
[Skip to Main Content] [Screen Reader Mode 🎧] [High Contrast 🌓]
[Font Size: A A A] [Voice Navigation 🎤] [Captions On/Off 📝]
```

- **Screen Reader Mode**: Optimizes all elements for JAWS/NVDA
- **Voice Navigation**: Say "Leads", "Settings", or "Help" to navigate
- **Captions**: Adds text captions to all video tutorials

---

## 2. Dashboard Overview

When you first log in, you'll see the **Dashboard**:

```
┌────────────────────────────────────────────────────────────┐
│  📊 DASHBOARD                    [Last refreshed: 2 min ago] │
├────────────────────────────────────────────────────────────┤
│  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌──────────┐          │
│  │ LEADS   │ │ QUAL.   │ │ CLOSE   │ │ PIPELINE │          │
│  │ THIS MO │ │ RATE    │ │ RATE    │ │ VALUE    │          │
│  │   47    │ │   68%   │ │   22%   │ │  $142K   │          │
│  └─────────┘ └─────────┘ └─────────┘ └──────────┘          │
│                                                             │
│  📈 LEAD TREND (Last 30 Days)                               │
│  ┌────────────────────────────────────────────────────┐     │
│  │  [Bar chart: daily leads delivered]                │     │
│  └────────────────────────────────────────────────────┘     │
│                                                             │
│  ⚡ RECENT LEADS                    [View All →]            │
│  ┌────────────────────────────────────────────────────┐     │
│  │ Name        | Score | Type    | Status    | Time   │     │
│  │─────────────|───────|─────────|───────────|────────│     │
│  │ J. Smith    | 82    | Hot     | Assigned  | 12min  │     │
│  │ A. Patel    | 45    | Warm    | Contacted | 1hr    │     │
│  │ M. Johnson  | 18    | Cold    | Nurture   | 3hr    │     │
│  │ L. Garcia   | 91    | 🔥 Elite | New      | 5min   │     │
│  └────────────────────────────────────────────────────┘     │
└────────────────────────────────────────────────────────────┘
```

### Key Metrics Explained

| Metric | What It Means |
|---|---|
| **Leads This Month** | Total qualified leads delivered to your account |
| **Qualification Rate** | % of leads meeting your custom ICP criteria |
| **Close Rate** | % of qualified leads that become customers (tracked manually) |
| **Pipeline Value** | Estimated total value of all active leads in your pipeline |

---

## 3. Viewing & Managing Leads

### Accessing Your Leads

Click **"Leads"** in the left sidebar. You'll see:

```
┌─────────────────────────────────────────────────────────────┐
│  LEADS                         [Filter ▼] [Export ▼] [🔍] │
├─────────────────────────────────────────────────────────────┤
│ ┌──────┬───────┬──────┬──────┬──────┬──────┬──────┬──────┐ │
│ │ Name │ Score│ Type │ Src  │ Stat │ Date │ Actn │      │ │
│ ├──────┼───────┼──────┼──────┼──────┼──────┼──────┤      │ │
│ │ ...  │ ...   │ ...  │ ...  │ ...  │ ...  │ [...]│      │ │
│ └──────┴───────┴──────┴──────┴──────┴──────┴──────┘      │ │
│                                            [1-25 of 47]    │
└─────────────────────────────────────────────────────────────┘
```

### Filters Available

| Filter | Options |
|---|---|
| **Score Range** | Cold (0–25), Warm (26–59), Hot (60–85), Elite (86+) |
| **Lead Type** | B2B, Real Estate, Financial, Legal |
| **Source Channel** | Website, SMS, WhatsApp, Facebook, Referral |
| **Status** | New, Assigned, Contacted, Negotiating, Closed Won, Closed Lost |
| **Date Range** | Today, This Week, This Month, Custom |
| **Language** | English, Spanish, French, Mandarin, Hindi, Arabic |

### Lead Detail View

Click any lead name to see full details:

```
┌──────────────────────────────────────────────────────────────┐
│  LEAD DETAIL: Sarah Chen                   [Edit] [Export]  │
├──────────────────────────────────────────────────────────────┤
│  📋 INFORMATION                                              │
│  Name:        Sarah Chen                                     │
│  Company:     LogiCo Logistics                               │
│  Role:        VP of Operations                               │
│  Email:       sarah.chen@logico.com                          │
│  Phone:       (555) 123-4567                                 │
│  ────────────────────────────────────────────────────────    │
│  🎯 QUALIFICATION                                            │
│  Score:       95/115 — Elite Hot Lead 🔥                     │
│  Intent:      Evaluating PM software                          │
│  Timeline:    Within 30 days                                  │
│  Budget:      $25K–$100K                                     │
│  Authority:   Decision-maker                                  │
│  Pain Point:  Managing 12 warehouses with spreadsheets       │
│  ────────────────────────────────────────────────────────    │
│  💬 FULL CHAT TRANSCRIPT                                     │
│  [Show/Hide ▼]                                               │
│  ┌──────────────────────────────────────────────────────┐    │
│  │ Bot: Welcome to Acme Software...                      │    │
│  │ User: Sure, go ahead...                               │    │
│  │ ... (full conversation)                               │    │
│  └──────────────────────────────────────────────────────┘    │
│  ────────────────────────────────────────────────────────    │
│  📊 ACTIVITY LOG                                             │
│  • 10:34 — Chat started (Website)                            │
│  • 10:37 — Lead scored (95 pts)                              │
│  • 10:38 — Alert sent to sales team                          │
│  • 11:24 — Mike Torres called lead (50 min response)         │
│  • 14:02 — Demo booked (Thursday 2:00 PM)                    │
└──────────────────────────────────────────────────────────────┘
```

---

## 4. Managing Lead Status

### Updating Lead Status

1. Open any lead detail
2. Click the **Status** dropdown (top-right of lead card)
3. Select from: **New → Assigned → Contacted → Negotiating → Closed Won → Closed Lost**

### Bulk Actions

Select multiple leads with checkboxes, then:

- **Assign To** → Reassign leads to a team member
- **Change Status** → Update status for all selected
- **Export Selected** → Download as CSV
- **Delete** → Remove from your view (cannot be undone)

---

## 5. Exporting Lead Data

### Quick Export

1. From **Leads** page, click **"Export"**
2. Choose format: **CSV** or **Excel**
3. Select date range: **This Month** | **Last Month** | **Custom Range**
4. Click **"Download"**

### Export Includes

| Column | Description |
|---|---|
| Name, Email, Phone, Company | Contact info |
| Lead Score, Classification | Qualification data |
| Intent, Timeline, Budget | Survey responses |
| Channel, Language | Source data |
| Full Chat Transcript | JSON blob (downloadable separately) |
| Status, Last Contacted | CRM status |

### Automated Exports (CRM Auto-Delivery Add-On)

If you've purchased the **CRM Auto-Delivery** add-on ($97/mo):

1. Go to **Settings → Integrations**
2. Select your CRM: **Salesforce** | **HubSpot** | **Pipedrive** | **Zoho** | **Slack** | **Custom API**
3. Follow the authentication prompts
4. Choose sync frequency: **Real-time** | **Hourly** | **Daily**

---

## 6. Settings & Configuration

### Account Settings

Go to **Settings → Account**:

- **Profile**: Update name, email, password
- **Notification Preferences**: Email/Slack alerts for new leads
- **Timezone**: Set your local timezone for lead timestamps
- **Team Members**: Add/remove users (max 5 on Pro, unlimited on Enterprise)

### Qualification Criteria

Go to **Settings → Qualification**:

- **Custom Criteria**: If you purchased the Custom Qualification Criteria add-on ($197), you can edit chatbot questions here
- **Score Thresholds**: Adjust what scores qualify as Cold/Warm/Hot/Elite
- **Industry Templates**: Switch between B2B, Real Estate, Financial, or Legal scripts

### Lead Package Management

Go to **Settings → Billing**:

- View your current plan (Starter/Growth/Pro/Elite/Enterprise)
- Upgrade or downgrade packages
- View add-ons you've purchased
- Download invoices

### Territory Settings

Go to **Settings → Territories** (with Exclusive Territory Rights add-on):

- View your locked ZIP codes
- Request territory expansion
- View competitor lead capture reports

---

## 7. Tracking Performance

### Monthly Performance Report

If you've purchased the **Monthly Performance Report** add-on ($47/mo):

1. Go to **Reports** in the sidebar
2. View automatically generated reports on the 1st of each month
3. Reports include:

```
📊 MONTHLY PERFORMANCE REPORT — [Month Year]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Leads Delivered:      47 (⬆ 12% from last month)
Qualification Rate:   68% (⬆ 3%)
Close Rate:           22% (⬇ 2%)
Avg. Response Time:   3.2 hours (⬇ 30 min)
Pipeline Value:       $142,000 (⬆ 18%)
Best Performing Channel: Website (62% of leads)
Top Lead Source City: Chicago, IL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Custom Reports

Use the **Report Builder** to create custom views:
- Filter by date, channel, score, status
- Compare month-over-month
- Export to PDF or CSV

---

## 8. Getting Help

### In-App Help

- Click the **?** icon in the bottom-right corner for the help menu
- Search the knowledge base for tutorials
- Chat with support (human, 9 AM–8 PM EST)

### Tutorial Videos

Accessible from **Help → Tutorials**:

- 📺 "Dashboard Overview" (2 min)
- 📺 "Managing Your Leads" (3 min)
- 📺 "Setting Up CRM Integration" (5 min)
- 📺 "Understanding Lead Scores" (4 min)

*All videos include captions and transcripts.*

### Contact Support

- **Email**: support@leadsqualiflow.com
- **Phone**: (555) 987-6543
- **Hours**: Monday–Friday, 9 AM–8 PM EST
- **Emergency**: For urgent lead issues (Enterprise clients only), use the "Emergency" button in the dashboard

---

## Quick Reference Card

```
┌─────────────────────────────────────────────────────────────┐
│  LEADS QUALIFLOW — DASHBOARD QUICK REFERENCE                │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  🔑 LOGIN: app.leadsqualiflow.com                            │
│                                                              │
│  📊 DASHBOARD → See your metrics at a glance                 │
│  👤 LEADS → View, filter, and manage all leads               │
│  📈 REPORTS → Performance analytics & export                 │
│  ⚙️ SETTINGS → Account, integrations, billing               │
│                                                              │
│  🎯 LEAD SCORE TIERS:                                        │
│     0–25   🟦 Cold → Nurture sequence                        │
│     26–59  🟩 Warm → SDR follow-up within 24h               │
│     60–85  🟧 Hot → Sales rep within 4h                     │
│     86+    🔥 Elite → Senior rep within 1h                  │
│                                                              │
│  🆘 HELP: support@leadsqualiflow.com                         │
└─────────────────────────────────────────────────────────────┘
```