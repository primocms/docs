<script>let { posts = [] } = $props();</script>
<section aria-label="Blog posts">
  <h1>Garden notes</h1>
  {#each posts ?? [] as post}
    <article>
      <h2><a href={post._meta.url}>{post.title || post._meta.name}</a></h2>
      {#if post.excerpt}<p>{post.excerpt}</p>{/if}
    </article>
  {:else}
    <p>No posts yet.</p>
  {/each}
</section>

<style>section{max-width:48rem;margin:2rem auto;padding-inline:1rem}article{padding:1rem;border-bottom:1px solid #d6dfd5}</style>
