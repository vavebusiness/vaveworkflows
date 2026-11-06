# Vave Workflow Store — Midnight HQ v2

This is a **14-page internal operations headquarters (13 original pages + the Partner Launch Pilot)**, built as a self-contained static website. It is not the Gumroad store itself.

## Open it

1. Unzip `Vave_Workflow_Store_HQ_Midnight_v2.zip` into a folder.
2. **For the best experience (Windows):** double-click `START_HQ_WINDOWS.bat`, or run `py HQ_LOCAL_SERVER.py` in the unzipped directory. On macOS/Linux: `python3 HQ_LOCAL_SERVER.py`.
3. Open `http://127.0.0.1:8765/` in your browser.
4. You may also open `index.html` directly for a quick preview, but localStorage behavior can vary when opening `file://` pages; use the local server for reliable cross-page data.

The server binds only to `127.0.0.1` by default, so it is not exposed to your network.

## What is included

| Page | Function |
| --- | --- |
| Command Center | Release/affiliate/client overview, urgent tasks and conversion chain |
| Products & releases | 17 real scenario IDs, editable price/scope and gated release checklist |
| Affiliate program | 28 sourced creator leads, scoring, CRM filters, SOP and economics |
| Vave Dispatch | Seven real prewritten email drafts, welcome automation map, Gumroad plan |
| Partnerships | Referral/white-label/community partner CRM and SOP |
| Client acquisition | Empty truthful client CRM, three offers, outbound system and pipeline charts |
| Marketing | Content calendar, campaign registry and funnel playbook |
| Operations & QA | Release blockers, delivery guidelines, customer support and privacy controls |
| Tasks | 18 seeded tasks, editable kanban board and database |
| Reports | Charts based on *local actual records*, not invented sales |
| Resource library | Prior product, affiliate and support documentation |
| Integration center | Exact boundaries for Make, Gumroad, Google Drive and email |
| Settings | Data export/import, reset, support/store preferences and secure deployment strategy |

### Interactive functions

- Add, view, edit and delete rows in product, affiliate, partner, client, email, task and content databases.
- Search or filter individual tables.
- Search the HQ globally with **Ctrl+K** or **Cmd+K**.
- Export each CRM as CSV; import CSV rows by matching column names.
- Export / import one **JSON backup** of the entire workspace.
- The HQ blocks manually setting a product to **Ready** or **Published** unless its four release-gate flags are checked.
- Responsive layout for phone, tablet and desktop.

## Data and privacy

- All edits save to **localStorage in the current browser**; they do not sync between devices.
- No Make scenarios are executed, no Gumroad products are created, no Gmail messages are sent.
- The product table uses real Make scenario IDs verified on 2 November 2026, all inactive at that time.
- The 28 affiliate rows are **sourced research**, not signed partners, approved payouts, or outreach sent.
- The clients and strategic partners CRMs start empty to avoid fictitious pipeline claims.
- Revenue appears as **unknown/unconnected**, never made-up sales.
- Seeded affiliate sources are sanitized: no email addresses or private customer records are embedded in the source code.
- If you later host the static site on public GitHub Pages, your **client-side JavaScript and seeded research are public**. It is not a secured team CRM. Do not publish private backup exports to the repository. Add authentication + private database before involving staff or sensitive client data.

## Files / structure

```text
Vave_Workflow_Store_HQ/
├── index.html
├── departments/                 # 7 full departments
├── systems/                     # tasks, reports, library, integrations, settings
├── assets/
│   ├── styles.css               # midnight-blue Apple-like design system
│   ├── app.js                   # CRM, navigation, search, data management
│   ├── data.js                  # public-safe seed snapshot
│   └── resources/               # sanitized public reference documents
├── data/                         # readable dataset snapshot (public-safe)
├── docs/                         # SOPs and security guidance
├── HQ_LOCAL_SERVER.py
├── START_HQ_WINDOWS.bat
└── START_HQ_MAC_LINUX.sh
```

## Workflow store vs other project

This HQ is **only for Vave Workflow Store**. It deliberately does not copy the private client/outreach database from the separately operated Vave Automations agency. The linked agency HQ provided the inspiration for department pages, playbook tabs, KPIs and disciplined operating statuses, while the colors and content here are unique to the store.

## Next development stages

1. Owner feedback on design / department order.
2. Decide whether this should be a private hosted app or a public-safe dashboard.
3. Add authenticated multiuser storage and role permissions.
4. Connect Make status read-only, then Gumroad inventory/revenue read-only, after seller authorization.
5. Add deliberate write actions with confirmation and audits.

**Do not publish products based solely on this HQ's local checkboxes.** Real blueprint exports and tests remain separate external evidence.

## Partner Launch Pilot (2 November 2026)

Open `systems/partner-pilot.html` from the navigation. This adds a full v1 partner recruitment and activation plan, interactive model and release checklist. The calculator and checklist save only browser-local assumptions and do **not** update live CRM, Gumroad or Make.

Supporting docs: `docs/PARTNER_PROGRAM_V1.md` and `docs/PARTNER_OUTREACH_AND_ONBOARDING.md`.

## Store-style Product Catalog (November 2026)
- Open `systems/catalog.html` for a Gumroad-like product grid.
- Each card opens `systems/product.html?id=<SKU>` containing detailed inputs, outputs, audiences, setup outline, proposed pricing, scope and release evidence.
- Add/edit future products with the in-browser product editor. Local changes do not update GitHub, Make or Gumroad; export a JSON backup to retain them.
- Data is seeded from `data/product_details.json`, linked to 17 verified development scenario IDs, with planned deliverables clearly labeled as such.
- Public Pages previews MUST only publish the sanitized `public-preview` branch, not the full internal CRM.

## Fifteen draft launch packages (7 November 2026)

Open `systems/launch-packs.html` to view the 15 first-batch dossiers, designs, scopes, proposed prices, affiliate concepts and release blockers. Local package ZIP files were prepared separately for owner delivery; no paid files are hosted in this HQ. All products remain **Packaging / untested**; no Make scenario was executed or activated, and no Gumroad listing was created or published.
