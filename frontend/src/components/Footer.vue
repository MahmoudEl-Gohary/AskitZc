<template>
  <footer class="bg-[#0b152e] text-white py-2">
    <div class="container mx-auto flex flex-col items-center space-y-2">
      <p class="text-sm tracking-wide">&copy; 2024 AskIt. All rights reserved.</p>
      <ul class="flex justify-center space-x-6 text-sm">
        <li>
          <a href="#" class="hover:text-blue-300 transition-colors duration-200">About</a>
        </li>
        <li>
          <a href="#" class="hover:text-blue-300 transition-colors duration-200">Terms</a>
        </li>
        <li>
          <a href="#" class="hover:text-blue-300 transition-colors duration-200">Privacy</a>
        </li>
      </ul>
    </div>
  </footer>
</template>

<style scoped>
/* Typography and Styling */
footer {
  font-family: 'Space Grotesk', sans-serif;
  background: linear-gradient(90deg, #00b5d1 0%, #00b5d191 100%); /* Gradient from cyan to a softer blue */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Soft shadow for depth */
}

footer p {
  color: #ffffff; /* Light gray text */
  opacity: 0.7; /* Subtle opacity for a modern look */
  font-weight: 400;
}

footer ul {
  display: flex;
  justify-content: center;
  gap: 2rem; /* More spacing between links for a cleaner look */
}

footer ul li a {
  color: #ffffff;
  font-weight: 500; /* Slightly bolder for better contrast */
  text-transform: uppercase;
  letter-spacing: 0.5px;
  transition: color 0.3s ease-in-out;
}

footer ul li a:hover {
  color: #fff2f29a; /* Light off-white color on hover */
}

footer .fa {
  transition: color 0.3s ease;
}

footer .fa:hover {
  color: #fff2f2; /* Hover effect for social icons */
}
</style>
