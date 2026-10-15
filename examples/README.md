# Tutorial companion workspaces

These source files back the downloadable ZIPs in the documentation. They contain fictional content and no user accounts, credentials, database, or connected domains.

| Workspace | Guide | Check |
| --- | --- | --- |
| `first-site` | Building from Scratch | Five blocks, General Page and Blog Post, four pages, and independent library copies |
| `editor-blog` | Build a blog for content editors | Site Field and Page Field references, an automatic Page List, and two fixed-layout posts |

Read each workspace's README for setup. Import a copy into a separate local CMS so testing does not write generated IDs or runtime state into these checked-in sources.

After editing, validate with `primo validate -d examples/first-site/sites/first-site` and `primo validate -d examples/editor-blog/sites/editor-blog`. Check the browser preview too. Use CLI 0.2.1 or later for static builds with resolved references; earlier 0.2.0 builds do not support the blog's full reference resolution.

Rebuild both ZIPs with `npm run build:examples`. The packaging script uses Python's standard library and excludes runtime state. Keep the guide examples and companion code consistent; the first-site README documents its explicit props, repeater defaults, and footer wrapper.
