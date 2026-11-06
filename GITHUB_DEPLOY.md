# Vave Workflow Store HQ — GitHub deployment

**Recommended: create a separate PRIVATE GitHub repository named `vave-workflow-store-hq`.** This repository contains internal partner research, launch planning, and CRM seed data, so do not make it public without reviewing every file.

## Deploy code
1. Create the separate repository in the `vavebusiness` GitHub account.
2. Upload the contents of this folder to repository root (not the zip itself).
3. Open `index.html` locally, or start `HQ_LOCAL_SERVER.py` to use the HQ with local browser storage.
4. The repository is storage/version control only. Hosting publicly via GitHub Pages will make site code and data assets public.
5. Before publishing, create a public-safe edition that removes internal partner records, unpublished marketing plans, and other confidential data, or implement real authentication and an access-controlled backend.

## No synchronization
The HQ stores edits in the current browser (`localStorage`). GitHub uploads/commits do not sync edits to devices, Gumroad, Gmail, or Make.

## No credentials
Do not commit `.env`, access tokens, customer contact lists, Gmail exports, or JSON backup files containing personal information.