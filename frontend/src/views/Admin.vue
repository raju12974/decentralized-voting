<template>
  <div>
    <CandidateForm />
    <Blockchain />
  </div>
</template>

<script>
import Blockchain from '@/components/Blockchain.vue';
import CandidateForm from '@/components/CandidateForm.vue';

export default {
  components: {
    CandidateForm,
    Blockchain
  },
};
</script>