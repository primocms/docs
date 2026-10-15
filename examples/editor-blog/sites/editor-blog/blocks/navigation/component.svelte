<script>let { brand_name, logo, links = [] } = $props();</script>
<nav aria-label="Main navigation">
  <a class="brand" href="/">{#if logo?.url}<img src={logo.url} alt={logo.alt || ""} />{/if}{brand_name}</a>
  <div>{#each links ?? [] as link}<a href={link.url}>{link.label}</a>{/each}</div>
</nav>
<style>nav{display:flex;gap:2rem;justify-content:space-between;align-items:center;padding:1rem 2rem;background:#e9efe8}nav div{display:flex;gap:1.25rem}.brand{display:flex;gap:.5rem;align-items:center;font-weight:700;text-decoration:none}.brand img{width:2rem;height:2rem}</style>
