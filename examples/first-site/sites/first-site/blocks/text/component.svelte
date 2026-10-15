<script>
  let { content, alignment } = $props();
</script>

<section class="text-block" class:text-center={alignment === "center"} class:text-right={alignment === "right"}>
  {@html content}
</section>

<style>
  .text-block {
    max-width: 800px;
    margin: 0 auto;
    padding: 3rem 2rem;
    line-height: 1.8;
  }

  .text-block.text-center { text-align: center; }
  .text-block.text-right { text-align: right; }

  .text-block :global(h2) {
    font-size: 2rem;
    margin-top: 2rem;
    margin-bottom: 1rem;
  }

  .text-block :global(p) {
    margin-bottom: 1.5rem;
  }

  .text-block :global(ul), .text-block :global(ol) {
    margin-bottom: 1.5rem;
    padding-left: 2rem;
  }

  .text-block :global(li) {
    margin-bottom: 0.5rem;
  }
</style>
