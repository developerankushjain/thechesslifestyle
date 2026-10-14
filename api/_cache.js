// Simple in-memory cache for deduplication of processed payments within warmed serverless lambdas
const processedPayments = new Map();

export function isAlreadyProcessed(paymentOrOrderId) {
  if (!paymentOrOrderId || paymentOrOrderId === 'FREE_ENTRY') {
    return false;
  }
  
  const now = Date.now();
  // Cleanup entries older than 24 hours
  for (const [id, timestamp] of processedPayments.entries()) {
    if (now - timestamp > 86400000) {
      processedPayments.delete(id);
    }
  }

  if (processedPayments.has(paymentOrOrderId)) {
    return true;
  }

  processedPayments.set(paymentOrOrderId, now);
  return false;
}
