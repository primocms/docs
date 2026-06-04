# Primo Documentation Context

## About Primo

Primo is a component-based CMS that streamlines the handoff between developers and content editors.

**Core Value Prop:** "Build with code. Hand off with confidence."

**The Problem Primo Solves:**
Traditional website development creates tension between developers and content editors:
- Developers need code control and modern tooling
- Clients need a simple, visual editing experience
- WordPress lets clients break designs
- Headless CMSs have terrible client UX
- Webflow is expensive and limiting

Primo solves this by coupling code and content in self-contained blocks that live together and can be used and updated visually by non-technical content editors.

## Key Features

1. **Code-First Development**
   - Write reusable blocks with Svelte and zero setup
   - Powerful in-browser IDE with instant responsive previews
   - Edit code, add fields, done

2. **Client-Proof Editing**
   - Give editors full content control while keeping design and structure locked down
   - You define the guardrails, they work freely within them
   - Page types, fields, and component options constrain what's editable
   - Editors get content autonomy without design access

3. **Block Library**
   - Build blocks once, reuse across all your sites
   - Browse the marketplace for starter sites and blocks
   - Server library of your best work

4. **Built-in Hosting**
   - Static site generation with hosting included
   - Deploy blazing-fast, secure, SEO-optimized sites with zero setup

## Target Audience

- Freelancers building sites for local businesses
- Small agencies managing multiple client sites
- In-house developers building internal & marketing sites
- Weekend devs building sites for friends and family
- Anyone tired of "I broke the website" texts

## Technology Stack

**Frontend:** Svelte 5 - modern component framework with:
- Simple syntax built on HTML, CSS, and JS
- Scoped styles (no CSS conflicts)
- Reactive JavaScript using runes ($state, $derived, $effect)
- Snippets for reusable template chunks
- Fast performance with small bundle sizes

**Backend:** PocketBase - single-file backend built on SQLite with realtime data, file storage, and authentication

**Note on Svelte syntax:** Blocks use Svelte 5 syntax. Fields are globally available (no need for `export let`). Most Svelte features work in blocks, but some are irrelevant (stores, context API, $bindable, custom elements, SvelteKit-specific features).

## Core Terminology

**USE THESE TERMS:**
- **"Primo"** - not "Primo CMS" (except in technical contexts like GitHub repo, domain)
- **"blocks"** - what users build (Svelte components with content fields attached)
- **"slots"** - areas where blocks can be placed (header, body, footer)
- **"editors"** - not "clients" in technical documentation
- **"page types"** - templates that define structure and available blocks
- **"component library" or "block library"** - personal library of reusable blocks

**DON'T USE:**
- "Primo CMS" in user-facing copy
- "components" when referring to blocks (unless explaining the relationship)
- "clients" in docs (use "editors" - save "clients" for marketing/handoff context)

## Architecture Overview

**Hierarchy:**
Site Groups → Sites → Page Types → Pages → Blocks → (optional) Sections

**Site Group Level:**
- Organizational containers for grouping related sites
- Useful for managing multiple client projects or environments
- Sites can be moved between groups
- Groups can be renamed and deleted (deleting a group deletes all sites within it)

**Site Level:**
- Site-wide content (navigation, logo, social links)
- CSS variables for design system
- Site-specific blocks (available only to this site)
- Site fields (global content like logo, navigation, footer)
- Head and foot HTML (for custom scripts, analytics, etc.)
- Each site is independent and tied to a domain/hostname
- Sites are created automatically when accessing a new domain

**Page Type Level:**
- Defines what kind of pages can exist (blog posts, events, team members)
- Controls which blocks are available for editors to use
- Sets required blocks that always appear (via slots)
- Defines page-level fields (metadata like title, author, publish date)
- Organizes blocks into slots: header, body, and footer
- Acts as templates and guardrails for editors

**Page Level:**
- Built by stacking blocks vertically
- Follows structure defined by page type
- Contains page-specific content and metadata
- Instances of page types with actual content
- Pages can be nested (parent/child relationships)
- Each site has a homepage (root page with no parent)

**Block Level:**
- Building blocks of pages
- Stack vertically to create layouts
- Svelte components with content fields
- Two types: Library blocks (reusable across all sites) and Site blocks (specific to one site)
- Can be added to page types to make them available to editors

**Section Level (Optional):**
- Horizontal containers within blocks
- Help organize complex layouts
- Use for multi-column or complex block layouts
- Sections are instances of blocks used within page types or pages

## Components vs Blocks

**Components:**
- Reusable Svelte code (Button, Hero, Card, Header)
- Pure code with props and logic
- Can be used anywhere in Svelte application

**Blocks:**
- Components with content fields attached
- Used specifically in page types and pages
- Data-driven versions of components
- Two types:
  - **Library Blocks**: Stored in your personal library, reusable across all sites
  - **Site Blocks**: Specific to one site, not shared across sites

**Relationship:** Blocks ARE components, just with editable content fields. You build a component once (like a Hero section), add content fields to it (headline, image, CTA), and it becomes a block that editors can use.

## Slots (Header, Body, Footer)

Page types organize blocks into three slots:

**Header Slot:**
- Blocks that appear at the top of every page of this type
- Typically includes navigation, site header, logo
- Defined at the page type level, not per-page
- Editors cannot modify header blocks on individual pages

**Body Slot:**
- Main content area where editors have full control
- Editors can add, remove, and reorder blocks
- Blocks are stacked vertically
- This is where most page content lives

**Footer Slot:**
- Blocks that appear at the bottom of every page of this type
- Typically includes site footer, copyright, links
- Defined at the page type level, not per-page
- Editors cannot modify footer blocks on individual pages

## The Collaboration Model

**Developer Phase:**
- Create site and configure site-wide settings
- Define page types with specific available blocks
- Set required blocks in header/footer slots
- Configure content fields (site fields, page type fields, block fields)
- Build and style components (blocks)
- Add blocks to page types to make them available

**Ongoing Collaboration:**
- Invite collaborators as content editors
- Editors can create pages, add blocks (from available options), manage content
- Editors can drag and drop to reorder blocks in the body slot
- Editors cannot touch code, modify page types, change header/footer blocks, or break design
- Developers can jump in anytime to modify structure or design
- Real-time collaboration with activity indicators showing who's working on what

**Result:** Mutual autonomy - devs control structure/design, editors control content/layouts. Both work independently without breaking each other's work.

## Key Workflows

### Creating a Site

1. **Domain-based creation**: Sites are automatically created when you access the application from a new domain/hostname
2. **Manual creation**: From the dashboard, click "Create Site" (requires domain to be configured first)
3. **Site setup**: Configure site name, hostname, and initial settings
4. **Site groups**: Sites can be organized into groups for better management

### Creating Page Types

1. Open the site editor
2. Click "Pages" → "Page Types" (developer only)
3. Click "Create Page Type"
4. Configure:
   - Name, icon, color (for visual identification)
   - Available blocks (which blocks editors can use)
   - Header slot blocks (required blocks at top)
   - Footer slot blocks (required blocks at bottom)
   - Page-level fields (metadata fields)

### Creating Blocks

**Library Blocks** (reusable across all sites):
1. Navigate to Library
2. Create a block group (optional, for organization)
3. Click "Create Block"
4. Write Svelte code (HTML, CSS, JS)
5. Add content fields
6. Save - block is now available in your library

**Site Blocks** (specific to one site):
1. Open a page type editor
2. Go to "Blocks" tab
3. Click "Create Block"
4. Write Svelte code (HTML, CSS, JS)
5. Add content fields
6. Save - block is now available to this site

**Adding Existing Blocks to Page Types:**
- From page type editor, go to "Blocks" tab
- Click "Add" to browse and add blocks from library or site blocks
- Or click "Import" to import blocks from files

### Creating Pages

1. Open site editor
2. Click "Pages" button in toolbar
3. Click "Create Page" (or right-click parent page to create child page)
4. Select page type
5. Enter page name and slug
6. Page is created with header/footer blocks from page type
7. Add blocks in body slot as needed

### Editing Pages

1. Navigate to page in editor
2. **Visual editing**: Click on content to edit inline (for supported fields)
3. **Adding blocks**: Click "+" button between blocks or at top/bottom
4. **Reordering blocks**: Drag and drop blocks to reorder
5. **Editing blocks**: Click block toolbar → "Edit" to modify block content
6. **Editing sections**: Hover over section → click to edit section content
7. **Page fields**: Edit page-level metadata in sidebar

### Publishing Workflow

1. Make changes to site, pages, or blocks
2. Click "Publish" button in toolbar (or Cmd/Ctrl+P)
3. System compiles all blocks, generates static HTML
4. Site is deployed to configured hostname
5. Changes go live immediately

**Publishing Process:**
- Compiles all Svelte blocks to JavaScript
- Generates static HTML for each page
- Copies compiled assets and uploads to site directory
- Updates site preview
- Serves static files via PocketBase

### Keyboard Shortcuts

**Global:**
- `Cmd/Ctrl + P`: Open publish dialog
- `Cmd/Ctrl + ↑/↓`: Navigate between pages at same level
- `Cmd/Ctrl + S`: Save (in code editors and block editors)
- `Cmd/Ctrl + E`: Toggle between code and content tabs (in editors)

**In Code Editors:**
- `Cmd/Ctrl + S`: Save
- `Cmd/Ctrl + E`: Toggle to content tab
- `Cmd/Ctrl + R`: Refresh preview

### Navigation Structure

**Routes:**
- `/admin/dashboard/sites` - Site management dashboard
- `/admin/sites/[site_id]` - Site editor (homepage)
- `/admin/sites/[site_id]/page-type--[page_type_id]` - Page type editor
- `/admin/sites/[site_id]/[...page]` - Page editor (page path)
- `/admin/site` - Current domain's site editor (if site exists for hostname)

**URL Structure:**
- Page URLs follow the page's slug path
- Nested pages create nested URL structures
- Homepage is at root path `/`

## Field Types

Fields are the content editing interface attached to blocks, page types, and sites. Available field types:

**Basic Content:**
- **Text**: Single-line text input
- **Rich Text**: WYSIWYG editor with formatting (TipTap/ProseMirror)
- **Markdown**: Markdown editor with live preview
- **Image**: Image upload with preview
- **Icon**: Icon picker (Iconify icons)
- **Link**: Link field with URL and optional text
- **URL**: URL input field

**Structured Content:**
- **Repeater**: Repeatable group of fields (for lists, arrays)
- **Group**: Organize related fields together
- **Select**: Dropdown selection with custom options
- **Number**: Numeric input
- **Slider**: Range slider for numeric values
- **Switch/Toggle**: Boolean on/off toggle

**Relational Content:**
- **Page Field**: Reference a field from another page (dynamic content)
- **Site Field**: Reference a site-wide field (global content)
- **Page**: Link to a specific page
- **Page List**: Select multiple pages

**Utility:**
- **Info**: Display-only markdown text (for documentation/help)

### Field Implementation Details

**Object Fields:**
- **Image** returns `{ url: string, alt: string }` - check with `{#if image?.url}`
- **Link** returns `{ url: string, label: string }` - check with `{#if link?.url}`
- **Icon** returns an SVG string - use `{@html icon}`, style with font-size and color

**Accessing Site Fields:**
- Site fields are NOT available via a global `SITE` object
- To use site fields in blocks: add a "Site Field" field to your block, then select which site field to reference
- Editing a site field from the block form updates it site-wide across all blocks that reference it
- Available in page types and blocks (not at site level)

**Accessing Page Fields:**
- To use page fields in blocks: add a "Page Field" field to your block, then select which page field to reference
- Editing a page field from the block form updates it for that page across all blocks that reference it
- Available in blocks only (not at page type level)
- Cannot be edited inline on the page yet

**Page and Page List Fields:**
- **Page**: Must specify a page_type, provides `_meta` property with `url`, `slug`, `name`
- **Page List**: Outputs ALL pages of a given type (no editor selection), editors cannot choose which pages

**Conditional Display:**
- Fields can be shown/hidden based on preceding sibling field values at the same level
- Comparison operators: "Equals" (`=`) or "Doesn't equal" (`!=`)
- Works with Select, Toggle, Text, URL, and Number fields
- The field being checked must come before the conditional field in the field list

**Styling Rich Text and Markdown:**
- Both output HTML via `{@html}`
- Use `:global()` to style rendered HTML elements
- Use a unique wrapper class to avoid affecting other elements

## Data Model & Collections

**Core Collections:**
- `sites`: Site records with hostname, name, settings
- `site_groups`: Organizational groups for sites
- `site_symbols`: Site-specific blocks
- `site_fields`: Site-wide content fields
- `site_entries`: Values for site fields
- `page_types`: Page type templates
- `page_type_fields`: Fields defined on page types
- `page_type_entries`: Values for page type fields
- `page_type_sections`: Required sections (header/footer) for page types
- `page_type_symbols`: Blocks available to a page type
- `pages`: Individual page instances
- `page_sections`: Sections on pages (body slot blocks)
- `page_section_entries`: Content values for page sections
- `library_symbols`: Reusable blocks in server library
- `library_symbol_groups`: Organization for library blocks

**Data Flow:**
- Content is stored as entries linked to fields
- Fields define structure, entries store values
- Multi-locale support (entries can have locale-specific values)
- Reactive updates via PocketBase realtime subscriptions

## Installation Options

**Self-Hosted:**

Since all code and content is stored in the database, Primo requires a persistent server environment. Local development is for testing only—you'll need a virtual machine or cloud hosting for production use.

**Recommended Hosting:**
- **Railway**: Easiest deployment with one-click setup, automatic SSL, and simple scaling
- **Hetzner**: More control over infrastructure, cost-effective for larger deployments
- **Other options**: Any VPS or cloud provider that supports Docker

**Local Development (Testing Only):**
- Requirements: Node.js 18+, npm/yarn, Git, devenv or Dev Container support
- Repo: github.com/primocms/primo
- Steps: 
  1. Clone repository
  2. `npm install`
  3. `npm run build` (required before first dev run)
  4. `npm run dev`
- Access points:
  - Main app: `http://localhost:5173`
  - PocketBase Admin: `http://localhost:8090/_`
  - Built app preview: `http://localhost:8090`
- Uses PocketBase for backend (SQLite database, file storage)
- Sites are generated as static files in `pb_data/storage/sites/[hostname]/`

<Warning>
Local development is for testing and development only. For production, deploy to a persistent server (Railway, Hetzner, or similar) since all your code and content lives in the database and needs to persist.
</Warning>

## Documentation Style Guide

**Tone:**
- Clear, helpful, developer-focused
- Concise and scannable
- Conversational but professional
- Use second person ("you")

**Mintlify Components:**
- `<Info>` - helpful tips and context
- `<Warning>` - important caveats
- `<Note>` - additional information
- `<Tip>` - pro tips and best practices
- `<Check>` - success states or confirmations
- `<Steps>` - sequential instructions
- `<Tabs>` - alternative options (Cloud vs Self-hosted, different code examples)
- `<Accordion>` - collapsible detailed content
- `<Card>` and `<CardGroup>` - feature highlights, next steps
- `<CodeGroup>` - multiple code examples with tabs

**Structure:**
- Start with clear H1 title
- Use H2s for major sections
- Use callouts (Info, Warning, etc.) for emphasis
- Use Steps for tutorials
- Use Accordions for advanced/optional content
- End with Next Steps cards linking to related pages

**Best Practices:**
- Keep it scannable with headers and callouts
- Use code examples liberally
- Provide context before diving into details
- Link to related pages
- Use concrete examples over abstract explanations

---

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
- Skip frontmatter on any MDX file
- Use absolute URLs for internal links
- Include untested code examples
- Make assumptions - always ask for clarification