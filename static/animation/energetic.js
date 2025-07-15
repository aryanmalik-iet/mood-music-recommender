// Energetic Mood Animation: Fire Bursts & Lightning
// Modularized for use in main script.js

export function createContinuousLightningEffect(backgroundEffects, moodAnimations) {
    // SMOOTH FIRE BURSTS (requestAnimationFrame, fewer, smaller, no blur)
    const fireInterval = setInterval(() => {
        const burstCount = Math.floor(Math.random() * 2) + 1; // 1-2 fire bursts per interval
        for (let i = 0; i < burstCount; i++) {
            const fire = document.createElement('div');
            const size = Math.random() * 26 + 26; // 26-52px
            const left = Math.random() * 85 + 7;
            fire.className = 'energetic-fire';
            fire.style.cssText = `
                position: absolute;
                left: ${left}%;
                bottom: -${size/2}px;
                width: ${size}px;
                height: ${size * 1.2}px;
                background: radial-gradient(ellipse at 50% 80%, #fff7a0 0%, #ffb347 40%, #ff7300 75%, transparent 100%);
                border-radius: 45% 45% 65% 65%/60% 60% 100% 100%;
                opacity: 0.8;
                pointer-events: none;
                z-index: 8;
                will-change: transform, opacity;
            `;
            backgroundEffects.appendChild(fire);
            moodAnimations.elements.push(fire);
            // Animate with rAF
            let start = null;
            const duration = 900 + Math.random() * 180; // 0.9-1.08s
            const startBottom = -size/2;
            const endBottom = window.innerHeight * 0.6;
            function animateFire(ts) {
                if (!start) start = ts;
                const elapsed = ts - start;
                const progress = Math.min(elapsed / duration, 1);
                fire.style.bottom = `calc(${startBottom}px + ${(endBottom - startBottom) * progress}px)`;
                fire.style.opacity = 0.8 - progress * 0.8;
                if (progress < 1) {
                    requestAnimationFrame(animateFire);
                } else {
                    if (fire.parentNode) fire.parentNode.removeChild(fire);
                }
            }
            requestAnimationFrame(animateFire);
        }
    }, 850); // slightly slower
    moodAnimations.intervals.push(fireInterval);

    // SMOOTH LIGHTNING (limit to 1 at a time, less frequent)
    let lightningActive = false;
    const lightningInterval = setInterval(() => {
        if (!lightningActive && Math.random() > 0.75) {
            lightningActive = true;
            const bolt = document.createElement('div');
            const startX = Math.random() * 80 + 10;
            const startY = Math.random() * 30 + 5;
            const length = Math.random() * 90 + 70;
            const angle = Math.random() * 60 - 30;
            bolt.className = 'energetic-lightning';
            bolt.style.cssText = `
                position: absolute;
                left: ${startX}%;
                top: ${startY}%;
                width: 3px;
                height: ${length}px;
                background: linear-gradient(to bottom, #fffbe0 0%, #ffe259 40%, #ff7300 90%, transparent 100%);
                border-radius: 2px 2px 12px 12px;
                box-shadow: 0 0 12px 3px #fffbe0, 0 0 22px 4px #ff7300;
                opacity: 0.87;
                transform: rotate(${angle}deg);
                pointer-events: none;
                z-index: 11;
                will-change: opacity, transform;
            `;
            backgroundEffects.appendChild(bolt);
            moodAnimations.elements.push(bolt);
            // Animate with rAF fade
            let start = null;
            const duration = 300 + Math.random() * 90; // 300-390ms
            function animateBolt(ts) {
                if (!start) start = ts;
                const elapsed = ts - start;
                const progress = Math.min(elapsed / duration, 1);
                bolt.style.opacity = 0.87 - progress * 0.87;
                if (progress < 1) {
                    requestAnimationFrame(animateBolt);
                } else {
                    if (bolt.parentNode) bolt.parentNode.removeChild(bolt);
                    lightningActive = false;
                }
            }
            requestAnimationFrame(animateBolt);
        }
    }, 320);
    moodAnimations.intervals.push(lightningInterval);
}


