<script setup lang="ts">
import { RouterLink } from 'vue-router';
</script>

<template>
  <section id="hero" class="relative text-gray-900 min-h-screen flex flex-col justify-center items-center text-center w-full h-screen backdrop-blur-sm">
    <div class="relative z-10 w-full max-w-screen-xl px-6 sm:px-12 lg:px-16">
      <!-- Heading -->
      <h1 class="text-4xl sm:text-5xl md:text-6xl font-bold mb-6 tracking-tight leading-tight text-[#00b4d1]">
        Ask. Learn. Connect. <br /> Empower Your Future.
      </h1>

      <!-- Paragraph -->
      <p class="text-lg sm:text-xl md:text-2xl font-medium mb-8 text-[#00b4d1] opacity-80">
        Dive into dynamic discourse that fuels curiosity, connects peers, and expands horizons at Zewail City. Your thoughts matter here!
      </p>

      <!-- Buttons -->
      <div class="flex flex-col sm:flex-row gap-6 sm:gap-8 justify-center w-full">
        <RouterLink to="/signup">
          <button class="bg-[#00b4d1] hover:bg-[#0099b3] text-white font-bold py-3 px-8 rounded-xl transition-all duration-300 transform hover:scale-105 shadow-lg">
            Join Now
          </button>
        </RouterLink>
      </div>
    </div>
  </section>
</template>

<script lang="ts">
export default {
  name: 'HeroSection'
}
</script>

<style scoped>
/* Ensure full viewport height */
.min-h-screen {
  height: 100vh;
}

/* Background Color and Gradient */
#hero {
  background-image: url('../../assets/Images/hmn11.jpg'); /* Background image */
  background-size: cover; /* Ensures the image covers the entire section */
  background-position: center; /* Centers the background image */
  background-repeat: no-repeat; /* Prevents the image from repeating */
  width: 100%; /* Ensures the section takes full width */
}

/* Typography Enhancements */
h1 {
  font-size: 2.25rem; /* Default size for mobile */
  font-weight: bold;
  text-align: center;
  letter-spacing: 0.5px;
  line-height: 1.2; /* For a tighter heading */
  color: #00b5d1be; /* Light blue color for the heading */
}

p {
  font-size: 1rem;
  font-weight: 500;
  color: #00b5d1be; /* Light blue color for the paragraph */
  text-align: center;
}

/* Button Styling */
button {
  font-size: 1rem;
  font-weight: 600;
  letter-spacing: 1px;
  padding: 0.75rem 1.5rem;
  border-radius: 8px;
  transition: all 0.3s ease;
}

/* Responsiveness */
@media (min-width: 768px) {
  h1 {
    font-size: 3rem; /* Larger font size for medium screens */
  }

  p {
    font-size: 1.25rem;
  }
}

@media (min-width: 1024px) {
  h1 {
    font-size: 3.5rem; /* Larger heading for larger screens */
  }
}
</style>
