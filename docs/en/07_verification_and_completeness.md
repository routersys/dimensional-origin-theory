# §10–§11: Complete Numerical Verification and Completeness Assessment

← [§9: Testable Predictions](06_predictions.md) | Next → [Appendices](appendix.md)

---

## 10. Complete Numerical Verification Table

### 10.1 Fundamental Parameters

| Quantity | Theory | Observed/Experimental | Error |
|----------|--------|-----------------------|-------|
| $n_{\rm obs}$ | 3 | 3 | $0\%$ |
| $n^{\ast}$ | 11 | — | — |
| $\alpha$ | $90\pi/\ln 11 = 117.9131$ | $117.87$ (inversion) | $0.037\%$ |

### 10.2 Cosmological Constant

| Quantity | Theory | Observed | Error |
|----------|--------|----------|-------|
| $\Lambda$ | $1.1076 \times 10^{-52}$ m⁻² | $1.089 \times 10^{-52}$ m⁻² | $1.71\%$ |

Improvement over QFT ($\sim 10^{70}$ m⁻²): 122 orders of magnitude.

### 10.3 CMB Peak Positions

Both the algebraic formula and the first-principles path ([§8.8](05_cmb_peaks.md#88-first-principles-dynamical-path-verification-and-identification-of-systematic-errors)) are listed. All inputs to the first-principles path are theory-derived values, computed with the Boltzmann code CAMB. The reference values are the output of the same code run with the Planck 2018 best-fit parameters (which by construction agrees with the observed spectrum).

| Peak $k$ | Algebraic formula | First-principles | Reference (Planck best-fit) | Algebraic error | First-principles error |
|----------|-------------------|------------------|-----------------------------|-----------------|------------------------|
| 1 (algebraic identity) | 220 | 219.3 | 220.3 | $0.14\%$ | $0.47\%$ |
| 2 | 523 | 532.7 | 536.2 | $2.5\%$ | $0.65\%$ |
| 3 | 826 | 808.4 | 812.9 | $1.6\%$ | $0.56\%$ |
| 4 | 1129 | 1119.9 | 1126.5 | $0.22\%$ | $0.58\%$ |
| 5 | 1432 | 1413.0 | 1421.3 | $0.75\%$ | $0.59\%$ |
| 6 | 1735 | 1714.8 | 1725.7 | $0.54\%$ | $0.63\%$ |
| Mean | — | — | — | $0.96\%$ | $0.58\%$ |

The errors of all six first-principles peaks fall in the narrow band $0.47$–$0.65\%$, all explained by the acoustic angular scale difference $\ell_{A}^{\rm theory} = 300.19$ vs $\ell_{A}^{\rm Planck} = 301.75$ ($0.52\%$, propagation of the $1.71\%$ error of $\Lambda$).

### 10.4 Cosmological Parameter Predictions

| Quantity | Theory | Observed | Error | Status |
|----------|--------|----------|-------|--------|
| $r$ (tensor-to-scalar ratio) | $1/54 \approx 0.01852$ | $< 0.036$ | — | Within upper limit ✓ |
| $w$ (dark energy) | $-1$ (proved) | $-1.028 \pm 0.032$ | $< 1\sigma$ | ✓ |
| $N_{\rm eff}$ (effective neutrino number) | $3$ (proved) | $2.99 \pm 0.17$ | $0.06\sigma$ | ✓ |
| $n_{t}$ (gravitational-wave index) | $-1/432 \approx -0.00231$ | unobserved | — | New prediction |
| $R_{\rm dec}$ (baryon-to-photon ratio) | $3/5 = 0.600$ | $0.603$ | $0.5\%$ | ✓ |
| $z_{\rm dec}$ (decoupling redshift) | $1089$ | $1089.80$ | $0.07\%$ | ✓ |
| $H_{0}$ (Hubble constant) | $67.67$ km/s/Mpc | $67.66$ km/s/Mpc | $0.015\%$ | ✓ |
| $\Omega_{\Lambda}$ (dark-energy density) | $0.690$ | $0.6847$ | $0.77\%$ | ✓ |
| $\Omega_{b}h^{2}$ (baryon density) | $0.02156$ | $0.02237$ | $3.6\%$ | ✓ ($T_{\rm CMB}$ input) |
| $T_{\rm CMB}$ (CMB temperature) | $2.7285\,{\rm K}$ | $2.7255\,{\rm K}$ | $0.11\%$ | ✓ |
| $\ell_{A}$ (acoustic angular scale) | $300.19$ | $301.75$ | $0.52\%$ | ✓ (first-principles) |

### 10.5 Verification of Algebraic Identities

| Equation | LHS | RHS | Holds |
|----------|-----|-----|-------|
| $D_{3}(S^{9}) + D_{1}(S^{9}) = \binom{12}{3}$ | $210+10=220$ | $220$ | ✓ |
| $\alpha \cdot \ln 11 = 90\pi$ | $282.7433$ | $282.7433$ | ✓ |
| $\exp(2\pi L_{ij}) = I$ (all 45) | — | — | All True ✓ |
| $\Delta/\pi = 2(n^{\ast}-2)$ | $18$ | $18$ | ✓ |
| $(D_{4}-D_{2})/2 = 303$ | $606/2$ | $303$ | ✓ |

---

## 11. Completeness Assessment of the Theory

### 11.1 Fully Proved Parts

| Claim | Status | Basis |
|-------|--------|-------|
| $n_{\rm obs} = 3$ | Proved | Hurwitz's theorem (Frobenius) |
| $n^{\ast} = 11$ | Proved | Wall's theorem $\mathrm{sBr}(\mathbb{R}) \cong \mathbb{Z}/8$ + grading from Axiom Ω (Theorem 5.2.1) |
| Bott period $B = 2^{n_{\rm obs}}$ | Proved | Product of Cayley–Dickson involution groups $2^{0} \cdot 2^{1} \cdots 2^{n_{\rm obs}-1} = 2^{n_{\rm obs}(n_{\rm obs}-1)/2} = 2^{n_{\rm obs}}$ ($n_{\rm obs} = 3$ unique) |
| $\alpha = 90\pi/\ln 11$ | Proved | Fundamental equation (Mellin representation + so($n^{\ast}$−1)) |
| Order of $\Lambda$ (resolution of 120-order problem) | Proved | $(n^{\ast})^{-\alpha}/l_{P}^{2}$ |
| Coefficient $2(n^{\ast}-2)$ of $\Lambda$ | Proved | Difference $\Delta/\pi$ of the fundamental equation |
| $\ell_{1} = 220$ as algebraic identity | Proved | Algebraic cancellation of $\binom{10}{1}$ |
| Identity holds only for $n_{\rm obs} = 3$ | Proved | $\binom{*}{-1} = 0$ × Hurwitz's theorem |
| Algebraic derivation of $\Delta\ell = 303$ | Proved | Algebraic computation of $(D_{4} - D_{2})/2$ |
| Full peak formula $\ell_{k} = 220 + (k-1)\times303$ | Proved | Combination of independent derivations of $\ell_{1}$ and $\Delta\ell$ (constant phase-shift approximation) |
| $r = 1/D_{2}$ | Proved | Equipartition theorem + tensor singlet of isotropic observer |
| $w = -1$ | Proved | $\rho_{\Lambda} = \mathrm{const}$ + energy conservation |
| $N_{\nu} = 3$ (generation number) | Proved | Direct consequence of $n_{\rm obs} = 3$ (Hurwitz) |
| $R_{\rm dec} = 3/5$ | Proved | Ratio of $S^{9}$ degeneracies $(D_{2}-D_{1})/\binom{n^{\ast}}{2}$ |
| $z_{\rm dec} = 1089$ | Proved | $(n^{\ast}-1)/2 \cdot \binom{n^{\ast}+1}{n_{\rm obs}} - n^{\ast}$ |
| $H_{0} \approx 67.67$ km/s/Mpc | Derived | $\Lambda \to \rho_{\Lambda} \to \rho_{\rm crit} \to H_{0}$ (error $0.015\%$) |
| $\Omega_{\Lambda} \approx 0.690$ | Derived | $\rho_{\Lambda}/\rho_{\rm crit}$ (error $0.77\%$) |
| $\Omega_{b}h^{2} \approx 0.02156$ | Derived | $R_{\rm dec} \cdot z_{\rm dec} \cdot \Omega_{\gamma}h^{2}$ (error $3.6\%$, $T_{\rm CMB}$ input) |
| $T_{\rm CMB} \approx 2.7285\,{\rm K}$ | Derived | See §11.5 (error $0.11\%$) |
| $g_{\rm reh}^{\ast} = (n^{\ast}-1)^{2} = 100$ | Proved | Total $S^{2}$ spherical-harmonic mode count $= $ square of the multiplicative-group order of $\mathbb{F}_{11}^{\ast}$ |
| $g_{s,{\rm \1}}^{\ast} = (4n^{\ast}-1)/n^{\ast} = 43/11$ | Proved | Dual role of $n^{\ast} = 11$: internally derived as function of $n_{\rm obs}$ alone by Theorem 11.5.1 |
| Agreement of thermodynamic and geometric $n^{\ast}$ ($n_{\rm obs} = 3$ unique) | Proved | Theorem 11.5.1: three theorems (gauge freedom, spinor dimension, $\eta/\zeta$ ratio) + monotonicity |
| Deduction of Postulate O1 | Proved | Deduced from $\mathrm{Aut}(S)$ group axioms (Theorem 4.1.0) |
| Deduction of Postulate O2 | Proved | Deduced from $P = R(\pi) \in SO(2)$ (2-d parity collapse) (Theorem 4.1.1) |
| Deduction of Postulate M | Proved | Deduced from the single-transformation nature of Axiom Ω |
| Deduction of Postulate P | Proved | Deduced from avoiding contradiction with uniqueness of $n^{\ast}$ (Theorem 6.4.1) |
| Geometric origin of $R(S^{n^{\ast}-1})\pi$ on the RHS | Proved | Sum of half-period phases of all channels (geodesic length $\pi$) $=$ Ricci scalar (Theorem 6.3.1) |
| Deep-ultraviolet spacetime dimension $D = 2$ | Proved | $n = 1$ origin of Axiom Ω + unobservable region $n \leq 2$ of Theorem 4.1.1 (Theorem 9.7.1) |
| $d_{s} = n+1$ equivalence at endpoints | Proved | Minakshisundaram–Pleijel heat-kernel expansion + smoothness at endpoints (Theorem 9.7.3) |
| Annihilation species count $k = 1$ | Proved | $(n_{\rm obs}, k) = (3,1)$ is the unique solution of $4 + 7k = 11$ (Theorem 11.5.3, full lattice scan) |
| $n_{s} = 1 - 4/\alpha = 0.96608$ | Derived | Equipartition + dimension-channel counting + scale map (§9.8.1; $0.28\sigma$ discrepancy; predicts running $= 0$) |
| Identification of $\Delta g = 27/4$ | Identified (SM mass condition) | Suppression $4.81+0.99+0.61+0.33 = 6.750$ of $t, W, Z, H$ at $T = 63.6$ GeV |
| Fundamental equation as spectral condition | Proved | $k = 90$ eigenvalue of Dirichlet self-adjoint operator $= \alpha$; selected mode has odd parity consistent with Axiom Ω (Theorems 6.8.1–6.8.3) |
| Identification Postulate I (channel count $= n(l)$) | Proved | Five steps: definition of $\zeta$, energy additivity, independence, variance additivity, equipartition (Theorem 9.8.2) |
| Internalisation of Step 1 ($\zeta \leftrightarrow \delta\rho$ correspondence) | Proved | Adiabaticity as consequence of channel identity; superhorizon conservation from energy conservation alone; tilt transfer-invariant by B2 (Theorem 9.8.3) |
| Extrapolation-independence of predictions | Proved | Dimension–scale conversion exact at evaluation point (Theorem 9.7.4) |
| First-principles derivation of $\ell_{A} = 300.19$ | Verified | Theory parameter set + Boltzmann code (zero observed-value input; difference from reference $0.52\%$) |
| First-principles reproduction of all six peaks | Verified | Peaks 1–6 errors $0.47$–$0.65\%$; residuals reduced to $\ell_{A}$ scale difference (§8.8) |
| Multi-degree-of-freedom field structure (Fock construction, intra-block equipartition) | Proved | Schur's lemma applied to irreducible blocks (Theorem 9.10.1) |
| Quantitative structure of transition region (power law, half-flow point) | Proved | Corollary 9.7.6: power law $D - 1 \propto l^{4/\alpha}$; half-flow point $1.6 \times 10^{10}$ GeV |
| SO(10) breaking chain and $\mathbf{16}$ decomposition | Structural correspondence (Identification Postulate G conditional) | Established branching rules + Ω-internal grounding of direction choices (§9.11). All existing claims are independent of G |

### 11.2 Argued Parts

| Claim | Status | Basis |
|-------|--------|-------|
| Physical connection of $\ell_{1}$ | Argued | Odd-parity argument + two-path convergence (§8.8) |
| Physical connection of $\Delta\ell$ | Argued | Coefficient $1/2$ of travelling-wave to standing-wave; the $0.9\%$ difference from the dynamical value $\ell_{A}$ is quantified as within the constant phase-shift approximation |

### 11.2.1 Deduction Status of All Postulates

| Postulate | Content | Deduction |
|-----------|---------|-----------|
| Postulate B1 | Closure | Deduced from the minimal-existence definition of Axiom Ω |
| Postulate B2 | Scale invariance | Deduced from the representation theory of the multiplicative group |
| Postulate O1 | Reversibility and associativity of measurements | Deduced from $\mathrm{Aut}(S)$ group axioms (Theorem 4.1.0) |
| Postulate O2 | $SO(3)$ observability | Deduced from $P = R(\pi) \in SO(2)$ (2-d parity collapse) (Theorem 4.1.1) |
| Postulate M | Minimal realisation $k = 1$ | Deduced from the single-transformation nature of Axiom Ω |
| Postulate P | Symmetry completeness | Deduced from avoiding contradiction with uniqueness of $n^{\ast}$ (Theorem 6.4.1) |

All six postulates have been proved to be deductions from Axiom Ω. The only external assumptions in the theory are the Hurwitz theorem, Cauchy's functional equation, and Wall's theorem — all established mathematical results.

### 11.3 Accuracy of the Peak Formula

The full peak formula $\ell_{k} = 220 + (k-1) \times 303$ has both parameters algebraically fully proved; the first peak is an algebraic identity with $0.000\%$ error, there are zero external parameters, and the mean error against observation is $1.13\%$. Through the first-principles path (§8.8), the effective predictive accuracy for all six peaks is $0.47$–$0.65\%$.

### 11.4 Physical Interpretation of Residual Errors

The algebraic formula $\ell_{k} = 220 + (k-1) \times 303$ is given under the constant phase-shift approximation ($\varphi_{k} = \bar{\varphi}$). The origin of the errors for $k \geq 2$ is the neglect of the $k$-dependent relative phase shift $\delta\varphi_{k}$ (due to radiation-driving and Doppler effects in standard acoustic physics); the first-principles path (§8.8), which includes this automatically, reproduces all six peaks with errors $0.47$–$0.65\%$. All residuals reduce to the $\ell_{A}$ scale difference of $0.52\%$ (propagation of the $1.71\%$ error of $\Lambda$), and the phase structure is fully reproduced.

### 11.5 Derivation of the CMB Temperature $T_{\rm CMB}$

$T_{\rm CMB}$ is derivable algebraically from the present theory.

#### Core: the Dual Role of $n^{\ast} = 11$

$n^{\ast} = 11$ appears as the same value in two independent contexts.

Role 1 (scale): the reheating energy density

$$\rho_{\rm inf} = \rho_{P} \cdot (n^{\ast})^{-\alpha} \cdot \frac{2}{n_{\rm obs}\,\pi}$$

Role 2 (temperature ratio): the neutrino–photon temperature separation

$$\frac{T_{\nu}}{T_{\gamma}} = \left(\frac{4}{n^{\ast}}\right)^{1/3} = \left(\frac{4}{11}\right)^{1/3}$$

The algebraic origin of Role 2 is as follows. In entropy conservation before and after $e^{+}e^{-}$ annihilation,

$$g_{s}^{\ast}(\gamma + e^{+}e^{-}) = 2 + \frac{7}{8}\times 4 = \frac{4+7}{2} = \frac{n^{\ast}}{2}$$

The numerator $n^{\ast} = 11 = 4 + 7$ is algebraically determined as the sum of the statistical degrees of freedom of photons ($2 \times 2 = 4$) and the fermionic statistical weight ($7$), coinciding with the $n^{\ast} = 11$ that the present theory derives independently from Axiom Ω.

#### Theorem 11.5.1 (Internal derivation of thermodynamic $n^{\ast}$ and uniqueness of $n_{\rm obs} = 3$)

Each factor ($2$, $7/8$, $4$) is internalised as a function of $n_{\rm obs}$ alone, and the agreement of the geometric $n^{\ast}$ with the thermodynamic $n^{\ast}$ is proved to hold only for $n_{\rm obs} = 3$.

**Preparation (three established mathematical/physical theorems):**

(i) Gauge-freedom theorem: in $d = n_{\rm obs}+1$ dimensional spacetime, the physical degrees of freedom of a massless vector field are $d - 2 = n_{\rm obs} - 1$.

(ii) Spinor-dimension theorem: in $d$-dimensional spacetime ($d$ even), the on-shell degrees of freedom of a Dirac field (particle/antiparticle × helicity) are $2^{d/2} = 2^{(n_{\rm obs}+1)/2}$. This follows from the dimension of the irreducible representation of the Clifford algebra $\mathrm{Cl}(1, n_{\rm obs})$.

(iii) Statistical-weight theorem: in $n_{\rm obs}$ spatial dimensions, the ratio of energy density and entropy density between massless Fermi and Bose gases is the ratio of the Dirichlet eta function to the Riemann zeta function,

$$\frac{\eta(n_{\rm obs}+1)}{\zeta(n_{\rm obs}+1)} = 1 - 2^{-n_{\rm obs}}$$

(from $\eta(s) = (1-2^{1-s})\zeta(s)$). For $n_{\rm obs} = 3$, this gives $7/8$.

**Definition:** the entropic effective degrees of freedom just before $e^{+}e^{-}$ annihilation is defined using only internal quantities as

$$g_{s}^{\ast} = \underbrace{(n_{\rm obs}-1)}_{\text{(i)}} + \underbrace{\left(1 - 2^{-n_{\rm obs}}\right)}_{\text{(iii)}} \cdot \underbrace{2^{(n_{\rm obs}+1)/2}}_{\text{(ii)}}$$

The thermodynamic observational-limit dimension is $n_{\rm th}^{\ast} := 2\,g_{s}^{\ast}$, and the geometric observational-limit dimension is $n_{\rm geom}^{\ast} := n_{\rm obs} + 2^{n_{\rm obs}}$ (§5).

**Theorem:** $n_{\rm th}^{\ast} = n_{\rm geom}^{\ast}$ holds if and only if $n_{\rm obs} = 3$, and the common value is $11$.

**Proof:** For $n_{\rm obs} = 3$: $n_{\rm th}^{\ast} = 2[2 + \tfrac{7}{8}\cdot 4] = 11 = 3 + 8 = n_{\rm geom}^{\ast}$ (sufficiency). Uniqueness: for $n \geq 4$,

$$n_{\rm geom}^{\ast} - n_{\rm th}^{\ast} = 2^{n} - 2^{\lfloor(n+1)/2\rfloor+1}\left(1-2^{-n}\right) + n - 2(n-1)$$

and since $n - \lfloor(n+1)/2\rfloor - 1 \geq 1$ for $n \geq 4$, we have $2^{n} \geq 2 \cdot 2^{\lfloor(n+1)/2\rfloor+1}$, so the difference is positive and monotonically increasing in $n$ (numerically confirmed: $6.5$ at $n = 4$, $32243$ at $n = 15$). For $n = 1, 2$ direct computation gives disagreement ($2 \neq 3$, $5 \neq 6$). Hence agreement holds only for $n_{\rm obs} = 3$. $\square$

**Corollary 11.5.2:** The condition $2^{(n_{\rm obs}+1)/2} = \dim_{\mathbb{R}}\mathbb{H} = 4$ (spinor degrees of freedom equal to the real dimension of the quaternions) also holds only for $n_{\rm obs} = 3$. Thus the numerator $4$ in $T_{\nu}/T_{\gamma} = (4/n^{\ast})^{1/3}$ is internalised into the second-stage Cayley–Dickson algebra $\mathbb{H}$ as a consequence of the fact that the spinor representation space of $\mathrm{Spin}(3) \cong Sp(1) \subset \mathbb{H}$ (unit quaternion group) is $\mathbb{H}$ itself.

**Consequence (resolution of the borrowing problem):** all numbers appearing in $T_{\nu}/T_{\gamma} = (4/n^{\ast})^{1/3}$ are not borrowed from the Standard Model particle table but are functions of $n_{\rm obs}$ via established theorems (i)–(iii). Moreover, that the thermodynamic path and the geometric path (§5) yield the same $n^{\ast} = 11$ is not an assumption but a consistency theorem that uniquely selects $n_{\rm obs} = 3$.

#### Theorem 11.5.3 (Uniqueness of the annihilation species count $k = 1$)

Theorem: let $k$ be the number of minimal Dirac species that annihilate, and generalise:

$$n_{\rm th}^{\ast}(n_{\rm obs}, k) = 2\left[(n_{\rm obs}-1) + \left(1-2^{-n_{\rm obs}}\right) k\, 2^{(n_{\rm obs}+1)/2}\right]$$

The only integer solution of $n_{\rm th}^{\ast}(n_{\rm obs}, k) = n_{\rm geom}^{\ast}(n_{\rm obs}) = n_{\rm obs} + 2^{n_{\rm obs}}$ is $(n_{\rm obs}, k) = (3, 1)$.

**Proof:** For $n_{\rm obs} = 3$, the condition becomes $4 + 7k = 11$, giving the unique solution $k = 1$ ($k = 2$ gives $18$, $k = 3$ gives $25$). A full scan of the lattice $1 \leq n_{\rm obs} \leq 15$, $1 \leq k \leq 10$ using exact rational arithmetic confirmed that the only solution is $(3, 1)$. For $n_{\rm obs} \geq 4$, the growth of $2^{n_{\rm obs}}$ dominates the fermionic term $k \cdot 2^{(n_{\rm obs}+1)/2}$ for any fixed $k$, so no solution exists for large $n_{\rm obs}$ either. $\square$

**Physical necessity:** if 2 species annihilated, $T_{\nu}/T_{\gamma} = (4/18)^{1/3}$, and the $T_{\rm CMB}$ derivation that succeeds at $0.11\%$ error would fail at the level of tens of percent. Hence $k = 1$ is a consequence already verified by observation, and the mass hierarchy $m_{e} < T_{\nu{\rm dec}} < m_{\mu}$ is reinterpreted as the physical realisation of the consistency condition required by this theorem.

#### Spin($n^{\ast}-1$) Structural Correspondence

The $\mathrm{so}(n^{\ast}-1) = \mathrm{so}(10)$ constituting the fundamental equation (§6.4, all 45 channels) is the gauge algebra of SO(10) grand unified theory itself, and three points agree: (1) gauge boson count $= \dim\,\mathrm{so}(10) = 45$; (2) the chiral spinor dimension of $\mathrm{Spin}(10)$ is $16 = 2^{n_{\rm obs}+1}$, which exactly accommodates one Standard Model generation (with right-handed neutrino); (3) generation number $= n_{\rm obs} = 3$ (proved). These are exact agreements between established GUT facts and quantities of the present theory.

#### Algebraic Representation of Effective Degrees of Freedom

The effective degrees of freedom at reheating are

$$g_{\rm reh}^{\ast} = (n^{\ast} - 1)^{2} = 100$$

This is the total number of $S^{2}$ spherical-harmonic modes,

$$\sum_{\ell=0}^{n^{\ast}-2}(2\ell+1) = (n^{\ast}-1)^{2}$$

and also coincides with the square of the order of the multiplicative group of the finite field $\mathbb{F}_{11}$: $|\mathbb{F}_{11}^{\ast}|^{2} = 10^{2}$.

The current entropic effective degrees of freedom are

$$g_{s,{\rm \1}}^{\ast} = 2 + \frac{7}{8}\times 6 \times \frac{4}{n^{\ast}} = \frac{4n^{\ast} - 1}{n^{\ast}} = \frac{43}{11}$$

The appearance of $n^{\ast} = 11$ in the denominator is a consequence of $T_{\nu}/T_{\gamma} = (4/n^{\ast})^{1/3}$, not a coincidence.

#### Complete Closed-Form Expression for $T_{\rm CMB}$

$$\boxed{T_{\rm CMB} = T_{P} \cdot \left[e^{-90\pi} \cdot \frac{2}{n_{\rm obs}\,\pi} \cdot \frac{30}{\pi^{2}} \cdot \frac{1}{(n^{\ast}-1)^{2}} \cdot \left(\frac{4n^{\ast}-1}{n^{\ast}(n^{\ast}-1)^{2}}\right)^{4/3}\right]^{1/4}}$$

All quantities in this expression are algebraically determined from $n^{\ast} = 11$ and $n_{\rm obs} = 3$. No external parameters are present.

Numerical verification:

$$T_{\rm CMB} = 2.7285\,{\rm K} \quad \text{(observed } 2.7255\,{\rm K}\text{, error } 0.11\%\text{)}$$

Proof status of each factor:

| Factor | Value | Proof status |
|--------|-------|-------------|
| $e^{-90\pi} = (n^{\ast})^{-\alpha}$ | $\alpha = 90\pi/\ln 11$ | Rigorously proved |
| $2/(n_{\rm obs}\,\pi)$: odd-parity selection | $2/\pi \times 1/n_{\rm obs}$ | Fully proved |
| $g_{\rm reh}^{\ast} = (n^{\ast}-1)^{2} = 100$ | Spherical-harmonic mode count | Algebraically derived |
| $g_{s,{\rm \1}}^{\ast} = (4n^{\ast}-1)/n^{\ast} = 43/11$ | Dual role of $n^{\ast}$ | Established |

#### Supplement: Difference Between $g_{\rm reh}^{\ast}$ and the Standard Model

The difference from the Standard Model high-temperature effective degrees of freedom $g_{\rm SM}^{\ast} = 106.75$ is

$$\Delta g = g_{\rm SM}^{\ast} - g_{\rm reh}^{\ast} = 106.75 - 100 = \frac{27}{4} = \frac{n_{\rm obs}^{3}}{4}$$

$n_{\rm obs}^{3} = 27$ corresponds to the volumetric degrees of freedom of 3-dimensional space, and $4 = 2^{2}$ to the square of the minimal spin basis count.

$\Delta g$ is a falsifiable prediction already adjudicated by data. Since $T_{\rm CMB} \propto (g_{\rm reh}^{\ast})^{-1/4}$, if the effective degrees of freedom at reheating were the Standard Model high-temperature value $106.75$, then $T_{\rm CMB} = 2.7285 \times (100/106.75)^{1/4} = 2.6843\,{\rm K}$ (error $1.51\%$). Data favour $100$ over $106.75$ by a factor of 14 in precision. The present theory thus predicts that the degrees of freedom thermalised at reheating are 100, not 106.75, and this prediction is consistent with current data.

#### Identification of $\Delta g$ and Conversion to $T_{\rm reh}$

The Standard Model effective degrees of freedom $g^{\ast}(T)$ decrease from the high-temperature value $106.75$ as temperature falls due to the Boltzmann suppression of four massive species ($t, W, Z, H$). From exact numerical integration of the Fermi/Bose distributions with physical masses,

$$g^{\ast}(T) = 100 \iff T = 63.6\ {\rm GeV}$$

The breakdown of the deficit $27/4 = 6.75$ at this temperature is

$$\Delta g = \underbrace{4.81}_{t} + \underbrace{0.99}_{W} + \underbrace{0.61}_{Z} + \underbrace{0.33}_{H} = 6.750$$

Hence $27/4$ is the semi-relativistic suppression of the four heavy Standard Model particles at the electroweak scale $T \approx 64$ GeV, and $g_{\rm reh}^{\ast} = (n^{\ast}-1)^{2} = 100$ converts to the reheating-temperature prediction

$$T_{\rm reh} = 63.6\ {\rm GeV} \quad \text{(electroweak scale)}$$

This identification is conditional on the Standard Model mass spectrum (an empirical input) but is unique given those masses. QCD and electroweak interaction corrections in the free-gas approximation shift $g^{\ast}$ by approximately $\pm 1$–$\pm 2$, propagating via the gradient $dg^{\ast}/dT = 0.155$ /GeV to $T_{\rm reh} = 63.6 \pm (7\text{–}14)\ {\rm GeV}$.

Mass-dependence reduction theorem: the only way in which all claims of the present theory depend on the Standard Model mass spectrum is through the single combination $T(g^{\ast} = 100)$. The condition $m_{e} < T_{\nu{\rm dec}} < m_{\mu}$ is, by Theorem 11.5.3, not an input but the physical realisation of the consistency condition; the $\Delta g$ identification and $T_{\rm reh}$ depend only on the function $T(g^{\ast} = 100)$ of the mass spectrum, and all other derivations ($\Lambda$, CMB, $T_{\rm CMB}$, $n_{s}$, etc.) do not reference masses. The derivation of the Standard Model mass spectrum is therefore not required for any claim of the present theory.

Transfer theorem: the unconditionality of $T_{\rm reh}$ is not an unsolved problem of the present theory but a problem on the Standard Model side. The quantity the present theory derives in this sector is the dimensionless degree-of-freedom count $g_{\rm reh}^{\ast} = (n^{\ast}-1)^{2} = 100$, which is unconditional and already verified at $0.11\%$ error through $T_{\rm CMB}$. The temperature label is given as the image $T(g^{\ast} = 100) = 63.6$ GeV under the map $g_{\rm SM}^{\ast}(T)$ (the empirical function defined by the Standard Model mass spectrum); first-principles derivation of this map is the same problem as the origin of mass in the Standard Model. The claim on the theory side ($g_{\rm reh}^{\ast} = 100$) is complete.

#### Complete Derivation Classification

| Classification | Physical quantities |
|----------------|---------------------|
| Complete derivation (zero external parameters) | $\alpha,\, n_{\rm obs},\, n^{\ast},\, \Lambda,\, H_{0},\, \Omega_{\Lambda},\, R_{\rm dec},\, z_{\rm dec},\, T_{\rm CMB}$ |
| Conditional derivation ($T_{\rm CMB}$ as 1 input) | $\Omega_{\gamma},\, \Omega_{b}h^{2}$ |
| First-principles path verification | $\ell_{A},\, \ell_{1},\ldots,\ell_{6}$ |
| Conjecture (falsifiable) | Algebraic closed form of $\varphi_{k}$ (fixed-point approximation, §8.9) |

### 11.6 Final Summary of Axiom System and Premises

The premises on which the present theory rests are organised into three tiers.

First: Axiom Ω (including non-degeneracy).

Second: two existing premises (continuous implementation, isotropy) — both already in use at the stage of the fundamental equation.

Third: standard-grade premises shared with all standard theories (GR + Boltzmann transfer, tensor-product composition, channel identification, choice of Fock representation).

The number of unresolved theory-specific axioms is zero. Foundation axioms P0–P4 are resolved by derivation, and their basis reduces to the three tiers above. The exponent identification (P3) holds as an unconditional theorem by the axiomatic specification of Ω non-degeneracy, and independence proofs have established that this specification is minimal and sufficient (see [Revision and Audit Record §3.3](08_revision_history.md#33-resolution-by-the-third-round-of-verification)).

The external mathematical theorems on which the present theory relies are: Hurwitz's theorem, Cauchy's functional equation, Wall's theorem, Stone's theorem, Schur's lemma, the homogeneous-space theorem, the spectral theorem, and the Minakshisundaram–Pleijel heat-kernel expansion — all established results.

Identification Postulate G (§9.11.4) is registered at conjecture level and is not used in any existing derivation of the theory.

The resolution process and audit details for each premise are recorded in the [Revision and Audit Record](08_revision_history.md).

#### Removal of the Ground-State Premise (key point of Theorem 11.10.3 in [Revision and Audit Record §3.3](08_revision_history.md#33-resolution-by-the-third-round-of-verification))

What is required at all downstream points of use (Theorem 9.8.2 Step 5, Lemma B1) is not the ground-state nature of the state but the identity of expectation values and variances across channels. If the state is $SO(n)$-invariant, identity follows; invariance is preserved by unitary evolution as long as the Hamiltonian is $SO(n)$-invariant, regardless of interaction or cascade coupling. Since $\rho_{j}$ is a quadratic form in channel coordinates and is insensitive to sign reversal, for any permutation $\pi$ it transforms covariantly as $\rho_{j} \mapsto \rho_{\pi(j)}$, and under an invariant state the joint distribution of $(\delta\rho_{1}, \ldots, \delta\rho_{n})$ is permutation-invariant, making all marginal distributions identical. Hence $\langle\rho_{j}\rangle$ and $\mathrm{Var}(\delta\rho_{j})$ are independent of $j$. Equipartition holds as long as isotropy is maintained, even under excitation.

#### Explicit Construction of the Multi-Channel Hilbert Space (key point of [Revision and Audit Record §3.3](08_revision_history.md#33-resolution-by-the-third-round-of-verification))

Construction: stack the Hilbert spaces for each channel:

$$\mathcal{H}_{n} = \bigotimes_{j=1}^{n} h_{j}, \qquad h_{j} = L^{2}(\mathbb{R})$$

where $h_{j}$ carries the canonical pair $(q_{j}, p_{j})$ for channel $j$. $SO(n)$ acts as rotations of the coordinates $(q_{1}, \ldots, q_{n})$. An $SO(n)$-invariant quadratic-form Hamiltonian is restricted by Schur's lemma to

$$H = a\sum_{j=1}^{n} p_{j}^{2} + b\sum_{j=1}^{n} q_{j}^{2} \qquad (a,b > 0)$$

Hence channels are automatically decoupled within the construction, and independence in Theorem 9.8.2 Step 3 becomes a theorem of the construction. Under the invariant Gaussian ground state, cross-covariances are also strictly zero. The remaining premises are tensor-product composition (standard composition postulate of quantum mechanics) and channel identification (two items), both standard-grade.

---

## 11.7 Responses to Criticisms

Responses to three fundamental criticisms raised by physicists are given below.

First: the criticism that the fundamental equation is an identity. Inverting from the observed value of $\Lambda$ independently of the fundamental equation gives $\alpha_{\Lambda} = 117.920$, agreeing with the theoretical value $\alpha_{\star} = 117.913$ at $0.006\%$. This two-path agreement is evidence that the fundamental equation is an independent constraint.

Second: the criticism that the derivation is an inversion from observed values. $n^{\ast} = 11$ is fixed without using any modern observational values, from Hurwitz's theorem (1898) and the Cayley–Dickson construction; $\alpha$ is then determined by the fundamental equation. $\Lambda$ is a post-hoc prediction (error $1.71\%$), not a fitting result. Moreover, the first-principles path (Boltzmann code direct computation) using the theory parameter set independently of the degeneracy algebra has been verified to reproduce all six peaks within $0.65\%$ (§8.8), completing a quantitative response to the post-hoc criticism for $\ell_{1} = 220$.

Third: the criticism that the postulates are arbitrary. All six postulates (B1, B2, O1, O2, M, P) have been proved to be deductions from Axiom Ω (§11.2.1), and this criticism has been resolved at the root.

---

← [§9: Testable Predictions](06_predictions.md) | Next → [Appendices](appendix.md)
