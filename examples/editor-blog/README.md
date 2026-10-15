# Editor-blog tutorial companion

This fictional Garden Studio workspace completes the Build a blog for content editors guide. You create these blocks and page types; they are not Primo presets.

## Open the example

Use Node.js 22.13 or a newer supported LTS release. Install the CLI with `npm install -g primo-cli`, then run from this extracted folder:

```bash
primo validate
primo add editor-blog
primo dev --author files
```

Open the editor URL printed by the CLI. The editor is read-only in files mode. Stop with Ctrl+C and run `primo dev --author cms` to edit in the browser and save changes back to files. Stop the server before changing modes.

Verify `/blog`, `/blog/first-post`, and `/blog/second-post`. The index lists both posts through Page List. Blog Post has an empty available-block list, so content editors fill in the post fields without changing its body layout. Each existing post includes its Post Content section; new posts receive that section from the starting layout.

## Inspect the connections

- `blocks/post-content/fields.yaml`: Page Field references use `blog-post--title`, `blog-post--publish_date`, and `blog-post--body`.
- `blocks/post-list/fields.yaml`: Page List references the `blog-post` page type.
- `blocks/navigation/fields.yaml` and `blocks/footer/fields.yaml`: Site Field references share branding and navigation across the two page types.
- `site/content.yaml`: Change `brand_name` to test shared content.
- `pages/blog/*.yaml`: Change a post title to test page-specific content and its index entry.

The Date field does not schedule publication. Page List includes all posts. Publishing includes every saved page. Use CLI 0.2.1 or later for static builds with resolved references, or publish through the CMS. Earlier CLI 0.2.0 static builds do not support all of these references. No accounts, tokens, database, or domain are included. Render only trusted editor HTML with `{@html}`.
