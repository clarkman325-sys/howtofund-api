"""
HowToFund API — the service behind the HowToFund Muse connector.

Endpoints:
  GET  /                    service info
  GET  /health              health check
  GET  /products            full funding-vertical catalog
  GET  /products/{id}       one vertical, in detail
  POST /prequalify          match a borrower profile to products (LendingTree-style)
  POST /request-callback    capture a lead for Isaiah to call back

"You bring the API — Muse brings the agent."
"""

import json
import uuid
from datetime import datetime, timezone
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field

from products import PRODUCTS
from matcher import prequalify, DISCLAIMER

app = FastAPI(
    title="HowToFund API",
    description=(
        "Business funding pre-qualification across every major lending vertical. "
        "Estimates are illustrative, not offers. HowToFund is a broker service, not a lender."
    ),
    version="0.1.0",
)

LEADS_DIR = Path(__file__).parent / "leads"
LEADS_DIR.mkdir(exist_ok=True)


class PrequalRequest(BaseModel):
    monthly_revenue: float = Field(..., gt=0, description="Average monthly business revenue, USD")
    time_in_business_months: int = Field(..., ge=0, description="Months the business has operated")
    credit_score: int | None = Field(None, ge=300, le=850, description="Owner's credit score, if known")
    industry: str | None = Field(None, description="e.g. restaurant, trucking, HVAC, retail")
    use_of_funds: str | None = Field(None, description="What the funding is for, in plain words")
    urgency: str | None = Field(
        None, description="asap | week | month | exploring"
    )
    equipment_value: float | None = Field(None, description="Value of owned equipment (for leaseback)")
    monthly_invoiced: float | None = Field(None, description="Monthly B2B invoicing (for factoring)")


class CallbackRequest(BaseModel):
    name: str
    phone: str | None = None
    email: str | None = None
    best_time: str | None = None
    note: str | None = None


@app.get("/")
def index():
    return {
        "service": "HowToFund API",
        "tagline": "Know how you're getting funded — before you apply.",
        "endpoints": ["/products", "/prequalify", "/request-callback"],
        "disclaimer": DISCLAIMER,
    }


@app.get("/health")
def health():
    return {"status": "ok", "time": datetime.now(timezone.utc).isoformat()}


@app.get("/products")
def list_products():
    return {"count": len(PRODUCTS), "products": PRODUCTS, "disclaimer": DISCLAIMER}


@app.get("/products/{product_id}")
def get_product(product_id: str):
    for p in PRODUCTS:
        if p["id"] == product_id:
            return {**p, "disclaimer": DISCLAIMER}
    raise HTTPException(status_code=404, detail=f"Unknown product '{product_id}'")


@app.post("/prequalify")
def prequalify_borrower(req: PrequalRequest):
    result = prequalify(req.model_dump())
    return JSONResponse(
        {
            **result,
            "profile_summary": {
                "monthly_revenue": req.monthly_revenue,
                "time_in_business_months": req.time_in_business_months,
                "credit_score": req.credit_score,
                "industry": req.industry,
                "use_of_funds": req.use_of_funds,
                "urgency": req.urgency,
            },
        }
    )


@app.post("/request-callback")
def request_callback(req: CallbackRequest):
    if not req.phone and not req.email:
        raise HTTPException(
            status_code=422, detail="Provide at least a phone number or an email."
        )
    lead = {
        "id": str(uuid.uuid4())[:8],
        "created_at": datetime.now(timezone.utc).isoformat(),
        **req.model_dump(),
        "status": "new",
    }
    path = LEADS_DIR / f"{lead['id']}.json"
    path.write_text(json.dumps(lead, indent=2))
    return {
        "ok": True,
        "lead_id": lead["id"],
        "message": (
            "Thanks — your request is in. Isaiah (HowToFund) will reach out personally, "
            "usually within one business day."
        ),
    }
