<script>
  let { image, alt_text, caption, full_width } = $props();
</script>

<figure class="image-block" class:full-width={full_width}>
  {#if image?.url}
    <img src={image.url} alt={alt_text || image.alt || ""} />
  {/if}
  {#if caption}
    <figcaption>{caption}</figcaption>
  {/if}
</figure>

<style>
  .image-block {
    margin: 2rem auto;
    max-width: 1000px;
    padding: 0 2rem;
  }

  .image-block.full-width {
    max-width: 100%;
    padding: 0;
  }

  .image-block img {
    width: 100%;
    height: auto;
    border-radius: 0.5rem;
  }

  .image-block figcaption {
    margin-top: 0.75rem;
    text-align: center;
    color: #666;
    font-style: italic;
    font-size: 0.9rem;
  }
</style>
