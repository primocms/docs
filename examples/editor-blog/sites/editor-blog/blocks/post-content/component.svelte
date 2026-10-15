<script>let { title, publish_date, body } = $props();</script>
<article>
  <h1>{title || "Untitled post"}</h1>
  {#if typeof publish_date === "string" && publish_date}
    <time datetime={publish_date}>{new Date(publish_date).toLocaleDateString("en-US", { timeZone: "UTC" })}</time>
  {/if}
  <div class="post-body">{@html typeof body === "string" ? body : ""}</div>
</article>

<style>
  article { max-width: 48rem; margin: auto; padding: 2rem 1rem; }
  .post-body :global(p) { line-height: 1.7; margin-block: 1rem; }
</style>
