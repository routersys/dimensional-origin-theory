# §9: Testable Predictions

← [§8: CMB Peak Structure](05_cmb_peaks.md) | Next → [§10–§11: Numerical Verification and Completeness Assessment](07_verification_and_completeness.md)

---

## 9. Testable Predictions

The following physical quantities are predicted by the present theory. The derivation status of each prediction is stated explicitly.

### 9.1 Tensor-to-Scalar Ratio

$$\boxed{r = \frac{1}{D_{2}(S^{9})} = \frac{1}{54} \approx 0.0185}$$

Derivation: the equipartition theorem of quantum statistics is applied to the quantum fluctuations of $S^{9}$ under multiplicative canonical quantisation.

In the mode expansion on $S^{9}$, $\ell = 0, 1$ describe the unperturbed background; the lowest perturbative order is scalar ($\ell = 2$). The number of scalar perturbation channels is $D_{2}(S^{9}) = 54$ (the $\ell = 2$ degeneracy), and the number of tensor perturbation channels is $1$ (the spin-2 $m = 0$ singlet seen isotropically by an $n_{\rm obs} = 3$-dimensional observer).

By the equipartition theorem (a fundamental principle of quantum statistics), independent modes carry equal fluctuation amplitude $h_{0}$. Since all $D_{2}$ scalar modes add to the observation,

$$P_{S} \propto D_{2} \cdot h_{0}^{2}, \quad P_{T} \propto 1 \cdot h_{0}^{2}$$

$$\boxed{r = \frac{P_{T}}{P_{S}} = \frac{1}{D_{2}} = \frac{1}{54} \approx 0.0185}$$

Validity of the equipartition theorem follows directly from the Hamiltonian structure of the multiplicative canonical quantisation. In the quantisation with multiplicative coordinate $u = \ln n$, each of the $D_{2}$ scalar modes constitutes an independent harmonic oscillator with identical boundary conditions, identical mass, and identical potential. This is a direct consequence of a theorem of quantum mechanics, not an assumption.

Proof that the tensor singlet count is 1: the gravitational waves measured by an isotropic observer in $n_{\rm obs} = 3$ dimensions correspond only to the azimuthally symmetric component ($m = 0$ singlet) of spin-2 harmonic tensors on $S^{9}$. Among the $D_{2} = 54$ modes, only one satisfies this condition.

The prediction lies within the current observational upper bound $r < 0.036$ (BICEP/Keck 2021) and can be tested by the CMB-S4 experiment.

### 9.2 Gravitational-Wave Spectral Index

When $r = 1/D_{2}$ is established, the consistency relation of general-relativistic inflation theory gives

$$\boxed{n_{t} = -\frac{r}{8} = -\frac{1}{8 D_{2}} = -\frac{1}{432} \approx -0.00231}$$

This relation holds as long as the present theory is consistent with general relativity. It is currently unobserved and is in principle testable by future experiments such as LISA.

### 9.3 Dark-Energy Equation of State

$$\boxed{w = -1}$$

Derivation: in the present theory $\varepsilon(n^{\ast}) = E_{0} \cdot (n^{\ast})^{-\alpha}$, and the observational-limit dimension $n^{\ast} = 11$ is constant in time. Since $\Lambda \propto \varepsilon(n^{\ast})$ does not vary in time,

$$\rho_{\Lambda} = \mathrm{const} \quad \Rightarrow \quad \frac{d\rho_{\Lambda}}{dt} = 0$$

Substituting into the energy conservation equation $\dot{\rho} + 3H(\rho + P) = 0$ proves $w = P/\rho = -1$.

This is a proven consequence, fully consistent with $\Lambda$CDM, not a proposed value. The discrepancy from the observed value $w = -1.028 \pm 0.032$ (Planck 2018) is within $1\sigma$.

### 9.4 Effective Neutrino Number

$$\boxed{N_{\rm eff} \approx 3}$$

Derivation: the generation number $N_{\nu} = 3$ is proved from $n_{\rm obs} = 3$ (§4). In the Standard Model electroweak theory, a generation number of 3 determines the integer part of the effective neutrino number $N_{\rm eff}$.

$$N_{\rm eff} = N_{\nu} + \delta N_{\rm QCD} = 3 + 0.046 = 3.046 \quad \text{(with standard QCD corrections)}$$

A thermal-correction estimate through extra dimensions $D_{2} = 54$ gives $N_{\rm eff} = 3(1+1/D_{2}) = 3.056$, but under the observational precision $\pm 0.17$ the values $3$, $3.046$, and $3.056$ are indistinguishable, and the integer prediction $N_{\nu} = 3$ is the proven consequence of the present theory.

The discrepancy from the observed value $N_{\rm eff} = 2.99 \pm 0.17$ (Planck 2018) is $0.06\sigma$.

### 9.5 Baryon-to-Photon Ratio and Decoupling Redshift

$$\boxed{R_{\rm dec} = \frac{3(n^{\ast} - n_{\rm obs})}{4(n^{\ast} - 1)} = \frac{3 \times 8}{4 \times 10} = \frac{3}{5} = 0.600}$$

Derivation: $R_{\rm dec} \equiv 3\rho_{b}/(4\rho_{\gamma})$ is obtained from the degeneracy of baryon and photon energy densities.

Modes on $S^{n^{\ast}-1}$ are identified with particle species. The photon mode degeneracy is that of spin-1 spherical harmonics $D_{1}(S^{9}) = n^{\ast} - 1 = 10$, the baryonic mode degeneracy is $D_{2} - D_{1} = n^{\ast}(n^{\ast}-3)/2 = 44$, and the total symmetric modes (all photon degrees of freedom) are $\binom{n^{\ast}}{2} = n^{\ast}(n^{\ast}-1)/2 = 55$.

The density ratio is

$$\frac{\rho_{b}}{\rho_{\gamma}} = \frac{D_{2} - D_{1}}{\binom{n^{\ast}}{2}} = \frac{n^{\ast}(n^{\ast}-3)/2}{n^{\ast}(n^{\ast}-1)/2} = \frac{n^{\ast} - 3}{n^{\ast} - 1} = \frac{8}{10}$$

$$R_{\rm dec} = \frac{3}{4} \cdot \frac{\rho_{b}}{\rho_{\gamma}} = \frac{3(n^{\ast} - n_{\rm obs})}{4(n^{\ast} - 1)} = \frac{3}{5}$$

Error against the observed value $R_{\rm dec} = 0.603$ (Planck 2018): $0.5\%$.

The decoupling redshift $z_{\rm dec}$ is also derived algebraically. Using $\ell_{1} = \binom{n^{\ast}+1}{n_{\rm obs}} = 220$ and $n^{\ast}$,

$$\boxed{z_{\rm dec} = \frac{n^{\ast} - 1}{2} \cdot \binom{n^{\ast}+1}{n_{\rm obs}} - n^{\ast} = 5 \times 220 - 11 = 1089}$$

Error against the observed value $z_{\rm dec} = 1089.80$ (Planck 2018): $0.07\%$.

### 9.6 Hubble Constant, Cosmological Density Parameters, and Baryon Density

From the cosmological constant $\Lambda$ (derived in [§7](04_cosmological_constant.md)), the following are derived in chain:

$$\rho_{\Lambda} = \frac{\Lambda c^{2}}{8\pi G}$$

$$\boxed{H_{0} = \sqrt{\frac{8\pi G\,\rho_{\Lambda}}{3\,\Omega_{\Lambda}}} \approx 67.67 \text{ km/s/Mpc}}$$

where $\Omega_{\Lambda} = \rho_{\Lambda}/\rho_{\rm crit}$ is determined self-consistently.

| Quantity | Theory | Observed (Planck 2018) | Error |
|----------|--------|------------------------|-------|
| $H_{0}$ | $67.67$ km/s/Mpc | $67.66$ km/s/Mpc | $0.015\%$ |
| $\Omega_{\Lambda}$ | $0.690$ | $0.6847$ | $0.77\%$ |

The baryon density is derived from $R_{\rm dec}$ (§9.5), $z_{\rm dec}$ (§9.5), and the photon density parameter $\Omega_{\gamma}$ (which depends on the CMB temperature $T_{\rm CMB}$):

$$\Omega_{b}h^{2} = \frac{4}{3} \cdot R_{\rm dec} \cdot (1 + z_{\rm dec}) \cdot \Omega_{\gamma}h^{2}$$

Substituting $R_{\rm dec} = 3/5$, $1 + z_{\rm dec} = 1090$, and $\Omega_{\gamma}h^{2} = 2.473 \times 10^{-5}$ (observed value),

$$\Omega_{b}h^{2} = \frac{4}{3} \times \frac{3}{5} \times 1090 \times 2.473 \times 10^{-5} = 0.02156$$

Error against the observed value $\Omega_{b}h^{2} = 0.02237$ (Planck 2018): $3.6\%$. $\Omega_{\gamma}h^{2}$ is the sole external input, calculated from the observed CMB temperature $T_{\rm CMB} = 2.7255\,{\rm K}$ ($T_{\rm CMB}$ itself is discussed in §11.5).

### 9.7 Dimensional Reduction at the Ultraviolet Limit and Connection to Quantum-Gravity Approaches

#### Theorem 9.7.1 (Deep-ultraviolet spacetime dimension $D = 2$)

Convention: in the present theory $n$ counts spatial dimensions and the spacetime dimension is $D = n + 1$ ($n_{\rm obs} = 3 \leftrightarrow$ 4-dimensional spacetime).

Theorem: the spacetime dimension of the present theory in the deep ultraviolet (below the Planck length) is $D = 2$.

**Proof:**

(a) Origin dimension: the minimal existence of Axiom Ω is one-dimensional ($n = 1$) energy (§2.2), and $\varepsilon(1) = E_{0}$ is at the Planck scale. The cascade $n = 1 \to 2 \to 3 \to \cdots$ corresponds to the monotone decrease of $\varepsilon(n)$; hence the energy domain above the Planck scale (below the Planck length) is $n = 1$, i.e. spacetime $D = 1 + 1 = 2$.

(b) Physical necessity (consistency with unobservability): by Theorem 4.1.1, observability requires $n \geq 3$, and by Lemma 4.1.2, at $n = 2$ the Ω-parity is absorbed into $P = R(\pi) \in SO(2)$ and cannot be realised spatially. Hence $n \leq 2$ is in principle unobservable; the dimension of the domain deeper than the boundary of observability ($n = 3$ established) is necessarily $n \leq 2$. The monotonicity of the cascade together with (a) fixes the deep-ultraviolet limit at $D = 2$. $\square$

#### Correspondence with Existing Quantum-Gravity Approaches

The ultraviolet flow of the spacetime spectral dimension $d_{s}$ ($4 \to 2$) has been reported by multiple independent quantum-gravity approaches. Causal dynamical triangulations (CDT, Ambjørn–Jurkiewicz–Loll 2005) numerically showed that $d_{s}$ decreases from approximately 4 at large scales to approximately 2 at small scales. In asymptotic-safety gravity, $d_{s} = 2$ exactly near the UV fixed point, because the Einstein–Hilbert action is scale-invariant only in two dimensions. In spin-foam models (Modesto), the scaling of the area spectrum gives $d_{s} = 2$ at the Planck scale and $4$ at low energy. Care is needed with the LQG spin-network direct definition, where the result is state-dependent (see Carlip's review).

Correspondence of the present theory: the two endpoints of the cascade ($n = 1 \leftrightarrow D = 2$ and $n_{\rm obs} = 3 \leftrightarrow D = 4$) agree with the two endpoints of the dimensional flow ($\text{UV}\ 2$, $\text{IR}\ 4$) shown by these approaches. In the present theory both endpoints are independently fixed from the minimal existence of Axiom Ω and Hurwitz's theorem, not as external inputs.

#### Corollary 9.7.2 (Dimension–scale map and discriminant prediction)

From $\varepsilon(n) = \rho_{P} \cdot n^{-\alpha}$ (density in Planck units) and the standard density–length conversion $l = l_{P}(\rho_{P}/\rho)^{1/4}$, the scale at which dimension $n$ is established is

$$l(n) = l_{P} \cdot n^{\alpha/4}, \qquad \frac{\alpha}{4} = 29.478$$

| $n$ | $l(n)$ | Corresponding energy | Meaning |
|-----|--------|----------------------|---------|
| 1 | $1.6 \times 10^{-35}$ m | $E_{P}$ | Planck length (origin, $D = 2$) |
| 2 | $1.2 \times 10^{-26}$ m | $1.6 \times 10^{10}$ GeV | Intermediate transition |
| 3 | $1.9 \times 10^{-21}$ m | $1.1 \times 10^{5}$ GeV | Establishment of 3-d space ($D = 4$) |
| 11 | $8.1 \times 10^{-5}$ m | — | Observational limit; vacuum energy domination |

Cross-check (exact): from $\rho_{\Lambda} = \dfrac{18}{8\pi} \cdot 11^{-\alpha}\rho_{P}$, the dark-energy length is

$$\left(\frac{\hbar c}{\rho_{\Lambda} c^{2}}\right)^{1/4} = l(11) \cdot \left(\frac{8\pi}{18}\right)^{1/4} = 80.7\,\mu{\rm m} \times 1.087 = 87.7\,\mu{\rm m}$$

This agrees to the right coefficient with the length $87.7\,\mu{\rm m}$ calculated from the observed value of $\Lambda$.

Discriminant prediction: the completion scale of the dimensional flow $2 \to 4$ of the present theory is $l(3) \approx 1.9 \times 10^{-21}$ m ($\approx 10^{14}\,l_{P}$, energy $\approx 10^{5}$ GeV), which differs by 13 orders of magnitude from the transition suggested by CDT at approximately $10\,l_{P}$. This is a falsifiable difference that can in principle distinguish the two. The current accelerator scale ($\sim 10^{-20}$ m) is larger than $l(3)$ and lies in the domain where 3 dimensions are established, so there is no conflict with existing observations.

Each dimension $n > 3$ is unobservable by Theorem 4.1.1 and Hurwitz's theorem, and the observed spatial dimension saturates at 3 for $l > l(3)$. The energy density of $n > 3$ contributes only as vacuum energy, and its terminus $n^{\ast} = 11$ gives $\Lambda$ (§7).

#### Theorem 9.7.3 (Spectral-dimension equivalence at the endpoints)

Theorem: at both endpoints of the cascade, the spacetime dimension $D = n + 1$ of the present theory and the spectral dimension $d_{s}$ agree exactly.

**Proof:** By the established theorem (Minakshisundaram–Pleijel heat-kernel expansion), the heat-kernel return probability on any smooth $D$-dimensional Riemannian manifold satisfies $P(s) \sim (4\pi s)^{-D/2}$ ($s \to 0$), from which $d_{s} := -2\,d\ln P/d\ln s \to D$ follows. Both endpoints of the present theory are fixed smooth manifolds. The UV endpoint ($n = 1$) is 2-dimensional spacetime and the observational endpoint ($n_{\rm obs} = 3$) is 4-dimensional spacetime, with spatial realisation given by sphere-type smooth geometry (§8). Hence $d_{s} = 2$ in the UV and $d_{s} = 4$ in the IR. For numerical verification, $d_{s} = D$ was confirmed to machine precision for $D = 2, 4, 12$ using the exact heat kernel (Poisson resummation form) on a flat torus $T^{D}$. $\square$

Through this result, the two-endpoint correspondence with CDT, asymptotic safety, and spin-foam models ($d_{s}: 4 \to 2$) becomes a theorem rather than a conjecture. The only undefined domain remaining is the transition region, where $d_{s}$ is not uniquely defined since the geometry is not a fixed manifold. This is not a defect of the present theory but a limitation of the definition domain of $d_{s}$ itself (the transition-region $d_{s}$ is method-dependent in all quantum-gravity approaches).

#### Theorem 9.7.4 (Independence of predictions from extrapolation)

Theorem: all testable predictions of Corollary 9.7.2 contain no extrapolation of the dimension conversion rule.

**Proof:** The conversion rule $\rho \sim l^{-D}$ is exact in a domain where the spacetime dimension $D$ is fixed. The prediction $l(3) = l_{P} \cdot 3^{\alpha/4}$ applies the $1/4$-power rule at the very point where $n = 3$ (i.e. $D = 4$) is established, so the conversion rule is exact at the evaluation point. The cross-check $87.7\,\mu{\rm m}$ is the length $(\hbar c/\rho_{\Lambda} c^{2})^{1/4}$ defined within 4-dimensional spacetime from $\rho_{\Lambda}$ as measured by a 4-dimensional observer, and is exact as an observer-side conversion. The only place where ambiguity in the conversion (whether to use the local dimension $D = n+1$ or the observer's 4) remains is the auxiliary quantity $l(2)$ inside the transition region ($1.2 \times 10^{-26}$–$1.1 \times 10^{-23}$ m), and no prediction depends on this. $\square$

#### Corollary 9.7.5 (Canonical profile of the transition region)

Reading the scale map (proved) in continuous dimension gives a closed-form profile for the transition region:

$$D(l) = 1 + \min\!\left[3,\ \left(\frac{l}{l_{P}}\right)^{4/\alpha}\right], \qquad \frac{4}{\alpha} = 0.03392$$

This reproduces exactly $D = 2$ at $l = l_{P}$ and $D = 4$ at $l = l(3)$, and uniquely interpolates the interior (e.g. $D = 2.26$ at $l = 10^{3}\,l_{P}$, $D = 2.73$ at $10^{7}\,l_{P}$). If quantum-gravity numerical simulations measure the $d_{s}(l)$ profile with high precision, this formula is in principle falsifiable.

#### Corollary 9.7.6 (Quantitative structure of the transition region)

Since the canonical profile (Corollary 9.7.5) is in closed form, the quantitative properties of the transition region are analytically determined. In the transition region ($l_{P} \leq l \leq l(3)$), $D(l) - 1 = (l/l_{P})^{4/\alpha}$, so the dimensional flow obeys a power law with respect to logarithmic scale:

$$\frac{d(D-1)}{d\ln l} = \frac{4}{\alpha}\,(D-1)$$

The flow rate increases monotonically from $4/\alpha = 0.03392$ e-fold$^{-1}$ (at $D = 2$) to $2 \times 0.03392$ e-fold$^{-1}$ (at $D = 3$); the full transition spans $\dfrac{\alpha}{4}\ln 3 = 32.4$ e-folds, i.e. $14.1$ decades of scale. The half-flow point ($D = 3$) is exactly reached at $l(2) = l_{P} \cdot 2^{\alpha/4} = 1.21 \times 10^{-26}\,{\rm m}$ ($1.6 \times 10^{10}$ GeV).

Comparison: the CDT dimensional flow completes at roughly $l \sim O(10)\,l_{P}$, and in asymptotic safety the flow proceeds rapidly from the $d_{s} = 2$ plateau near the UV fixed point to 4. The flow of the present theory is a slow power law spanning 14.1 decades, and quantitatively disagrees with those approaches in the entire transition region (the agreement at both endpoints being a theorem). The discriminant prediction takes the form: if the half-flow of dimension ($D = 3$ equivalent) is measured at a scale significantly removed from $1.6 \times 10^{10}$ GeV, the canonical profile of the present theory is falsified.

### 9.8 Derivation of the Scalar Spectral Index $n_{s}$

#### 9.8.1 Mechanism-based derivation ($n_{s} = 1 - 4/\alpha$)

Derivation: the equipartition principle used in §9.1 to derive $r = 1/D_{2}$ (independent channels of multiplicative canonical quantisation carry equal fluctuation amplitude $h_{0}$) is applied to the scale-dependent channel count. The number of dimensions established at scale $l$ is $n(l)$ (from the map $l(n) = l_{P}\,n^{\alpha/4}$ of Corollary 9.7.2, derived), and each dimension constitutes an independent fluctuation channel. By equipartition, channel contributions add, so the fluctuation power at scale $l$ is

$$P(k) \propto n(l(k)) \cdot h_{0}^{2}, \qquad l \sim 1/k$$

Since the inverse slope of the scale map is $d\ln n/d\ln l = 4/\alpha$,

$$n_{s} - 1 = \frac{d\ln P}{d\ln k} = -\frac{d\ln n}{d\ln l} = -\frac{4}{\alpha}$$

$$\boxed{n_{s} = 1 - \frac{4}{\alpha} = 1 - \frac{4\ln 11}{90\pi} = 0.96608}$$

Discrepancy from the observed value $n_{s} = 0.9649 \pm 0.0042$ (Planck 2018): $0.28\sigma$.

Status of the derivation: equipartition (equal zero-point amplitudes of independent harmonic oscillators with identical boundary conditions, identical mass, and identical potential) is a theorem of quantum mechanics under the self-adjoint quantisation on $L^{2}([0, \ln n^{\ast}])$ established in §6.8. Channel addition (independence) likewise. The scale map is derived in Corollary 9.7.2. The remaining step is the following identification postulate I, proved as Theorem 9.8.2.

Identification postulate I: the number of independent channels sampled by fluctuations at scale $l$ equals the number of dimensions $n(l)$ established at that scale.

#### Theorem 9.8.2 (Proof of identification postulate I)

Theorem: identification postulate I is a theorem of the Axiom Ω system.

**Proof (five steps, each a definition or an established theorem):**

Step 1 (Definition of the observable): the primordial scalar fluctuation observed in the CMB is the curvature perturbation $\zeta$, defined via the total energy-density fluctuation $\delta\rho$ on uniform-density hypersurfaces (standard cosmological definition).

Step 2 (Additivity of energy): the $n(l)$ dimensions established at scale $l$ each carry an equal share of the total energy density $\varepsilon$:

$$\rho = \sum_{j=1}^{n(l)} \rho_{j}, \qquad \langle\rho_{j}\rangle = \varepsilon/n$$

The equal sharing follows from the $SO(n)$ isotropy of Lemma B0 (transitive action on directions). Additivity of energy over constituents is by definition.

Step 3 (Independence): the fluctuations $\delta\rho_{j}$ of each dimension correspond to independent oscillators in distinct coordinate directions. The Hilbert space of this multi-channel structure is explicitly constructed by the tensor-product construction

$$\mathcal{H}_{n} = \bigotimes_{j=1}^{n} h_{j}$$

(see [Revision and Audit Record §3.3](08_revision_history.md#33-resolution-by-the-third-round-of-verification)), and since an $SO(n)$-invariant quadratic-form Hamiltonian is forced into a decoupled form by Schur's lemma, independence is a theorem of the construction.

Step 4 (Additivity of variances): the variance of a sum of independent random variables equals the sum of variances (theorem of probability theory).

Step 5 (Equipartition): oscillators with identical boundary conditions, identical mass, and identical potential have equal zero-point variance (theorem of quantum mechanics, valid under the self-adjoint quantisation of §6.8): $\mathrm{Var}(\delta\rho_{j}) = h_{0}^{2}$ (independent of $j$).

Therefore $P(k) \propto \mathrm{Var}(\delta\rho) = n(l(k)) \cdot h_{0}^{2}$. The channel count $= n(l)$ is not an assumption but a consequence of the fact that the observable is the total energy fluctuation and that energy is additive over dimensions. $\square$

Corollary: the additivity rule $P_{S} \propto D_{2} \cdot h_{0}^{2}$ in $r = 1/D_{2}$ of §9.1 is proved by the same five steps, upgrading the $r$ derivation to the same theorem status. Both predictions ($r = 1/54$ and $n_{s} = 1 - 4/\alpha$) share a single proof, so the CMB-S4 test of $r$ simultaneously adjudicates the derivation of $n_{s}$.

#### Theorem 9.8.3 (Internalisation of Step 1)

Theorem: Step 1 of Theorem 9.8.2 (correspondence of the observed scalar fluctuation with $\delta\rho$) decomposes into pure definitions and internal theorems of the present theory, containing no independent external assumption.

**Proof (four steps):**

Step A (freedom of definition): the curvature perturbation $\zeta$ is a definition of a gauge-invariant quantity; the choice of definition carries no physical claim. On uniform-density hypersurfaces, $\zeta = \delta\rho/[3(1+w)\rho]$ (algebraic correspondence with $\delta\rho$ on flat slices).

Step B (internal derivation of adiabaticity):

Lemma B0 (identity of response functions): the geometric realisation at scale $l$ is $SO(n(l))$-invariant (same symmetry structure as $SO(3)$ of Theorem 4.1.1 and $SO(n^{\ast}-1)$ of §6.4), and the rotation group acts transitively on directions. Hence there always exists an isometry mapping one direction $j$ to another, and the background values ($\rho_{j}$, $p_{j}$) and linear response functions (squared sound speed $c_{s,j}^{2}$) are identical for all $j$: $c_{s,j}^{2} = c_{s}^{2}$.

Lemma B1 (identity of states): each channel is in the ground state of the quantisation in §6.8. Zero-point variance is ineliminable even in the ground state (theorem of quantum mechanics), and this is the source of the zero-point variance in Step 5. Identical Hamiltonian + identical state gives all expectations equal.

Step B body (vanishing of non-adiabatic pressure): each channel's perturbation satisfies $\delta p_{j} = c_{s,j}^{2}\,\delta\rho_{j}$. For the total,

$$\delta p_{\rm nad} = \sum_{j} c_{s,j}^{2}\,\delta\rho_{j} - \frac{\sum_{j} c_{s,j}^{2}\,\dot{\rho}_{j}}{\sum_{j} \dot{\rho}_{j}}\sum_{j} \delta\rho_{j}$$

This is generally non-zero when the $c_{s,j}^{2}$ differ, but by Lemma B0 all $c_{s,j}^{2} = c_{s}^{2}$, so it vanishes identically (verified by symbolic computation). Adiabaticity is a consequence not of identical channels per se but of the identity of response functions guaranteed by $SO(n)$ isotropy.

Step C (internal derivation of superhorizon conservation): by the established theorem (Wands–Malik–Lyth–Liddle 2000), $\dot{\zeta} = -\dfrac{H}{\rho+p}\,\delta p_{\rm nad}$; the derivation of this theorem uses only local energy conservation $\nabla_{\mu}T^{\mu\nu} = 0$, not Einstein's equations. The present theory already uses the same conservation law in §9.3 (proof of $w = -1$), so no new external input is introduced. Together with Step B, $\dot{\zeta} = 0$, i.e. the primordial spectrum is conserved until observation.

Step D (invariance of the tilt under transfer): the transfer coefficient $1/[3(1+w)\rho]$ is $k$-independent since, by Postulate B2 (scale invariance), $w$ at horizon crossing is $k$-independent. Hence $P_{\zeta}(k) \propto P_{\delta\rho}(k)$, and $n_{s} = 1 - 4/\alpha$ is independent of the choice of definition. $\square$

Consequence: by Theorems 9.8.2 + 9.8.3, the only theory-external element on which the derivations of $n_{s}$ and $r$ rely is GR + Boltzmann transfer in the observable domain ($D = 4$). This is the same shared premise already declared in §8.8 Conclusion 3 (shared by all cosmologies) and has been jointly verified with the theory's parameter set by the first-principles six-peak verification (§8.8). The $n_{s}$ and $r$ sectors are thus closed on a single shared premise together with the CMB sector.

Additional consequence: since the tilt is exactly constant, the running is strictly zero:

$$\frac{dn_{s}}{d\ln k} = 0$$

Consistent with the observed value $-0.0045 \pm 0.0067$ (Planck 2018) at $0.67\sigma$. A future detection of running would immediately falsify this derivation.

#### 9.8.2 Alternative conjecture (recorded)

Conjecture A (identification of e-fold number): $N = D_{2}(S^{9}) = 54 \Rightarrow n_{s} = 1 - 2/N = 26/27 = 0.96296$ (discrepancy $0.46\sigma$). $N = 54$ lies inside the standard required range $50$–$60$, and this has the elegance of closing $r = (1-n_{s})/2$ exactly in terms of $D_{2}$ alone, but lacks the mechanism of §9.8.1. The difference $0.0031$ between the two is resolvable at CMB-S4 precision ($\sigma(n_{s}) \sim 0.002$), and observations will provide the final verdict.

### 9.9 Derivation of Dimension Waves from the Axiom

#### Theorem 9.9.1 (Existence of dimension waves is a theorem)

Theorem: the existence of wave modes of the dimension field is a theorem of the Axiom Ω system, not an assumption.

**Proof:** As established in §6.8, quantum mechanics in the dimension coordinate $u = \ln n$ is formulated by a Dirichlet self-adjoint operator on $L^{2}([0, \ln n^{\ast}])$, whose eigenmodes are standing waves:

$$\Psi_{k}(u) = \sin\!\left(\frac{\pi k\, u}{\ln n^{\ast}}\right), \qquad k = 1, 2, 3, \ldots$$

These are literally waves in the dimension direction $u$, and their existence is a consequence of the spectral theorem. Dimension waves are therefore not a new assumption to be introduced but a structure already contained in the quantisation of §6.8. $\square$

#### Corollary 9.9.2 (Observational manifestation of dimension waves)

A local fluctuation $\delta n$ of the dimension number induces an energy-density fluctuation

$$\delta\varepsilon = -\alpha\,\varepsilon\,\frac{\delta n}{n}$$

(direct consequence of $\varepsilon = E_{0} n^{-\alpha}$). This is the same primordial scalar fluctuation treated in Theorem 9.8.2; its spectrum $P \propto n(l)$ and tilt $n_{s} = 1 - 4/\alpha$ are already derived. The observational manifestation of dimension waves is therefore the primordial scalar spectrum of the CMB, and the observation of $n_{s}$ ($0.28\sigma$ consistent) provides the first indirect verification of dimension waves.

The derivation of $n_{s}$ (Theorems 9.8.2 + 9.8.3) is closed using $\delta\rho_{j}$ alone and does not use the spatial locality of $\delta n$. Reading $\delta n(x)$ as a local field on space is an interpretive note; the established results of the theory do not depend on it.

#### Scope limitation

This section establishes only the existence of dimension waves and their scalar manifestation. The relation between dimension waves and other physical degrees of freedom (including tensor modes of the metric) is not among the established results of the theory and is not claimed here.

### 9.10 Multi-Degree-of-Freedom Field Structure: Second Quantisation and Block Equipartition

#### Theorem 9.10.1 (Fock construction and intra-block equipartition)

The finite-tensor-product construction of §11.10.4 is lifted to an infinite-degree-of-freedom field structure as follows.

Construction: taking the single-particle space as the $S^{9}$ spherical-harmonic decomposition

$$\mathcal{H}_{1} = \overline{\bigoplus_{\ell \geq 0} V_{\ell}}, \qquad \dim V_{\ell} = D_{\ell}(S^{9})$$

(each $V_{\ell}$ is $SO(10)$-irreducible), the field state space is the symmetric Fock space

$$\mathcal{F} = \bigoplus_{N \geq 0} \mathrm{Sym}^{N} \mathcal{H}_{1}$$

The action of $SO(10)$ (the isometry group of $S^{9}$) is lifted to $\mathcal{F}$ by the second-quantisation functor.

Theorem: an $SO(10)$-invariant quadratic-form Hamiltonian is restricted, by applying Schur's lemma block-by-block to each irreducible block, to the form

$$H = \sum_{\ell} \omega_{\ell} \sum_{m=1}^{D_{\ell}} a_{\ell m}^{\dagger}\, a_{\ell m} \qquad (\omega_{\ell} > 0)$$

Hence all $D_{\ell}$ modes in the same $\ell$-block carry identical frequency, and the zero-point variance in the ground state is exactly equal (intra-block equipartition). Moreover, the modes are automatically decoupled and independence holds. $\square$

Consequence: the equipartition of the $D_{2} = 54$ scalar modes used in $r = 1/D_{2}$ of §9.1 is precisely the application of this theorem to the $\ell = 2$ block, grounded at the field level rather than with a finite number of channels. The frequency ratio $\omega_{\ell}/\omega_{\ell'}$ between blocks is not determined by this construction, but this does not affect the derivations of $r$ and $n_{s}$, which use only intra-block equipartition.

Status of remaining premises: the choice of Fock representation (in infinite degrees of freedom non-equivalent representations exist) and the form of interaction terms are outside this construction; both are standard-grade premises shared with standard field theory. Derivation of interactions is not carried out.

### 9.11 SO(10) Structural Correspondence and the Breaking Chain

#### 9.11.1 Location of the Structural Agreement

The isometry algebra $\mathrm{so}(10)$ of the spatial sphere $S^{n^{\ast}-2} = S^{9}$ of the present theory has dimension 45, coinciding with the dimension 45 of the gauge adjoint representation of the SO(10) grand unified theory. The Weyl spinor of $\mathrm{Spin}(10)$ is 16-dimensional, coinciding with the 16 of one Standard Model generation (including right-handed neutrino). The generation number $3 = n_{\rm obs}$ is proved. This section unfolds this structural agreement into a chain using only established group theory and existing internal structures of Ω, with the status of each step rigorously distinguished.

#### Theorem 9.11.2 (Breaking chain: mathematics of branching and Ω-internal grounding)

The following inclusion chain is established group theory, and the direction choice at each step is grounded in existing structures of the present theory:

$$SO(10) \;\supset\; SO(3) \times SO(7) \;\supset\; SO(3) \times G_{2} \;\supset\; SO(3) \times SU(3)$$

Step 1 ($10 = 3 + 7$): split into the 3 observable directions (Theorem 4.1.1, Hurwitz) and the 7 hidden directions. Since $7 = n^{\ast} - 1 - n_{\rm obs} = \dim \mathrm{Im}\,\mathbb{O}$, the number of hidden directions coincides with the dimension of the imaginary part of the octonions. The choice of split count 3 is grounded by Hurwitz's theorem and contains no external selection. Dimension count: $\dim = 3 + 21 = 24$, coset 21.

Step 2 ($SO(7) \supset G_{2}$): identifying the octonion multiplication of the Cayley–Dickson tower (§4–§5) with the hidden 7 directions (Identification Postulate G, §9.11.4), the symmetry is reduced to the automorphism group of the multiplication, $\mathrm{Aut}(\mathbb{O}) = G_{2}$ ($\dim 14$). $G_{2} \subset SO(7)$ is established.

Step 3 ($G_{2} \supset SU(3)$): fixing the complex unit $i$.

$$\mathrm{Stab}_{G_{2}}(i) = SU(3), \qquad G_{2}/SU(3) = S^{6}$$

is established. The $i$ being fixed is precisely the unit that §6.8 (Necessity of the complex Hilbert space) already requires internally; this step contains no new selection.

Verification of branching rules (established branching):

$$\mathbf{10} = (\mathbf{3},\mathbf{1}) \oplus (\mathbf{1},\mathbf{7}), \qquad \mathbf{45} = (\mathbf{3},\mathbf{1}) \oplus (\mathbf{1},\mathbf{21}) \oplus (\mathbf{3},\mathbf{7})$$

$$\mathbf{16} = (\mathbf{2},\mathbf{8}), \qquad \mathbf{8} \xrightarrow{\;G_{2}\;} \mathbf{7} \oplus \mathbf{1}, \qquad \mathbf{7} \xrightarrow{\;SU(3)\;} \mathbf{3} \oplus \bar{\mathbf{3}} \oplus \mathbf{1}$$

$$\therefore\quad \mathbf{16} = (\mathbf{2},\mathbf{3}) \oplus (\mathbf{2},\bar{\mathbf{3}}) \oplus 2\,(\mathbf{2},\mathbf{1})$$

That is, the representation content of one-generation type — colour triplets, anti-triplets, and two singlets accompanied by $\mathrm{Spin}(3)$ doublets — is exactly reproduced, together with the dimension counts $2 \times 8 = 16$, $3 + 3 + 1 + 1 = 8$, $3 + 21 + 21 = 45$ (isomorphic to the Günaydin–Gürsey 1973 decomposition). The total fermionic content is $3 \times 16 = 48$ by $n_{\rm obs} = 3$ generations. $\square$

#### 9.11.3 Location of the Electroweak Factor and Stopping Point of the Chain

$G_{2}$ has rank 2, and $SU(3) \times SU(2) \times U(1)$ of rank 4 cannot be embedded in $G_{2}$. Indeed,

$$\mathrm{Stab}_{G_{2}}(\mathbb{H}) = SO(4) \cong (SU(2) \times SU(2))/\mathbb{Z}_{2}$$

Fixing all of the Cayley–Dickson flag $\mathbb{C} \subset \mathbb{H} \subset \mathbb{O}$ reduces the subgroup to

$$\mathrm{Stab}_{G_{2}}(i) \cap \mathrm{Stab}_{G_{2}}(\mathbb{H}) \cong U(2) \subset SU(3)$$

Hence realising $\mathbb{H}$ as a fixed direction inside the octonions causes the colour $SU(3)$ itself to break to $U(2)$. The structure of the present theory therefore forces the reading that the Cayley–Dickson $\mathbb{H}$ is realised not as a breaking direction inside the octonions but as an independent spin structure (Corollary 11.5.2, $\mathrm{Spin}(3) \cong Sp(1)$). Candidates for the electroweak factor $SU(2) \times U(1)$ exist in the Cayley–Dickson $\mathbb{H}$ ($Sp(1) = SU(2)$) and $\mathbb{C}$ ($U(1)$), but the chain inside $\mathrm{so}(10)$ stops at $SO(3) \times SU(3)$. The integration of both layers (electroweak factor and $\mathrm{so}(10)$ structure) is not derived and is not claimed in this section.

Note: for the Pati–Salam type $SO(10) \supset SO(6) \times SO(4)$ split $10 = 6 + 4$, no grounding source exists within the present theory; nor does a grounding source exist for the complex-structure selection in the $SU(5)$ path. Neither is adopted. The adopted chain is the unique path possessing a grounding source.

#### 9.11.4 Identification Postulate G and Rigorous Classification of Status

Identification Postulate G: the hidden 7 directions carry the octonion multiplication structure of the Cayley–Dickson tower, and the branching content of the $\mathrm{so}(10)$ channels corresponds to the representation content of physical degrees of freedom.

Classification of status: the inclusion relations and branching rules of the chain are established mathematics (Theorem 9.11.2). The grounding of direction choices at each step (the $3 + 7$ split, the roles of $i$ and $\mathbb{H}$) comes from existing theorems and structures of the present theory and contains no new selection. Identification Postulate G is at the conjecture level (falsifiable) and is assigned the same status as the closed form in §8.9. It holds a weaker status than the standard-grade premises (GR + Boltzmann transfer, etc.). None of the existing claims of the theory ($\Lambda$, CMB, $n_{s}$, $r$, $T_{\rm CMB}$, etc.) depend on Identification Postulate G. Unresolved items include: the hypercharge normalisation, the global structure ($\mathbb{Z}_{6}$ quotient), Yukawa couplings and the mass spectrum, and the scale of breaking.

Note on scales: the scale map $l(n)$ of the present theory places the $SO(10)$ completion at large scales ($l(10) \sim 10^{-6}\,{\rm m}$), so a naive identification of scale with high-energy symmetry restoration — the standard grand-unification picture — runs opposite to the direction of the present theory and is not made. For the same reason, gauging of the 45 channels is not claimed. If gauging were claimed, proton decay via $X, Y$-type mediators would immediately conflict with current experimental lower bounds; the absence of this conflict is therefore part of the falsification criterion for Identification Postulate G (which is consistent only in the form claiming representation content without claiming gauging).

Record (proximity indistinguishable from coincidence): the cascade scale $1.6 \times 10^{10}$ GeV at $n = 2 \to 3$ established by the first-step split (Corollary 9.7.2) lies inside the seesaw-mechanism typical range $10^{10}$–$10^{14}$ GeV. As with the $n_{\rm obs}^{3}$ proximity in §8.9, this cannot currently be distinguished from coincidence and is recorded as such.

---

← [§8: CMB Peak Structure](05_cmb_peaks.md) | Next → [§10–§11: Numerical Verification and Completeness Assessment](07_verification_and_completeness.md)
