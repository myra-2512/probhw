from scipy.stats import binom

n = 10
p = 0.5

prob_2 = binom.pmf(2, n, p)
prob_3 = binom.pmf(3, n, p)
prob_4 = binom.pmf(4, n, p)

total_prob = prob_2 + prob_3 + prob_4

print(f"P(X=2): {prob_2:.4f}")
print(f"P(X=3): {prob_3:.4f}")
print(f"P(X=4): {prob_4:.4f}")
print(f"Probability of 2 to 4 heads: {total_prob:.4f}")
