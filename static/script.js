function createLoadingParticles() {
    const particlesContainer = document.getElementById('loadingParticles');
    const particleCount = 15;
    
    for (let i = 0; i < particleCount; i++) {
        const particle = document.createElement('div');
        particle.className = 'loading-particle';
        
        // Random positioning and colors
        const colors = ['#00ffff', '#ff00ff', '#ffff00', '#ff6b6b', '#00ff88'];
        const randomColor = colors[Math.floor(Math.random() * colors.length)];
        
        particle.style.left = Math.random() * 100 + '%';
        particle.style.background = randomColor;
        particle.style.animationDelay = Math.random() * 4 + 's';
        particle.style.animationDuration = (Math.random() * 3 + 2) + 's';
        particle.style.boxShadow = `0 0 8px ${randomColor}`;
        
        particlesContainer.appendChild(particle);
    }
}

// Initialize loading screen
function initializeLoading() {
    createLoadingParticles();
    
    // Hide loading screen after 3 seconds
    setTimeout(() => {
        const loadingScreen = document.getElementById('loadingScreen');
        loadingScreen.classList.add('fade-out');
        
        // Remove from DOM after transition
        setTimeout(() => {
            loadingScreen.style.display = 'none';
        }, 800);
    }, 3000);
}

// Call this at the very beginning of your DOMContentLoaded event

       // Enhanced Music Recommender JavaScript
class MusicRecommender {
    constructor() {
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
        this.loading.style.display = 'block';
        this.addSubmissionEffects();
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

    createBackgroundEffects() {
        this.createParticles();
        this.createFloatingShapes();
        this.startAnimationLoop();
    }

    createParticles() {
        this.particles.innerHTML = '';
        const particleCount = window.innerWidth < 768 ? 15 : 25;
        
        for (let i = 0; i < particleCount; i++) {
            const particle = document.createElement('div');
            particle.className = 'particle';
            
            const size = Math.random() * 6 + 2;
            const x = Math.random() * 100;
            const y = Math.random() * 100;
            const duration = Math.random() * 10 + 100;
            const delay = Math.random() * 5;
            
            particle.style.cssText = `
                width: ${size}px;
                height: ${size}px;
                left: ${x}%;
                top: ${y}%;
                animation-duration: ${duration}s;
                animation-delay: ${delay}s;
                background: ${this.getParticleColor()};
            `;
            
            this.particles.appendChild(particle);
        }
    }

    createFloatingShapes() {
        this.floatingShapes.innerHTML = '';
        const shapeCount = window.innerWidth < 768 ? 5 : 8;
        
        for (let i = 0; i < shapeCount; i++) {
            const shape = document.createElement('div');
            shape.className = 'floating-shape';
            
            const size = Math.random() * 100 + 50;
            const x = Math.random() * 100;
            const y = Math.random() * 100;
            const duration = Math.random() * 15 + 10;
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

    createMoodSpecificEffects() {
        // Create continuous mood-specific visual effects
        switch (this.currentMood) {
            case 'happy':
                this.createContinuousBubbleEffect();
                break;
            case 'sad':
                this.createContinuousRainEffect();
                break;
            case 'romantic':
                this.createContinuousHeartEffect();
                break;
            case 'energetic':
                this.createContinuousLightningEffect();  
                break;
            case 'calm':
                this.createContinuousWaveEffect();
                break;
        }
    }

    createContinuousBubbleEffect() {
    const emojis = ['😃', '🥳', '🤗'];
    const bubbleInterval = setInterval(() => {
        for (let i = 0; i < 3; i++) {
            const timeout = setTimeout(() => {
                const bubble = document.createElement('div');
                bubble.className = 'mood-bubble';
                bubble.innerHTML = emojis[Math.floor(Math.random() * emojis.length)];
                bubble.style.cssText = `
                    position: absolute;
                    font-size: ${Math.random() * 20 + 25}px;
                    left: ${Math.random() * 100}%;
                    top: 100%;
                    animation: bubbleRise 4s ease-out forwards;
                    pointer-events: none;
                    z-index: 5;
                    filter: blur(0.5px) brightness(1.2);
                `;
                
                this.backgroundEffects.appendChild(bubble);
                this.moodAnimations.elements.push(bubble);
                
                const removeTimeout = setTimeout(() => {
                    if (bubble.parentNode) {
                        bubble.parentNode.removeChild(bubble);
                    }
                }, 4000);
                
                this.moodAnimations.timeouts.push(removeTimeout);
            }, i * 500);
            
            this.moodAnimations.timeouts.push(timeout);
        }
    }, 2000);
    
       this.moodAnimations.intervals.push(bubbleInterval);
   }

    createContinuousRainEffect() {
        const rainInterval = setInterval(() => {
            for (let i = 0; i < 10; i++) {
                const timeout = setTimeout(() => {
                    const drop = document.createElement('div');
                    drop.className = 'mood-rain';
                    drop.style.cssText = `
                        position: absolute;
                        width: 2px;
                        height: ${Math.random() * 25 + 15}px;
                        background: linear-gradient(to bottom, rgba(173, 216, 230, 0.9), rgba(173, 216, 230, 0.3));
                        left: ${Math.random() * 100}%;
                        top: -30px;
                        animation: rainFall 2s linear forwards;
                        pointer-events: none;
                        z-index: 5;
                    `;
                    
                    this.backgroundEffects.appendChild(drop);
                    this.moodAnimations.elements.push(drop);
                    
                    const removeTimeout = setTimeout(() => {
                        if (drop.parentNode) {
                            drop.parentNode.removeChild(drop);
                        }
                    }, 2000);
                    
                    this.moodAnimations.timeouts.push(removeTimeout);
                }, i * 100);
                
                this.moodAnimations.timeouts.push(timeout);
            }
        }, 780);
        
        this.moodAnimations.intervals.push(rainInterval);
    }

    createContinuousHeartEffect() {
        const heartInterval = setInterval(() => {
            for (let i = 0; i < 2; i++) {
                const timeout = setTimeout(() => {
                    const heart = document.createElement('div');
                    heart.innerHTML = '♥';
                    heart.className = 'mood-heart';
                    heart.style.cssText = `
                        position: absolute;
                        font-size: ${Math.random() * 25 + 20}px;
                        color: rgba(255, 20, 147, 0.8);
                        left: ${Math.random() * 100}%;
                        top: 100%;
                        animation: heartRise 5s ease-out forwards;
                        pointer-events: none;
                        z-index: 5;
                    `;
                    
                    this.backgroundEffects.appendChild(heart);
                    this.moodAnimations.elements.push(heart);
                    
                    const removeTimeout = setTimeout(() => {
                        if (heart.parentNode) {
                            heart.parentNode.removeChild(heart);
                        }
                    }, 5000);
                    
                    this.moodAnimations.timeouts.push(removeTimeout);
                }, i * 1000);
                
                this.moodAnimations.timeouts.push(timeout);
            }
        }, 3000);
        
        this.moodAnimations.intervals.push(heartInterval);
    }

    createContinuousLightningEffect() {
    const lightningInterval = setInterval(() => {
        // Create main lightning spark at random position
        const centerX = Math.random() * 100;
        const centerY = Math.random() * 100;
        
        // Create lightning branches (3-6 branches per spark)
        const branchCount = Math.floor(Math.random() * 4) + 3;
        
        for (let i = 0; i < branchCount; i++) {
            const timeout = setTimeout(() => {
                const branch = document.createElement('div');
                branch.className = 'lightning-branch';
                
                const angle = (360 / branchCount) * i + Math.random() * 60 - 30;
                const length = Math.random() * 150 + 50;
                
                branch.style.cssText = `
                    position: absolute;
                    width: ${length}px;
                    height: 3px;
                    background: linear-gradient(90deg, 
                        transparent 0%, 
                        #FFD700 20%, 
                        #FFFFFF 50%, 
                        #00FFFF 80%, 
                        transparent 100%);
                    left: ${centerX}%;
                    top: ${centerY}%;
                    transform-origin: 0 50%;
                    transform: rotate(${angle}deg);
                    animation: lightningBranch 0.3s ease-out forwards;
                    pointer-events: none;
                    z-index: 5;
                    box-shadow: 0 0 15px #FFD700, 0 0 30px #00FFFF;
                `;
                
                this.backgroundEffects.appendChild(branch);
                this.moodAnimations.elements.push(branch);
                
                // Add electric glow effect
                const glow = document.createElement('div');
                glow.className = 'lightning-glow';
                glow.style.cssText = `
                    position: absolute;
                    width: 20px;
                    height: 20px;
                    background: radial-gradient(circle, rgba(255, 255, 255, 0.8), rgba(0, 255, 255, 0.4), transparent);
                    border-radius: 50%;
                    left: ${centerX}%;
                    top: ${centerY}%;
                    transform: translate(-50%, -50%);
                    animation: electricGlow 0.5s ease-out forwards;
                    pointer-events: none;
                    z-index: 6;
                `;
                
                this.backgroundEffects.appendChild(glow);
                this.moodAnimations.elements.push(glow);
                
                const removeTimeout = setTimeout(() => {
                    if (branch.parentNode) branch.parentNode.removeChild(branch);
                    if (glow.parentNode) glow.parentNode.removeChild(glow);
                }, 500);
                
                this.moodAnimations.timeouts.push(removeTimeout);
            }, i * 50);
            
            this.moodAnimations.timeouts.push(timeout);
        }
        
        // Create electric particles around the spark
        for (let i = 0; i < 15; i++) {
            const particleTimeout = setTimeout(() => {
                const particle = document.createElement('div');
                particle.className = 'electric-particle';
                particle.style.cssText = `
                    position: absolute;
                    width: 4px;
                    height: 4px;
                    background: #FFD700;
                    border-radius: 50%;
                    left: ${centerX + (Math.random() - 0.5) * 20}%;
                    top: ${centerY + (Math.random() - 0.5) * 20}%;
                    animation: electricParticle 1s ease-out forwards;
                    pointer-events: none;
                    z-index: 5;
                    box-shadow: 0 0 8px #FFD700;
                `;
                
                this.backgroundEffects.appendChild(particle);
                this.moodAnimations.elements.push(particle);
                
                const removeParticleTimeout = setTimeout(() => {
                    if (particle.parentNode) {
                        particle.parentNode.removeChild(particle);
                    }
                }, 1000);
                
                this.moodAnimations.timeouts.push(removeParticleTimeout);
            }, i * 30);
            
            this.moodAnimations.timeouts.push(particleTimeout);
        }
        
    }, 800); // Lightning every 0.8 seconds
    
        this.moodAnimations.intervals.push(lightningInterval);
    }

    createContinuousWaveEffect() {
        const waveInterval = setInterval(() => {
            const wave = document.createElement('div');
            wave.className = 'mood-wave';
            wave.style.cssText = `
                position: absolute;
                width: 100px;
                height: 100px;
                background: radial-gradient(circle, rgba(0, 255, 127, 0.4) 0%, transparent 70%);
                border-radius: 50%;
                left: ${Math.random() * 100}%;
                top: ${Math.random() * 100}%;
                transform: scale(0);
                animation: waveExpand 4s ease-out forwards;
                pointer-events: none;
                z-index: 5;
            `;
            
            this.backgroundEffects.appendChild(wave);
            this.moodAnimations.elements.push(wave);
            
            const removeTimeout = setTimeout(() => {
                if (wave.parentNode) {
                    wave.parentNode.removeChild(wave);
                }
            }, 4000);
            
            this.moodAnimations.timeouts.push(removeTimeout);
        }, 1500);
        
        this.moodAnimations.intervals.push(waveInterval);
    }

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

    startAnimationLoop() {
        const animate = () => {
            this.updateParticlePositions();
            this.animationFrameId = requestAnimationFrame(animate);
        };
        animate();
    }

    updateParticlePositions() {
        const particles = this.particles.querySelectorAll('.particle');
        particles.forEach(particle => {
            const rect = particle.getBoundingClientRect();
            if (rect.top > window.innerHeight + 100) {
                particle.style.top = '-10px';
                particle.style.left = Math.random() * 100 + '%';
            }
        });
    }

    handleMouseMove(e) {
        const x = e.clientX / window.innerWidth;
        const y = e.clientY / window.innerHeight;
        
        // Create subtle interactive effects
        this.moodOverlay.style.transform = `translate(${x * 10}px, ${y * 10}px)`;
        this.particles.style.transform = `translate(${x * -5}px, ${y * -5}px)`;
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

// Enhanced CSS animations
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

// Initialize the application when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    // 🧠 This makes the loading screen disappear
    initializeLoading();

    // 🎵 This starts the app (mood animations, feedback button, etc.)
    const app = new MusicRecommender();
    window.musicRecommender = app;

    // 🧼 This cleans up effects when page unloads
    window.addEventListener('beforeunload', () => {
        app.destroy();
    });
});


// Service worker registration for PWA capabilities (optional)
if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
        navigator.serviceWorker.register('/sw.js')
            .then(registration => {
                console.log('SW registered: ', registration);
            })
            .catch(registrationError => {
                console.log('SW registration failed: ', registrationError);
            });
    });
}

// Performance monitoring
const observer = new PerformanceObserver((list) => {
    for (const entry of list.getEntries()) {
        if (entry.entryType === 'measure') {
            console.log(`${entry.name}: ${entry.duration}ms`);
        }
    }
});

observer.observe({ entryTypes: ['measure'] });

// Utility functions
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
