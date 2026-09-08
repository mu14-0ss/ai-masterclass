// Jua Kali job quotation calculator
function buildQuote(jobType, materialCost, labourDays, dailyRate) {
  const labourCost = labourDays * dailyRate;
  const subtotal = materialCost + labourCost;
  const vat = subtotal * 0.16;
  const total = subtotal + vat;
  return {
    job: jobType,
    materials: materialCost,
    labour: labourCost,
    vat: Math.round(vat),
    total: Math.round(total)
  };
}

const jobs = [
  buildQuote("Steel door installation", 12000, 2, 2500),
  buildQuote("Floor tiling (45 sqm)", 8100, 3, 2000),
  buildQuote("Carpentry: 6 chairs", 4800, 4, 1800),
];

jobs.forEach(q => {
  console.log(`Job: ${q.job}`);
  console.log(`  Materials: KES ${q.materials.toLocaleString()}`);
  console.log(`  Labour: KES ${q.labour.toLocaleString()}`);
  console.log(`  VAT (16%): KES ${q.vat.toLocaleString()}`);
  console.log(`  TOTAL: KES ${q.total.toLocaleString()}`);
  console.log("");
});