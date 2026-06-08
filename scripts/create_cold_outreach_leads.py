#!/usr/bin/env python3
"""Create a cold-outreach seed database for incubated businesses.

The workbook is intentionally capped at 100 leads per business so the list can
be grown over time without becoming unmanageable during validation.
"""
from __future__ import annotations

import csv
import html
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

MAX_EMAILS_PER_BUSINESS = 100
DATE_ADDED = datetime.now(timezone.utc).date().isoformat()
OUT_DIR = Path("output/cold_mailing")
CSV_PATH = OUT_DIR / "cold_mailing_leads_seed.csv"
XLSX_PATH = OUT_DIR / "cold_mailing_leads_seed.xlsx"
README_PATH = OUT_DIR / "README.md"

BUSINESS_OFFERS = {
    "hvac-missed-call-recovery": "Missed-call recovery + emergency lead triage for HVAC companies",
    "property-maintenance-triage": "Tenant maintenance request triage for property managers",
    "construction-bid-inbox": "Bid inbox triage and deadline/risk detection for construction contractors",
    "dental-insurance-checklist": "Dental insurance verification checklist and pre-appointment QA",
    "msp-security-reporting": "Security reporting assistant for managed service providers",
    "med-spa-lead-recovery": "Med spa lead recovery from forms, calls, SMS, and DMs",
    "law-firm-intake-triage": "Legal intake triage and case-fit summary for small law firms",
    "chiropractic-reactivation-engine": "Inactive patient reactivation workflow for chiropractic clinics",
    "restaurant-catering-followup": "Catering inquiry follow-up and event-value tracking for restaurants",
    "b2b-podcast-repurposing-system": "Podcast-to-content repurposing workflow for B2B teams",
}

ROWS = [
    # HVAC
    {"business_slug":"hvac-missed-call-recovery","prospect_company":"HVAC USA","email":"sales@hvacusa.com","source_url":"https://www.hvacusa.com/contactus","source_note":"Public contact page/search result","city_state_country":"USA","confidence":"medium","priority":"P2"},
    {"business_slug":"hvac-missed-call-recovery","prospect_company":"Avatex Service Company","email":"avatexheatandac@gmail.com","source_url":"https://www.avatexservicecompany.com/contact-us/","source_note":"Public contact page/search result","city_state_country":"Houston, TX, USA","confidence":"high","priority":"P1"},
    {"business_slug":"hvac-missed-call-recovery","prospect_company":"Mr Good Guy HVAC","email":"mrgoodguyhvac@gmail.com","source_url":"https://mrgoodguyhvac.com/contact-us/","source_note":"Public contact page/search result","city_state_country":"USA","confidence":"high","priority":"P1"},
    {"business_slug":"hvac-missed-call-recovery","prospect_company":"Balanced Air Heating & Cooling","email":"balancedairhvac@gmail.com","source_url":"https://balancedairhvac.com/contact/","source_note":"Public contact page/search result","city_state_country":"Cleveland, OH, USA","confidence":"high","priority":"P1"},
    {"business_slug":"hvac-missed-call-recovery","prospect_company":"Always Cool Air and Heat LLC","email":"alwayscoolairandheatllc@gmail.com","source_url":"https://www.facebook.com/groups/729884078932539/posts/1175030931084516/","source_note":"Public social/search result; verify before sending","city_state_country":"USA","confidence":"medium","priority":"P2"},
    {"business_slug":"hvac-missed-call-recovery","prospect_company":"A-Advanced Home Services","email":"aadvancedhomeservices@gmail.com","source_url":"https://www.a-advanced.com/contact/","source_note":"Public contact page/search result","city_state_country":"Mineral, VA, USA","confidence":"high","priority":"P1"},
    {"business_slug":"hvac-missed-call-recovery","prospect_company":"100% Service HVAC","email":"100servicehvac@gmail.com","source_url":"https://100percentservicehvac.com/accessibility-statement/","source_note":"Public site accessibility/contact info","city_state_country":"Colorado, USA","confidence":"medium","priority":"P2"},
    {"business_slug":"hvac-missed-call-recovery","prospect_company":"WeatherGuard HVAC","email":"goweatherguardhvac@gmail.com","source_url":"https://www.weatherguardhvac.com/contact","source_note":"Public contact page/search result","city_state_country":"USA","confidence":"high","priority":"P1"},

    # Property management
    {"business_slug":"property-maintenance-triage","prospect_company":"Madison Property Management","email":"mpm@madisonproperty.com","source_url":"https://www.madisonproperty.com/contact","source_note":"Search result listed email; contact page has maintenance flow","city_state_country":"Madison, WI, USA","confidence":"medium","priority":"P1"},
    {"business_slug":"property-maintenance-triage","prospect_company":"TGN Property Management","email":"leasing.in.california@gmail.com","source_url":"https://www.tgnpropertymanagement.com/contact-us","source_note":"Public contact page/search result","city_state_country":"Los Angeles, CA, USA","confidence":"medium","priority":"P2"},
    {"business_slug":"property-maintenance-triage","prospect_company":"PMI SoJay Property Management","email":"sojaypropertymanager@gmail.com","source_url":"https://www.pmisojay.com/contact","source_note":"Public contact page/search result","city_state_country":"Swedesboro, NJ, USA","confidence":"high","priority":"P1"},
    {"business_slug":"property-maintenance-triage","prospect_company":"Century 21 1st Choice Realty / Property Management","email":"stormyc21@gmail.com","source_url":"https://www.suu.edu/housing/property-management-companies.html","source_note":"Public university housing vendor list/search result","city_state_country":"Cedar City, UT, USA","confidence":"medium","priority":"P2"},
    {"business_slug":"property-maintenance-triage","prospect_company":"Providence Property Management","email":"providencepmnwa@gmail.com","source_url":"https://www.providencepropertymgmt.com/contact","source_note":"Public contact page/search result","city_state_country":"Fayetteville, AR, USA","confidence":"high","priority":"P1"},
    {"business_slug":"property-maintenance-triage","prospect_company":"Real Property Management Colorado","email":"realpropcoloradocos@gmail.com","source_url":"https://www.allbusiness.com/company-profile/real-property-management-colorado","source_note":"Public company profile/search result","city_state_country":"Colorado Springs, CO, USA","confidence":"medium","priority":"P2"},
    {"business_slug":"property-maintenance-triage","prospect_company":"The Property Management Company of Jacksonville","email":"jacksonvillepropertymanager@gmail.com","source_url":"https://www.tpmcjax.com/contact-us","source_note":"Public contact page/search result","city_state_country":"Jacksonville, FL, USA","confidence":"high","priority":"P1"},
    {"business_slug":"property-maintenance-triage","prospect_company":"Quechee Lakes Rentals","email":"quecheelakerentals@gmail.com","source_url":"https://advancement.dartmouth.org/s/1353/images/gid2/editor_documents/real_estate_and_rentals.pdf","source_note":"Public rental/vendor PDF search result; verify before sending","city_state_country":"VT, USA","confidence":"medium","priority":"P3"},

    # Construction
    {"business_slug":"construction-bid-inbox","prospect_company":"Hazard Construction","email":"estimating@hazardconstruction.com","source_url":"https://hazardconstruction.com/bidding-subcontractor/","source_note":"Public bidding/subcontractor page/search result","city_state_country":"USA","confidence":"high","priority":"P1"},
    {"business_slug":"construction-bid-inbox","prospect_company":"Anvil Builders","email":"estimating@anvilbuilders.com","source_url":"http://www.sbeinc.com/files/PDFNewsletter/01-02-2025%20SBE%20Weekly%20Newspaper.pdf","source_note":"Public bid newspaper/PDF search result; verify before sending","city_state_country":"USA","confidence":"medium","priority":"P2"},
    {"business_slug":"construction-bid-inbox","prospect_company":"Thomas Construction Group","email":"estimating@thomasconstructiongroup.com","source_url":"https://greaterdiversity.com/wp-content/uploads/Classifieds-02-22-2024-Final.pdf","source_note":"Public advertisement-for-bids PDF search result; verify before sending","city_state_country":"USA","confidence":"medium","priority":"P2"},

    # Dental
    {"business_slug":"dental-insurance-checklist","prospect_company":"S.A.H. Dentistry","email":"info@sahandwdentistry.com","source_url":"https://www.sahandwdentistry.com/office","source_note":"Public dental office page/search result","city_state_country":"Port St. Lucie, FL, USA","confidence":"high","priority":"P1"},
    {"business_slug":"dental-insurance-checklist","prospect_company":"Smile 101","email":"dentalsmile4250@gmail.com","source_url":"https://www.smile101.com/contact/","source_note":"Public contact page/search result","city_state_country":"USA","confidence":"high","priority":"P1"},
    {"business_slug":"dental-insurance-checklist","prospect_company":"Clarity Dental DMV","email":"info.claritydentaldmv@gmail.com","source_url":"https://www.claritydentaldmv.com/contact/","source_note":"Public contact page/search result","city_state_country":"Vienna, VA, USA","confidence":"high","priority":"P1"},
    {"business_slug":"dental-insurance-checklist","prospect_company":"Southern Pines Dentistry","email":"sopinesdental@gmail.com","source_url":"https://southernpinesdentistry.com/contact-us/","source_note":"Public contact page/search result","city_state_country":"Southern Pines, NC, USA","confidence":"high","priority":"P1"},
    {"business_slug":"dental-insurance-checklist","prospect_company":"Bellevue Premier Dental","email":"bellevuepremierdental@gmail.com","source_url":"https://www.bellevuepremierdental.com/contact/","source_note":"Public contact page/search result","city_state_country":"Bellevue, WA, USA","confidence":"high","priority":"P1"},

    # MSP
    {"business_slug":"msp-security-reporting","prospect_company":"MSPNetworks","email":"sales@mspnetworks.com","source_url":"https://mspnetworks.com/contact","source_note":"Public contact page/search result","city_state_country":"NY, USA","confidence":"high","priority":"P1"},
    {"business_slug":"msp-security-reporting","prospect_company":"WYRE Technology","email":"solutions@wyretechnology.com","source_url":"https://wyretechnology.com/what-is-an-msp-2024/","source_note":"Public site/search result","city_state_country":"Chattanooga, TN, USA","confidence":"medium","priority":"P2"},
    {"business_slug":"msp-security-reporting","prospect_company":"Exact IT Consulting","email":"support@exactitconsulting.com","source_url":"https://exactitconsulting.com/battle-benefits-house-vs-managed-it/","source_note":"Public site/search result","city_state_country":"Lexington, KY, USA","confidence":"medium","priority":"P2"},
    {"business_slug":"msp-security-reporting","prospect_company":"CIT Solutions","email":"info@citsolutions.net","source_url":"https://www.citsolutions.net/solutions/managed-services/","source_note":"Public managed services page/search result","city_state_country":"Minneapolis/St. Paul, MN, USA","confidence":"high","priority":"P1"},
    {"business_slug":"msp-security-reporting","prospect_company":"Dog Bytes Computers","email":"dogbytescomputers@gmail.com","source_url":"https://dog-bytes.com/managed-it-services.html","source_note":"Public managed IT page/search result","city_state_country":"USA","confidence":"high","priority":"P1"},
    {"business_slug":"msp-security-reporting","prospect_company":"24/7 Tech On Call","email":"365techoncall@gmail.com","source_url":"https://24x7techoncall.com/contact","source_note":"Public contact page/search result","city_state_country":"USA","confidence":"high","priority":"P1"},
    {"business_slug":"msp-security-reporting","prospect_company":"TAC Group","email":"info@thetacgroup.com","source_url":"https://www.instagram.com/p/DE75zF3B-EY/","source_note":"Public social/search result; verify before sending","city_state_country":"USA","confidence":"medium","priority":"P3"},
    {"business_slug":"msp-security-reporting","prospect_company":"powersolution.com","email":"moreinfo@powersolution.com","source_url":"https://www.facebook.com/powersolutiondotcom/photos/still-sharing-the-password-for-info-or-support-that-could-be-costing-your-busine/1674196687605625/","source_note":"Public social/search result; verify before sending","city_state_country":"NJ, USA","confidence":"medium","priority":"P3"},

    # Med spa
    {"business_slug":"med-spa-lead-recovery","prospect_company":"Muse Medspa","email":"medspamuse@gmail.com","source_url":"https://www.musemedspausa.com/contact/","source_note":"Public contact page extracted","city_state_country":"Bala Cynwyd, PA, USA","confidence":"high","priority":"P1"},
    {"business_slug":"med-spa-lead-recovery","prospect_company":"Victoria Heavenly Spa","email":"victoriaheavenlyspa@gmail.com","source_url":"https://www.victoriaheavenlyspa.com/contact/contact-victoria-heavenly-spa-houston-premier-medspa/","source_note":"Public contact page/search result","city_state_country":"Houston, TX, USA","confidence":"high","priority":"P1"},
    {"business_slug":"med-spa-lead-recovery","prospect_company":"Swift Injections","email":"swiftinjectionsbycorrine@gmail.com","source_url":"https://www.swiftinjections.com/contact","source_note":"Public contact page/search result","city_state_country":"Houston, TX, USA","confidence":"high","priority":"P1"},
    {"business_slug":"med-spa-lead-recovery","prospect_company":"MedSpa At Villagio","email":"medspaatvillagio@gmail.com","source_url":"https://medspaatvillagio.com/","source_note":"Public site/search result","city_state_country":"Katy, TX, USA","confidence":"high","priority":"P1"},
    {"business_slug":"med-spa-lead-recovery","prospect_company":"Renew Society Medspa","email":"contact.renewsociety@gmail.com","source_url":"https://www.facebook.com/p/Renew-Society-Medspa-100083657066508/","source_note":"Public social/search result; verify before sending","city_state_country":"Richardson, TX, USA","confidence":"medium","priority":"P2"},
    {"business_slug":"med-spa-lead-recovery","prospect_company":"Studio N MedSpa","email":"studio.n.inc@gmail.com","source_url":"https://www.studionphilly.com/contact","source_note":"Public contact/careers page/search result","city_state_country":"Philadelphia, PA, USA","confidence":"medium","priority":"P2"},
    {"business_slug":"med-spa-lead-recovery","prospect_company":"AVOUS Medspa & Wellness","email":"avousmedspa@gmail.com","source_url":"https://avousmedspa.com/contact/","source_note":"Public contact page/search result","city_state_country":"Fort Myers, FL, USA","confidence":"high","priority":"P1"},
    {"business_slug":"med-spa-lead-recovery","prospect_company":"Flow IV Medspa","email":"flowivmedspa@gmail.com","source_url":"https://www.flowivmedspa.com/contact","source_note":"Public contact page/search result","city_state_country":"Santa Rosa, CA, USA","confidence":"high","priority":"P1"},

    # Law
    {"business_slug":"law-firm-intake-triage","prospect_company":"Law Office of Steven Wittekiend","email":"swittlaw@gmail.com","source_url":"https://www.swittlaw.com/","source_note":"Public law firm site/search result","city_state_country":"Burnet, TX, USA","confidence":"high","priority":"P1"},
    {"business_slug":"law-firm-intake-triage","prospect_company":"Blake Law Office","email":"blakelawinfo@gmail.com","source_url":"https://theblakelaw.com/contact-us/","source_note":"Public contact page/search result","city_state_country":"Galesburg, IL, USA","confidence":"high","priority":"P1"},
    {"business_slug":"law-firm-intake-triage","prospect_company":"Park Law Office","email":"parklawoffice2006@gmail.com","source_url":"https://www.shonaparklawoffice.com/","source_note":"Public law firm site/search result","city_state_country":"Greenup, IL, USA","confidence":"high","priority":"P1"},
    {"business_slug":"law-firm-intake-triage","prospect_company":"Law Office of Frank Huerta Jr.","email":"fhjrlaw@gmail.com","source_url":"https://www.frankhuertalaw.com/sitemap/","source_note":"Public law firm site/search result","city_state_country":"Fresno, CA, USA","confidence":"high","priority":"P1"},
    {"business_slug":"law-firm-intake-triage","prospect_company":"Stockman Law Office","email":"stockmaninjurylaw@gmail.com","source_url":"https://www.stockmaninjurylaw.com/","source_note":"Public law firm site/search result","city_state_country":"Duluth, MN, USA","confidence":"high","priority":"P1"},

    # Chiropractic
    {"business_slug":"chiropractic-reactivation-engine","prospect_company":"Strickland Chiropractic Clinic","email":"stricklandchiro@gmail.com","source_url":"https://www.stricklandchiropractic.com/contact","source_note":"Public contact page extracted","city_state_country":"Huntsville, AL, USA","confidence":"high","priority":"P1"},
    {"business_slug":"chiropractic-reactivation-engine","prospect_company":"Great America Chiropractic","email":"drlinchiro.pi@gmail.com","source_url":"https://www.greatamericachiro.com/contact-us/","source_note":"Public contact page/search result","city_state_country":"San Jose, CA, USA","confidence":"medium","priority":"P2"},
    {"business_slug":"chiropractic-reactivation-engine","prospect_company":"Core Chiropractic","email":"springsccfrontdesk@gmail.com","source_url":"https://springscorechiro.com/contact-us/","source_note":"Public contact page/search result","city_state_country":"Colorado Springs, CO, USA","confidence":"high","priority":"P1"},
    {"business_slug":"chiropractic-reactivation-engine","prospect_company":"ALIGNance Chiropractic","email":"dr.katiesv@gmail.com","source_url":"https://www.alignancechiro.com/contact","source_note":"Public contact page/search result","city_state_country":"Kansas City, KS, USA","confidence":"high","priority":"P1"},
    {"business_slug":"chiropractic-reactivation-engine","prospect_company":"Seattle Chiropractic Spine & Injury Center","email":"seattlechiropractic@gmail.com","source_url":"https://www.seattlechiropracticspineandinjurycenter.com/contactus","source_note":"Public contact page/search result","city_state_country":"Seattle, WA, USA","confidence":"high","priority":"P1"},
    {"business_slug":"chiropractic-reactivation-engine","prospect_company":"Downtown Louisville Chiropractic & Rehab","email":"downtown.chirorehab@gmail.com","source_url":"https://downtown-louisville-chiropractic.com/contact-us/","source_note":"Public contact page/search result","city_state_country":"Louisville, KY, USA","confidence":"high","priority":"P1"},
    {"business_slug":"chiropractic-reactivation-engine","prospect_company":"Chiropractic Wellness Center","email":"cwcfamilychiro@gmail.com","source_url":"https://www.cwc-familychiro.com/contact","source_note":"Public contact page/search result","city_state_country":"Kansas City, MO, USA","confidence":"high","priority":"P1"},
    {"business_slug":"chiropractic-reactivation-engine","prospect_company":"True Health Chiropractic Clinic","email":"drdominicmeans@gmail.com","source_url":"https://www.siouxfallssdchiropractor.com/contact-us","source_note":"Public contact page/search result","city_state_country":"Sioux Falls, SD, USA","confidence":"high","priority":"P1"},
    {"business_slug":"chiropractic-reactivation-engine","prospect_company":"Grain Valley Chiropractic","email":"grainvalleychiro@gmail.com","source_url":"https://www.gvcchiro.com/contact-us/","source_note":"Public contact page/search result","city_state_country":"Grain Valley, MO, USA","confidence":"high","priority":"P1"},

    # Restaurant catering
    {"business_slug":"restaurant-catering-followup","prospect_company":"The Smith Restaurant","email":"catering@thesmithrestaurant.com","source_url":"https://thesmithrestaurant.com/catering/","source_note":"Public catering page extracted","city_state_country":"NYC / Washington DC / Chicago, USA","confidence":"high","priority":"P1"},
    {"business_slug":"restaurant-catering-followup","prospect_company":"Millersville University Catering Services","email":"catering@millersville.edu","source_url":"https://www.millersville.edu/dining/catering.php","source_note":"Public catering page/search result; not restaurant but useful process example","city_state_country":"Millersville, PA, USA","confidence":"medium","priority":"P3"},
    {"business_slug":"restaurant-catering-followup","prospect_company":"Hot Coals Catering","email":"catering@hotcoals.com.au","source_url":"https://www.instagram.com/p/DYZRCb5ju9j/","source_note":"Public social/search result; non-US, verify before sending","city_state_country":"Australia","confidence":"medium","priority":"P3"},

    # B2B podcast/content
    {"business_slug":"b2b-podcast-repurposing-system","prospect_company":"Speakerbox Media","email":"studio@speakerboxmedia.com","source_url":"https://speakerboxmedia.com/","source_note":"Public site/search result","city_state_country":"Austin, TX, USA","confidence":"high","priority":"P1"},
    {"business_slug":"b2b-podcast-repurposing-system","prospect_company":"Edit My Podcast Agency","email":"unknown@example.invalid","source_url":"https://editmypodcast.agency/","source_note":"Search result mentioned emailing agency but no public email captured; replace after verification","city_state_country":"Unknown","confidence":"needs_email","priority":"P3"},
]

# Remove placeholder invalid emails from final lead rows but keep a gap note in README.
ROWS = [r for r in ROWS if not r["email"].endswith(".invalid")]

COLUMNS = [
    "business_slug", "offer", "prospect_company", "email", "city_state_country",
    "source_url", "source_note", "confidence", "priority", "max_emails_per_business",
    "date_added", "cold_mail_status", "last_contacted_at", "reply_status", "notes",
]

for r in ROWS:
    r["offer"] = BUSINESS_OFFERS[r["business_slug"]]
    r["max_emails_per_business"] = str(MAX_EMAILS_PER_BUSINESS)
    r["date_added"] = DATE_ADDED
    r["cold_mail_status"] = "not_contacted"
    r["last_contacted_at"] = ""
    r["reply_status"] = ""
    r["notes"] = "Publicly listed contact; verify freshness and comply with CAN-SPAM/GDPR before sending."

# Deduplicate by email.
seen = set()
deduped = []
for row in ROWS:
    email = row["email"].lower()
    if email in seen:
        continue
    seen.add(email)
    deduped.append(row)
ROWS = deduped

counts = Counter(r["business_slug"] for r in ROWS)
SUMMARY_COLUMNS = ["business_slug", "current_email_count", "remaining_until_cap", "max_emails_per_business", "offer"]
SUMMARY_ROWS = []
for slug, offer in BUSINESS_OFFERS.items():
    current = counts[slug]
    SUMMARY_ROWS.append({
        "business_slug": slug,
        "current_email_count": current,
        "remaining_until_cap": MAX_EMAILS_PER_BUSINESS - current,
        "max_emails_per_business": MAX_EMAILS_PER_BUSINESS,
        "offer": offer,
    })

RULES_ROWS = [
    {"rule":"cap_per_business", "value": str(MAX_EMAILS_PER_BUSINESS), "notes":"Temporary ceiling requested by Andre to let the database grow without overloading cold outreach."},
    {"rule":"source_quality", "value":"public_contact_only", "notes":"Seed leads come from public websites/search snippets. Avoid private scraping or sensitive data."},
    {"rule":"before_sending", "value":"verify + unsubscribe + identity", "notes":"Verify email freshness, include sender identity/address, reason for contact, and opt-out/unsubscribe path."},
    {"rule":"campaign_mode", "value":"small_batches", "notes":"Send in small batches per business, track replies, and stop targeting segments with poor response or opt-out signals."},
]


def write_csv() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    with CSV_PATH.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNS)
        w.writeheader()
        w.writerows(ROWS)


def col_name(index: int) -> str:
    result = ""
    while index:
        index, rem = divmod(index - 1, 26)
        result = chr(65 + rem) + result
    return result


def sheet_xml(rows: list[dict], columns: list[str]) -> str:
    all_rows = [columns] + [[str(r.get(c, "")) for c in columns] for r in rows]
    xml_rows = []
    for row_idx, row in enumerate(all_rows, start=1):
        cells = []
        for col_idx, value in enumerate(row, start=1):
            ref = f"{col_name(col_idx)}{row_idx}"
            safe = html.escape(str(value), quote=False)
            cells.append(f'<c r="{ref}" t="inlineStr"><is><t>{safe}</t></is></c>')
        xml_rows.append(f'<row r="{row_idx}">{"".join(cells)}</row>')
    return (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" '
        'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">'
        '<sheetViews><sheetView workbookViewId="0"><pane ySplit="1" topLeftCell="A2" activePane="bottomLeft" state="frozen"/></sheetView></sheetViews>'
        '<sheetData>' + ''.join(xml_rows) + '</sheetData>'
        '<autoFilter ref="A1:O1"/>'
        '</worksheet>'
    )


def write_xlsx() -> None:
    sheets = [
        ("Leads", ROWS, COLUMNS),
        ("Resumen", SUMMARY_ROWS, SUMMARY_COLUMNS),
        ("Reglas", RULES_ROWS, ["rule", "value", "notes"]),
    ]
    with ZipFile(XLSX_PATH, "w", ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", """<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>
<Types xmlns=\"http://schemas.openxmlformats.org/package/2006/content-types\">
<Default Extension=\"rels\" ContentType=\"application/vnd.openxmlformats-package.relationships+xml\"/>
<Default Extension=\"xml\" ContentType=\"application/xml\"/>
<Override PartName=\"/xl/workbook.xml\" ContentType=\"application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml\"/>
<Override PartName=\"/xl/worksheets/sheet1.xml\" ContentType=\"application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml\"/>
<Override PartName=\"/xl/worksheets/sheet2.xml\" ContentType=\"application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml\"/>
<Override PartName=\"/xl/worksheets/sheet3.xml\" ContentType=\"application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml\"/>
</Types>""")
        z.writestr("_rels/.rels", """<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>
<Relationships xmlns=\"http://schemas.openxmlformats.org/package/2006/relationships\">
<Relationship Id=\"rId1\" Type=\"http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument\" Target=\"xl/workbook.xml\"/>
</Relationships>""")
        sheet_entries = []
        rel_entries = []
        for idx, (name, rows, cols) in enumerate(sheets, start=1):
            sheet_entries.append(f'<sheet name="{html.escape(name)}" sheetId="{idx}" r:id="rId{idx}"/>')
            rel_entries.append(f'<Relationship Id="rId{idx}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet{idx}.xml"/>')
            z.writestr(f"xl/worksheets/sheet{idx}.xml", sheet_xml(rows, cols))
        z.writestr("xl/workbook.xml", '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"><sheets>' + ''.join(sheet_entries) + '</sheets></workbook>')
        z.writestr("xl/_rels/workbook.xml.rels", '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">' + ''.join(rel_entries) + '</Relationships>')


def write_readme() -> None:
    lines = [
        "# Cold Mailing Leads Seed Database",
        "",
        f"Generated: {DATE_ADDED}",
        "",
        "Files:",
        f"- `{XLSX_PATH.name}` — Excel workbook with `Leads`, `Resumen`, and `Reglas` sheets.",
        f"- `{CSV_PATH.name}` — CSV version for scripts/imports.",
        "",
        f"Temporary cap: **{MAX_EMAILS_PER_BUSINESS} emails per business**.",
        "",
        "## Current counts",
        "",
    ]
    for row in SUMMARY_ROWS:
        lines.append(f"- `{row['business_slug']}`: {row['current_email_count']}/{MAX_EMAILS_PER_BUSINESS}")
    lines += [
        "",
        "## Compliance / hygiene notes",
        "",
        "- Use only public business contact emails or opt-in lead sources.",
        "- Verify each email before sending; several seed rows are from search snippets and should be freshness-checked.",
        "- Include sender identity, business address/contact, and a clear opt-out/unsubscribe line.",
        "- Send small batches and track replies/opt-outs; do not blast all categories at once.",
        "- Remove contacts that bounce, opt out, or are not relevant.",
        "",
        "## Recommended growth loop",
        "",
        "1. Pick one business case.",
        "2. Add 10-20 verified public emails.",
        "3. Run a small cold-mail batch.",
        "4. Track replies and objections.",
        "5. Improve the offer/copy before growing toward the 100-email cap.",
    ]
    README_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    write_csv()
    write_xlsx()
    write_readme()
    print(f"wrote {XLSX_PATH} with {len(ROWS)} leads")
    print(f"wrote {CSV_PATH}")
    print(f"wrote {README_PATH}")
    for row in SUMMARY_ROWS:
        print(f"{row['business_slug']}: {row['current_email_count']}/{MAX_EMAILS_PER_BUSINESS}")


if __name__ == "__main__":
    main()
