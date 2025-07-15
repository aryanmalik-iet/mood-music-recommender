// Central export for mood animation modules
import { createContinuousBubbleEffect } from './happy.js';
import { createContinuousRainEffect } from './sad.js';
import { createContinuousHeartEffect } from './romantic.js';
import { createContinuousLightningEffect } from './energetic.js';
import { createContinuousWaveEffect } from './calm.js';

export const moodAnimations = {
    happy: createContinuousBubbleEffect,
    sad: createContinuousRainEffect,
    romantic: createContinuousHeartEffect,
    energetic: createContinuousLightningEffect,
    calm: createContinuousWaveEffect
};

