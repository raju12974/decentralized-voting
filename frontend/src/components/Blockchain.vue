<template>
  <div class="container mt-5">
    <div class="card shadow">
      <div class="card-header bg-info text-white">
        <h1 class="card-title">Blockchain</h1>
      </div>
      <div class="card-body">
        <pre class="bg-light p-3 rounded">{{ chain }}</pre>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      chain: [],
    };
  },
  async created() {
    const response = await fetch('http://localhost:5000/chain');
    this.chain = await response.json();
  },
};
</script>