// Romantic Mood Animation: Hearts
export function createContinuousHeartEffect(backgroundEffects, moodAnimations) {
    const firstBatch = Math.floor(Math.random() * 4) + 3; // 3 to 6
    for (let i = 0; i < firstBatch; i++) {
        setTimeout(() => {
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
            backgroundEffects.appendChild(heart);
            moodAnimations.elements.push(heart);
            const removeTimeout = setTimeout(() => {
                if (heart.parentNode) {
                    heart.parentNode.removeChild(heart);
                }
            }, 5000);
            moodAnimations.timeouts.push(removeTimeout);
        }, Math.random() * 1000);
    }
    const heartInterval = setInterval(() => {
        const numHearts = Math.floor(Math.random() * 4) + 3; // 3 to 6
        for (let i = 0; i < numHearts; i++) {
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
                backgroundEffects.appendChild(heart);
                moodAnimations.elements.push(heart);
                const removeTimeout = setTimeout(() => {
                    if (heart.parentNode) {
                        heart.parentNode.removeChild(heart);
                    }
                }, 5000);
                moodAnimations.timeouts.push(removeTimeout);
            }, Math.random() * 3000);
            moodAnimations.timeouts.push(timeout);
        }
    }, 3000);
    moodAnimations.intervals.push(heartInterval);
}

