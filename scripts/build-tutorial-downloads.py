"""Package checked-in tutorial sources as reproducible downloadable workspaces."""
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

root = Path(__file__).resolve().parents[1]
downloads = root / 'downloads'
downloads.mkdir(exist_ok=True)
for name in ('first-site', 'editor-blog'):
    source = root / 'examples' / name
    files = sorted(p for p in source.rglob('*') if p.is_file()
                   and not any(part in {'.primo', 'node_modules', '.DS_Store', '.mcp.json'}
                               for part in p.relative_to(source).parts))
    if not (source / 'server.yaml').is_file() or not files:
        raise SystemExit(f'Missing workspace sources: {source}')
    with ZipFile(downloads / f'{name}.zip', 'w', ZIP_DEFLATED) as archive:
        for file in files:
            info = ZipInfo(f'{name}/{file.relative_to(source).as_posix()}', (2026, 10, 11, 0, 0, 0))
            info.compress_type = ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            archive.writestr(info, file.read_bytes())
    print(f'{name}.zip: {len(files)} source files')
