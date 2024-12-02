<script setup lang="ts">
const scrollToSection = (sectionId: string) => {
  const element = document.getElementById(sectionId);
  if (element) {
    element.scrollIntoView({ behavior: 'smooth' });
  }
};
</script>

<template>
  <header class="bg-gradient-to-r from-[#00b4d1] to-[#00a1b5] sticky top-0 z-50 shadow-lg">
    <div class="container mx-auto flex items-center justify-between px-6 py-4 max-w-screen-xl">
      <div class="flex items-center space-x-3">
        <img src="../assets/Icons/header.png" alt="Logo" class="h-12 w-12" />
        <span class="text-3xl font-semibold text-white tracking-tight">askit.zc</span>
      </div>
      <nav class="flex items-center space-x-6">
          <a href="/profile" class="text-white hover:text-[#fff2f2] cursor-pointer transition-all duration-300">Profile</a>
          <a href="/feed" class="text-white hover:text-[#fff2f2] cursor-pointer transition-all duration-300">Feed</a>
          <a href="/search" class="text-white hover:text-[#fff2f2] cursor-pointer transition-all duration-300">Search</a>
          <a href="/notifications" class="text-white hover:text-[#fff2f2] cursor-pointer transition-all duration-300">Notifications</a>
          <button @click="logout" class="bg-[#ff4d4d] text-white hover:bg-[#ff2d2d] rounded-lg px-6 py-2 font-medium transition-all duration-300">
            Log Out
          </button>
      </nav>
    </div>
  </header>
</template>

<style scoped>
/* Typography and Styling */
.font-space-grotesk {
  font-family: 'Space Grotesk', sans-serif;
}

/* Header Background with Linear Gradient */
header {
  background: linear-gradient(90deg, #00b5d1 0%, #00b5d191 100%); /* Gradient from cyan to a softer blue */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Subtle shadow for depth */
  border-bottom: 1px solid rgba(255, 255, 255, 0.1); /* Light transparent border */
}

/* Links Styling */
a {
  font-size: 1rem;
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  transition: color 0.3s ease-in-out;
}

a:hover {
  color: #fff2f29a; /* Light off-white color on hover */
}

/* Action Button Styling */
button {
  font-size: 1rem;
  font-weight: 600;
  letter-spacing: 1px;
  padding: 0.75rem 1.5rem;
  background-color: #00b4d1; /* Cyan button color */
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* Soft shadow */
  transition: background-color 0.3s ease, transform 0.3s ease, box-shadow 0.3s ease;
}

button:hover {
  background-color: #0099b3; /* Darker cyan on hover */
  transform: translateY(-3px); /* Slight lift on hover */
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2); /* More shadow on hover */
}



/* Mobile Responsiveness */
@media (max-width: 768px) {
  nav {
    display: none; /* Hide desktop menu */
  }

  .md:hidden {
    display: flex; /* Show mobile hamburger icon */
  }
}
</style>
