# Primo documentation context

Primo is a Svelte 5 CMS backed by PocketBase. Developers define blocks and fields; content editors use those fields and configured page layouts. Follow `AGENTS.md` for documentation style and Mintlify components.

## Verify product behavior

Check documentation against the versioned CMS, CLI, and MCP source. The October 14, 2026 publication review uses CMS v3.3.1, CLI 0.2.1, and MCP 0.1.10. Uncommitted implementation changes are not evidence of released behavior.

- Hosted content is stored in PocketBase. `primo pull` exports Svelte and YAML files; `primo push` imports them as a draft by default. CLI 0.2.1 adds `primo publish`, `primo push --publish`, and `primo status --hosted` for servers that support the publication API.
- Sites can be created before assigning a domain. A homepage is the root page; nested page URLs follow page slugs and ancestry.
- Library blocks are copied into independent site blocks. Library edits do not update existing site copies.
- Page types define fields, available blocks, and header/body/footer templates. Header/footer content is shared across pages of that type. Body defaults are copied when a page is created.
- Editors can edit shared slot content but cannot change its structure. An empty available-block list fixes the body layout.
- Form dialogs require Save. Inline editing and page layout actions save automatically. Publish updates the whole site.
- Field keys become component props in the browser compiler. Use runes, not legacy `export let` or `$:`. If you declare `$props()` yourself, declare every field you use.
- Field defaults are content values, not `default` or `required` schema properties. Info fields provide guidance; condition rules affect the form, not rendered output.
- Markdown field values are resolved to HTML by the CMS. Render trusted content with `{@html}`; do not assume sanitization.
- Site Field and Page Field references connect content explicitly. Page List returns all pages of its configured type.
- Head fragments contain markup with bare field names, without their own `<svelte:head>` wrapper. Put titles in page type heads. Footer files use `foot.html` and contain static HTML.
- CLI 0.2.1 static builds supply field props, resolve CMS field references and rich content, hydrate interactive blocks, and include both site and page type footers. Older 0.2.0 builds have the documented limitations. Static output has no CMS and expects root-relative URLs at the hostname root.
- Use Node.js 22.13 or a newer supported LTS release for the CLI; its current interactive dependencies fail on Node 18.
- Use persistent storage for the CMS and test backups. Files exported with the CLI do not include user accounts or server settings.
- SMTP is optional for generated invitation links and required for sending invitations from Primo. Initial `PRIMO_USER_*` accounts are server developers.

## Page structure

Start documentation pages with YAML `title` and `description`; use H2 for the first content heading. Snippet fragments are not standalone documentation pages. Keep terminology consistent: blocks, page types, slots, fields, content editors, and the block library.

# Mintlify documentation

## Working relationship
- You can push back on ideas-this can lead to better documentation. Cite sources and explain your reasoning when you do so
- ALWAYS ask for clarification rather than making assumptions
- NEVER lie, guess, or make up anything

## Project context
- Format: MDX files with YAML frontmatter
- Config: docs.json for navigation, theme, settings
- Components: Mintlify components

## Content strategy
- Document just enough for user success - not too much, not too little
- Prioritize accuracy and usability
- Make content evergreen when possible
- Search for existing content before adding anything new. Avoid duplication unless it is done for a strategic reason
- Check existing patterns for consistency
- Start by making the smallest reasonable changes

## docs.json

- Refer to the [docs.json schema](https://mintlify.com/docs.json) when building the docs.json file and site navigation

## Frontmatter requirements for pages
- title: Clear, descriptive page title
- description: Concise summary for SEO/navigation

## Writing standards
- Second-person voice ("you")
- Prerequisites at start of procedural content
- Test all code examples before publishing
- Match style and formatting of existing pages
- Include both basic and advanced use cases
- Language tags on all code blocks
- Alt text on all images
- Relative paths for internal links

## Git workflow
- NEVER use --no-verify when committing
- Ask how to handle uncommitted changes before starting
- Create a new branch when no clear branch exists for changes
- Commit frequently throughout development
- NEVER skip or disable pre-commit hooks

## Do not
- Skip frontmatter on standalone MDX documentation pages
- Use absolute URLs for internal links
- Include untested code examples
- Make assumptions - always ask for clarification
