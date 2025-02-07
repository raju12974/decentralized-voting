<template>
  <div>
    <h1 class="text-center my-4">Welcome to the Decentralized Voting System</h1>
    <Dashboard />

    <Vote />
  </div>
</template>

<script>
import Dashboard from '@/components/Dashboard.vue';
import Vote from '@/components/Vote.vue';

export default {
  components: {
    Dashboard,
    Vote
  },
};
</script>