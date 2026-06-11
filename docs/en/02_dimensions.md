# §4–§5: Derivation of $n_{\rm obs} = 3$ and $n^{\ast} = 11$

← [§1–§3: Axiom Ω and Setup](01_axiom_and_setup.md) | Next → [§6: The Fundamental Equation](03_fundamental_equation.md)

---

## 4. Derivation of the Observed Spatial Dimension $n_{\rm obs} = 3$

### 4.1 Deduction of Postulates O1 and O2 from Axiom Ω

Postulates O1 and O2 are deduced from Axiom Ω without any external assumptions; they are consequences of Axiom Ω, not separately imposed postulates.

#### Theorem 4.1.0 (Deduction of Postulate O1)

Theorem: Postulate O1 (reversibility and associativity of the composition of physical measurements) is deduced from Axiom Ω.

**Proof:**

Step 1: Axiom Ω defines the state space $S = \{\neg\exists, \exists\}$ and the transformation $\sigma: \neg\exists \mapsto \exists$, $\exists \mapsto \neg\exists$. Since $\sigma^{2} = \mathrm{id}$ and $\sigma \neq \mathrm{id}$, we have $\sigma \in \mathrm{Aut}(S)$.

Step 2: A physical measurement is a homomorphism $\varphi: S \to S$, and the collection of all such maps is $\mathrm{End}(S)$. Since $\sigma$ is bijective, $\sigma \in \mathrm{Aut}(S) \subset \mathrm{End}(S)$.

Step 3: $\mathrm{Aut}(S)$ is a group. The associativity $(\sigma \circ \tau) \circ \rho = \sigma \circ (\tau \circ \rho)$ is the associativity of composition of maps, which is a theorem of set theory and contains no external assumption.

Step 4: The conditions for a measurement to be physically meaningful are: (i) composition of measurements is closed on $S$ (consequence of Postulate B1); (ii) an inverse measurement exists (consequence of $\sigma \in \mathrm{Aut}(S)$); (iii) associativity of composition (consequence of Step 3). All of these follow from Axiom Ω. $\square$

It follows that the algebra of measurements must be an associative division algebra; the non-associative octonions are excluded by Axiom Ω.

#### Theorem 4.1.1 (Deduction of Postulate O2)

Theorem: Realising the symmetry imposed by Axiom Ω requires the rotation group $SO(n_{\rm obs})$ of the observation space to be non-abelian, and the minimal dimension for which this holds is $n_{\rm obs} = 3$.

**Proof:**

**Lemma 4.1.1 (Parity structure of Axiom Ω):** $\sigma$ is an involution ($\sigma^{2} = \mathrm{id}$, $\sigma \neq \mathrm{id}$) and implies $\neg\exists \neq \exists$ (non-equivalence of states). This is realised spatially as parity inversion $P: \mathbf{x} \mapsto -\mathbf{x}$.

**Lemma 4.1.2 (Parity collapse in two dimensions):** In two-dimensional space $P: (x,y) \mapsto (-x,-y)$ coincides with the rotation $R(\pi) \in SO(2)$.

$$P = R(\pi) \in SO(2) \quad (2\text{-dimensional})$$

In two dimensions, spatial inversion is thus identified with an element of the rotation symmetry, and the parity of Axiom Ω ($\neg\exists \neq \exists$) cannot be realised spatially.

**Lemma 4.1.3 ($SO(n)$ non-abelian $\Leftrightarrow n \geq 3$):**

$(\Leftarrow)$: for $n \geq 3$, $SO(3) \subset SO(n)$ contains non-commuting elements (e.g. $R_{x}(\pi/2)R_{y}(\pi/2) \neq R_{y}(\pi/2)R_{x}(\pi/2)$, numerically verified in Appendix C).

$(\Rightarrow)$: $SO(1) = \{e\}$ is trivially abelian. $SO(2) \cong U(1)$ is abelian since $e^{i\theta} e^{i\phi} = e^{i(\theta+\phi)} = e^{i(\phi+\theta)}$.

From Lemma 4.1.2, parity is absorbed into $SO(2)$ and vanishes for $n = 2$; from Lemma 4.1.3, the minimal dimension for non-abelianness is $n = 3$. Therefore

$$\boxed{n_{\rm obs} = 3 \text{ is the minimal dimension at which the parity structure of Axiom Ω is genuinely non-trivially realised.}} \quad \square$$

The classical Postulate O2 (observability via $SO(3)$ or higher rotations) follows automatically as a corollary of this theorem.

### 4.2 Fixing $n_{\rm obs} = 3$ via Hurwitz's Theorem

By Theorem 4.1.0, the algebra of observations must be an associative division algebra.

Hurwitz's theorem (1898): over the reals, there exist exactly four division algebras:

| Algebra | Total dimension | Commutative | Associative | Imaginary dimension | Rotation group |
|---------|-----------------|-------------|-------------|---------------------|----------------|
| $\mathbb{R}$ | 1 | ✓ | ✓ | 0 | $SO(1)$ (trivial) |
| $\mathbb{C}$ | 2 | ✓ | ✓ | 1 | $SO(2)$ (1-axis) |
| $\mathbb{H}$ (quaternions) | 4 | ✗ | ✓ | 3 | $SO(3)$ (3-axis) |
| $\mathbb{O}$ (octonions) | 8 | ✗ | ✗ | 7 | — |

Applying the postulates to each algebra:

$\mathbb{O}$ (octonions) is non-associative. For basis elements $e_{1}, e_{2}, e_{4}$ we have $(e_{1}e_{2})e_{4} = e_{3}e_{4} = e_{7}$ but $e_{1}(e_{2}e_{4}) = e_{1}e_{6} = -e_{7}$, so $(e_{1}e_{2})e_{4} \neq e_{1}(e_{2}e_{4})$. Excluded by Postulate O1.

$\mathbb{R}$ (imaginary dimension 0) has $SO(0)$ as the trivial group, with no independent rotation. Fails Postulate O2.

$\mathbb{C}$ (imaginary dimension 1) has $SO(2)$ with only a single rotation axis (a one-parameter group), with no independent depth direction. Fails Postulate O2.

$\mathbb{H}$ (imaginary dimension 3) is associative, satisfying Postulate O1. $SO(3)$ acts naturally on the pure-imaginary quaternion space $\mathrm{Im}\,\mathbb{H} \cong \mathbb{R}^{3}$, giving independent three-dimensional rotations. Satisfies Postulates O1 and O2 simultaneously.

The unique division algebra satisfying Postulates O1 and Theorem 4.1.1 simultaneously is the quaternions $\mathbb{H}$, and the dimension of its imaginary part gives the dimension of the observation space:

$$\boxed{n_{\rm obs} = \dim_{\mathbb{R}}(\mathrm{Im}\,\mathbb{H}) = 3}$$

---

## 5. Derivation of the Observational-Limit Dimension $n^{\ast} = 11$

### 5.1 Minimality Theorem for the Observational Limit

#### Definition (observational-limit dimension)

$\mathrm{Cl}(n)$ is a $\mathbb{Z}/2$-graded algebra (even part $\mathrm{Cl}^{0}$, odd part $\mathrm{Cl}^{1}$) with grading automorphism $\alpha: e_{i} \mapsto -e_{i}$. The observational-limit dimension $n^{\ast}$ is defined as the minimal $n > n_{\rm obs}$ for which $\mathrm{Cl}(n)$ is graded Morita equivalent (Morita equivalent as a superalgebra) to $\mathrm{Cl}(n_{\rm obs})$:

$$n^{\ast} := \min\left\lbrace n > n_{\rm obs} \;\mid\; \mathrm{Cl}(n) \sim_{\rm gr} \mathrm{Cl}(n_{\rm obs})\right\rbrace$$

#### Necessity of the grading from Axiom Ω

The grading automorphism $\alpha: e_{i} \mapsto -e_{i}$ is the action induced on the Clifford algebra by spatial parity $P: \mathbf{x} \mapsto -\mathbf{x}$, and by Lemma 4.1.1 this $P$ is the spatial realisation of the involution $\sigma$ ($\neg\exists \leftrightarrow \exists$) of Axiom Ω. Therefore, equivalence of observations must preserve Ω-parity, and the only admissible equivalence relation is the graded one. This is not an external choice but a consequence of Axiom Ω. Physically, the grading corresponds to the superselection rule for fermionic parity.

Using ungraded equivalence would produce a counter-example: $\mathrm{Cl}(3,0) \cong M_{2}(\mathbb{C})$ and $\mathrm{Cl}(7,0) \cong M_{8}(\mathbb{C}) \cong M_{2}(\mathbb{C}) \otimes M_{4}(\mathbb{R})$ (real dimension $128 = 8 \times 16$, centre $\mathbb{C}$, constructively verified), so under ungraded equivalence the minimum would be $7$ rather than $11$. The graded equivalence excludes this counter-example.

#### Theorem 5.2.1 (Fixing $n^{\ast} = 11$)

External theorem (Wall 1964, graded Brauer group): the graded Brauer group over the reals is $\mathrm{sBr}(\mathbb{R}) \cong \mathbb{Z}/8$, and $\mathrm{Cl}(p) \sim_{\rm gr} \mathrm{Cl}(q)$ if and only if $p \equiv q \pmod{8}$. This is an established mathematical theorem holding the same epistemological status as Hurwitz's theorem in the present theory.

Therefore

$$n^{\ast} = \min\{n > 3 \mid n \equiv 3 \pmod{8}\} = 11 \qquad \blacksquare$$

The counter-example $n = 7$ is excluded. Indeed, the graded invariant — the type of the even part — is $\mathrm{Cl}^{0}(3,0) \cong \mathbb{H}$ (a division algebra, type $\mathbb{H}$; the quaternion relations of the bi-vectors $e_{12}, e_{13}, e_{23}$ are constructively verified), whereas $\mathrm{Cl}^{0}(7,0) \cong M_{8}(\mathbb{R})$ (contains a non-trivial idempotent $(1+e_{1234})/2$, hence not a division algebra, type $\mathbb{R}$); this difference in type directly demonstrates non-equivalence. By contrast, $\mathrm{Cl}^{0}(11,0) \cong M_{16}(\mathbb{H})$ has the matching type $\mathbb{H}$.

$$\boxed{n^{\ast} = n_{\rm obs} + 8 = 11}$$

Postulate M (minimality principle): the observational limit adopts the minimum value in the above definition. Dimensions in the family $n \equiv 3 \pmod{8}$ beyond $n = 11$ (i.e. $19, 27, \ldots$) belong to the same graded Morita class and provide no new independent realisation.

### 5.2 Connection to Frobenius's Theorem

By Frobenius's theorem, the maximum dimension of a division algebra is 8 (the octonions $\mathbb{O}$). This is the limit of energy-balance closure and is the origin of Bott periodicity 8.

### 5.3 Consistency of the Bott Period $B = 2^{n_{\rm obs}}$

The standard Bott periodicity theorem is an external theorem stating that the algebraic type of Clifford algebras repeats with period 8 in dimension $n$:

$$\mathrm{Cl}(n+8) \cong \mathrm{Cl}(n) \otimes M(16, \mathbb{R})$$

The derivation of $n^{\ast} = 11$ is carried by Theorem 5.2.1 (Wall's graded Brauer group theorem $\mathrm{sBr}(\mathbb{R}) \cong \mathbb{Z}/8$ plus the necessity of the grading from Axiom Ω). Independently, the consistency that the total order of the Cayley–Dickson involution group equals the period $8$ holds only for $n_{\rm obs} = 3$. This is shown below.

**Theorem (Consistency of the Cayley–Dickson involution group):** The total order of the involution groups at the stages of the Cayley–Dickson construction equals $2^{n_{\rm obs}}$ if and only if $n_{\rm obs} = 3$.

**Proof (five lemmas):**

**Lemma 1 (Algebraic realisation of Axiom Ω):**
Axiom Ω $\neg\exists \to \exists$ defines two states, "nothingness" $(\neg\exists)$ and "existence" $(\exists)$. These are exclusive and exhaustive in propositional logic, so the state space is isomorphic to the two-element set $S = \{0,1\}$.

The automorphism group of $S$ is $\mathrm{Aut}(S) = \mathbb{Z}/2\mathbb{Z}$ (the only bijections on a two-element set are the identity and the transposition). The transformation of Axiom Ω is uniquely realised as the non-trivial element of $\mathbb{Z}/2\mathbb{Z}$. The double-negation law $\neg(\neg\exists) = \exists$ gives $\phi^{2} = \mathrm{id}$, so this map is an involution $\sigma: A \to A$, $\sigma^{2} = \mathrm{id}$, $\sigma \neq \mathrm{id}$. This involution is the origin of the doubling map in the Cayley–Dickson construction.

**Lemma 2 (Necessity of the Cayley–Dickson construction):**
From an algebra $A$ with involution $\sigma$, form the double $A' = A \oplus A \cdot e$ with the multiplication

$$(a,b)(c,d) = (ac - db^{\ast}, da + bc^{\ast})$$

where $b^{\ast} = \sigma(b)$. This doubling preserves the multiplicative norm property $|ab|^{2} = |a|^{2}|b|^{2}$ as long as consistency of physical measurements (Postulate O1: all measurements are reversible) is maintained.

External theorem (Hurwitz): over the reals, the only division algebras with multiplicative norm are $\mathbb{R}, \mathbb{C}, \mathbb{H}, \mathbb{O}$ (dimensions $1, 2, 4, 8$). At the fourth stage, the sedenions $\mathbb{S}$, the multiplicative norm breaks, and the algebraic requirement of Postulate O1 is lost. The Cayley–Dickson construction therefore stops at $k = 3$ (the octonions $\mathbb{O}$).

**Lemma 3 (Growth law of the involution group at each stage):**
Define inductively the new involution $\sigma_{k}$ added at Cayley–Dickson stage $k$:

$$\sigma_{k}(a + b \cdot e_{k}) = \sigma_{k-1}(a) - b \cdot e_{k} \quad (a,b \in A_{k-1})$$

Let $G_{k} = \langle \sigma_{0}, \sigma_{1}, \ldots, \sigma_{k-1} \rangle$.

$G_{k} \cong (\mathbb{Z}/2\mathbb{Z})^{k}$ is proved by three points:

(i) $\sigma_{j}^{2} = \mathrm{id}$ (induction): $k = 0$ is trivial. Assuming $\sigma_{k-1}^{2} = \mathrm{id}$,

$$\sigma_{k}^{2}(a + b \cdot e_{k}) = \sigma_{k}(\sigma_{k-1}(a) - b \cdot e_{k}) = \sigma_{k-1}^{2}(a) + b \cdot e_{k} = a + b \cdot e_{k}$$

so $\sigma_{k}^{2} = \mathrm{id}$.

(ii) $\sigma_{i}\sigma_{j} = \sigma_{j}\sigma_{i}$ ($i < j$): for any $x = a + b \cdot e_{j} \in A_{j}$, since $\sigma_{i}$ (an involution at stage $i \leq j-1$) acts independently of the $e_{j}$ coefficient,

$$\sigma_{i}(\sigma_{j}(x)) = \sigma_{i}(\sigma_{j-1}(a) - b \cdot e_{j}) = \sigma_{i}\sigma_{j-1}(a) - \sigma_{i}(b) \cdot e_{j}$$

$$\sigma_{j}(\sigma_{i}(x)) = \sigma_{j}(\sigma_{i}(a) + \sigma_{i}(b) \cdot e_{j}) = \sigma_{j-1}\sigma_{i}(a) - \sigma_{i}(b) \cdot e_{j}$$

The equality reduces to commutativity of $\sigma_{i}$ with $\sigma_{j-1}$ inside $A_{j-1}$, established by induction.

(iii) Independence: $\sigma_{j}$ flips the sign of $e_{j}$ and acts trivially on $e_{i}$ ($i < j$). Since $e_{j}$ is a new basis element introduced at stage $j$, $\sigma_{j}$ cannot be expressed as a product of $\sigma_{0}, \ldots, \sigma_{j-1}$.

By (i)(ii)(iii), $G_{k} \cong (\mathbb{Z}/2\mathbb{Z})^{k}$, so $|G_{k}| = 2^{k}$. $\square$

| Stage $k$ | Algebra | $G_{k}$ | $\vert G_{k}\vert$ |
|-----------|---------|---------|---------------------|
| 0 | $\mathbb{R}$ | $\{\mathrm{id}\}$ | $1 = 2^{0}$ |
| 1 | $\mathbb{C}$ | $\mathbb{Z}/2\mathbb{Z}$ | $2 = 2^{1}$ |
| 2 | $\mathbb{H}$ | $(\mathbb{Z}/2\mathbb{Z})^{2}$ | $4 = 2^{2}$ |
| 3 | $\mathbb{O}$ | $(\mathbb{Z}/2\mathbb{Z})^{3}$ | $8 = 2^{3}$ |

**Lemma 4 (Total involution-group size at $n_{\rm obs}$ stages):**
The associative division algebras are $\mathbb{R}, \mathbb{C}, \mathbb{H}$ ($n_{\rm obs}$ in total, by Hurwitz), so the cumulative involution-group size is

$$B = \prod_{k=0}^{n_{\rm obs}-1} |G_{k}| = \prod_{k=0}^{n_{\rm obs}-1} 2^{k} = 2^{\sum_{k=0}^{n_{\rm obs}-1} k} = 2^{n_{\rm obs}(n_{\rm obs}-1)/2}$$

**Lemma 5 (Uniqueness of $n_{\rm obs} = 3$):**
The necessary and sufficient condition for $B = 2^{n_{\rm obs}(n_{\rm obs}-1)/2} = 2^{n_{\rm obs}}$ is

$$\frac{n_{\rm obs}(n_{\rm obs}-1)}{2} = n_{\rm obs} \iff n_{\rm obs}(n_{\rm obs}-3) = 0 \iff n_{\rm obs} \in \{0,3\}$$

$n_{\rm obs} = 0$ contradicts the axiomatic premise $n \geq 1$ and is excluded. Hence $n_{\rm obs} = 3$ is the unique solution.

**Conclusion:**

$$\boxed{B = 2^{n_{\rm obs}} = 8 \quad \text{(holds only for } n_{\rm obs} = 3\text{)}} \qquad \blacksquare$$

The identity

$$\prod_{k=0}^{n_{\rm obs}-1} 2^{k} = 2^{n_{\rm obs}(n_{\rm obs}-1)/2} = 2^{n_{\rm obs}}$$

is a rigorous algebraic fact, providing the consistency that the total order of the Cayley–Dickson involution group equals the period $8$ only when $n_{\rm obs} = 3$.

### 5.4 Final Determination of $n^{\ast}$

$$\boxed{n^{\ast} = n_{\rm obs} + 8 = 3 + 8 = 11}$$

The complete derivation chain is:

```
Axiom Ω (¬∃ → ∃)
 │
 ├─ Existence of Z/2Z involution σ (Aut(S) = Z/2Z, Lemma 1)
 │
 ├─ Spatial realisation of σ = parity P (Lemma 4.1.1)
 │   └─ Induced action on Clifford algebra α: e_i → -e_i = Z/2 grading
 │
 ├─ Hurwitz theorem: n_obs = 3  (associative division algebras are R, C, H)
 │
 ├─ Equivalence of observations preserves Ω-parity (grading) ⟹ graded Morita equivalence
 │
 ├─ Wall theorem: sBr(R) ≅ Z/8 ⟹ Cl(p) ~gr Cl(q) ⟺ p ≡ q (mod 8)
 │
 └─ n* = min{n > 3 | n ≡ 3 (mod 8)} = 11
     (consistency note: ∏ 2^k = 2^{n(n-1)/2} = 2^n = 8 holds only for n_obs = 3, §5.3)
```

The external theorems used are Hurwitz's theorem, Cauchy's functional equation, and Wall's theorem — all established mathematical results.

---

← [§1–§3: Axiom Ω and Setup](01_axiom_and_setup.md) | Next → [§6: The Fundamental Equation](03_fundamental_equation.md)
