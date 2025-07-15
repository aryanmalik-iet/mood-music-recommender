// Happy Mood Animation: Bubbles
export function createContinuousBubbleEffect(backgroundEffects, moodAnimations) {
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
                    animation: bubbleRise 4s linear forwards;
                    pointer-events: none;
                    z-index: 5;
                `;
                backgroundEffects.appendChild(bubble);
                moodAnimations.elements.push(bubble);
                const removeTimeout = setTimeout(() => {
                    if (bubble.parentNode) {
                        bubble.parentNode.removeChild(bubble);
                    }
                }, 4000);
                moodAnimations.timeouts.push(removeTimeout);
            }, i * 500);
            moodAnimations.timeouts.push(timeout);
        }
    }, 2000);
    moodAnimations.intervals.push(bubbleInterval);
}

