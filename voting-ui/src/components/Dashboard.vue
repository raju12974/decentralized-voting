<template>
    <div class="container mt-5">
      <div class="card shadow">
        <div class="card-header bg-primary text-white">
          <h1 class="card-title">Dashboard</h1>
        </div>
        <div class="card-body">
          <p class="lead">Total Votes: <strong>{{ totalVotes }}</strong></p>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        totalVotes: 0,
      };
    },
    async created() {
      const response = await fetch('http://localhost:5000/chain');
      const chain = await response.json();
      this.totalVotes = chain.length - 1; // Exclude genesis block
    },
  };
  </script>