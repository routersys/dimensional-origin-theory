# §13: Coincidence Rarity Audit — Quantification of Accidentalness by Exhaustive Scan

← [§12: Formalisation of Axiom Ω](09_formal_system.md) | Next → [§14: Internalisation of the $\mathbf{16}$ Representation Correspondence](11_spinor_internalization.md)

This document counts whether the principal numerical coincidences are reproducible by post-hoc selection, by exhaustive scan of the expression space. The method is as follows: enumerate all natural expressions mechanically generatable from the same materials as those used by the theory, and count how many fall near the observed values. The rarer a coincidence is within that space, the less it can be explained by selection freedom.

## 1. First CMB Peak $\ell_{1} = 220$

Expression space: monomials and two-term combinations $(\pm D_{i} \pm D_{j})/d$ of the $S^{9}$ degeneracies $D_{0}, \ldots, D_{7}$, with $d \in \{1, 2, 4\}$. Total: 360 expressions.

Results:

| Tolerance | Number of expressions falling near 220 |
|-----------|----------------------------------------|
| 0.5% | 1 |
| 1% | 1 |
| 2% | 2 |
| 5% | 6 |

At observational precision (0.5% level), the unique solution in the space is $D_{1} + D_{3} = 220$. Moreover, only this unique solution carries the complete cancellation to the exact binomial-coefficient identity $\binom{12}{3}$. The naive upper bound on the coincidence probability is $1/360 \approx 0.3\%$.

## 2. Acoustic Scale $\Delta\ell = 303$

In the same 360-expression space, the only expression within 2% of 303 is $(D_{4} - D_{2})/2$ (unique even when the tolerance is widened to 5%). Upper bound $1/360 \approx 0.3\%$.

The naive joint upper bound for two independent unique solutions holding simultaneously is approximately $10^{-5}$.

## 3. Coefficient of $\Lambda$: $2(n^{\ast}-2) = 18$

Expression space: 384 expressions formed from binary operations (sum, difference, product) on the natural quantities of the theory $\{2, 3, 8, 9, 10, 11, 45, 90\}$ with coefficients $\{1, 2\}$ allowed. The coefficient window corresponding to within 5% of the observed $\Lambda$ is $[16.8, 18.6]$.

Results: the values in the window are the two candidates $\{17, 18\}$, and there are 7 representations of expressions giving 18 (e.g. $2(n^{\ast}-2) = 2n_{\rm obs}^{2} = (n^{\ast}-1)+(n^{\ast}-3) = \ldots$).

Judgement: this row has weak discriminating power. The numerical value 18 is only one of two candidates in the window, and since the representation of 18 is not unique, the Cartan-decomposition story of §7.3 is one of several equivalent readings. The evidential force for the $\Lambda$ coincidence lies not in the algebraic story of the coefficient but in the coarse structure by which the exponent $\alpha$ suppresses 120 orders of magnitude. The claimed strength of this row should be reduced in the document.

## 4. Limitations of the Method

First, the definition of the expression space is itself a choice, and the results depend on the prior configuration of the space (prior sensitivity). The spaces above are constructed solely from the materials and operations actually used by the theory, minimising but not eliminating arbitrariness. Second, because the theory presents many observables, the overall look-elsewhere effect is larger than the simple product of individual upper bounds. Third, rarity is not a proof of non-post-hoc status; it provides a quantitative lower bound on the explanatory power of the post-hoc hypothesis.

## 5. Conclusions

The two identities for $\ell_{1}$ and $\Delta\ell$ are the unique solutions within the scan space at observational precision and are statistically non-trivial. The $\Lambda$ coefficient lacks discriminating power. The accidentality hypothesis is quantitatively disfavoured for the former two, and cannot be excluded for the coefficient story.

The verification code is included as [coincidence_audit.py](coincidence_audit.py). All procedures — expression-space generation, counting, and tolerance scanning — are reproducible from the code.

---

← [§12: Formalisation of Axiom Ω](09_formal_system.md) | Next → [§14: Internalisation of the $\mathbf{16}$ Representation Correspondence](11_spinor_internalization.md)
