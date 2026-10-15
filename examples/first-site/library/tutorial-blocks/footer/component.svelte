<script>
  let { copyright_text, links = [] } = $props();
</script>

<div class="footer">
  <div class="footer-content">
    <div class="footer-links">
      {#each links as link}
        <a href={link.url}>{link.label}</a>
      {/each}
    </div>
    <p class="copyright">{copyright_text}</p>
  </div>
</div>

<style>
  .footer {
    background: #1a1a1a;
    color: white;
    padding: 3rem 2rem;
    margin-top: 4rem;
  }

  .footer-content {
    max-width: 1200px;
    margin: 0 auto;
    text-align: center;
  }

  .footer-links {
    display: flex;
    justify-content: center;
    gap: 2rem;
    margin-bottom: 2rem;
    flex-wrap: wrap;
  }

  .footer-links a {
    color: white;
    text-decoration: none;
    transition: opacity 0.2s;
  }

  .footer-links a:hover {
    opacity: 0.7;
  }

  .copyright {
    color: #888;
    font-size: 0.9rem;
  }
</style>
