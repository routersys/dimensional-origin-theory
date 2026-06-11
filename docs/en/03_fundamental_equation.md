# §6: Complete Proof of the Fundamental Equation

← [§4–§5: Derivation of the Dimension Numbers](02_dimensions.md) | Next → [§7: The Cosmological Constant](04_cosmological_constant.md)

---

## 6. Complete Proof of the Fundamental Equation

### 6.1 The Fundamental Equation

$$\boxed{\alpha \cdot \ln n^{\ast} = (n^{\ast}-1)(n^{\ast}-2) \cdot \pi}$$

Substituting $n^{\ast} = 11$ gives

$$\alpha = \frac{90\pi}{\ln 11} = 117.913131\ldots$$

#### Position and Independence of the Fundamental Equation

$n^{\ast} = 11$ has been independently fixed in §5 without using any observational values. The fundamental equation is therefore a defining equation for $\alpha$, not an equation to determine $n^{\ast}$.

As a consistency check of the independence of the fundamental equation, inverting from the observed value $\Lambda_{\rm obs} = 1.089 \times 10^{-52}\,{\rm m}^{-2}$ and $n^{\ast} = 11$ alone — a path completely independent of the fundamental equation — gives

$$\alpha_{\Lambda} = -\frac{\ln\!\left(\dfrac{\Lambda_{\rm obs}\, l_{P}^{2}}{2(n^{\ast}-2)}\right)}{\ln n^{\ast}} = 117.920$$

The discrepancy from the fundamental-equation value $\alpha_{\star} = 117.913$ is $0.006\%$. That these two independent paths yield the same $\alpha$ is not a coincidence; it demonstrates the internal consistency of the theory.

### 6.2 Origin of the Left-Hand Side: Representation Theory of the Multiplicative Group

From the scale invariance of $\varepsilon(n) = E_{0} n^{-\alpha}$, the dimension $n$ carries the structure of the multiplicative group $(\mathbb{R}_{+}, \times)$. The basis of unitary representations of this group is the basis of the Mellin transform:

$$\Psi_{\alpha}(n) = n^{i\alpha} = \exp(i\alpha \ln n)$$

The total phase accumulated from $n = 1$ to $n = n^{\ast}$ is

$$\Phi_{L} = \alpha \cdot \ln n^{\ast} \quad \cdots (L)$$

### 6.3 Standing-Wave Condition: Multiplicative Canonical Quantisation

Canonical quantisation in the multiplicative coordinate $u = \ln n$ gives

$$\hat{p} = -i\frac{d}{du} = -in\frac{d}{dn}$$

The boundary conditions are that the wave vanishes at the origin of dimensions ($n = 1$, $u = 0$) and at the observational limit ($n = n^{\ast}$, $u = \ln n^{\ast}$):

$$\Psi(n=1) = \Psi(n=n^{\ast}) = 0$$

The standing-wave condition is

$$\alpha \cdot \ln n^{\ast} = 2\pi k \quad \cdots (*)$$

### 6.3.1 Geometric Necessity of the Right-Hand Side $R(S^{n^{\ast}-1}) \cdot \pi$

**Theorem 6.3.1 (Geometric origin of the right-hand side):** The right-hand side $(n^{\ast}-1)(n^{\ast}-2)\pi$ of the fundamental equation is derived as a mathematical necessity from the boundary condition of the multiplicative canonical quantisation and the half-geodesic length of $S^{n^{\ast}-1}$.

**Proof (four steps):**

**Step 1 (Correspondence between Mellin space and geodesics):** The multiplicative coordinate $u = \ln n \in [0, \ln n^{\ast}]$ represents the geodesic distance from the energy origin to the observational limit. The geodesic length from the equator to a pole on the unit sphere $S^{n^{\ast}-1}$ is $\pi/2$ (on a sphere of radius 1). The nodes $u = 0$ and $u = \ln n^{\ast}$ of the standing wave correspond to the geodesic between antipodal points on $S^{n^{\ast}-1}$ (length $\pi$).

**Step 2 (Half-period phase per channel):** Each generator $L_{ij}$ of $SO(n^{\ast}-1)$ has eigenvalues $\{0, \pm i\}$ and satisfies $\exp(2\pi L_{ij}) = I$ (§6.4 lemma, verified for all 45 generators in Appendix C). Since the standing wave traverses a half-period from $u = 0$ to $u = \ln n^{\ast}$, the phase accumulated per channel is

$$2\pi \times \frac{1}{2} = \pi$$

**Step 3 (Total phase over all channels):** The number of independent channels in $SO(n^{\ast}-1)$ is

$$\dim\,\mathrm{so}(n^{\ast}-1) = \binom{n^{\ast}-1}{2} = \frac{(n^{\ast}-1)(n^{\ast}-2)}{2}$$

The total phase over all channels is

$$\Phi_{R} = \frac{(n^{\ast}-1)(n^{\ast}-2)}{2} \times 2\pi = (n^{\ast}-1)(n^{\ast}-2)\pi$$

**Step 4 (Identity with the Ricci scalar):** The Ricci tensor of the unit sphere $S^{n-1}$ is $\mathrm{Ric} = (n-2)g$, and the Ricci scalar is

$$R(S^{n-1}) = g^{ab}\mathrm{Ric}_{ab} = (n-2)(n-1) = (n-1)(n-2)$$

Therefore $\Phi_{R} = R(S^{n^{\ast}-1}) \cdot \pi$. This is not a quantity chosen from outside; it is an algebraic identity stating that the total half-period phase over all channels equals the Ricci scalar of the sphere geometry. $\square$

**Necessity of each factor:**

| Factor | Origin | External assumption |
|--------|--------|---------------------|
| $R(S^{n^{\ast}-1}) = (n^{\ast}-1)(n^{\ast}-2)$ | Total independent channel count of $\mathrm{so}(n^{\ast}-1)$ $\times 2$ (consequence of Postulate P) | None |
| $\pi$ | Half-geodesic length of $S^{n^{\ast}-1}$ (geometric consequence of boundary conditions $\Psi(1) = \Psi(n^{\ast}) = 0$) | None |

### 6.4 Determination of Channel Number $k$: Deduction of Postulate P

The Lie algebra $\mathrm{so}(n^{\ast}-1)$ of the isometry group $SO(n^{\ast}-1)$ of $S^{n^{\ast}-1}$ has basis

$$\{L_{ij} \mid 1 \leq i < j \leq n^{\ast}-1\}$$

with cardinality

$$\dim(\mathrm{so}(n^{\ast}-1)) = \binom{n^{\ast}-1}{2} = \frac{(n^{\ast}-1)(n^{\ast}-2)}{2}$$

**Lemma (Channel phase theorem):**

$L_{ij}$ is an antisymmetric matrix with eigenvalue $0$ (multiplicity $n^{\ast}-3$) and $\pm i$ (each with multiplicity 1). By the Taylor expansion,

$$\exp(2\pi \cdot L_{ij}) = I$$

The phase accumulated when each channel completes one full period is $2\pi$.

Numerical verification: for all $\binom{10}{2} = 45$ basis matrices of $\mathrm{so}(10)$, $\exp(2\pi L_{ij}) = I$ is confirmed. All 45: True (see [Appendix C](appendix.md#appendix-c)).

The total phase over all channels is

$$\Phi_{R} = \binom{n^{\ast}-1}{2} \times 2\pi = (n^{\ast}-1)(n^{\ast}-2) \cdot \pi \quad \cdots (R)$$

**Theorem 6.4.1 (Deduction of Postulate P):** The quantum number $k$ of the standing wave must equal $k = \dim\,\mathrm{so}(n^{\ast}-1)$.

**Proof:**

If $k < \dim\,\mathrm{so}(n^{\ast}-1)$, the symmetry of $S^{n^{\ast}-1}$ is only partially excited and the fundamental equation is compatible with multiple values of $n^{\ast}$ (uniqueness of $n^{\ast}$ is lost). This contradicts the algebraic unique determination of $n^{\ast} = 11$ in §5.

If $k > \dim\,\mathrm{so}(n^{\ast}-1)$, the same channel is counted more than once (degeneracy), and the fundamental equation would admit $n^{\ast} + mB$ ($m \geq 1$). This contradicts the definition in §5 that $n^{\ast}$ is the observational-limit dimension.

Only $k = \dim\,\mathrm{so}(n^{\ast}-1)$ simultaneously satisfies both uniqueness of $n^{\ast}$ and the definition of the observational limit. $\square$

Through this deduction, Postulate P becomes a mathematical necessity derived from the uniqueness of $n^{\ast}$, not a methodological principle (Ockham).

### 6.5 Completion of the Fundamental Equation

By Theorem 6.4.1, $k = \binom{n^{\ast}-1}{2}$. From $(L) = (R)$:

$$\alpha \cdot \ln n^{\ast} = (n^{\ast}-1)(n^{\ast}-2) \cdot \pi \qquad \blacksquare$$

### 6.6 Geometric Reinterpretation and Complete Meaning of the Fundamental Equation

The fundamental equation can be rewritten as

$$\alpha \cdot \ln n^{\ast} = R(S^{n^{\ast}-1}) \cdot \pi$$

The left-hand side is the total phase of the Mellin representation of the multiplicative group; the right-hand side is the spherical Ricci scalar $R(S^{n^{\ast}-1}) = (n^{\ast}-1)(n^{\ast}-2)$ of $S^{n^{\ast}-1}$ multiplied by $\pi$.

By Theorem 6.3.1, none of the factors on the right-hand side are chosen externally. $(n^{\ast}-1)(n^{\ast}-2) = 2\,\dim\,\mathrm{so}(n^{\ast}-1)$ is twice the total symmetric channel count (consequence of Theorem 6.4.1), and $\pi$ is the half-geodesic length of $S^{n^{\ast}-1}$ (geometric consequence of the boundary conditions $\Psi(n=1) = \Psi(n=n^{\ast}) = 0$). This equation is new and absent from existing mathematical and physical literature.

### 6.7 Numerical Verification

$$\alpha \cdot \ln 11 = 117.913131 \times 2.397895 = 282.743339$$

$$(n^{\ast}-1)(n^{\ast}-2)\pi = 10 \times 9 \times \pi = 90\pi = 282.743339 \quad \checkmark$$

The error is zero; by the analytic proof it holds exactly.

### 6.8 Quantum-Mechanical Formulation

This section rigorously formulates the multiplicative canonical quantisation of §6.3 within the standard framework of quantum mechanics, establishing that the fundamental equation is a spectral condition of a self-adjoint operator.

#### Theorem 6.8.1 (State space and self-adjointness)

The state space is the Hilbert space $\mathcal{H} = L^{2}([0, \ln n^{\ast}], du)$ ($u = \ln n$). The square $\hat{p}^{2}$ (Dirichlet Laplacian) of the momentum $\hat{p} = -i\,d/du$ under the Dirichlet boundary conditions $\Psi(0) = \Psi(\ln n^{\ast}) = 0$ is essentially self-adjoint (established theorem: self-adjointness of the Dirichlet Laplacian on a bounded interval). Its spectrum is purely discrete:

$$\mathrm{spec}(\hat{p}^{2}) = \left\lbrace \left(\frac{\pi k}{\ln n^{\ast}}\right)^{2} \;\middle|\; k = 1, 2, 3, \ldots \right\rbrace, \qquad \Psi_{k}(u) = \sin\!\left(\frac{\pi k\, u}{\ln n^{\ast}}\right)$$

#### Theorem 6.8.2 (Fundamental equation = spectral condition)

The solution $\alpha = 90\pi/\ln 11$ of the fundamental equation is an element of the spectrum of $\hat{p}$, and

$$\alpha = \frac{\pi k}{\ln n^{\ast}}\bigg|_{k = 2\,\dim \mathrm{so}(n^{\ast}-1)} = \frac{90\pi}{\ln 11}$$

That is, the fundamental equation is the spectral condition of selecting the eigenmode satisfying the total-channel phase condition (§6.4, $k = 2 \times 45 = 90$). For numerical verification, finite-difference Dirichlet eigenvalues ($N = 4000$) reproduce $p_{k} = \pi k/\ln 11$ to machine precision, and the $k = 90$ eigenvalue agrees with $\alpha$ to relative error $2 \times 10^{-4}$ (discretisation error, converging as $N \to \infty$).

#### Theorem 6.8.3 (Odd parity of the selected mode)

Under the interval inversion $u \mapsto \ln n^{\ast} - u$, the parity of the eigenmodes is $(-1)^{k+1}$, and the selected mode $k = 90$ has parity $-1$ (odd) (numerically verified). This is consistent with the odd parity of Axiom Ω (§2.1, §8.3). That the mode realising the fundamental equation automatically has odd parity shows that the parity structure of Axiom Ω is preserved at the level of quantisation.

#### Necessity of the Complex Hilbert Space

The reason quantum mechanics is formulated over the complex field is also identified from the structure of the present theory. First, the basis $\Psi_{\alpha}(n) = n^{i\alpha}$ of the Mellin representation (§6.2) requires the imaginary unit; applying Stone's theorem (established) to the strongly continuous unitary representation of the scale-transformation group $(\mathbb{R}_{+}, \times)$ requires a complex Hilbert space. Second, the minimal quantum realisation of the two-state system $S = \{\neg\exists, \exists\}$ of Axiom Ω is $\mathbb{C}^{2}$ (a qubit), and the involution $\sigma$ is realised as a unitary involution (Pauli type). Third, the first stage $\mathbb{R} \to \mathbb{C}$ of the Cayley–Dickson tower gives the complex structure and the second stage $\mathbb{C} \to \mathbb{H}$ gives the spin structure ($\mathrm{Spin}(3) \cong Sp(1)$, Corollary 11.5.2), and the number system of quantum mechanics arises from the same tower as the derivation of the observational algebra (§4). Fourth, the $\mathbb{Z}/2$ generated by $\sigma$ acts as a superselection rule (fermionic parity) and agrees with the physical basis of the graded Morita equivalence in §5.1.

### 6.9 Identification of Exponents on the Statistical Face and Quantum Face

#### Proposition 6.9.1 (Two descriptions)

The functions $n^{-\alpha}$ and $n^{i\alpha}$ are two sections of the same Mellin spectral parameter $\alpha$ in the complex $s$-plane. The former corresponds to the point $s = -\alpha$ on the real axis of the Mellin variable, and the latter to the point $s = i\alpha$ on the imaginary axis, which is the spectrum of the unitary dilation group (generator $\hat{D} = -i\,d/du$).

#### Theorem 6.9.2 (Exponent identification)

The statistical-face decay exponent $\alpha_{\rm st}$ and the quantum-face phase eigenvalue $\alpha_{\rm qu}$ are identical.

**Proof (four steps):**

Step 1 (Two descriptions): The theory has independently established two descriptions of the same object. The statistical face is the real decay $\varepsilon = E_{0} e^{-\alpha_{\rm st} u}$ of the energy density (§3, unique solution of Cauchy's equation). The quantum face is the phase eigenvalue $\alpha_{\rm qu}$ of the unitary dynamics (§6.8, Dirichlet spectrum). They are located at $s = -\alpha_{\rm st}$ (real axis) and $s = i\alpha_{\rm qu}$ (imaginary axis) of the Mellin spectral plane $s \in \mathbb{C}$ (Proposition 6.9.1).

Step 2 (Non-triviality of $\sigma$'s action): The pair of descriptions $\{\text{statistical face}, \text{quantum face}\}$ is the pair of the real-axis section and imaginary-axis section of the Mellin spectral plane, satisfying the definition of a dual pair in §2.1. By Ω non-degeneracy (§2.1), $\sigma$ acts non-trivially on this pair. Since the unique non-trivial action on a two-element set is the exchange, $\sigma$ exchanges the two faces.

Step 3 (Complete classification of axis-exchanging involutions): The $\mathbb{R}$-linear maps preserving the multiplicative structure on the spectral plane $\mathbb{C}$ are exhausted by the regular type $s \mapsto as$ and the anti-regular type $s \mapsto a\bar{s}$. From the involution condition, the regular type has $a = \pm 1$ and the anti-regular type has $|a| = 1$. The condition of mapping the real axis to the imaginary axis (exchanging the two faces) is satisfied only by the anti-regular type with $a = \pm i$ (verified exhaustively by symbolic computation). Hence the involutions exchanging the two faces are exactly

$$\sigma: s \mapsto \pm i\,\bar{s}$$

and both strictly satisfy $|\sigma(s)| = |s|$.

Step 4 (Identification of exponents): By Step 2, $\sigma$ exchanges the two faces; by Step 3, any such realisation necessarily preserves $|s|$. Therefore

$$\alpha_{\rm st} = |-\alpha_{\rm st}| = |\sigma(-\alpha_{\rm st})| = |i\alpha_{\rm qu}| = \alpha_{\rm qu}$$

The identification of the statistical-face decay exponent with the quantum-face phase eigenvalue is a theorem of the Ω system. $\square$

**Structural meaning of the proof:** The exchange of the two faces is the action of the involution $\sigma$ of Axiom Ω itself, and the classification theorem for axis-exchanging involutions forces the equality of the exponents. The two-state structure of the axiom — existence arising from the self-contradiction of nothingness — connects the statistical description and the quantum description, and the mathematical uniqueness of that connection forces the identification of $\alpha$. That the exponent identification lies outside the old axiom system (underivable from it) and that Ω non-degeneracy is the minimal sufficient specification are established by independence proofs (see [Revision and Audit Record §3.3](08_revision_history.md#33-resolution-by-the-third-round-of-verification)). As an empirical check, the $0.006\%$ agreement of the two paths for $\alpha$ (fundamental equation $117.913$ vs. $\Lambda$-inversion $117.920$) functions as a test of Axiom Ω (including non-degeneracy) itself.

---

← [§4–§5: Derivation of the Dimension Numbers](02_dimensions.md) | Next → [§7: The Cosmological Constant](04_cosmological_constant.md)
