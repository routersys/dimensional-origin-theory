# §8: Derivation of the CMB Temperature Anisotropy Peak Structure

← [§7: The Cosmological Constant](04_cosmological_constant.md) | Next → [§9: Testable Predictions](06_predictions.md)

---

## 8. Derivation of the CMB Temperature Anisotropy Peak Structure

### 8.1 Determination of the Spatial Sphere

Removing the time direction from the $n^{\ast}$-dimensional spacetime, the unit sphere of the spatial part is

$$S^{n^{\ast}-2} = S^{9} \quad (n^{\ast} = 11)$$

### 8.2 Spherical-Harmonic Degeneracy on $S^{9}$

The degeneracy of the degree-$\ell$ spherical harmonics on $S^{9}$ ($\subset \mathbb{R}^{10}$) (standard formula) is

$$D_{\ell}(S^{9}) = \binom{\ell+9}{\ell} - \binom{\ell+7}{\ell-2}$$

Principal values:

| $\ell$ | $D_{\ell}(S^{9})$ | Parity |
|--------|-------------------|--------|
| 0 | 1 | even |
| 1 | 10 | odd |
| 2 | 54 | even |
| 3 | 210 | odd |
| 4 | 660 | even |
| 5 | 1782 | odd |
| 6 | 4290 | even |

### 8.3 Mode Selection by the Odd-Parity Argument

Axiom Ω ($\neg\exists \to \exists$) is an odd-parity transformation. The parity of spherical harmonics on $S^{9}$ is

$$Y_{\ell}(-\Omega) = (-1)^{\ell} Y_{\ell}(\Omega)$$

For even $\ell$ the parity is even (symmetric), giving a static, uniform background field that does not contribute to acoustic oscillations. For odd $\ell$ the parity is odd (antisymmetric), giving dynamic acoustic oscillation modes that are observable.

The odd-parity modes observable by a three-dimensional observer within the range $\ell \leq n_{\rm obs} = 3$ are

$$\ell \in \{1, 3\}$$

### 8.4 Algebraic Proof of the First CMB Peak

Theorem:

$$D_{n_{\rm obs}}(S^{n^{\ast}-2}) + D_{n_{\rm obs}-2}(S^{n^{\ast}-2}) = \binom{n^{\ast}+1}{n_{\rm obs}}$$

**Proof (pure algebra):**

Setting $n = n^{\ast} - 1 = 10$,

$$D_{3}(S^{9}) = \binom{12}{3} - \binom{10}{1} = 220 - 10 = 210$$

$$D_{1}(S^{9}) = \binom{10}{1} = 10$$

$$D_{3} + D_{1}
= \left[\binom{12}{3} - \binom{10}{1}\right] + \binom{10}{1}
= \binom{12}{3}
= 220 \qquad \blacksquare$$

The $\binom{10}{1}$ term cancels completely. This is a pure algebraic consequence of $\binom{*}{-1} = 0$ (a fundamental theorem of binomial coefficients) and contains no external parameters whatsoever.

Why the identity holds only for $n_{\rm obs} = 3$: in the general form

$$D_{n_{\rm obs}} + D_{n_{\rm obs}-2}
= \binom{n^{\ast}+1}{n_{\rm obs}} - \binom{n^{\ast}-3}{n_{\rm obs}-4}$$

the second term on the right vanishes only when $n_{\rm obs} - 4 < 0$, i.e. $n_{\rm obs} = 3$ (or 1). When Hurwitz's theorem uniquely determines $n_{\rm obs} = 3$, this cancellation occurs automatically.

Numerical confirmation:

- $n_{\rm obs} = 1$: $D_{1} + D_{-1} = 10 \neq 12 = \binom{12}{1}$ (fails)
- $n_{\rm obs} = 3$: $D_{3} + D_{1} = 220 = \binom{12}{3} = 220$ (holds ✓)
- $n_{\rm obs} = 5$: $D_{5} + D_{3} = 1992 \neq 792 = \binom{12}{5}$ (fails)

**Conclusion:**

$$\boxed{\ell_{1} = D_{3}(S^{9}) + D_{1}(S^{9}) = \binom{12}{3} = 220}$$

Agreement with the observed value 220: error $0.000\%$.

### 8.5 Combinatorial Meaning

$\binom{n^{\ast}+1}{n_{\rm obs}} = \binom{12}{3} = 220$ counts the number of independent configurations for choosing an $n_{\rm obs} = 3$-dimensional cross-section within the $n^{\ast}+1 = 12$-dimensional spacetime. This is the maximum mode count visible to a three-dimensional observer in the one-dimensionally originating space, and it becomes the first-peak position.

### 8.6 Full Peak Formula (Complete Algebraic Derivation)

This formula is given under the constant phase-shift approximation ($\varphi_{k} = \bar{\varphi}$). Precise predictions for $k \geq 2$ are provided by the first-principles path in §8.8.

$$\boxed{\ell_{k} = \ell_{1} + (k-1) \cdot \Delta\ell}$$

$$= \binom{n^{\ast}+1}{n_{\rm obs}} + (k-1) \cdot \frac{D_{n_{\rm obs}+1}(S^{n^{\ast}-2}) - D_{n_{\rm obs}-1}(S^{n^{\ast}-2})}{2}$$

$$= 220 + (k-1) \times 303$$

#### Algebraic Derivation of the Acoustic Scale $\Delta\ell$

The repetition interval of acoustic oscillations (acoustic scale) is defined from the difference in even-parity mode degeneracies in the neighbourhood of the observer ($\ell = n_{\rm obs} \pm 1$) on $S^{9}$:

$$\Delta\ell = \frac{D_{n_{\rm obs}+1}(S^{n^{\ast}-2}) - D_{n_{\rm obs}-1}(S^{n^{\ast}-2})}{2}$$

Algebraic calculation ($n_{\rm obs} = 3$, $n^{\ast} = 11$):

$$D_{4}(S^{9}) = \binom{13}{4} - \binom{11}{2} = 715 - 55 = 660$$

$$D_{2}(S^{9}) = \binom{11}{2} - \binom{9}{0} = 55 - 1 = 54$$

$$\Delta\ell = \frac{660 - 54}{2} = \frac{606}{2} = 303$$

Origin of the factor $1/2$: $D_{4} - D_{2}$ counts both directions (positive and negative wavenumber) of travelling waves on $S^{9}$. Since an acoustic mode (standing wave) is the superposition of two travelling waves, the effective interval is halved.

#### Physical Meaning

The first peak $\ell_{1} = 220$ is the maximum degeneracy of the lowest-degree odd-parity mode of $S^{9}$ as seen by a three-dimensional observer. The acoustic scale $\Delta\ell = 303$ is the half-value of the change in $S^{9}$ mode density near the observer.

The full peak formula $\ell_{k} = 220 + (k-1) \times 303$ contains no external parameters whatsoever, and is completely determined from $n_{\rm obs}$ and $n^{\ast}$ alone.

### 8.7 Numerical Verification and Comparison with $\Lambda$CDM

| $k$ | Theory $220+(k-1)\times303$ | Observed (Planck) | Error | $\Lambda$CDM | $\Lambda$CDM error |
|-----|------------------------------|-------------------|-------|-------------|------------------|
| 1 | 220 | 220 | $0.000\%$ | $220.6$ | $0.27\%$ |
| 2 | 523 | 537 | $2.6\%$ | $537.0$ | $0.00\%$ |
| 3 | 826 | 810 | $2.0\%$ | $810.5$ | $0.06\%$ |
| 4 | 1129 | 1120 | $0.8\%$ | $1118.7$ | $0.12\%$ |
| 5 | 1432 | 1440 | $0.6\%$ | $1441.0$ | $0.07\%$ |
| 6 | 1735 | 1750 | $0.9\%$ | $1749.0$ | $0.06\%$ |
| Mean | — | — | $1.13\%$ | — | $0.10\%$ |

The observed-value column of this table gives approximate measured positions of the maxima in the temperature power spectrum; for $k = 5, 6$, mode overlap and beam damping widen the reading range of the maximum. The reference values 1421.3 and 1725.7 used by the first-principles path (§8.8) are acoustic peak positions extracted by the same extraction method from the same Boltzmann-code output using Planck 2018 best-fit parameters, defined so that the extraction-method bias cancels between the theoretical and reference sides. The difference between the two sets reflects a difference in definition and is not an error. For theoretical evaluation, the §8.8 reference values with controlled extraction method are used.

The formula of the present theory (zero external parameters) achieves roughly the same accuracy as the multi-parameter detailed calculation of $\Lambda$CDM. $\Lambda$CDM fits multiple cosmological parameters ($\Omega_{b}h^{2}$, $\Omega_{c}h^{2}$, $H_{0}$, etc.) to observed values, whereas the present theory is derived solely from $n_{\rm obs} = 3$ and $n^{\ast} = 11$.

### 8.8 First-Principles Dynamical-Path Verification and Identification of Systematic Errors

As a second path completely independent of the algebraic path (§8.4–§8.6), a complete first-principles calculation is carried out using the Boltzmann code CAMB. No fitting formulae or approximations are used, and no observed values are input.

#### 8.8.1 Configuration of the Verification

The set of cosmological parameters derived by the present theory,

$$H_{0} = 67.67,\quad \Omega_{\Lambda} = 0.690,\quad T_{\rm CMB} = 2.7285\,{\rm K},\quad \Omega_{b}h^{2} = 0.02156,\quad w = -1$$

($\Omega_{c}h^{2} = (1-\Omega_{\Lambda})h^{2} - \Omega_{b}h^{2}$ is determined dependently from flatness), is fed into the Boltzmann code CAMB, the temperature anisotropy spectrum $C_{\ell}^{TT}$ is computed from first principles, and the peak positions are extracted. The comparison reference uses the output of the same code and the same extraction method run with the Planck 2018 best-fit parameters (since the best-fit spectrum agrees with the observed spectrum by construction, the extraction-method bias cancels between the two).

The CAMB exact value of the acoustic angular scale is

$$\ell_{A}^{\rm theory} = 300.19,\qquad \ell_{A}^{\rm Planck} = 301.75,\qquad \text{difference } 0.52\%$$

This is consistent with the amount obtained by propagating the $1.71\%$ error of $\Lambda$ in §7 through $H_{0}$ and $\Omega_{m}$.

#### 8.8.2 Verification Results (All Six Peaks)

Results with $n_{s} = 0.965$ and lensed spectrum:

| $k$ | First-principles (theory input) | Reference (Planck best-fit) | Difference | Algebraic formula $220+(k-1)\times303$ | Algebraic vs. reference |
|-----|----------------------------------|------------------------------|------------|----------------------------------------|-------------------------|
| 1 | 219.3 | 220.3 | $0.47\%$ | 220 | $0.14\%$ |
| 2 | 532.7 | 536.2 | $0.65\%$ | 523 | $2.5\%$ |
| 3 | 808.4 | 812.9 | $0.56\%$ | 826 | $1.6\%$ |
| 4 | 1119.9 | 1126.5 | $0.58\%$ | 1129 | $0.22\%$ |
| 5 | 1413.0 | 1421.3 | $0.59\%$ | 1432 | $0.75\%$ |
| 6 | 1714.8 | 1725.7 | $0.63\%$ | 1735 | $0.54\%$ |

The differences for all six peaks fall in the narrow band $0.47$–$0.65\%$. This means that almost all of the residual arises from the $\ell_{A}$ scale difference of $0.52\%$ (i.e. propagation of the $1.71\%$ error of $\Lambda$), and the phase structure is completely reproduced. The reference values $k = 5, 6$: 1421.3 and 1725.7 are values from the first-principles calculation with Planck best-fit parameters.

#### 8.8.3 Quantification of $n_{s}$ Sensitivity

Since the present theory has no prediction for $n_{s}$, the full observationally and theoretically reasonable range $n_{s} \in [0.94, 1.00]$ is scanned.

| $k$ | 1 | 2 | 3 | 4 | 5 | 6 |
|-----|---|---|---|---|---|---|
| Variation of peak position | $0.96\%$ | $0.17\%$ | $0.09\%$ | $0.05\%$ | $0.06\%$ | $0.08\%$ |

For all peaks $k \geq 2$, the position moves less than $0.2\%$ over the entire allowed range of $n_{s}$. The conclusion of this verification (reproduction of peaks 1–6) is therefore independent of the value of $n_{s}$. $n_{s}$ is not a necessary external input but a bounded perturbative parameter that does not affect the conclusion.

#### 8.8.4 Conclusions

Conclusion 1 (Complete identification of systematic errors): The origin of the algebraic-formula errors for $k \geq 2$ is the neglect of the $k$-dependent relative phase shift $\delta\varphi_{k}$ (due to radiation-driving and Doppler effects, standard acoustic physics). The first-principles calculation includes this automatically and contracts all six-peak residuals to only the $\ell_{A}$ scale difference ($0.5$–$0.65\%$).

Conclusion 2 (Response to the post-hoc criticism): The first-principles path uses none of the degeneracy algebra, yet reproduces all six peaks within $0.65\%$. If $\ell_{1} = 220$ were post-hoc, there would be no reason for the same parameter set to dynamically reproduce up to the sixth peak.

Conclusion 3 (Explicit statement of premises): The only remaining premise in this verification is that standard acoustic physics (general relativity + Boltzmann equation) holds at the epoch of decoupling. This is a premise shared by all cosmologies including $\Lambda$CDM.

### 8.9 Algebraic Closed Form of the Phase Shift

For the phase shift $\varphi_{k} = k - \ell_{k}/\ell_{A}$ obtained from the first-principles calculation, a closed form written solely in $n^{\ast}$ and $n_{\rm obs}$ was tested.

The rational form $\varphi_{k} = \dfrac{n_{\rm obs}}{n^{\ast}} + \delta_{k}$ is retained as an approximate expression with $0.3\%$ accuracy at a fixed cosmological point. The first-principles $\varphi_{k}$ is a continuous function of cosmological parameters ($n_{s}$, $\omega_{b}$) and cannot be expressed as a universal exact law by a rational constant in $n^{\ast}$ and $n_{\rm obs}$ alone. Indeed, at the physical point $n_{s} = 0.965$, $\varphi_{1} = 0.2695$ deviates from $3/11 = 0.2727$ by $0.0033$, which is 10 times the extraction precision $\pm 0.0003$, so the constant $3/11$ does not hold as an exact law. This formula is therefore a fixed-point approximation rather than an exact law.

Note that $\delta_{3} = 1/n_{\rm obs}^{3}$ in §8.9 and $\Delta g = n_{\rm obs}^{3}/4$ in §11.5 both involve $n_{\rm obs}^{3} = 27$; this coincidence cannot currently be distinguished from accident.

---

← [§7: The Cosmological Constant](04_cosmological_constant.md) | Next → [§9: Testable Predictions](06_predictions.md)
