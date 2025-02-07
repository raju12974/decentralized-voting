<template>
  <div class="container mt-5">
    <div class="card shadow">
      <div class="card-header bg-warning text-white">
        <h1 class="card-title">Add Candidate</h1>
      </div>
      <div class="card-body">
        <form @submit.prevent="addCandidate" class="needs-validation" novalidate>
          <div class="mb-3">
            <label for="name" class="form-label">Candidate Name:</label>
            <input
              type="text"
              id="name"
              v-model="name"
              class="form-control"
              required
            />
          </div>
          <button type="submit" class="btn btn-primary">Add Candidate</button>
        </form>
        <p v-if="message" class="mt-3 text-muted" :class="{ 'text-danger': isError }">{{ message }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import apiClient from '@/api';

export default {
  data() {
    return {
      name: '',
      message: '',
      isError: false
    };
  },
  methods: {
    async addCandidate() {
      this.message = '';
      this.isError = false;

      if(!this.name) {
        this.message = 'Candidate name is required';
        this.isError = true;
        return;
      }
     
      try {
        let response = await apiClient.post('/add-candidate', {
          name: this.name
        })

        this.message = "Candidate added successfully";
        this.isError = false;
      } catch (error) {
        this.message = error.response.data.message;
        this.isError = true;
      }
    },
  },
};
</script>