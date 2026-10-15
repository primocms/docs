<script>
  let { headline, subheadline, cta_text, cta_link, background_image } = $props();
</script>

<section class="hero" style={background_image?.url ? `background-image: url(${background_image.url})` : ''}>
  <div class="hero-content">
    <h1>{headline}</h1>
    <p>{subheadline}</p>
    {#if cta_link}
      <a href={cta_link} class="cta-button">{cta_text || "Learn more"}</a>
    {/if}
  </div>
</section>

<style>
  .hero {
    min-height: 60vh;
    display: flex;
    align-items: center;
    justify-content: center;
    background: linear-gradient(135deg, #4f46b6 0%, #764ba2 100%);
    background-size: cover;
    background-position: center;
    color: white;
    text-align: center;
    padding: 4rem 2rem;
  }

  .hero-content {
    max-width: 800px;
  }

  .hero h1 {
    font-size: 3.5rem;
    margin-bottom: 1rem;
    font-weight: 700;
  }

  .hero p {
    font-size: 1.5rem;
    margin-bottom: 2rem;
    opacity: 0.95;
  }

  .cta-button {
    display: inline-block;
    padding: 1rem 2.5rem;
    background: white;
    color: #4f46b6;
    text-decoration: none;
    border-radius: 0.5rem;
    font-weight: 600;
    font-size: 1.1rem;
    transition: transform 0.2s, box-shadow 0.2s;
  }

  .cta-button:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
  }

  @media (max-width: 768px) {
    .hero h1 {
      font-size: 2.5rem;
    }
    .hero p {
      font-size: 1.25rem;
    }
  }
</style>
