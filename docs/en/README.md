# One-Dimensional Origin Unified Theory

---

> Abstract
>
> Starting from a single axiom — "existence arises from the self-contradiction of nothingness (¬∃ → ∃)" —
> this paper presents an independent research programme that derives, without any assumptions,
> the number of spatial dimensions, physical constants, the cosmological constant,
> the CMB temperature anisotropy peak structure, and the CMB temperature.
> The core is the discovery and proof of a new equation absent from existing literature:
>
> $$\alpha \cdot \ln(n^{\ast}) = R(S^{n^{\ast}-1}) \cdot \pi$$
>
> From this equation the energy-scale exponent $\alpha = 90\pi/\ln 11 \approx 117.91$
> and the observational-limit dimension $n^{\ast} = 11$ are fixed algebraically,
> and the 120-order cosmological-constant problem is resolved without tuning.
> All CMB acoustic peak positions emerge as pure algebraic identities from the degeneracies
> of spherical harmonics on $S^{9}$, free of any external parameters.
>
> The principal established results are as follows.
> The observed spatial dimension $n_{\rm obs} = 3$ follows from Hurwitz's theorem,
> and the observational-limit dimension $n^{\ast} = 11$ from the graded Brauer group
> $\mathrm{sBr}(\mathbb{R}) \cong \mathbb{Z}/8$ (Wall's theorem) combined with the
> grading necessitated by Axiom Ω.
> The derivation chain from Axiom Ω to $n^{\ast} = 11$ is internally complete,
> and all six postulates (B1, B2, O1, O2, M, P) are deduced from Axiom Ω.
> The identification of the statistical-face decay exponent with the quantum-face phase eigenvalue
> holds as an unconditional theorem under Ω non-degeneracy.
> The two-path agreement of $\alpha$ (fundamental equation $117.913$ vs.
> $\Lambda$-inversion $117.920$, $0.006\%$) serves as an empirical test of Axiom Ω.
> The CMB temperature $T_{\rm CMB} = 2.7285\,{\rm K}$ (error $0.11\%$) is derived with zero
> external parameters, and $n^{\ast} = 11$ playing a dual role — algebraically identical
> to the statistical mechanics of $e^{+}e^{-}$ annihilation — constitutes a consistency theorem
> that uniquely selects $n_{\rm obs} = 3$.
> First-principles Boltzmann code (CAMB) calculations, taking only theory-derived parameters
> as input, reproduce all six peaks with errors $0.47$–$0.65\%$; the residuals all reduce to
> the propagation of the $1.71\%$ error in $\Lambda$ ($\ell_{A} = 300.19$, difference $0.52\%$
> from the reference), and the conclusions are independent of $n_{s}$.
> The deep-ultraviolet spacetime dimension $D = 2$ agrees at both ends with the spectral
> dimension flow $4 \to 2$ reported by CDT, asymptotic-safety gravity, and spin-foam models;
> the dimension-flow completion scale $l(3) \approx 10^{14}\,l_{P}$ yields a falsifiable
> discriminant prediction differing from existing approaches by 13 orders of magnitude.
> $\mathrm{so}(10)$ coincides exactly with the SO(10) GUT gauge algebra,
> and the $\mathbf{16}$ decomposition reproduces the representation content of one
> Standard Model generation.
> The number of unresolved theory-specific axioms is zero, and the theory rests solely on
> Axiom Ω (including non-degeneracy), two existing premises
> (continuous implementation, isotropy), and standard-grade premises.

---

## Document Structure

| File | Contents |
|------|----------|
| README.md (this file) | Abstract, main results, numerical tables, conclusions |
| [§1–§3: Axiom Ω and Setup](01_axiom_and_setup.md) | Motivation, Axiom Ω, uniqueness of the energy-density function |

All sections continue sequentially from `01_axiom_and_setup.md`; each file carries a navigation link to the next.

---

## Four Core Claims

### Claim 1: Discovery of a New Equation

The equation

$$\alpha \cdot \ln n^{\ast} = R(S^{n^{\ast}-1}) \cdot \pi$$

is absent from existing literature. Substituting $n^{\ast} = 11$ (derived independently in §4–§5) gives

$$\alpha = \frac{90\pi}{\ln 11} = 117.913131\ldots$$

### Claim 2: Resolution of the 120-Order Cosmological-Constant Problem

$$\Lambda = 2(n^{\ast}-2) \cdot \frac{(n^{\ast})^{-\alpha}}{l_{P}^{2}} = 1.1076 \times 10^{-52}\,\text{m}^{-2}$$

Error $1.71\%$ against the observed value $1.089 \times 10^{-52}\,\text{m}^{-2}$. No parameter tuning.

### Claim 3: Algebraic Identity for the First CMB Peak

$$\ell_{1} = D_{3}(S^{9}) + D_{1}(S^{9}) = \binom{12}{3} = 220$$

Zero error against the observed value 220.

### Claim 4: Full Acoustic-Peak Formula (Zero External Parameters) and First-Principles Verification

$$\ell_{k} = 220 + (k-1) \times 303$$

Derived entirely algebraically from $n_{\rm obs} = 3$ and $n^{\ast} = 11$ alone
(constant phase-shift approximation).
The first-principles path — Boltzmann code fed exclusively with theory-derived parameters
($H_{0}$, $\Omega_{\Lambda}$, $T_{\rm CMB}$, $\Omega_{b}h^{2}$, $w = -1$) —
reproduces all six peaks with errors below $0.65\%$ (§8.8).

---

## Key Numerical Summary

### Fundamental Parameters

| Quantity | Theory | Observed/Experimental | Error |
|----------|--------|-----------------------|-------|
| $n_{\rm obs}$ | 3 | 3 | 0% |
| $n^{\ast}$ | 11 | — | — |
| $\alpha$ | $90\pi/\ln 11 = 117.9131$ | $117.87$ (inversion) | $0.037\%$ |

### Cosmological Constant

| Quantity | Theory | Observed | Error |
|----------|--------|----------|-------|
| $\Lambda$ | $1.1076 \times 10^{-52}$ m⁻² | $1.089 \times 10^{-52}$ m⁻² | $1.71\%$ |

Improvement over QFT prediction ($\sim 10^{70}$ m⁻²): 122 orders of magnitude.

### CMB Peak Positions

| Peak $k$ | Algebraic formula | First-principles | Reference (Planck best-fit) | Algebraic error | First-principles error |
|----------|-------------------|------------------|-----------------------------|-----------------|------------------------|
| 1 | 220 | 219.3 | 220.3 | $0.14\%$ | $0.47\%$ |
| 2 | 523 | 532.7 | 536.2 | $2.5\%$ | $0.65\%$ |
| 3 | 826 | 808.4 | 812.9 | $1.6\%$ | $0.56\%$ |
| 4 | 1129 | 1119.9 | 1126.5 | $0.22\%$ | $0.58\%$ |
| 5 | 1432 | 1413.0 | 1421.3 | $0.75\%$ | $0.59\%$ |
| 6 | 1735 | 1714.8 | 1725.7 | $0.54\%$ | $0.63\%$ |
| Mean | — | — | — | $0.96\%$ | $0.58\%$ |

The reference is the output of the same Boltzmann code run with Planck 2018 best-fit parameters
(which by construction agrees with the observed spectrum).

### Cosmological Parameter Predictions

| Quantity | Theory | Observed | Error | Status |
|----------|--------|----------|-------|--------|
| $r$ (tensor-to-scalar ratio) | $1/54 \approx 0.0185$ | $< 0.036$ | — | Within upper limit ✓ |
| $w$ (dark energy) | $-1$ (proven) | $-1.028 \pm 0.032$ | $< 1\sigma$ | ✓ |
| $N_{\rm eff}$ (effective neutrino number) | $3$ (proven) | $2.99 \pm 0.17$ | $0.06\sigma$ | ✓ |
| $n_{t}$ (gravitational-wave index) | $-1/432 \approx -0.00231$ | unobserved | — | New prediction |
| $n_{s}$ (scalar index) | $1-4/\alpha = 0.96608$ | $0.9649 \pm 0.0042$ | $0.28\sigma$ | ✓ |
| $R_{\rm dec}$ (baryon-photon ratio) | $3/5 = 0.600$ | $0.603$ | $0.5\%$ | ✓ |
| $z_{\rm dec}$ (decoupling redshift) | $1089$ | $1089.80$ | $0.07\%$ | ✓ |
| $H_{0}$ (Hubble constant) | $67.67$ km/s/Mpc | $67.66$ km/s/Mpc | $0.015\%$ | ✓ |
| $\Omega_{\Lambda}$ (dark-energy density) | $0.690$ | $0.6847$ | $0.77\%$ | ✓ |
| $\Omega_{b}h^{2}$ (baryon density) | $0.02156$ | $0.02237$ | $3.6\%$ | ✓ |
| $T_{\rm CMB}$ (CMB temperature) | $2.7285\,{\rm K}$ | $2.7255\,{\rm K}$ | $0.11\%$ | ✓ |
| $\ell_{A}$ (acoustic angular scale) | $300.19$ | $301.75$ | $0.52\%$ | ✓ |

---

## Conclusions

The core claims of the theory are as follows.

First, the new equation $\alpha \cdot \ln n^{\ast} = R(S^{n^{\ast}-1}) \cdot \pi$ has been discovered and proved.

Second, the 120-order cosmological-constant problem has been resolved without parameter tuning (error $1.71\%$).

Third, the first CMB acoustic peak $\ell_{1} = 220$ is derived as an algebraic identity with zero error.

Fourth, the full acoustic-peak formula $\ell_{k} = 220 + (k-1) \times 303$ is derived entirely algebraically. With zero external parameters it achieves an accuracy roughly comparable to the multi-parameter $\Lambda$CDM fit (mean error $1.13\%$).

Fifth, the CMB temperature $T_{\rm CMB} \approx 2.7285\,{\rm K}$ (error $0.11\%$) is derived with zero external parameters. The key is the dual role of $n^{\ast} = 11$: the value fixed by Axiom Ω is algebraically identical to the statistical mechanics of $e^{+}e^{-}$ annihilation.

Sixth, all six postulates (B1, B2, O1, O2, M, P) have been proved to be deduced from Axiom Ω. The only external assumptions in the theory are established mathematical theorems.

Seventh, the first-principles path — Boltzmann code direct computation using only theory-derived parameters — has been verified to reproduce all six peaks within $0.65\%$. The residuals all reduce to propagation of the $1.71\%$ error in $\Lambda$ ($\ell_{A}$ scale difference $0.52\%$), and the phase structure is fully reproduced. The conclusions are independent of $n_{s}$. The two-path convergence (algebraic and first-principles) provides a quantitative answer to the post-hoc criticism.

Eighth, all factors in $T_{\nu}/T_{\gamma} = (4/n^{\ast})^{1/3}$ have been internalized as functions of $n_{\rm obs}$ alone via three established theorems: the gauge-freedom theorem, the spinor-dimension theorem, and the $\eta/\zeta$ statistical-weight theorem. The agreement between the thermodynamic $n^{\ast}_{\rm th}$ and the geometric $n^{\ast}_{\rm geom}$ holds only for $n_{\rm obs} = 3$ (Theorem 11.5.1), so the dual role of $n^{\ast} = 11$ is not a coincidence but a consistency theorem that uniquely selects $n_{\rm obs} = 3$.

Ninth, the equivalence relation for the observational limit is determined to be the graded Morita equivalence forced by the parity of Axiom Ω, and Wall's theorem fixes $n^{\ast} = \min\{n > 3 \mid n \equiv 3 \pmod{8}\} = 11$. The derivation chain depends only on three external theorems: Hurwitz, Cauchy, and Wall.

Tenth, the deep-ultraviolet ($\leq$ Planck length) spacetime dimension $D = 2$ is proved from the $n = 1$ origin of Axiom Ω and the requirement $n \geq 3$ for observability (Theorem 4.1.1). Both cascade endpoints (UV $D = 2$, IR $D = 4$) agree with the spectral dimension flow of CDT, asymptotic-safety gravity, and spin-foam models; the dimension-scale map reproduces the dark-energy length to the right coefficient. The dimension-flow completion scale $l(3) \approx 1.9 \times 10^{-21}$ m is a falsifiable discriminant prediction differing from existing approaches by 13 orders of magnitude.

Eleventh, the number of annihilating species $k = 1$ is a theorem, not a premise (Theorem 11.5.3; $(3,1)$ is the unique solution of $4 + 7k = 11$). $\mathrm{so}(10)$ coincides exactly with the SO(10) GUT algebra, and the $\mathbf{16}$ decomposition reproduces the representation content of one Standard Model generation.

Twelfth, $n_{s} = 1 - 4/\alpha = 0.96608$ is derived from the equipartition principle (the same argument as $r = 1/D_{2}$) and the proved scale map, carrying the immediately falsifiable prediction of strictly zero running ($0.67\sigma$ consistent with observation).

Thirteenth, $\Delta g = 27/4$ is rigorously identified as the semi-relativistic suppression of the four heavy Standard Model particles at the electroweak scale $T = 63.6$ GeV, and $g^{\ast}_{\rm reh} = 100$ is converted into a reheating-temperature prediction. The fundamental equation is a spectral condition of a self-adjoint operator on $L^{2}([0, \ln n^{\ast}])$; the selected mode $k = 90$ automatically has odd parity, and the parity structure of Axiom Ω is preserved at the quantization level. The necessity of quantum mechanics over the complex field is identified from the first stage of the Cayley–Dickson tower.

Fourteenth, the identification of exponents (equality of the statistical-face decay exponent and the quantum-face phase eigenvalue) holds as an unconditional theorem under Ω non-degeneracy. The action of $\sigma$ on the pair of descriptions is uniquely determined as an exchange; the involutions exchanging the two axes of the spectral plane are restricted to $s \mapsto \pm i\bar{s}$ (complete classification, symbolically verified), and both preserve $|s|$, forcing $\alpha_{\rm st} = \alpha_{\rm qu}$. Independence proofs have established that the exponent identification cannot be derived from the old axiom system, and that Ω non-degeneracy is the minimal sufficient specification.

Fifteenth, the number of unresolved theory-specific axioms is zero. Foundation axioms P0–P4 have been resolved by derivation; the theory rests solely on Axiom Ω (including non-degeneracy), two existing premises (continuous implementation and isotropy, both already used at the stage of the fundamental equation), and standard-grade premises shared with all standard theories (GR + Boltzmann transfer, tensor-product composition, channel identification, choice of Fock representation).

Starting from a single axiom (Axiom Ω), passing only through established external mathematical theorems (Hurwitz, Cauchy, Wall, Stone, Schur, homogeneous-space theorem, spectral theorem, Minakshisundaram–Pleijel heat-kernel expansion), multiple independent cosmological observables are reproduced. This structure is the essential value of the theory.

---

*This paper is a record of independent research. Independent verification, criticism, and discussion — including numerical verification code — are welcome.*
