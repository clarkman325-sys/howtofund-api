/**
 * HowToFund Leads webhook.
 *
 * 1. Go to script.google.com -> New project.
 * 2. Delete the placeholder code and paste this entire file.
 * 3. Save, then Deploy -> New deployment -> Web app.
 *    - Execute as: Me
 *    - Who has access: Anyone
 * 4. Deploy, authorize, and copy the Web app URL.
 * 5. In the Render dashboard (howtofund-api -> Environment), add:
 *      LEADS_WEBHOOK_URL = <the web app URL>
 *
 * Every POST from the API's /request-callback endpoint appends one row
 * to the "HowToFund Leads" spreadsheet.
 */

const SHEET_ID = "1RBCKsaR9pAyJppC1W6L2dL-DcAaRhPIee0baZAcRfsE";
const SHEET_NAME = "Sheet1";

function doPost(e) {
  try {
    const lead = JSON.parse(e.postData.contents);
    const sheet = SpreadsheetApp.openById(SHEET_ID).getSheetByName(SHEET_NAME);
    sheet.appendRow([
      lead.created_at || new Date().toISOString(),
      lead.id || "",
      lead.name || "",
      lead.phone || "",
      lead.email || "",
      lead.business_name || "",
      lead.product_id || "",
      lead.best_time || "",
      lead.note || "",
      lead.status || "new",
    ]);
    return ContentService.createTextOutput(JSON.stringify({ ok: true }))
      .setMimeType(ContentService.MimeType.JSON);
  } catch (err) {
    return ContentService.createTextOutput(
      JSON.stringify({ ok: false, error: String(err) })
    ).setMimeType(ContentService.MimeType.JSON);
  }
}
