# Anna AI Onboarding Questionnaire Blueprint (Expanded)

This blueprint outlines the structure and fields for the interactive onboarding system managed by "Anna," the AI Expert. This version includes the "AI Clone" expansion.

## Step 1: Business Profile
- **Business Name**: Text Input (Required)
- **Industry**: Dropdown (SaaS, Real Estate, Financial Services, Legal, Medical, Home Services, Other)
- **Company Size**: Dropdown (1-10, 11-50, 51-200, 200+)
- **Website URL**: URL Input

## Step 2: Ideal Customer Profile (ICP)
- **Target Industries**: Multi-Checkbox (SaaS, Real Estate, Finance, Legal, Health, Construction, Other)
- **Target Company Size**: Dropdown (1-10, 11-50, 51-200, 200+)
- **Decision-Maker Role/Title**: Text Input
- **Primary Pain Points**: Textarea

## Step 3: Qualification Criteria
- **Minimum Budget Range**: Dropdown (<$1k, $1k-$5k, $5k-$10k, $10k+)
- **Purchase Timeline**: Dropdown (Immediate, 30 days, 1-3 months, Exploring)
- **Decision Authority**: Dropdown (Sole decision-maker, Part of team, Need to convince others)
- **Custom Qualifying Questions**: Textarea (up to 3 questions)

## Step 4: Preferences
- **Languages**: Checkboxes (English, Spanish, French, Mandarin, Hindi, Arabic, Other)
- **Lead Delivery Method**: Dropdown (Email, CRM, Slack)
- **Follow-up Cadence**: Dropdown (Instant, Daily, Weekly)
- **Territory/Geographic Focus**: Text Input

## Step 5: Your AI Clone (New)
- **AI Clone Option**: Radio (Yes/No) - "Would you like an AI clone that prospects can talk to?"
- **Communication Style**: Dropdown (Professional, Casual, Friendly, Direct, Consultative)
- **Sales Philosophy**: Textarea - "What's your personal sales philosophy or approach?"
- **Key Points**: Textarea - "Share 3-5 key points you always want prospects to know about your offering"
- **Objection Handling**: Textarea - "What's a common objection you hear, and how do you handle it?"
- **Closing Line**: Text Input - "Your typical closing line or call to action"

## Step 6: Review & Submit
- **Summary**: Display all collected data for final review, including AI Clone details.
- **Confirmation**: Accessible submit button.
- **Post-Submission**: Success message indicating chatbot and AI Clone readiness within 24 hours.

## Technical Requirements
- **Accessibility**: WCAG 2.1 AA compliant.
- **ARIA**: Legends, fieldsets, aria-live for progress/errors.
- **Focus Management**: Move focus to step header on navigation.
- **Keyboard**: Full tab/enter support.
- **Progress Tracking**: "Step X of 6" displayed and announced.
