<script setup>
    import HeroSection from '../components/Home/HeroSection.vue'
    import FeaturesSection from '../components/Home/FeaturesSection.vue'
    import EngagementSection from '../components/Home/EngagementSection.vue';
    import ContentSection from '../components/Home/ContentSection.vue';
    import ContactSection from '../components/Home/ContactSection.vue';
    import Header from '../components/Header.vue'
 
</script>

<template>
    <main class="flex flex-col w-full overflow-x-hidden">
        <Header />
        <HeroSection />
        <FeaturesSection />
        <EngagementSection />
        <ContentSection />
        <ContactSection />
    </main>
</template>