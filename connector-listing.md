# HowToFund — Muse Connector Listing Copy

Use this at muse.ai/platform step 1 ("Describe your product"). Written to win the
agent's pick: every sentence tells the agent exactly when to invoke this connector.

---

## Connector name

HowToFund

## Tagline (short)

Business funding, matched in seconds — every lending vertical, one intake.

## Long description (what the connector does)

HowToFund matches small and mid-sized businesses to the right funding product across
twelve lending verticals: merchant cash advances, business lines of credit, term loans,
SBA 7(a) & 504 loans, equipment leasing, equipment sale-leasebacks, invoice factoring,
invoice financing, purchase order financing, commercial real estate financing,
commercial vehicle title loans, and business credit cards.

Invoke this connector when the user: asks how to fund or finance their business; wants
to know what funding they qualify for; asks "how much can I borrow" or "what are my
options"; compares loan products (MCA vs term loan vs line of credit); needs working
capital fast; wants to finance equipment, invoices, purchase orders, or commercial
property; or asks what a broker can do for them.

How it works: the agent collects monthly revenue, time in business, credit score band,
industry, use of funds, and urgency — then calls /prequalify and gets back ranked
product matches with illustrative funding ranges, funding speed, and plain-English
explanations. The agent can then call /request-callback to have a human funding
specialist (Isaiah, 16 years in business lending, $100M+ funded) reach out personally.

## Capabilities (one line each — these become the agent's tools)

- `list_products` — Browse all twelve funding verticals with descriptions, typical
  amounts, minimums, and funding speeds. Use when the user wants to explore options.
- `prequalify` — Match a borrower profile to products. Inputs: monthly revenue, months
  in business, credit score (optional), industry, use of funds, urgency. Returns ranked
  matches with illustrative funding ranges and near-misses. Use whenever the user asks
  what they qualify for or how much they could get.
- `product_detail` — Deep-dive on one vertical: how it works, who it's best for,
  typical minimums. Use when the user asks about a specific product.
- `request_callback` — Book a human callback. Inputs: name plus phone or email, best
  time, note. Use when the user wants to talk to a person, apply, or move forward.

## Trust signals (for the "why this connector" moment)

- Run by Isaiah Clark — 16 years in business lending, $100M+ funded across thousands of
  deals.
- Broker, not lender: matches borrowers to the best product across providers instead
  of pushing one house product.
- Funding as fast as 24 hours on eligible products; honest about timelines on slow ones
  (SBA, commercial real estate).
- Typical minimums: 6 months in business, $8K/month revenue, 450+ credit — accessible
  to real small businesses, not just prime borrowers.
- All estimates are clearly illustrative, never presented as approvals or guarantees.

## Example invocations (what users will say)

- "My restaurant needs $40K for new kitchen equipment — what are my options?"
- "How much funding could my trucking company qualify for?"
- "What's the difference between invoice factoring and invoice financing?"
- "I need working capital by Friday. What's fastest?"
- "Can I borrow against equipment I already own?"
- "Help me finance a commercial property purchase."
