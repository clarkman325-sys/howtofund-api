# HowToFund API

The service behind the HowToFund Muse connector. One intake, every funding vertical —
a LendingTree-style matcher for business lending, run by a broker with 16 years and
$100M+ funded.

## Verticals covered (12)

Merchant cash advance · Business line of credit · Term loan · SBA 7(a) & 504 ·
Equipment leasing · Equipment sale-leaseback · Invoice factoring · Invoice financing ·
Purchase order financing · Commercial real estate financing · Commercial vehicle
title loans · Business credit cards

## Run locally ($0)

```bash
cd ~/workspace/howtofund-api
pip install -r requirements.txt
uvicorn app:app --reload --port 8000
```

Then open http://localhost:8000/docs for the interactive API playground.

## Try the matcher

```bash
curl -X POST http://localhost:8000/prequalify \
  -H 'Content-Type: application/json' \
  -d '{"monthly_revenue": 45000, "time_in_business_months": 18,
       "credit_score": 620, "industry": "restaurant",
       "use_of_funds": "need equipment fast", "urgency": "asap"}'
```

## Deploy free (keeps the $0 rule)

Render free tier: connect this folder as a repo, set build command
`pip install -r requirements.txt`, start command `uvicorn app:app --host 0.0.0.0 --port $PORT`.
Alternatives: Fly.io free tier, Cloudflare Workers (via port), Railway trial.

## The Muse connector path

1. Deploy the API to a public HTTPS URL.
2. At muse.ai/platform: "Describe your product" — use `connector-listing.md` in this folder.
3. Submit for review (functional / security / legal).
4. Once approved, the connector appears in the Muse directory — users reach
   HowToFund just by asking their agent for funding help.

## Compliance notes (do not skip)

- Every response carries the disclaimer: estimates are illustrative, not offers.
- HowToFund is a broker, not a lender. The API never approves or guarantees funding.
- `/request-callback` stores leads as local JSON — wire it to email/SMS before
  pointing real traffic at it.
- No client names, rates, or deal details are exposed anywhere in this service.
