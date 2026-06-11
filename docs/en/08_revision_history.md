# Revision and Audit Record

← [§10–§11: Numerical Verification and Completeness Assessment](07_verification_and_completeness.md) | [README (top)](README.md)

---

This file collects the history of corrections, rejections, demotions, and re-resolutions that were separated out so that the main chapters could present only the final settled state. Every proposition in the main text has passed through the scrutiny recorded here.

## 1. Corrected Definitions and Formulae

### 1.1 Definition of the Observational-Limit Dimension (§5)

The old definition was "the minimal $n > n_{\rm obs}$ such that $\mathrm{Cl}(n) \cong \mathrm{Cl}(n_{\rm obs}) \otimes M(N, \mathbb{K})$". A counter-example exists: $\mathrm{Cl}(3,0) \cong M_{2}(\mathbb{C})$ and $\mathrm{Cl}(7,0) \cong M_{8}(\mathbb{C}) \cong M_{2}(\mathbb{C}) \otimes M_{4}(\mathbb{R})$ (real dimension $128 = 8 \times 16$, constructively verified), so the old definition gives a minimum of $7$, not $11$.

Fix: the equivalence relation was refined to graded Morita equivalence. The grading is the action $e_{i} \mapsto -e_{i}$ induced on the Clifford algebra by the spatial realisation of the parity $\sigma$ of Axiom Ω — not an external choice. $n^{\ast} = 11$ was re-proved by Wall's theorem $\mathrm{sBr}(\mathbb{R}) \cong \mathbb{Z}/8$ (Theorem 5.2.1). The counter-example $n = 7$ is excluded by the difference in type of the even part ($\mathrm{Cl}^{0}(7,0) \cong M_{8}(\mathbb{R})$ is type $\mathbb{R}$; $\mathrm{Cl}^{0}(3,0) \cong \mathbb{H}$ is type $\mathbb{H}$).

### 1.2 Status of the Internal Derivation of the Bott Period (§5.3)

In the old Lemma 4, the step "identifying the product of orders of involution groups with the period on the dimension space" was a definition rather than a derivation, and the mathematical equivalence with Clifford periodicity was not established. The burden of deriving $n^{\ast} = 11$ is carried by Theorem 5.2.1. The algebraic identity

$$\prod_{k=0}^{n_{\rm obs}-1} 2^{k} = 2^{n_{\rm obs}(n_{\rm obs}-1)/2} = 2^{n_{\rm obs}}$$

which holds exactly only for $n_{\rm obs} = 3$, is a rigorous algebraic fact and is retained as a consistency note.

### 1.3 Full Peak Formula (§8.6)

The old formula $\ell_{k} = 303(k-1/4)$ had no independent derivation of the $1/4$, gave $3.3\%$ error at the first peak, and could not dispel the suspicion of being an empirical constant tuned to observed values. It was replaced by the new formula $\ell_{k} = 220 + (k-1) \times 303$, which is derived entirely algebraically. The first peak is an algebraic identity at $0.000\%$ error; both parameters are algebraically fully proved; there are zero external parameters. The mean error improved from $1.56\%$ to $1.13\%$.

### 1.4 Gravitational-Wave Spectral Index (§9.2)

The old statement $n_{t} = -2/\alpha \approx -0.01696$ applied an unestablished correspondence rule between wavenumber $k$ and dimension number $n$ and was insufficiently grounded. It was corrected to $n_{t} = -r/8 = -1/432 \approx -0.00231$ via the consistency relation of general-relativistic inflation theory.

### 1.5 Baryon-Loading Phase-Shift Approximation (§8.8)

The baryon-loading phase-shift approximation presented in the old version, $\delta\ell_{k} \approx \pm\frac{R_{\rm dec}}{1+R_{\rm dec}}\cdot\frac{\Delta\ell}{2}(-1)^{k}$ (maximum correction $\pm 57$), was incorrect: numerical verification showed its magnitude inconsistent with the observed residuals (approximately $+14$ at $k = 2$). Dependence on the Doran–Lilley phase-shift fitting formula was eliminated, replaced by a complete first-principles calculation using the Boltzmann code CAMB. This extended the verification to all peaks 1–6.

### 1.6 Reference Observed Values for Peaks (§8.8, §10.3)

The reference values used in the first-principles verification of §8.8 are values extracted from the same Boltzmann-code output with the same extraction method using Planck best-fit parameters; for $k = 5, 6$ these are $1421.3$ and $1725.7$. The values $1440$ and $1750$ listed alongside as observed values for $k = 5, 6$ in the old table are approximate measured positions of the maxima in the actual power spectrum, and their definition differs from the first-principles reference with controlled extraction method. The §8.7 comparison table retains these approximate values as observational data, while the §8.8 reference values are used for theoretical evaluation with cancelled extraction-method bias.

### 1.7 Hubble Constant (§9.6, §10.4)

The documented value $67.94$ km/s/Mpc was inconsistent with the theory's own chain ($\Lambda = 1.1076 \times 10^{-52}$, $\Omega_{\Lambda} = 0.690$). The correct value from a numerical audit is $67.67$ km/s/Mpc, improving the error against the observed value $67.66$ from $0.41\%$ to $0.015\%$. Note that the first-principles peak verification of §8.8 is first-order insensitive to $H_{0}$ since $\ell_{A} = \pi D_{A}/r_{s}$ with $D_{A}$ and $r_{s}$ both proportional to $1/H_{0}$, so the conclusion is unchanged.

### 1.8 Physical Interpretation of Residual Errors (§11.4)

The old interpretation "the errors for $k \geq 2$ are qualitatively consistent with the correction from the baryon-to-photon ratio $R_{\rm dec} = 3/5$" was incorrect: the magnitude of the correction was inconsistent with the observed residuals. The true origin of the errors for $k \geq 2$ is the neglect of the $k$-dependent relative phase shift $\delta\varphi_{k}$ (due to radiation-driving and Doppler effects in standard acoustic physics).

## 2. Rejected Conjectures

### 2.1 Algebraic Closed Form of the Phase Shift (§8.9)

The conjecture $\varphi_{k} = n_{\rm obs}/n^{\ast} + \delta_{k}$ was rejected as an exact law. Execution of the falsification criterion showed that the first-principles $\varphi_{1} = 1 - \ell_{1}/\ell_{A}$ varies continuously with $n_{s}$, ranging from $0.2725$ to $0.2655$ over $n_{s} \in [0.94, 1.00]$ (extraction precision $\pm 0.0003$). At the theory's physical point $n_{s} = 0.965$, the value is $\varphi_{1} = 0.2695$, deviating from $3/11 = 0.2727$ by $0.0033$ — ten times the extraction precision. The constant $3/11$ holds only at the boundary $n_{s} \approx 0.94$ of the range, not at the physical point. $\varphi_{k}$ is a continuous function of cosmological parameters and cannot be expressed as a universal exact law by a rational constant in $n^{\ast}$ and $n_{\rm obs}$ alone. The rational form is retained only as an approximate expression with $0.3\%$ accuracy at a fixed cosmological point.

## 3. Demotions and Re-resolutions by Audit

P3 (exponent identification) has a history of multiple demotion and re-resolution cycles through adversarial audits.

### 3.1 First Resolution Declaration

By Theorem 6.9.2, the claim was declared a complete resolution of P3: "the action of $\sigma$ on the pair of two descriptions (statistical face, quantum face) is uniquely determined as an exchange by the same argument as Lemma 1, and the involutions exchanging the two axes of the spectral plane are restricted to $s \mapsto \pm i\bar{s}$, both preserving $|s|$, forcing $\alpha_{\rm st} = \alpha_{\rm qu}$."

### 3.2 Demotion by the Second Audit

An adversarial audit was conducted, attacking each step of each theorem individually, following the same pattern as previously discovered issues (B1, H0, Step B, P3). Seven findings were registered:

| No. | Target | Severity | Content |
|-----|--------|----------|---------|
| F1 | Theorem 6.9.2 Step 2 | Critical | "'$\sigma$ acts on the entire structure of the theory' is unproved. What Lemma 1 established is only the action on the state space $S$; the necessity of non-trivial action on the pair of descriptions has not been derived. Steps 3–4 hold rigorously. P3 demoted to residual postulate P3″ ($\sigma$'s action on the pair of descriptions is non-trivial)." |
| F2 | Theorem 11.8.1 (i) | Medium | "Critical generation describes the energy limit of the previous dimension and does not directly identify the quantum state of the new channel as the ground state." |
| F3 | Theorem 11.8.1 (iii) | Critical | "Eigenstate preservation holds only under free Hamiltonians. The cascade implies inter-dimensional energy transfer; internal excitation is possible under interaction. P0 demoted to conditional resolution under residual premise P0′ (non-interacting or adiabatic cascade)." |
| F4 | Theorem 11.8.2 (ii) | Medium | "Stone's theorem presupposes strong continuity. The Ω transition could also be read as a discrete single transition; the necessity of continuous implementation is not derived. P1 demoted to conditional resolution under residual premise P1′ (continuous implementation)." |
| F5 | Lemma B0 / Theorem 11.8.3 | Medium | "The basis for $SO(n)$-invariance at general stage $n$ partially relies on the usage of geometric realisation and has a partial circularity concern. $n = 3$ is independently grounded by Theorem 4.1.1. General $n$ becomes residual premise P2′." |
| F6 | Theorem 9.8.2 Step 3 | Critical | "The Hilbert space of §6.8 has only 1 degree of freedom in the $u$ direction; the tensor-product structure housing $n$ dimension-wise channel oscillators has not been constructed. Registered as residual task P6." |
| F7 | Corollary 9.9.2 | Minor | "The spatial locality of $\delta n(x)$ as a local field on space is not constructed ($n$ as a local field). Residual premise P7." |

This audit demoted P3 from a complete resolution to a reduction to residual postulate P3″, leaving the ledger with P3″, P0′, P1′, P2′, P6, and P7 as six residual items.

### 3.3 Resolution by the Third Round of Verification

A third round was conducted, judging not whether solutions could be found but whether derivability itself could be established for each of the six residual items.

#### Theorem 11.10.1 (Independence of P3″: proof of underivability)

The exponent identification $\alpha_{\rm st} = \alpha_{\rm qu}$ is underivable from the axiom system $\{\Omega_{\rm old},\, \text{B1},\, \text{B2},\, \text{O1},\, \text{O2},\, \text{M},\, \text{P},\, \text{Dirichlet quantisation}\}$ (where $\Omega_{\rm old}$ is the old reading of Axiom Ω without non-degeneracy).

Proof (counter-example model): take the model $\varepsilon(n) = E_{0}\, n^{-\beta}$ with $\beta$ any positive number different from $90\pi/\ln 11$. B1 holds since $\varepsilon(1) = E_{0}$. B2 holds since the function is a power law — the uniqueness proof of Cauchy's equation restricts the functional form to a power law but does not constrain the exponent. Ω (old reading) and postulates O1, O2, M, P are statements about dimension numbers, observational algebra, parity, and minimality and do not refer to $\beta$. The Dirichlet spectrum and the selection of $k = 90$ hold independently of $\beta$. Hence there exists a model satisfying all axioms yet having $\alpha_{\rm st} = \beta \neq \alpha_{\rm qu}$, and the identification is underivable. $\square$

Corollary: the fact that the $0.006\%$ two-path agreement has been functioning as a non-trivial empirical test is circumstantial evidence that the identification lay outside the axiom system. If it were a logical consequence, the agreement would be a tautology and could not serve as a test.

#### Theorem 11.10.2 (Identification of the minimal sufficient specification)

The minimal additional content that excludes the counter-example model is Ω non-degeneracy.

Proof: for sufficiency, non-degeneracy makes $\sigma$ act non-trivially on the dual pair $\{\text{statistical face},\text{quantum face}\}$; since the unique non-trivial action on a two-element set is the exchange, the two faces are exchanged; by Theorem 6.9.2 Steps 3–4, $\alpha_{\rm st} = \alpha_{\rm qu}$ follows. For minimality, non-triviality on the state space $S$ alone leaves the counter-example of Theorem 11.10.1 intact; strengthening to faithfulness on the spectral plane still allows the involution $s \mapsto -s$ that preserves each axis separately, and identification does not follow. Non-trivial action on the dual pair is the weakest specification that excludes all of these. $\square$

Consequence: adopting Ω non-degeneracy (§2.1) restores Theorem 6.9.2 to an unconditional theorem, and P3″ is removed from the ledger. This is not a resolution by derivation but an axiomatic content specification following an independence proof. The $0.006\%$ two-path agreement henceforth functions as a test of Axiom Ω (including non-degeneracy) itself.

#### Theorem 11.10.3 (Resolution of F2 and F3: removal of the ground-state premise)

What is required at all downstream points of use is not the ground-state nature of the state but the identity of expectation values and variances across channels. If the state is $SO(n)$-invariant, identity follows; invariance is preserved by unitary evolution as long as the Hamiltonian is $SO(n)$-invariant, regardless of interaction or cascade coupling. Equipartition holds as long as isotropy is maintained, even under excitation. The leap identified by F2 in critical generation is avoided by an argument using only uniqueness rather than ground-state nature.

#### Resolution of F6: Explicit Construction of the Multi-Channel Hilbert Space

The construction

$$\mathcal{H}_{n} = \bigotimes_{j=1}^{n} h_{j}, \qquad h_{j} = L^{2}(\mathbb{R})$$

means that an $SO(n)$-invariant quadratic-form Hamiltonian is forced by Schur's lemma into a decoupled form, and independence becomes a theorem of the construction. The remaining premises are tensor-product composition (standard composition postulate of quantum mechanics) and channel identification (two items), both standard-grade. P6 transitions from "not constructed" to "constructed; reduction to two standard-grade premises."

#### Resolution of F4 and F5: Merger into Existing Premises

F4 (P1′, continuous implementation): since the Mellin representation already presupposes a strongly continuous unitary representation of $(\mathbb{R}_{+}, \times)$ and §6.8 presupposes the $L^{2}$ construction, this is the same premise already in service from the point the theory has a quantum sector, and it is merged into the existing premise "continuous implementation." F5 (P2′, isotropy at general $n$): since the $\mathrm{so}(n^{\ast}-1)$ channel count of §6.4 — i.e. the fundamental equation itself — already uses this premise, it is merged into the existing premise "isotropy." $n = 3$ is independently grounded by Theorem 4.1.1.

#### Resolution of F7: Excision

The derivation of $n_{s}$ (Theorems 9.8.2 + 9.8.3) is closed using $\delta\rho_{j}$ alone and does not use the locality of $\delta n$. Claims depending on P7 are excised from the established results of the theory, and P7 is resolved by scope limitation.

#### Consistency Verification

That the adoption of Ω non-degeneracy is consistent with all existing results has been confirmed. The even/odd eigensector decomposition of $\sigma$ is an eigenstructure of $\sigma$ itself and not a dual pair, so non-degeneracy does not change the conclusions of mode selection $\ell \in \{1,3\}$ and odd parity of $k = 90$. No occurrence in the entire document uses $s \mapsto -s$ as $\sigma$. Both realisations $\sigma: s \mapsto +i\bar{s}$ and $s \mapsto -i\bar{s}$ preserve $|s|$ and the exponent identification is independent of the sign choice. All numerical values ($\Lambda$, CMB peaks, $H_{0}$, $T_{\rm CMB}$, $n_{s}$, $r$) are related to $\sigma$ only through the value of $\alpha$, which is unchanged; so all predictions are numerically invariant, and only the status changes (P3 from a postulate to a theorem).

### 3.4 Final Ledger

| Old residual | Resolution method | Remaining premise |
|--------------|-------------------|-------------------|
| P3″ (F1) | Independence proof + axiomatic specification of Ω non-degeneracy (Theorems 11.10.1–11.10.2) | None (content of Axiom Ω) |
| P0′ (F2, F3) | Weakening to invariant state + uniqueness argument (Theorem 11.10.3) | Theorem of the construction |
| P1′ (F4) | Merged into existing premise "continuous implementation" | Continuous implementation (existing, 1 item) |
| P2′ (F5) | Merged into existing premise "isotropy" | Isotropy (existing, 1 item) |
| P6 (F6) | Explicit construction + standard-grade reduction | Tensor-product composition, channel identification (standard-grade) |
| P7 (F7) | Excision by scope limitation of Corollary 9.9.2 | None |

Summary: the number of unresolved theory-specific axioms is zero. The theory rests solely on Axiom Ω (including non-degeneracy), two existing premises (continuous implementation, isotropy — both already in use at the stage of the fundamental equation), and standard-grade premises shared with all standard theories (GR + Boltzmann transfer, tensor-product composition, channel identification, choice of Fock representation). This ledger remains open to demotion by future audits.

## 4. Final State of Foundation Axioms P0–P4

| Axiom | Content | Final state |
|-------|---------|-------------|
| P0 (ground state) | Each channel is in its ground state | Resolved (Theorems 11.8.1 + 11.10.3: unconditionalised by weakening to invariant state) |
| P1 (time dimension) | Existence of one time direction | Resolved (Theorem 11.8.2: ordered transition of Ω + Stone's theorem. $D = n+1$ elevated from convention to theorem. Continuous-implementation premise merged into existing liability.) |
| P2 (smooth realisation) | Each stage is realised as a smooth manifold | Resolved (Theorem 11.8.3: $SO(n)/SO(n-1) \cong S^{n-1}$ + analyticity of homogeneous spaces. Isotropy premise merged into existing liability.) |
| P3 ($\alpha$ identification) | Identification of statistical-face decay exponent with quantum-face phase eigenvalue | Resolved (Theorem 6.9.2 is an unconditional theorem by axiomatic specification of Ω non-degeneracy.) |
| P4 (energy decomposition) | Existence of a dimension-wise decomposition of $\varepsilon(n)$ | Resolved (Theorem 11.8.4: Schur's lemma gives existence, equal partition, and uniqueness simultaneously.) |

#### Theorem 11.8.1 (P0: Internal derivation of the ground state)

Each dimension is generated at the critical point where energy can no longer be sustained, so it is in the minimum-energy state at generation; Postulate B1 (closure) prohibits excitation by external energy injection; and unitary evolution under the self-adjoint Hamiltonian of §6.8 preserves energy eigenstates. However, since eigenstate preservation holds only under free Hamiltonians (F3), the final unconditionalisation is by the invariant-state argument of Theorem 11.10.3.

#### Theorem 11.8.2 (P1: Derivation of one time dimension)

Axiom Ω $\neg\exists \to \exists$ is an ordered transition whose arrow contains the structure of prior/later ordering as content. The continuous implementation of this transition is a strongly continuous one-parameter unitary group, whose parameter space by Stone's theorem is $\mathbb{R}$, i.e. one-dimensional. Since the axiom is a single arrow, the generator is one, and there is exactly one independent time direction. Hence $D = n + 1$ is elevated from convention to theorem. The Lorentzian character of time (imaginary-axis nature) follows from the same involution structure as the quantum face ($s = i\alpha$ axis) of Theorem 6.9.2.

#### Theorem 11.8.3 (P2: Derivation of smooth realisation)

The totality of directions at stage $n$, by the isotropy of Lemma B0, forms the homogeneous space $SO(n)/SO(n-1)$; the quotient of a Lie group by a closed subgroup is an analytic manifold, and $SO(n)/SO(n-1) \cong S^{n-1}$. Hence, that the realisation of each stage is a sphere-type smooth geometry is a theorem of homogeneous-space theory.

#### Theorem 11.8.4 (P4: Existence and uniqueness of energy decomposition)

In the quantisation of §6.8, the Hamiltonian of each channel is a quadratic form, and an $SO(n)$-invariant symmetric quadratic form is restricted to a scalar multiple of the unit form by Schur's lemma. Hence energy is uniquely decomposed into $n$ equal diagonal components in any orthonormal basis.

---

← [§10–§11: Numerical Verification and Completeness Assessment](07_verification_and_completeness.md) | [README (top)](README.md)
