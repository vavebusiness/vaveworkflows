# Private-data warning and deployment design

This version is a static web app. It uses local browser storage. It has **no authentication, database API, server-side permission checks or connected Gumroad/Make/Gmail accounts**.

## Safe use now
- Run on localhost.
- Add only public research and non-sensitive planning notes.
- Export encrypted backups through your own protected storage if they include business data.
- Do not publish JSON backups, passwords, API keys or private CRM records to GitHub Pages.

## How to become a real team HQ
1. Add SSO or secured passwordless login.
2. Use private hosted Postgres/Supabase/Firebase with row-level access rules.
3. Move editable records to server endpoints with validation and audit logs.
4. Keep API keys only on server; use OAuth for Make/Gumroad/Google where supported.
5. Add real-time connector reads and explicit write confirmations.
6. Establish data retention, consent/opt-out, backup and role policy.

## Supported locally
- Editable CRM records, release gates and campaigns.
- Search, filters, tabs, priority board, analytics based on stored rows.
- JSON backup/restore and per-table CSV import/export.

## Not supported yet
- A live synced database between devices.
- Automatic Gmail outreach, newsletters, Gumroad purchases or Make execution.
- Remote hosting with private identity/CRM security.