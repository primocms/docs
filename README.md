# Primo documentation

This repository contains the Mintlify documentation for Primo. Pages use MDX with YAML frontmatter; `docs.json` defines navigation, redirects, and site settings.

## Preview and validate

Use a supported Node.js LTS release. Install the pinned dependencies and start the preview from this directory:

```bash
npm ci
npm run dev
```

Open the URL printed by Mintlify, usually `http://localhost:3000`.

```bash
npm run check:links
npm run check:a11y
```

The link checker also scans `AGENTS.md`, whose component examples contain illustrative paths such as `/auth` and `/images/dashboard.png`. Treat those separately from links in product documentation. The accessibility checker currently requests an `alt` attribute on `<video>`, although HTML video uses accessible labels, captions, and fallback content rather than image alt text. The demonstration videos provide `aria-label`, burned-in captions, caption files, and download links; review those instead of adding an invalid attribute. The current Mintlify preview removes raw `<track>` elements from MDX video markup. The new walkthroughs therefore also link directly to the caption files and provide a written transcript. The standalone demo gallery retains native caption tracks.

## Maintain accurate documentation

Read `AGENTS.md` before editing. Check product behavior against the CMS, CLI, and MCP implementation for the version being documented. Do not present uncommitted or unreleased implementation changes as released features.

Keep browser, CLI, and deployment instructions consistent, especially source-of-truth modes, push safety, save behavior, and publishing. Test copyable examples and check internal links, media paths, and the rendered preview.

## Publish

If this repository is connected to Mintlify's GitHub integration, pushing to its configured deployment branch publishes documentation changes. Review locally before pushing.

## Audit baseline — October 11, 2026

The documentation audit checked all 37 MDX files, repository guidance, navigation, styles, demo captions, and the demo index against these source versions:

- CMS [v3.3.1](https://github.com/primocms/primo/tree/765db21631535e46b8ac3c456428a6f5d82dbbd4)
- CLI [0.2.0 source](https://github.com/primocms/primo-cli/tree/26043d87f0baa46d3c35318fd591e121ba9ccfe4)
- MCP [0.1.9 source](https://github.com/primocms/mcp/tree/0329f1610011228dca465814ab9ba7957189f592)

Corrections cover field types and defaults, Svelte runes, page URLs, shared slots, library copy behavior, invitations and roles, save/publish behavior, static build limitations, environment variables, persistent storage, backups, and deployment instructions. Empty blog, multi-developer, library, and marketplace guides now contain usable workflows.

A second clarity pass labels custom block, page type, and field names as examples, explains fixed and flexible layouts, shortens repeated guidance, and completes the library-to-site step in the first-site tutorial.

Validation passed for all MDX/frontmatter, 66 Svelte examples compiled with supplied field props, 20 YAML examples, one JSON example, 102 shell examples checked for syntax, the Mintlify configuration schema, all 34 navigation routes in the local preview, 36 internal heading links, and 63 referenced local video assets. The file-authored Hero example passed CLI validation and a static build with an unset image. Site colors meet the checker's contrast thresholds.

The installation page now separates local development from shared CMS deployment. A domain guide covers routing, DNS, HTTPS, the manual connected status, and publication. Four additional silent walkthroughs provide captions and transcripts for local startup, field references, layout controls, and CLI push recovery. They use paced captures of actual UI and CLI output; `videos/demos/manifest.json` records their provenance. The hosted Railway recordings cover deployment, persistence through redeployment, generated-hostname assignment, and publishing. The deployment video is held for later review and omitted from the docs page and demo gallery; the hostname and publishing video remains included. The temporary deployment was removed after recording. A custom registrar-DNS recording still needs an owned domain; its script is in `videos/production-plan.md`.

The two downloadable workspaces are generated from `examples/` with `npm run build:examples`. Both passed CLI 0.2.0 validation; the first-site workspace built four pages. All 20 companion Svelte files compiled for browser and server output, and all 75 YAML files parsed. Browser checks verified shared site references, separate post values, fixed/flexible layout controls, and a refused stale push followed by a fresh pull and successful push. These checks used the published CMS 3.3.1 binary (source commit `4b994903d4297e6e859df094289b1743d9f8dfde`, checksum recorded in the video manifest). Those static-output limitations applied to CLI 0.2.0; the October 14 review below covers the newer release.

The standard link/accessibility commands still report the instructional sample links in `AGENTS.md` and video-alt findings described above. Railway deployment, persistence through redeployment, Railway-provided HTTPS, and public-site publishing were exercised on a disposable instance. SMTP delivery, custom-domain DNS/TLS provisioning, and disaster recovery procedures were checked against source and primary documentation; this audit did not exercise those flows or restore a live production database. Review those workflows on your deployment before relying on them operationally.

## Publication review — October 14, 2026

The final pass checked the released CMS v3.3.1 and the published npm packages `primo-cli` 0.2.1 and `primo-mcp` 0.1.10. The CLI now supports automatic field props, field-reference and rich-content resolution, interactive hydration, and page type footers in static builds. The guides describe this behavior and distinguish older 0.2.0 limitations. Use Node.js 22.13 or a newer supported LTS release: a clean install's interactive dependencies fail on Node 18.

This pass added domain assignment before publication in the quickstart, corrected the initial Nginx/Certbot sequence, kept the VPS backend port on loopback, completed automated account examples, and preserved environment settings in the Docker update command. All 26 video embeds now provide direct caption downloads and written walkthroughs. The Railway deployment video remains omitted from the docs and gallery, and the private Free-plan narration remains outside this repository.

Validation passed for all 37 MDX files, 66 Svelte examples, 20 YAML examples, one JSON example, and 103 shell examples. All 34 navigation routes, 37 internal heading links, 62 referenced assets, and the current Mintlify configuration schema passed. Both downloadable workspaces validate with CLI 0.2.1 and build four pages each; the blog output contains the expected page references, post bodies, and dates. Quote YAML dates to preserve their string type. The ZIPs match their checked-in sources. All 20 included videos decode successfully and have caption files and posters.

Browser checks verified transcript expansion, the quickstart tabs, and the documented accordion's interaction after a CLI static build; both site and page type footer fragments appeared. The standard Mintlify commands retain only the known `AGENTS.md` sample-link findings and invalid video-alt suggestions described above. These are not unresolved product-document links or missing video labels. Custom-domain DNS/TLS provisioning, SMTP delivery, and production disaster recovery were not exercised during this local publication pass.

The live publication check found that this Mintlify deployment serves MP4s and posters but returns 404 for repository ZIP and WebVTT paths. Tutorial downloads and caption links therefore use the committed files on `raw.githubusercontent.com/primocms/docs/main/`. Keep those files in this repository, rebuild the ZIPs after source changes, and verify the live download bytes after publishing. Native video tracks use the same caption URLs with anonymous CORS; written walkthroughs remain available when Mintlify strips track elements.
