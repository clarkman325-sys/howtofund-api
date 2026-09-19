"""
HowToFund product catalog — every funding vertical Isaiah brokers,
encoded as data so the pre-qualification engine (and later, AI agents)
can match borrowers to the right products.

All amounts and speeds are ILLUSTRATIVE industry-typical figures, not offers.
Per-product minimums reflect Isaiah's working guidelines as a broker.
"""

PRODUCTS = [
    {
        "id": "mca",
        "name": "Merchant Cash Advance",
        "tagline": "Fast working capital repaid from future sales",
        "description": (
            "A lump sum of working capital in exchange for a fixed percentage of future "
            "credit/debit card sales or bank deposits. Not a loan — approval is based on revenue, "
            "not credit. Funding can land in as little as 24 hours."
        ),
        "min_tib_months": 6,
        "min_monthly_revenue": 8000,
        "min_credit_score": 450,
        "typical_amount_min": 5000,
        "typical_amount_max": 500000,
        "funding_speed": "24 hours",
        "revenue_multiple_low": 0.75,
        "revenue_multiple_high": 1.25,
        "best_for": ["urgent working capital", "payroll gaps", "inventory", "bad credit OK"],
    },
    {
        "id": "business_loc",
        "name": "Business Line of Credit",
        "tagline": "Revolving credit you draw only when you need it",
        "description": (
            "A revolving credit facility the business draws from as needed and repays, then reuses. "
            "Ideal for smoothing cash flow, covering seasonal dips, or handling surprise expenses. "
            "Interest accrues only on what is drawn."
        ),
        "min_tib_months": 6,
        "min_monthly_revenue": 10000,
        "min_credit_score": 550,
        "typical_amount_min": 10000,
        "typical_amount_max": 250000,
        "funding_speed": "2-5 days",
        "revenue_multiple_low": 1.0,
        "revenue_multiple_high": 3.0,
        "best_for": ["cash flow smoothing", "seasonal gaps", "unexpected expenses", "flexibility"],
    },
    {
        "id": "term_loan",
        "name": "Business Term Loan",
        "tagline": "A lump sum with fixed payments over 1-5 years",
        "description": (
            "A traditional lump-sum loan repaid in fixed installments over 1 to 5 years. "
            "Lower cost than a cash advance, best for planned investments like expansion, "
            "renovations, or large equipment purchases."
        ),
        "min_tib_months": 12,
        "min_monthly_revenue": 15000,
        "min_credit_score": 600,
        "typical_amount_min": 25000,
        "typical_amount_max": 500000,
        "funding_speed": "3-10 days",
        "revenue_multiple_low": 2.0,
        "revenue_multiple_high": 6.0,
        "best_for": ["expansion", "renovations", "large purchases", "lower cost capital"],
    },
    {
        "id": "sba_loan",
        "name": "SBA Loan (7(a) & 504)",
        "tagline": "Government-backed loans with the lowest rates and longest terms",
        "description": (
            "Loans partially guaranteed by the U.S. Small Business Administration, including 7(a) "
            "working-capital loans and 504 loans for real estate and heavy equipment. Lowest rates "
            "and longest terms available — but slower, with heavy documentation."
        ),
        "min_tib_months": 24,
        "min_monthly_revenue": 25000,
        "min_credit_score": 650,
        "typical_amount_min": 50000,
        "typical_amount_max": 5000000,
        "funding_speed": "30-90 days",
        "revenue_multiple_low": 2.0,
        "revenue_multiple_high": 8.0,
        "best_for": ["lowest rates", "long terms", "real estate", "heavy equipment", "not urgent"],
    },
    {
        "id": "equipment_lease",
        "name": "Equipment Leasing",
        "tagline": "Get the equipment now, pay as it earns",
        "description": (
            "Finance new or used equipment — trucks, machinery, medical devices, kitchen build-outs — "
            "with the equipment itself as collateral. Preserves working capital and often requires "
            "little money down. End-of-term buyout options available."
        ),
        "min_tib_months": 6,
        "min_monthly_revenue": 8000,
        "min_credit_score": 550,
        "typical_amount_min": 10000,
        "typical_amount_max": 1000000,
        "funding_speed": "2-7 days",
        "revenue_multiple_low": 1.0,
        "revenue_multiple_high": 5.0,
        "best_for": ["equipment", "vehicles", "machinery", "preserve cash"],
    },
    {
        "id": "equipment_leaseback",
        "name": "Equipment Sale-Leaseback",
        "tagline": "Unlock cash from equipment you already own",
        "description": (
            "Sell equipment you already own to a funder and lease it right back. Converts idle equity "
            "in trucks, machinery, or devices into immediate working capital — while you keep using "
            "the equipment every day."
        ),
        "min_tib_months": 12,
        "min_monthly_revenue": 15000,
        "min_credit_score": 550,
        "typical_amount_min": 25000,
        "typical_amount_max": 2000000,
        "funding_speed": "5-14 days",
        "revenue_multiple_low": 1.0,
        "revenue_multiple_high": 4.0,
        "best_for": ["unlock equity", "owned equipment", "working capital", "no new debt on books"],
    },
    {
        "id": "invoice_factoring",
        "name": "Invoice Factoring",
        "tagline": "Sell unpaid invoices for cash today",
        "description": (
            "Sell outstanding B2B invoices to a factor at a small discount and get 70-90% of the "
            "invoice value within days. The factor collects from your customers. Approval is based "
            "on your customers' creditworthiness, not yours."
        ),
        "min_tib_months": 6,
        "min_monthly_revenue": 10000,
        "min_credit_score": 500,
        "typical_amount_min": 10000,
        "typical_amount_max": 10000000,
        "funding_speed": "2-5 days",
        "revenue_multiple_low": 0.5,
        "revenue_multiple_high": 2.0,
        "best_for": ["unpaid invoices", "B2B", "slow-paying customers", "payroll"],
    },
    {
        "id": "invoice_financing",
        "name": "Invoice Financing",
        "tagline": "Borrow against invoices, keep collecting yourself",
        "description": (
            "Like factoring, but you keep control of collections: borrow against the value of unpaid "
            "invoices and repay as customers pay you. Your customers never know a funder is involved."
        ),
        "min_tib_months": 6,
        "min_monthly_revenue": 10000,
        "min_credit_score": 550,
        "typical_amount_min": 10000,
        "typical_amount_max": 5000000,
        "funding_speed": "2-5 days",
        "revenue_multiple_low": 0.5,
        "revenue_multiple_high": 2.0,
        "best_for": ["unpaid invoices", "keep customer relationships", "confidential funding"],
    },
    {
        "id": "po_financing",
        "name": "Purchase Order Financing",
        "tagline": "Fund large orders before your customer pays",
        "description": (
            "A funder pays your suppliers directly so you can fulfill large purchase orders you "
            "couldn't otherwise afford to take on. Built for manufacturers, wholesalers, distributors, "
            "and importers with confirmed POs from creditworthy buyers."
        ),
        "min_tib_months": 6,
        "min_monthly_revenue": 15000,
        "min_credit_score": 500,
        "typical_amount_min": 50000,
        "typical_amount_max": 5000000,
        "funding_speed": "5-14 days",
        "revenue_multiple_low": 1.0,
        "revenue_multiple_high": 4.0,
        "best_for": ["large orders", "manufacturing", "wholesale", "importers", "growth"],
    },
    {
        "id": "cre_finance",
        "name": "Commercial Real Estate Financing",
        "tagline": "Purchase, refinance, or pull cash from commercial property",
        "description": (
            "Financing for commercial property: purchases, rate-and-term refinances, and cash-out "
            "refinances across office, retail, industrial, mixed-use, and multifamily. Longer timelines "
            "than working-capital products, but far larger checks and lower rates."
        ),
        "min_tib_months": 12,
        "min_monthly_revenue": 20000,
        "min_credit_score": 620,
        "typical_amount_min": 100000,
        "typical_amount_max": 10000000,
        "funding_speed": "21-60 days",
        "revenue_multiple_low": 4.0,
        "revenue_multiple_high": 12.0,
        "best_for": ["property purchase", "refinance", "cash out equity", "large checks"],
    },
    {
        "id": "title_loan",
        "name": "Commercial Vehicle Title Loan",
        "tagline": "Borrow against vehicles your business owns free and clear",
        "description": (
            "Short-term capital secured by the title of company-owned vehicles or heavy equipment. "
            "Fast approval based on equity in the asset — keep driving the vehicles while you repay."
        ),
        "min_tib_months": 6,
        "min_monthly_revenue": 8000,
        "min_credit_score": 450,
        "typical_amount_min": 5000,
        "typical_amount_max": 50000,
        "funding_speed": "24-72 hours",
        "revenue_multiple_low": 0.25,
        "revenue_multiple_high": 1.0,
        "best_for": ["fast cash", "owned vehicles", "bad credit OK", "keep driving"],
    },
    {
        "id": "business_credit_card",
        "name": "Business Credit Card",
        "tagline": "Revolving credit with rewards for everyday spend",
        "description": (
            "Unsecured revolving credit for everyday business expenses, often with rewards or cash back. "
            "Useful as a supplement to larger funding — not a replacement for real working capital."
        ),
        "min_tib_months": 6,
        "min_monthly_revenue": 5000,
        "min_credit_score": 650,
        "typical_amount_min": 1000,
        "typical_amount_max": 50000,
        "funding_speed": "7-14 days",
        "revenue_multiple_low": 0.25,
        "revenue_multiple_high": 1.0,
        "best_for": ["everyday spend", "rewards", "supplement", "build credit"],
    },
]

# Keywords mapping a borrower's stated use of funds to product ids.
USE_OF_FUNDS_MAP = {
    "payroll": ["mca", "business_loc", "invoice_factoring"],
    "cash flow": ["business_loc", "mca", "invoice_financing"],
    "inventory": ["mca", "business_loc", "po_financing"],
    "equipment": ["equipment_lease", "equipment_leaseback", "sba_loan", "term_loan"],
    "vehicle": ["equipment_lease", "title_loan"],
    "truck": ["equipment_lease", "title_loan"],
    "expand": ["term_loan", "sba_loan", "business_loc"],
    "expansion": ["term_loan", "sba_loan", "business_loc"],
    "renovation": ["term_loan", "sba_loan"],
    "real estate": ["cre_finance", "sba_loan"],
    "property": ["cre_finance", "sba_loan"],
    "refinance": ["cre_finance", "term_loan"],
    "invoice": ["invoice_factoring", "invoice_financing"],
    "receivables": ["invoice_factoring", "invoice_financing"],
    "purchase order": ["po_financing"],
    "supplier": ["po_financing", "business_loc"],
    "emergency": ["mca", "title_loan", "business_loc"],
    "urgent": ["mca", "title_loan", "business_loc"],
    "marketing": ["mca", "business_loc"],
    "hire": ["mca", "business_loc", "term_loan"],
}

# Products that fund fast — boosted when urgency is high.
FAST_PRODUCTS = {"mca", "title_loan", "business_loc", "invoice_factoring", "invoice_financing"}
SLOW_PRODUCTS = {"sba_loan", "cre_finance"}
