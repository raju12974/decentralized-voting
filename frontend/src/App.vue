<template>
  <div :class="darkMode ? 'bg-dark text-white' : 'bg-light text-dark'" class="vh-100">
    <nav class="navbar navbar-expand-lg" :class="darkMode ? 'navbar-dark bg-dark' : 'navbar-light bg-light'">
      <div class="container">
        <a class="navbar-brand" href="#">Voting System</a>
        
        <!-- Home and Admin links -->
        <ul class="navbar-nav ml-auto">
          <li class="nav-item">
            <router-link to="/" class="nav-link">Home</router-link>
          </li>
          <li class="nav-item">
            <router-link to="/admin" class="nav-link">Admin</router-link>
          </li>
        </ul>
      </div>
    </nav>
    <div class="container mt-4">
      <router-view />
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      darkMode: true, // Default to dark mode
    };
  },
  methods: {
    toggleDarkMode() {
      this.darkMode = !this.darkMode;
    }
  }
};
</script>

<style>
/* Ensure smooth transitions */
body {
  transition: background 0.3s ease, color 0.3s ease;
}
</style>
