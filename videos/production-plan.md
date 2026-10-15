# Deployment and domain recordings

The Railway deployment and generated-hostname walkthroughs were recorded on October 11, 2026, against an isolated Primo 3.3.1 service with fictional Garden Studio content. The service deployment is removed after recording. The user approved deletion of its temporary volume, which was removed. Volume removal triggered a fresh deployment, so cleanup also disconnected the image source and removed that deployment. Verify no active deployments and no retained volume after cleanup. The manifest records versions, capture format, and verification results.

- `railway-deployment`: CLI project/service setup, persistent storage, private account variables, pinned image deployment, HTTPS sign-in, saved-content edit, and redeployment. All 37 exported site files matched before and after redeployment.
- `railway-hostname-publishing`: an existing Railway-generated hostname, assignment in Primo, manual connected status, publication, and verification of the homepage, About page, and nested blog URL. Four public HTTPS routes passed.

Both are silent paced captures of actual hosted UI and actual CLI responses, with captions, downloadable tracks, and written steps. Credential entry, fixture import, and deployment waiting are omitted. Custom registrar DNS configuration remains a separate recording that needs an owned domain.

## Future extended Railway recording (3–4 minutes)

**Place:** `reference/deployment.mdx`, below the Railway procedure.

**Prepare:** A Railway account and a disposable project with an agreed spending limit; the Primo deployment template linked in the guide; a fresh browser profile; example email addresses. Enter credentials off camera. Record the Primo version and recording date in `videos/demos/manifest.json`.

1. Explain the outcome: a shared browser editor with persistent storage. Show the deployment template and its repository.
2. Show the service's volume mounted at `/app/pb_data`. Explain that database records, uploads, and saved site data need this disk across deployments.
3. Show the required environment variable names from the deployment guide. Keep their values hidden. Distinguish the PocketBase superuser from the regular Primo user account.
4. Deploy. Cut the waiting period and label the cut. Show healthy logs without credentials or personal information.
5. Generate the CMS hostname, open HTTPS, and sign in off camera. Show the Primo dashboard and create a fictional demo site.
6. Save a visible change, redeploy the same service with the same volume, then show the change still present. This verifies persistence.
7. Show where collaborators enter the CMS and link to the separate publishing/domain guides.

**Verify:** HTTPS loads; the regular user can access the dashboard; the volume survives redeployment; saved content and uploaded demo media remain. Keep written instructions and current variable names alongside the video.

**Captions:** “Deploy the shared CMS”; “Mount persistent storage at /app/pb_data”; “Configure account variables privately”; “Open your CMS over HTTPS”; “Verify saved data after redeployment.”

## Future custom-domain recording (2–3 minutes)

**Place:** `dashboard/connecting-domains.mdx`, after prerequisites.

**Prepare:** A working disposable Primo deployment, an approved demo hostname, access to its DNS zone and hosting/reverse-proxy settings, and a fictional site with a homepage and one nested page. Use a hostname whose existing traffic can safely be redirected. Obtain the actual DNS targets from the host; never substitute invented target values.

1. Show the CMS hostname and public site hostname as two separate addresses.
2. Open the site's dashboard actions and assign its public domain without a scheme or path.
3. Add the same hostname to the hosting service or reverse proxy so requests reach Primo. Show the provider's actual required DNS records.
4. Create those records in the approved demo DNS zone. Keep account details hidden.
5. Cut DNS/certificate waiting periods with an explicit caption. Verify the hostname resolves and serves a valid HTTPS certificate.
6. Return to Primo and choose **Mark as connected**. Explain that this is a manual status flag; it does not create DNS records or prove connectivity.
7. Publish in the editor. Open the public homepage and nested page, then check images and internal links.
8. If showing a wildcard setup, explain that `PRIMO_BASE_DOMAIN` also requires wildcard DNS and TLS. Keep this as a separate advanced segment.

**Verify:** The correct site is served on the intended hostname, HTTPS is valid, publication reaches the public site, and nested URLs/media work. Follow the actual hosting arrangement instead of implying Primo provisions DNS or certificates itself.

**Captions:** “Assign your public site hostname”; “Route the hostname to Primo”; “Copy DNS records from your host”; “Verify DNS and HTTPS”; “Mark the domain connected”; “Publish and check the public site.”

## Existing local walkthroughs

The four additions recorded on October 11 use paced captures of actual Primo screens and actual CLI output, with burned-in instructions, WebVTT captions, posters, and written steps in the demo gallery. They are silent. The manifest records their versions and capture format.

- `start-local`: workspace creation, validation, files mode, and CMS mode.
- `field-references`: Site Field and Page Field targets and the scope of edits.
- `fixed-flexible-layouts`: the last-block confirmation, preserved sections, restored layout controls, and independent post content.
- `cli-sync-recovery`: pull, refused stale push, saved local work, fresh pull, reapplied edit, and successful push. Publishing is a separate hosted-editor step.

For future recordings, replace each complete clip only after checking the UI against the documented release. Retain caption tracks, download fallback links, and written instructions. Never show tokens, passwords, private email addresses, billing information, or unrelated browser tabs.
