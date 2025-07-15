// Optimized loading particles for low-end devices
function createLoadingParticles() {
    const particlesContainer = document.getElementById('loadingParticles');
    // Device capability detection: low-end if <=2GB RAM, <=2 cores, or small screen
    const isLowEnd = (
        (window.deviceMemory && window.deviceMemory <= 2) ||
        (navigator.hardwareConcurrency && navigator.hardwareConcurrency <= 2) ||
        (window.innerWidth <= 600)
    );
    // Fewer, lighter particles on low-end devices
    const particleCount = isLowEnd ? 7 : 15;
    const minDuration = isLowEnd ? 1.5 : 2;
    const maxDuration = isLowEnd ? 2.5 : 5;
    const minSize = isLowEnd ? 6 : 8;
    const maxSize = isLowEnd ? 10 : 16;
    const boxShadow = isLowEnd ? '0 0 4px' : '0 0 8px';

    for (let i = 0; i < particleCount; i++) {
        const particle = document.createElement('div');
        particle.className = 'loading-particle';
        // Random positioning and colors
        const colors = ['#00ffff', '#ff00ff', '#ffff00', '#ff6b6b', '#00ff88'];
        const randomColor = colors[Math.floor(Math.random() * colors.length)];
        const size = Math.random() * (maxSize - minSize) + minSize;
        particle.style.left = Math.random() * 100 + '%';
        particle.style.background = randomColor;
        particle.style.width = `${size}px`;
        particle.style.height = `${size}px`;
        particle.style.animationDelay = Math.random() * 2 + 's';
        particle.style.animationDuration = (Math.random() * (maxDuration - minDuration) + minDuration) + 's';
        particle.style.boxShadow = `${boxShadow} ${randomColor}`;
        particlesContainer.appendChild(particle);
    }
}


function hideRecommendation() {
    const resultDiv = document.getElementById("result-placeholder");
    if (resultDiv) {
        resultDiv.style.display = "none";
    }
}
const hasLoadedBefore = sessionStorage.getItem("hasLoaded");
let initialLoadDone = false;

document.addEventListener("DOMContentLoaded", () => {
    // --- Language select hover effect logic ---
    const languageSelect = document.getElementById('language');
    const recommendBtn = document.querySelector('.recommend-btn');
    if (languageSelect && recommendBtn) {
        languageSelect.addEventListener('change', function() {
            recommendBtn.classList.add('hovered');
        });
        recommendBtn.addEventListener('click', function() {
            recommendBtn.classList.remove('hovered');
        });
    }

    if (!hasLoadedBefore) {
        initializeLoading(); // show loader
        sessionStorage.setItem("hasLoaded", "true");
    } else {
        const loadingScreen = document.getElementById("loadingScreen");
        if (loadingScreen) loadingScreen.remove();
        initialLoadDone = true; // ✅ still set true, since loader skipped
    }

    // Hide result only if it is empty (no recommendation)
    const resultDiv = document.getElementById("result-placeholder");
    if (resultDiv && resultDiv.innerText.trim() === "") {
        resultDiv.style.display = "none";
    } else if (resultDiv) {
        resultDiv.style.display = "";
    }

    // ✅ Always initialize the app
    const app = new MusicRecommender();
    window.musicRecommender = app;

    // Show result when requesting a new recommendation
    const form = document.getElementById('recommendForm');
    if (form) {
        form.addEventListener('submit', function() {
            const resultDiv = document.getElementById("result-placeholder");
            if (resultDiv) resultDiv.style.display = "";
        });
    }

    // Hide result when mood is changed
    const moodSelect = document.getElementById('mood');
    if (moodSelect) {
        moodSelect.addEventListener('change', function() {
            const resultDiv = document.getElementById("result-placeholder");
            if (resultDiv) resultDiv.style.display = "none";
        });
    }

    window.addEventListener("beforeunload", () => {
        app.destroy();
    });
});

/**
 * Show loading screen with animated particles for initial load.
 */
function initializeLoading() {
    createLoadingParticles();

    setTimeout(() => {
        const loadingScreen = document.getElementById("loadingScreen");
        loadingScreen.classList.add("fade-out");

        setTimeout(() => {
            loadingScreen.remove();
            initialLoadDone = true; // ✅ after loader finishes
        }, 800);
    }, 3000);
}




// Dynamically import modular mood animation system for mood effects
(async function() {
    if (!window.moodAnimations) {
        try {
            const mod = await import('./animation/index.js');
            window.moodAnimations = mod.moodAnimations;
        } catch (e) {
            console.error('Failed to load mood animation modules:', e);
        }
    }
})();

// Main app class for Mood Music Recommender
class MusicRecommender {
    constructor() {
        // Detect low-end device (used globally for all optimizations)
        this.isLowEnd = (
            (window.deviceMemory && window.deviceMemory <= 2) ||
            (navigator.hardwareConcurrency && navigator.hardwareConcurrency <= 2) ||
            (window.innerWidth <= 600)
        );
        this.init();
        this.setupEventListeners();
        this.createBackgroundEffects();
        this.updateMoodBackground();
    }

    init() {
        this.form = document.getElementById('recommendForm');
        this.moodSelect = document.getElementById('mood');
        this.loading = document.getElementById('loading');
        this.toggleBtn = document.getElementById('toggleFeedbackBtn');
        this.feedbackDiv = document.getElementById('feedback-form');
        this.feedbackForm = document.getElementById('feedbackForm');
        this.backgroundEffects = document.getElementById('backgroundEffects');
        this.particles = document.getElementById('particles');
        this.floatingShapes = document.getElementById('floatingShapes');
        this.moodOverlay = document.getElementById('moodOverlay');
        
        this.currentMood = 'happy';
        this.animationFrameId = null;
        
        // Track mood-specific animations
        this.moodAnimations = {
            intervals: [],
            timeouts: [],
            elements: []
        };
    }

    setupEventListeners() {
        // Form submission
        this.form.addEventListener('submit', (e) => this.handleFormSubmit(e));
        
        // Mood change
        this.moodSelect.addEventListener('change', (e) => this.handleMoodChange(e));
        
        // Feedback toggle
        this.toggleBtn.addEventListener('click', () => this.toggleFeedback());
        
        // Feedback form submission
        this.feedbackForm.addEventListener('submit', (e) => this.handleFeedbackSubmit(e));
        
        // Close feedback on outside click
        document.addEventListener('click', (e) => this.handleOutsideClick(e));
        
        // Keyboard shortcuts
        document.addEventListener('keydown', (e) => this.handleKeyboard(e));
        
        // Window resize
        window.addEventListener('resize', () => this.handleResize());
        
        // Mouse movement for interactive effects
        document.addEventListener('mousemove', (e) => this.handleMouseMove(e));
    }

    handleFormSubmit(e) {
    e.preventDefault();
    if (!initialLoadDone) return;

    this.addSubmissionEffects();

    setTimeout(() => {
        this.form.submit(); // ✅ submit manually after animation
    }, 500); // match with your particle animation time
}


    handleMoodChange(e) {
        // Stop all current mood animations
        this.stopMoodAnimations();
        
        this.currentMood = e.target.value;
        this.updateMoodBackground();
        this.createMoodSpecificEffects();
    }

    // New method to stop all mood animations
    stopMoodAnimations() {
        // Clear all intervals
        this.moodAnimations.intervals.forEach(interval => clearInterval(interval));
        this.moodAnimations.intervals = [];
        
        // Clear all timeouts
        this.moodAnimations.timeouts.forEach(timeout => clearTimeout(timeout));
        this.moodAnimations.timeouts = [];
        
        // Remove all mood-specific elements
        this.moodAnimations.elements.forEach(element => {
            if (element && element.parentNode) {
                element.parentNode.removeChild(element);
            }
        });
        this.moodAnimations.elements = [];
    }

    updateMoodBackground() {
        // Remove existing mood classes
        const moodClasses = ['mood-happy', 'mood-sad', 'mood-romantic', 'mood-energetic', 'mood-calm'];
        this.moodOverlay.classList.remove(...moodClasses);
        
        // Add current mood class
        this.moodOverlay.classList.add(`mood-${this.currentMood}`);
        
        // Update particles and shapes
        this.updateParticles();
        this.updateFloatingShapes();
    }

    /**
     * Create animated background shapes (no interactive dots)
     */
    /**
     * Create animated background shapes and static dots
     */
    createBackgroundEffects() {
        this.createParticles(); // Show static dots
        this.createFloatingShapes();
    }

    /**
     * Create static background dots (no animation, no movement)
     */
    createParticles() {
        this.particles.innerHTML = '';
        const particleCount = this.isLowEnd ? 10 : 20;
        for (let i = 0; i < particleCount; i++) {
            const particle = document.createElement('div');
            particle.className = 'particle';
            const size = Math.random() * 6 + 2;
            const x = Math.random() * 100;
            const y = Math.random() * 100;
            particle.style.cssText = `
                width: ${size}px;
                height: ${size}px;
                left: ${x}%;
                top: ${y}%;
                background: ${this.getParticleColor()};
                position: absolute;
                border-radius: 50%;
                opacity: 0.7;
            `;
            this.particles.appendChild(particle);
        }
    }

    /**
     * Create floating animated shapes for the background
     */
    /**
     * Create floating animated shapes for the background
     * Uses fewer, slower shapes on low-end devices
     */
    createFloatingShapes() {
        this.floatingShapes.innerHTML = '';
        const shapeCount = this.isLowEnd
            ? (window.innerWidth < 768 ? 5 : 10)
            : (window.innerWidth < 768 ? 12 : 24);
        const minSize = this.isLowEnd ? 40 : 50;
        const maxSize = this.isLowEnd ? 70 : 150;
        const minDuration = this.isLowEnd ? 18 : 10;
        const maxDuration = this.isLowEnd ? 28 : 25;
        for (let i = 0; i < shapeCount; i++) {
            const shape = document.createElement('div');
            shape.className = 'floating-shape';
            const size = Math.random() * (maxSize - minSize) + minSize;
            const x = Math.random() * 100;
            const y = Math.random() * 100;
            const duration = Math.random() * (maxDuration - minDuration) + minDuration;
            const delay = Math.random() * 8;
            shape.style.cssText = `
                width: ${size}px;
                height: ${size}px;
                left: ${x}%;
                top: ${y}%;
                animation-duration: ${duration}s;
                animation-delay: ${delay}s;
                border-radius: ${Math.random() > 0.5 ? '50%' : '10%'};
                background: ${this.getShapeGradient()};
            `;
            this.floatingShapes.appendChild(shape);
        }
    }

    getParticleColor() {
        const colors = {
            happy: ['#FFD700', '#FFA500', '#FF69B4', '#00CED1'],
            sad: ['#4682B4', '#6495ED', '#87CEEB', '#B0C4DE'],
            romantic: ['#FF1493', '#FF69B4', '#FFB6C1', '#DDA0DD'],
            energetic: ['#FF4500', '#FF6347', '#FFD700', '#FF00FF'],
            calm: ['#00FF7F', '#40E0D0', '#98FB98', '#87CEEB']
        };
        
        const moodColors = colors[this.currentMood] || colors.happy;
        return moodColors[Math.floor(Math.random() * moodColors.length)];
    }

    getShapeGradient() {
        const gradients = {
            happy: 'linear-gradient(45deg, rgba(255, 215, 0, 0.3), rgba(255, 165, 0, 0.3))',
            sad: 'linear-gradient(45deg, rgba(70, 130, 180, 0.3), rgba(100, 149, 237, 0.3))',
            romantic: 'linear-gradient(45deg, rgba(255, 20, 147, 0.3), rgba(255, 182, 193, 0.3))',
            energetic: 'linear-gradient(45deg, rgba(255, 69, 0, 0.3), rgba(255, 215, 0, 0.3))',
            calm: 'linear-gradient(45deg, rgba(0, 255, 127, 0.3), rgba(64, 224, 208, 0.3))'
        };
        
        return gradients[this.currentMood] || gradients.happy;
    }

    updateParticles() {
        const particles = this.particles.querySelectorAll('.particle');
        particles.forEach(particle => {
            particle.style.background = this.getParticleColor();
        });
    }

    updateFloatingShapes() {
        const shapes = this.floatingShapes.querySelectorAll('.floating-shape');
        shapes.forEach(shape => {
            shape.style.background = this.getShapeGradient();
        });
    }

    /**
     * Create mood-specific animation, passing low-end flag for optimization
     */
    createMoodSpecificEffects() {
        // Modular mood animation system
        if (window.moodAnimations && window.moodAnimations[this.currentMood]) {
            window.moodAnimations[this.currentMood](
                this.backgroundEffects,
                this.moodAnimations,
                this.isLowEnd // pass low-end flag for animation throttling
            );
        }
    }

// ...

    addSubmissionEffects() {
        // Add a pulse effect to the form
        this.form.style.animation = 'pulse 0.5s ease-in-out';
        
        // Create loading particles
        this.createLoadingParticles();
        
        setTimeout(() => {
            this.form.style.animation = '';
        }, 500);
    }

    createLoadingParticles() {
        for (let i = 0; i < 8; i++) {
            setTimeout(() => {
                const particle = document.createElement('div');
                particle.style.cssText = `
                    position: absolute;
                    width: 8px;
                    height: 8px;
                    background: #00ffff;
                    border-radius: 50%;
                    left: 50%;
                    top: 50%;
                    transform: translate(-50%, -50%);
                    animation: loadingParticle 1s ease-out forwards;
                    pointer-events: none;
                    z-index: 15;
                `;
                
                this.loading.appendChild(particle);
                
                setTimeout(() => {
                    particle.remove();
                }, 1000);
            }, i * 100);
        }
    }

    // startAnimationLoop() {
    //     const animate = () => {
    //         this.updateParticlePositions();
    //         this.animationFrameId = requestAnimationFrame(animate);
    //     };
    //     animate();
    // }


    // updateParticlePositions() {
    //     const particles = this.particles.querySelectorAll('.particle');
    //     particles.forEach(particle => {
    //         const rect = particle.getBoundingClientRect();
    //         if (rect.top > window.innerHeight + 100) {
    //             particle.style.top = '-10px';
    //             particle.style.left = Math.random() * 100 + '%';
    //         }
    //     });
    // }


    /**
     * Subtle parallax effect for mood overlay on mouse move
     */
    handleMouseMove(e) {
        const x = e.clientX / window.innerWidth;
        const y = e.clientY / window.innerHeight;
        this.moodOverlay.style.transform = `translate(${x * 10}px, ${y * 10}px)`;
    }

    toggleFeedback() {
        if (this.feedbackDiv.style.display === 'block') {
            this.feedbackDiv.style.display = 'none';
            this.toggleBtn.textContent = '💬 Give Feedback';
        } else {
            this.feedbackDiv.style.display = 'block';
            this.toggleBtn.textContent = '❌ Close Feedback';
            this.feedbackDiv.scrollIntoView({ behavior: 'smooth' });
        }
    }

    handleFeedbackSubmit(e) {
        e.preventDefault();
        
        const submitBtn = this.feedbackForm.querySelector('button[type="submit"]');
        submitBtn.disabled = true;
        submitBtn.textContent = 'Sending...';
        
        const googleFormURL = 'https://docs.google.com/forms/d/e/1FAIpQLSdyQHT3Q6n9eK9_qxefTPad4voYAASxO-Jk93M7vgeb3B5yHw/formResponse';
        const formData = new FormData();
        formData.append('entry.1406473944', document.getElementById('feedback').value);
        formData.append('entry.641565808', document.getElementById('suggestion').value);
        
        fetch(googleFormURL, {
            method: 'POST',
            mode: 'no-cors',
            body: formData
        })
        .then(() => {
            this.showMessage('✅ Thank you for your feedback!', 'success');
            this.feedbackForm.reset();
            this.feedbackDiv.style.display = 'none';
            this.toggleBtn.textContent = '💬 Give Feedback';
        })
        .catch(() => {
            this.showMessage('❌ Failed to send. Please try again.', 'error');
        })
        .finally(() => {
            submitBtn.disabled = false;
            submitBtn.textContent = 'Send Feedback';
        });
    }

    showMessage(text, type) {
        const message = document.createElement('div');
        message.className = `${type}-message`;
        message.textContent = text;
        document.body.appendChild(message);
        
        setTimeout(() => {
            message.remove();
        }, 3000);
    }

    handleOutsideClick(e) {
        if (!this.feedbackDiv.contains(e.target) && e.target !== this.toggleBtn) {
            if (this.feedbackDiv.style.display === 'block') {
                this.feedbackDiv.style.display = 'none';
                this.toggleBtn.textContent = '💬 Give Feedback';
            }
        }
    }

    handleKeyboard(e) {
        if (e.key === 'Escape' && this.feedbackDiv.style.display === 'block') {
            this.feedbackDiv.style.display = 'none';
            this.toggleBtn.textContent = '💬 Give Feedback';
        }
        
        // Quick mood selection with number keys
        const moodKeys = {
            '1': 'happy',
            '2': 'sad',
            '3': 'romantic',
            '4': 'energetic',
            '5': 'calm'
        };
        
        if (moodKeys[e.key]) {
            this.moodSelect.value = moodKeys[e.key];
            this.handleMoodChange({ target: { value: moodKeys[e.key] } });
        }
    }

    handleResize() {
        // Recreate effects on resize for better responsiveness
        this.createParticles();
        this.createFloatingShapes();
    }

    destroy() {
        // Stop all mood animations
        this.stopMoodAnimations();
        
        if (this.animationFrameId) {
            cancelAnimationFrame(this.animationFrameId);
        }
        
        // Remove event listeners
        window.removeEventListener('resize', this.handleResize);
        document.removeEventListener('mousemove', this.handleMouseMove);
        document.removeEventListener('click', this.handleOutsideClick);
        document.removeEventListener('keydown', this.handleKeyboard);
    }
}

// CSS keyframes for all background and mood animations
const additionalCSS = `
@keyframes bubbleRise {
    0% { transform: translateY(0) scale(1); opacity: 1; }
    100% { transform: translateY(-100vh) scale(0.5); opacity: 0; }
}

@keyframes rainFall {
    0% { transform: translateY(0); opacity: 1; }
    100% { transform: translateY(100vh); opacity: 0; }
}

@keyframes heartRise {
    0% { transform: translateY(0) rotate(0deg); opacity: 1; }
    100% { transform: translateY(-100vh) rotate(360deg); opacity: 0; }
}

@keyframes energyPulse {
    0% { transform: scale(1); opacity: 1; }
    100% { transform: scale(4); opacity: 0; }
}

@keyframes sparkFlash {
    0% { transform: scale(1); opacity: 1; }
    50% { transform: scale(2); opacity: 0.8; }
    100% { transform: scale(0); opacity: 0; }
}

@keyframes waveExpand {
    0% { transform: scale(0); opacity: 1; }
    100% { transform: scale(3); opacity: 0; }
}

@keyframes lightningFlash {
    0% { opacity: 0; }
    50% { opacity: 1; }
    100% { opacity: 0; }
}

@keyframes lightningBranch {
    0% { 
        transform: rotate(var(--angle)) scaleX(0);
        opacity: 0;
    }
    10% { 
        transform: rotate(var(--angle)) scaleX(0.3);
        opacity: 1;
    }
    30% { 
        transform: rotate(var(--angle)) scaleX(1);
        opacity: 0.9;
    }
    100% { 
        transform: rotate(var(--angle)) scaleX(0);
        opacity: 0;
    }
}

@keyframes electricGlow {
    0% { 
        transform: translate(-50%, -50%) scale(0);
        opacity: 1;
    }
    50% { 
        transform: translate(-50%, -50%) scale(2);
        opacity: 0.8;
    }
    100% { 
        transform: translate(-50%, -50%) scale(4);
        opacity: 0;
    }
}

@keyframes electricParticle {
    0% { 
        transform: scale(1);
        opacity: 1;
    }
    50% { 
        transform: scale(1.5) translate(${Math.random() * 100 - 50}px, ${Math.random() * 100 - 50}px);
        opacity: 0.7;
    }
    100% { 
        transform: scale(0) translate(${Math.random() * 200 - 100}px, ${Math.random() * 200 - 100}px);
        opacity: 0;
    }
}

@keyframes loadingParticle {
    0% { transform: translate(-50%, -50%) scale(1); opacity: 1; }
    100% { transform: translate(-50%, -50%) scale(0) translateY(-50px); opacity: 0; }
}
`;

// Add additional CSS to the document
const style = document.createElement('style');
style.textContent = additionalCSS;
document.head.appendChild(style);




// Performance monitoring for custom measurements
const observer = new PerformanceObserver((list) => {
    for (const entry of list.getEntries()) {
        if (entry.entryType === 'measure') {
            console.log(`${entry.name}: ${entry.duration}ms`);
        }
    }
});
observer.observe({ entryTypes: ['measure'] });

// Utility functions for debounce, throttle, color, lerp
const utils = {
    debounce: (func, wait) => {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    },
    
    throttle: (func, limit) => {
        let inThrottle;
        return function() {
            const args = arguments;
            const context = this;
            if (!inThrottle) {
                func.apply(context, args);
                inThrottle = true;
                setTimeout(() => inThrottle = false, limit);
            }
        };
    },
    
    getRandomColor: () => {
        return `hsl(${Math.random() * 360}, 70%, 60%)`;
    },
    
    lerp: (start, end, factor) => {
        return start + (end - start) * factor;
    }
};

// Export for potential module use
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { MusicRecommender, utils };
}
