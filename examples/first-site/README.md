# First-site tutorial companion

This fictional Garden Studio site contains the five blocks and two page types from the Building from Scratch guide. The library originals and site copies are independent. Explicit Svelte props and safe empty repeater defaults make the examples usable in files as well as the browser. The Footer uses a div because Primo supplies the page-level footer wrapper.

## Open the complete example

Use Node.js 22.13 or a newer supported LTS release. Install the CLI with `npm install -g primo-cli`, then run these commands from this extracted folder:

```bash
primo validate
primo add first-site
primo dev --author files
```

Open the editor URL printed by the CLI. The first run imports the source and library; the editor is read-only. Stop with Ctrl+C and run `primo dev --author cms` to edit in the browser and save changes back to files. Stop the server before switching modes. Work in a copy if you want to retain the original example.

Verify Home, About, Blog, and the first post. Home and About share General Page but keep different body content. Both page types have a shared footer section. The Blog Post page fields are metadata; its visible title is in the Text section until you connect a display block through Page Field references, as explained in the guide.

No accounts, tokens, database, or public domain are included. This is source code, not a server backup. Image fields intentionally start empty so you can use your own images. Publishing needs a deployed CMS and connected domain.

## Compare files

- `sites/first-site/blocks/`: Svelte code, field definitions, and default content.
- `sites/first-site/page-types/`: Available blocks, fields, layout, and metadata tags.
- `sites/first-site/pages/`: Complete sample content; folder paths define URLs.
- `library/tutorial-blocks/`: Independent library originals.
