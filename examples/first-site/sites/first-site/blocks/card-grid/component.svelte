<script>
  let { cards = [], columns } = $props();
</script>

<section class="card-grid" style="--columns: {Math.max(1, Number(columns) || 3)}">
  {#each cards as card}
    <div class="card">
      {#if card.image?.url}
        <img src={card.image.url} alt={card.image.alt || card.title} />
      {/if}
      <div class="card-content">
        <h3>{card.title}</h3>
        {#if card.description}
          <p>{card.description}</p>
        {/if}
        {#if card.link}
          <a href={card.link} class="card-link">Learn More →</a>
        {/if}
      </div>
    </div>
  {/each}
</section>

<style>
  .card-grid {
    display: grid;
    grid-template-columns: repeat(var(--columns), 1fr);
    gap: 2rem;
    padding: 3rem 2rem;
    max-width: 1200px;
    margin: 0 auto;
  }

  .card {
    background: white;
    border-radius: 0.5rem;
    overflow: hidden;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    transition: transform 0.2s, box-shadow 0.2s;
  }

  .card:hover {
    transform: translateY(-4px);
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.15);
  }

  .card img {
    width: 100%;
    height: 200px;
    object-fit: cover;
  }

  .card-content {
    padding: 1.5rem;
  }

  .card-content h3 {
    margin-bottom: 0.75rem;
    font-size: 1.5rem;
  }

  .card-content p {
    color: #666;
    margin-bottom: 1rem;
  }

  .card-link {
    color: #4f46b6;
    text-decoration: none;
    font-weight: 600;
  }

  @media (max-width: 768px) {
    .card-grid {
      grid-template-columns: 1fr;
    }
  }
</style>
