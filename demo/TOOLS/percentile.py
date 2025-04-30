from tdigest import TDigest
import random

# Initialize a t-digest
digest = TDigest()

# Simulate streaming data. For example, adding 10,000 random numbers.
for _ in range(10000):
    value = random.uniform(0, 100)  # Random float between 0 and 100
    digest.update(value)

# Querying for quantiles
median = digest.percentile(50)  # Approximate median
p90 = digest.percentile(90)     # Approximate 90th percentile
p95 = digest.percentile(95)     # Approximate 95th percentile

print(f"Approximate median: {median}")
print(f"Approximate 90th percentile: {p90}")
print(f"Approximate 95th percentile: {p95}")