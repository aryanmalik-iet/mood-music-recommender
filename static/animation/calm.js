// Calm Mood Animation: Waves
export function createContinuousWaveEffect(backgroundEffects, moodAnimations) {
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
        backgroundEffects.appendChild(wave);
        moodAnimations.elements.push(wave);
        const removeTimeout = setTimeout(() => {
            if (wave.parentNode) {
                wave.parentNode.removeChild(wave);
            }
        }, 4000);
        moodAnimations.timeouts.push(removeTimeout);
    }, 1500);
    moodAnimations.intervals.push(waveInterval);
}

