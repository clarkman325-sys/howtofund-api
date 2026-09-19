"""
Pre-qualification engine: matches a borrower profile against the product catalog.

Returns ranked matches with illustrative funding ranges, plus "almost there"
near-misses. Nothing here is an offer or approval — estimates only.
"""

from products import PRODUCTS, USE_OF_FUNDS_MAP, FAST_PRODUCTS, SLOW_PRODUCTS

DISCLAIMER = (
    "Illustrative estimates based on typical industry ranges, not offers, approvals, "
    "or guarantees. Actual amounts, rates, and terms depend on full underwriting by the "
    "funding provider. HowToFund is a broker service, not a lender."
)


def _estimate_range(product, monthly_revenue):
    low = int(product["revenue_multiple_low"] * monthly_revenue)
    high = int(product["revenue_multiple_high"] * monthly_revenue)
    low = max(low, product["typical_amount_min"])
    high = min(high, product["typical_amount_max"])
    if low > high:
        low = high = product["typical_amount_min"]
    # Round to nearest thousand for readability
    low = (low // 1000) * 1000
    high = (high // 1000) * 1000
    return low, high


def _check_eligibility(product, profile):
    """Returns (eligible: bool, failed_criteria: list of str)."""
    failed = []
    tib = profile.get("time_in_business_months", 0) or 0
    rev = profile.get("monthly_revenue", 0) or 0
    credit = profile.get("credit_score")  # may be None

    if tib < product["min_tib_months"]:
        failed.append(
            f"needs {product['min_tib_months']}+ months in business (has {tib})"
        )
    if rev < product["min_monthly_revenue"]:
        failed.append(
            f"needs ${product['min_monthly_revenue']:,}+ monthly revenue (has ${rev:,})"
        )
    if credit is not None and credit < product["min_credit_score"]:
        failed.append(
            f"needs {product['min_credit_score']}+ credit score (has {credit})"
        )
    return (len(failed) == 0, failed)


def _fit_score(product, profile):
    """Heuristic fit score: use-of-funds keywords + urgency vs funding speed."""
    score = 50  # base
    use = (profile.get("use_of_funds") or "").lower()
    urgency = (profile.get("urgency") or "exploring").lower()

    for keyword, product_ids in USE_OF_FUNDS_MAP.items():
        if keyword in use and product["id"] in product_ids:
            # Earlier-listed products in the keyword map are stronger fits
            score += 30 - (10 * product_ids.index(product["id"]))

    if urgency in ("asap", "urgent", "immediately"):
        if product["id"] in FAST_PRODUCTS:
            score += 20
        if product["id"] in SLOW_PRODUCTS:
            score -= 25
    elif urgency in ("exploring", "planning"):
        if product["id"] in SLOW_PRODUCTS:
            score += 10  # time to do it right

    return score


def prequalify(profile):
    matches = []
    near_misses = []

    for product in PRODUCTS:
        eligible, failed = _check_eligibility(product, profile)
        if eligible:
            low, high = _estimate_range(product, profile.get("monthly_revenue", 0) or 0)
            matches.append(
                {
                    "product_id": product["id"],
                    "product_name": product["name"],
                    "tagline": product["tagline"],
                    "illustrative_range": {"low": low, "high": high},
                    "funding_speed": product["funding_speed"],
                    "fit_score": _fit_score(product, profile),
                    "why": product["best_for"][:3],
                }
            )
        else:
            # Near-miss: only one failed criterion and it's close
            if len(failed) == 1:
                near_misses.append(
                    {
                        "product_id": product["id"],
                        "product_name": product["name"],
                        "blocked_by": failed[0],
                        "tagline": product["tagline"],
                    }
                )

    matches.sort(key=lambda m: m["fit_score"], reverse=True)
    return {
        "matches": matches,
        "near_misses": near_misses,
        "match_count": len(matches),
        "disclaimer": DISCLAIMER,
    }
