# Meta setup notes

## Minimum setup checklist
- Instagram account is Professional
- Facebook Page is linked to Instagram
- correct Facebook account has admin access to the Page
- Meta Developers access works
- Graph API Explorer is reachable

## Minimum permissions for initial publishing foundation
- instagram_basic
- instagram_content_publish
- pages_read_engagement

## Notes
- Some operations, especially comment handling, may need additional permissions later.
- Tokens from Graph API Explorer are often short-lived.
- For production use, plan token renewal or long-lived token flow.
- Do not commit live tokens to git.

## Suggested storage guidance
Use one of these patterns:
1. project-local untracked `.env`
2. dedicated local secrets folder outside versioned repo
3. runtime config/secret manager when available

## Recommended confirmation output
At the end of setup, confirm:
- selected Facebook page
- selected Instagram business account
- username when available
- where credentials were stored
- whether read-only validation succeeded
- what remains before posting automation
