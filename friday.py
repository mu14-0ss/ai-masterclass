// Rule-based prediction engine
// Returns { hitGoal: bool, confidence: number (0-1), score: number }

const predictGoal = (sleep, water, steps) => {
  // Weighted score (max 100)
  const sleepScore = Math.min(sleep / 8.0, 1.0) * 35;   // 35% weight
  const waterScore = Math.min(water / 10.0, 1.0) * 25;  // 25% weight
  const stepsScore = Math.min(steps / 12000, 1.0) * 40; // 40% weight

  const totalScore  = sleepScore + waterScore + stepsScore;
  const hitGoal     = totalScore >= 60;

  // Confidence: how far from the 60-point threshold (capped at 95%)
  const distance    = Math.abs(totalScore - 60);
  const confidence  = Math.min(0.50 + distance * 0.012, 0.95);

  return { hitGoal, confidence, score: Math.round(totalScore) };
};

// Test cases
const testDays = [
  { label: "Strong day",    sleep: 8.0, water: 10, steps: 12100 },
  { label: "Weak day",      sleep: 5.5, water:  4, steps:  7800 },
  { label: "Borderline",    sleep: 7.0, water:  8, steps:  9500 },
  { label: "Sleep-focused", sleep: 9.0, water:  6, steps:  8000 },
];

testDays.forEach(d => {
  const result = predictGoal(d.sleep, d.water, d.steps);
  const out = result.hitGoal ? "HIT" : "MISS";
  console.log(`${d.label.padEnd(16)} | Score: ${String(result.score).padStart(2)}  | ${out} | Conf: ${(result.confidence * 100).toFixed(0)}%`);
});
