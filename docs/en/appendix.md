# Appendices A–D

← [§10–§11: Numerical Verification and Completeness Assessment](07_verification_and_completeness.md) | [README (top)](README.md)

---

## Appendix A: Equation System

$$\text{Axiom Ω}: \quad \neg\exists \;\rightarrow\; \exists$$

$$\text{E-0 (energy density)}: \quad \varepsilon(n) = E_{0} \cdot n^{-\alpha}$$

$$\text{Fundamental equation}: \quad \alpha \cdot \ln n^{\ast} = (n^{\ast}-1)(n^{\ast}-2)\pi \quad \Rightarrow \quad \alpha = \frac{90\pi}{\ln 11}$$

$$\text{E-}\Lambda\text{ (cosmological constant)}: \quad \Lambda = 2(n^{\ast}-2) \cdot \frac{(n^{\ast})^{-\alpha}}{l_{P}^{2}}$$

$$\text{E-}H\text{ (Hubble constant)}: \quad H_{0} = \sqrt{\frac{8\pi G\,\rho_{\Lambda}}{3\,\Omega_{\Lambda}}}, \quad \rho_{\Lambda} = \frac{\Lambda c^{2}}{8\pi G}$$

$$\text{E-CMB (first peak)}: \quad \ell_{1} = D_{3}(S^{9}) + D_{1}(S^{9}) = \binom{12}{3} = 220$$

$$\text{E-CMB (full peaks)}: \quad \ell_{k} = \binom{n^{\ast}+1}{n_{\rm obs}} + (k-1) \cdot \frac{D_{n_{\rm obs}+1}(S^{n^{\ast}-2}) - D_{n_{\rm obs}-1}(S^{n^{\ast}-2})}{2} = 220 + (k-1) \times 303$$

$$\text{E-}R\text{ (baryon-to-photon ratio)}: \quad R_{\rm dec} = \frac{3(n^{\ast} - n_{\rm obs})}{4(n^{\ast} - 1)} = \frac{3}{5}$$

$$\text{E-}z\text{ (decoupling redshift)}: \quad z_{\rm dec} = \frac{n^{\ast}-1}{2} \cdot \binom{n^{\ast}+1}{n_{\rm obs}} - n^{\ast} = 1089$$

$$\text{E-}r\text{ (tensor-to-scalar ratio)}: \quad r = \frac{1}{D_{2}(S^{9})} = \frac{1}{54} \approx 0.0185$$

$$\text{E-}w\text{ (dark energy)}: \quad w = -1 \quad (\text{proved consequence of } \rho_{\Lambda} = \mathrm{const})$$

$$\text{E-}N_{\rm eff}\text{ (effective neutrino number)}: \quad N_{\rm eff} = 3\left(1 + \frac{1}{D_{2}}\right) = 3.056$$

$$\text{E-}n_{t}\text{ (gravitational-wave index)}: \quad n_{t} = -\frac{1}{8 D_{2}} = -\frac{1}{432} \approx -0.00231$$

$$\text{E-}n_{s}\text{ (scalar spectral index)}: \quad n_{s} = 1 - \frac{4}{\alpha} = 1 - \frac{4\ln 11}{90\pi} = 0.96608$$

$$\text{E-}T\text{ (CMB temperature)}: \quad T_{\rm CMB} = T_{P} \cdot \left[(n^{\ast})^{-\alpha} \cdot \frac{2}{n_{\rm obs}\,\pi} \cdot \frac{30}{\pi^{2}(n^{\ast}-1)^{2}} \cdot \left(\frac{4n^{\ast}-1}{n^{\ast}(n^{\ast}-1)^{2}}\right)^{4/3}\right]^{1/4} \approx 2.7285\,{\rm K}$$

---

## Appendix B: Derivation Formula for Spherical-Harmonic Degeneracy on $S^{9}$

The degeneracy of degree-$\ell$ spherical harmonics on $S^{9} \subset \mathbb{R}^{10}$ (embedding-space dimension $n = 10$) is

$$D_{\ell}(S^{9}) = \binom{9+\ell}{\ell} - \binom{7+\ell}{\ell-2}, \quad \ell \geq 2$$

$$D_{0} = 1, \quad D_{1} = 10$$

---

## Appendix C: Numerical Confirmation of the Channel Phase Theorem for $\mathrm{so}(10)$

For all $\binom{10}{2} = 45$ generators $L_{ij}$ ($1 \leq i < j \leq 10$) of $\mathrm{so}(10)$,

$$\exp(2\pi \cdot L_{ij}) = I_{10\times 10}$$

was confirmed by numerical computation in Python/numpy (Taylor expansion of the matrix exponential, convergence criterion $\|e^{2\pi L} - I\| < 10^{-12}$): all 45 generators gave True.

---

## Appendix D: Detailed Algebraic Proof of the Full Peak Formula

Theorem: for $n_{\rm obs} = 3$ and $n^{\ast} = 11$,

$$\ell_{k} = 220 + (k-1) \times 303 \quad (k = 1, 2, 3, \ldots)$$

**Proof:**

Step 1: $\ell_{1} = 220$ is proved algebraically in [§8.4](05_cmb_peaks.md#84-algebraic-proof-of-the-first-cmb-peak).

Step 2: Computation of the acoustic scale $\Delta\ell = 303$.

$$D_{4}(S^{9}) = \binom{13}{4} - \binom{11}{2} = 715 - 55 = 660$$

$$D_{2}(S^{9}) = \binom{11}{2} - \binom{9}{0} = 55 - 1 = 54$$

$$\Delta\ell = \frac{D_{n_{\rm obs}+1} - D_{n_{\rm obs}-1}}{2} = \frac{660 - 54}{2} = 303$$

Step 3: Identification of $\Delta\ell$ as the acoustic scale.

The even-parity modes on $S^{9}$ describe the static background; their change in mode density $D_{4} - D_{2} = 606$ represents the increment in spatial capacity for the next acoustic oscillation. Since an acoustic standing wave is the superposition of two travelling-wave directions, the effective $\ell$-space interval is $606/2 = 303$.

Step 4: Validity of the full peak formula.

Starting from the first peak $\ell_{1} = 220$ with spacing $\Delta\ell = 303$, the sequence is arithmetic:

$$\ell_{k} = \ell_{1} + (k-1)\Delta\ell = 220 + (k-1) \times 303 \qquad \blacksquare$$

---

← [§10–§11: Numerical Verification and Completeness Assessment](07_verification_and_completeness.md) | [README (top)](README.md)

---

*This paper is a record of independent research. Independent verification, criticism, and discussion — including numerical verification code — are welcome.*
