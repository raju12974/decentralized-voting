<template>
  <div class="card p-4 shadow-lg bg-dark text-white">
    <h3 class="mb-3">Vote for a Candidate</h3>

    <!-- voter id -->
    <div class="mb-3">
      <label for="voter_id" class="form-label">Voter ID:</label>
      <input
        type="text"
        id="voter_id"
        v-model="voter_id"
        class="form-control"
        required
      />
    </div>

    <div class="mb-3">
      <label for="candidateSelect" class="form-label">Select Candidate</label>
      <select class="form-select" v-model="selectedCandidate" id="candidateSelect">
        <option disabled value="">Choose a candidate</option>
        <option v-for="candidate in candidates" :key="candidate.id" :value="candidate.id">
          {{ candidate.name }}
        </option>
      </select>
    </div>

    <button class="btn btn-primary w-100" @click="submitVote" :disabled="!selectedCandidate">
      Submit Vote
    </button>

    <div v-if="message" class="alert mt-3" :class="isError ? 'alert-danger' : 'alert-success'">
      {{ message }}
    </div>
  </div>
</template>

<script>
import apiClient from '@/api.js';

export default {
  data() {
    return {
      candidates: [],
      selectedCandidate: "",
      message: "",
      isError: false,
      voter_id: ""
    };
  },
  methods: {
    async fetchCandidates() {
      try {
        const response = await apiClient.get('/candidates');
        this.candidates = response.data;
      } catch (error) {
        console.error("Error fetching candidates", error);
      }
    },
    async submitVote() {
      try {
        const response = await apiClient.post('/vote', {
          voter_id: this.voter_id,
          candidate_id: this.selectedCandidate
        })

        const result = await response.data;
        this.message = result.message;
        this.isError = false;
      } catch (error) {
        this.message = error.response.data.message;
        this.isError = true;
      }
      
    },
  },
  mounted() {
    this.fetchCandidates();
  }
};
</script>

<style>
body {
  background-color: #121212; /* Dark theme */
}
</style>
