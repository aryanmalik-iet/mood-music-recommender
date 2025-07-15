// Sad Mood Animation: Rain
export function createContinuousRainEffect(backgroundEffects, moodAnimations) {
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
                    top: 0%;
                    animation: rainFall 2s linear forwards;
                    pointer-events: none;
                    z-index: 5;
                `;
                backgroundEffects.appendChild(drop);
                moodAnimations.elements.push(drop);
                const removeTimeout = setTimeout(() => {
                    if (drop.parentNode) {
                        drop.parentNode.removeChild(drop);
                    }
                }, 2000);
                moodAnimations.timeouts.push(removeTimeout);
            }, i * 100);
            moodAnimations.timeouts.push(timeout);
        }
    }, 780);
    moodAnimations.intervals.push(rainInterval);
}

