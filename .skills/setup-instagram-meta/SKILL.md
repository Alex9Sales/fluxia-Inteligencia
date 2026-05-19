---
name: setup-instagram-meta
description: Configure Instagram Business publishing and comment-access foundations through Meta Graph API for OpenClaw-based workflows. Use when connecting an Instagram professional account for the first time, validating Meta credentials, retrieving page and Instagram business IDs, testing tokens, or preparing secure publication access for Fluxia/Friday operations.
---

# Setup Instagram Meta

Configure the Meta-side foundation required for Instagram automation in a controlled way.

Use this skill to guide setup, validate credentials, and prepare safe publication access. Do not use it to plan content strategy or run the day-to-day Instagram operation.

## Goal

Finish with:
- Instagram professional account confirmed
- Facebook page linkage confirmed
- valid access token tested
- page ID identified
- Instagram business account ID identified
- credentials saved in a controlled local path
- publication connectivity tested

## Workflow

### 1. Confirm prerequisites

Ask the user to confirm all of these before proceeding:
- Instagram account is Professional (Business or Creator)
- Instagram is linked to a Facebook Page
- user has access to the Facebook account that manages that page
- user understands the access token is sensitive

If any item is missing, stop and resolve that first.

### 2. Guide Meta Developer access

Direct the user to:
- `https://developers.facebook.com`
- `https://developers.facebook.com/tools/explorer`

Use plain, stepwise guidance. Ask for confirmation after each major milestone.

### 3. Collect the minimum required permissions

Guide the user to request at least:
- `instagram_basic`
- `instagram_content_publish`
- `pages_read_engagement`

If the intended operation later includes comment management, note that additional permissions may be required and should be handled separately.

### 4. Validate the token immediately

When the user provides a token, validate it right away with a read-only call before using it for anything else.

Preferred check:
- list pages available to the token
- inspect whether each page has an `instagram_business_account`

If validation fails:
- explain the likely cause
- direct the user back to the permission/token step
- do not continue with invalid credentials

### 5. Identify target page and Instagram business ID

Show returned accounts in a human-readable way.

For each available page, present:
- page name
- page ID
- whether an Instagram business account is linked
- Instagram business account ID when available

Ask the user to confirm which page/account should be used.

### 6. Save credentials safely

Do not default to dumping secrets into arbitrary project paths.

Preferred storage strategy:
- save under a clearly named local folder controlled by the user or project
- use a `.env` file only when that is already the accepted pattern in the target project
- keep filenames and location explicit
- remind the user that tokens are sensitive and may expire

Minimum variables to save:
- `INSTAGRAM_BUSINESS_ID`
- `FACEBOOK_PAGE_ID`
- `INSTAGRAM_ACCESS_TOKEN`
- `META_API_VERSION`

### 7. Install or prepare helper script

If helper scripts are needed, use bundled scripts from this skill rather than generating ad hoc broken scripts in chat.

Use `scripts/meta_token_check.py` for validation-oriented checks.

If future publication automation is needed, note that a separate operator skill or publication script should handle posting.

### 8. Test final connectivity

Run a safe read-only test against the confirmed Instagram business account.

Success condition:
- account id returned
- username returned when available
- no OAuth or permission error

### 9. Close with a clear summary

Summarize:
- which account was connected
- where credentials were saved
- what was validated successfully
- what still remains before automated publication can happen

## Security rules

- Treat access tokens as secrets.
- Prefer short-lived validation followed by a safer storage decision.
- Do not paste tokens into long-lived docs or tracked files.
- Do not commit `.env` files containing live tokens.
- If a token was exposed in chat, recommend rotation.

## Error handling

Common failures to explain clearly:
- invalid token
- missing permission
- Instagram account is not professional
- page not linked to Instagram
- page selected instead of user context, or vice versa

When errors happen, explain the fix path in plain language instead of just repeating raw API output.

## Resources

### scripts/
- `meta_token_check.py` — validate token, list pages, and surface linked Instagram business accounts cleanly

### references/
- `meta-setup-notes.md` — checklist, permission notes, and storage guidance for setup sessions
