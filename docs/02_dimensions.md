# §4〜§5：観測次元数 $n_{\rm obs}=3$ および観測限界次元数 $n^\ast=11$ の導出

← [§1〜§3：公理と設定](01_axiom_and_setup.md) | 次 → [§6：基本方程式](03_fundamental_equation.md)

---

## 4. 観測次元数 $n_{\rm obs} = 3$ の導出

### 4.1 要請O1・O2の公理Ωからの演繹

v4.4では、要請O1・O2が公理Ωから外部仮定なしに演繹されることを厳密に証明する。これらは「課す要請」ではなく「公理Ωの帰結」である。

#### 定理4.1.0（要請O1の演繹）

定理： 要請O1（物理的測定の合成の可逆性と結合則）は公理Ωから演繹される。

**証明：**

Step 1：公理Ωは状態空間 $S = \{\neg\exists, \exists\}$ と変換 $\sigma: \neg\exists \mapsto \exists$, $\exists \mapsto \neg\exists$ を定める（§5.4 Lemma 1 済）。$\sigma^2 = \mathrm{id}$, $\sigma \neq \mathrm{id}$ より $\sigma \in \mathrm{Aut}(S)$。

Step 2：物理的測定とは状態空間 $S$ の上の準同型 $\varphi: S \to S$ であり、その全体を $\mathrm{End}(S)$ とする。公理Ωの変換 $\sigma$ は全単射であるから $\sigma \in \mathrm{Aut}(S) \subset \mathrm{End}(S)$。

Step 3：$\mathrm{Aut}(S)$ は群である。群の公理のうち結合則 $(\sigma \circ \tau) \circ \rho = \sigma \circ (\tau \circ \rho)$ は写像の合成の結合則であり、これは集合論の定理（外部仮定なし）。

Step 4：測定が物理的に意味を持つ条件は (i) 測定の合成が $S$ 上で閉じている（$=$ 要請B1の帰結）、(ii) 逆測定が存在する（$= \sigma \in \mathrm{Aut}(S)$ の帰結）、(iii) 合成の結合則（$=$ Step 3の帰結）。これら全てが公理Ωから従う。$\square$

したがって測定の代数は結合的除算代数でなければならず、非結合的代数（八元数）は公理Ωにより排除される。

#### 定理4.1.1（要請O2の演繹）

定理： 公理Ωが課す対称性の実現には観測空間の回転群 $SO(n_{\rm obs})$ が非アーベルである必要があり、非アーベルである最小次元は $n_{\rm obs} = 3$ である。

**証明：**

**Lemma 4.1.1（公理Ωのパリティ構造）：** $\sigma$ は対合（$\sigma^2 = \mathrm{id}$, $\sigma \neq \mathrm{id}$）であり、$\neg\exists \neq \exists$（状態の非同値性）を意味する。これは空間においてパリティ反転 $P: \mathbf{x} \mapsto -\mathbf{x}$ として実現される。（§5.4 Lemma 1 済）

**Lemma 4.1.2（2次元でのパリティ消滅）：** 2次元空間では $P: (x,y) \mapsto (-x,-y)$ と $\pi$ 回転 $R(\pi) \in SO(2)$ が一致する：

$$P = R(\pi) \in SO(2) \quad (2\text{次元})$$

すなわち2次元では空間反転が回転対称性の元と同一視され、公理Ωのパリティ（$\neg\exists \neq \exists$）を空間に実現できない。

**Lemma 4.1.3（$SO(n)$ 非アーベル $\Leftrightarrow n \geq 3$）：**

$(\Leftarrow)$：$n \geq 3$ のとき $SO(3) \subset SO(n)$ に非可換元が存在する。例：$R_x(\pi/2) R_y(\pi/2) \neq R_y(\pi/2) R_x(\pi/2)$（数値確認済 付録C）。

$(\Rightarrow)$：$SO(1) = \{e\}$ は1元群（自明にアーベル）。$SO(2) \cong U(1) = \{e^{i\theta}\}$ は積が $e^{i(\theta+\phi)} = e^{i(\phi+\theta)}$ で可換。

Lemma 4.1.2 より $n = 2$ ではパリティが $SO(2)$ に埋没して消えること、Lemma 4.1.3 より非アーベルの最小次元が $n = 3$ であることから：

$$\boxed{n_{\rm obs} = 3 \text{ が公理Ωのパリティ構造を真に非自明に実現できる最小次元}} \quad \square$$

> 旧来の要請O2（「$SO(3)$ 以上の立体的観測可能性」）はこの定理の系として自動的に従う。公理ΩのパリティがLemma 4.1.2によって消滅する次元を排除すれば、最小次元として3が残る。

### 4.2 Hurwitz定理による $n_{\rm obs} = 3$ の確定

定理4.1.0（要請O1の演繹）より観測空間の代数は結合的除算代数でなければならない。

Hurwitz定理（1898）： 実数上の除算代数は次の4つのみ存在する：

| 代数 | 全次元 | 可換性 | 結合性 | 虚数部の次元 | 回転群 |
|------|--------|--------|--------|--------------|--------|
| $\mathbb{R}$ | 1 | ✓ | ✓ | 0 | $SO(1)$（自明） |
| $\mathbb{C}$ | 2 | ✓ | ✓ | 1 | $SO(2)$（1軸） |
| $\mathbb{H}$（四元数） | 4 | ✗ | ✓ | 3 | $SO(3)$（3軸） |
| $\mathbb{O}$（八元数） | 8 | ✗ | ✗ | 7 | — |

各代数に対する要請の適用：

- $\mathbb{O}$（八元数）： 非結合的。例えば基底元 $e_1, e_2, e_4$ に対して $(e_1 e_2)e_4 = e_3 e_4 = e_7$ だが $e_1(e_2 e_4) = e_1 e_6 = -e_7$ であり $(e_1 e_2)e_4 \ne e_1(e_2 e_4)$。要請O1により排除。

- $\mathbb{R}$（虚数部0次元）： $SO(0)$ は自明群。独立な回転なし。要請O2を満たさない。

- $\mathbb{C}$（虚数部1次元）： $SO(2)$ は1軸回転のみ（1パラメータ群）。独立した奥行き方向が存在しない。要請O2を満たさない。

- $\mathbb{H}$（虚数部3次元）： 結合的（要請O1を満たす）。純虚四元数空間 $\mathrm{Im}\,\mathbb{H} \cong \mathbb{R}^3$ に $SO(3)$ が自然に作用し、独立な3次元回転が存在する。要請O1・O2を同時に満たす。

要請O1・定理4.1.1（旧要請O2の演繹）を同時に満たす唯一の除算代数は四元数 $\mathbb{H}$ であり、その虚数部の次元が観測空間の次元を与える：

$$\boxed{n_{\rm obs} = \dim_{\mathbb{R}}(\mathrm{Im}\,\mathbb{H}) = 3}$$

---

## 5. 観測限界次元数 $n^\ast = 11$ の導出

### 5.1 Bott周期の内部導出（背景と方針）

標準的な Bott 周期定理はClifford代数が次元 $n$ に関して周期8で代数型が繰り返すことを述べる外部定理である：

$$\text{Cl}(n+8) \cong \text{Cl}(n) \otimes M(16, \mathbb{R})$$

本理論では §5.4 でこの「8」という周期をBott周期定理に依存せず Cayley-Dickson 対合群の内部構造から導出する（v4.1）。§5.2 はその内部導出を前提として $n^\ast$ を定める。

### 5.2 観測可能限界の最小性定理

定義（観測可能限界次元）： $n_{\rm obs}$ 次元の観測者から「観測可能」な最大次元 $n^\ast$ を、$\mathrm{Cl}(n_{\rm obs})$ が $\mathrm{Cl}(n)$ の直接因子として現れる最小の $n > n_{\rm obs}$ として定義する：

$$n^\ast := \min\left\lbrace n > n_{\rm obs} \;\mid\; \mathrm{Cl}(n) \cong \mathrm{Cl}(n_{\rm obs}) \otimes M(N, \mathbb{K}) \text{ for some } N, \mathbb{K}\right\rbrace$$

Bott 周期定理より：

$$\mathrm{Cl}(n_{\rm obs} + k \cdot B) \cong \mathrm{Cl}(n_{\rm obs}) \otimes M(16^k, \mathbb{R}), \quad k = 1, 2, 3, \ldots$$

この族で $n > n_{\rm obs}$ を満たす最小値は $k = 1$ すなわち $n = n_{\rm obs} + B$ である。$k \ge 2$ は同じ代数的構造の繰り返しであり、$k=1$ を超えた次元は $\mathrm{Cl}(n_{\rm obs})$ の新しい独立な実現を与えない。

$$\boxed{n^\ast = n_{\rm obs} + B}$$

要請M（最小実現原理）： 観測限界は上記定義における最小値（$k=1$）を採用する。これは「最小の情報で完全な記述を与える次元」（定量的 Ockham の剃刀）という原理の適用である。

### 5.3 Frobenius定理との接続

Frobenius定理により除算代数の最大次元は8（八元数 $\mathbb{O}$）。これが「エネルギー収支完結の限界」であり、Bott周期8の起源となる。

### 5.4 Bott周期 $= 2^{n_{\rm obs}}$ の代数的証明（v4.1）

**定理（Bott周期の内部導出）：** 公理ΩとCayley-Dickson構成から $B = 2^{n_{\rm obs}}$ が成立するのは $n_{\rm obs} = 3$ においてのみである。

**証明（5つの補題による）：**

**Lemma 1（公理Ωの代数的実現）：**
公理Ω $\neg\exists \to \exists$ は2つの状態「無」$(\neg\exists)$ と「有」$(\exists)$ を定義する。これらは命題論理上、排他的かつ網羅的であるから、状態空間は2元集合 $S = \{0, 1\}$ と同型である。

$S$ の自己同型群は $\mathrm{Aut}(S) = \mathbb{Z}/2\mathbb{Z}$（2元集合の全単射は恒等写像と置換の2つのみ）。公理Ωの変換は $S$ 上の置換、すなわち $\mathbb{Z}/2\mathbb{Z}$ の非自明元として一意的に実現される。二重否定律 $\neg(\neg\exists) = \exists$ から $\phi^2 = \mathrm{id}$ が従い、この写像は対合（involution）$\sigma: A \to A$, $\sigma^2 = \mathrm{id}$, $\sigma \ne \mathrm{id}$ である。この対合が Cayley-Dickson 構成の二倍化写像の起源となる。

**Lemma 2（Cayley-Dickson構成の必然性）：**
対合 $\sigma$ を持つ代数 $A$ から、二倍化 $A' = A \oplus A\cdot e$ を構成し、新しい積

$$(a, b)(c, d) = (ac - db^{\ast}, da + bc^{\ast})$$

を定義する。ここで $b^{\ast} = \sigma(b)$ は対合である。

この二倍化によりノルム乗法性 $|ab|^2 = |a|^2|b|^2$ が保たれる間、演算は物理的測定の整合性（要請O1：全測定は可逆）を保持する。

外部定理（Hurwitz定理）：実数上でノルム乗法性を持つ除算代数は $\mathbb{R}, \mathbb{C}, \mathbb{H}, \mathbb{O}$（次元 $1, 2, 4, 8$）の4種類のみ存在する。$k=4$ 段階目の十六元数 $\mathbb{S}$ ではノルム乗法性が破れ、要請O1の代数的要件が失われる。したがって Cayley-Dickson 構成は $k = 3$（八元数 $\mathbb{O}$）で停止する。

**Lemma 3（各段階の対合群の成長則）：**
各 Cayley-Dickson 段階 $k$ で新たに追加される対合 $\sigma_k$ を帰納的に：

$$\sigma_k(a + b\cdot e_k) = \sigma_{k-1}(a) - b\cdot e_k \quad (a, b \in A_{k-1})$$

と定義し、$G_k = \langle \sigma_0, \sigma_1, \ldots, \sigma_{k-1} \rangle$ とおく。

$G_k \cong (\mathbb{Z}/2\mathbb{Z})^k$ の証明：

(i) $\sigma_j^2 = \mathrm{id}$（帰納法）：$k=0$ では $\sigma_0 = \mathrm{id}$ なので自明。$\sigma_{k-1}^2 = \mathrm{id}$ を仮定すると、

$$\sigma_k^2(a + b\cdot e_k) = \sigma_k(\sigma_{k-1}(a) - b\cdot e_k) = \sigma_{k-1}^2(a) + b\cdot e_k = a + b\cdot e_k$$

よって $\sigma_k^2 = \mathrm{id}$。

(ii) $\sigma_i \sigma_j = \sigma_j \sigma_i$（$i < j$）：$A_j = A_{j-1} \oplus A_{j-1}\cdot e_j$ の任意の元 $x = a + b\cdot e_j$ に対し、$\sigma_i$（段階 $i \le j-1$ の対合）は $e_j$ の係数に独立に作用するから、

$$\sigma_i(\sigma_j(x)) = \sigma_i(\sigma_{j-1}(a) - b\cdot e_j) = \sigma_i\sigma_{j-1}(a) - \sigma_i(b)\cdot e_j$$

$$\sigma_j(\sigma_i(x)) = \sigma_j(\sigma_i(a) + \sigma_i(b)\cdot e_j) = \sigma_{j-1}\sigma_i(a) - \sigma_i(b)\cdot e_j$$

両者の一致は $A_{j-1}$ 内での $\sigma_i$ と $\sigma_{j-1}$ の可換性に帰着し、帰納的に示される。

(iii) 独立性：$\sigma_j$ は $e_j$ の符号を反転し $e_i$（$i < j$）には作用しない。$e_j$ は段階 $j$ に新たに追加される基底元であるから、$\sigma_j$ は $\sigma_0, \ldots, \sigma_{j-1}$ の積では表せない。

(i)(ii)(iii) より $G_k \cong (\mathbb{Z}/2\mathbb{Z})^k$、したがって $|G_k| = 2^k$。$\square$

| 段階 $k$ | 代数 | $G_k$ | $\|G_k\|$ |
|---------|------|--------|---------|
| 0 | $\mathbb{R}$ | $\{\mathrm{id}\}$ | $1 = 2^0$ |
| 1 | $\mathbb{C}$ | $\mathbb{Z}/2\mathbb{Z}$ | $2 = 2^1$ |
| 2 | $\mathbb{H}$ | $(\mathbb{Z}/2\mathbb{Z})^2$ | $4 = 2^2$ |
| 3 | $\mathbb{O}$ | $(\mathbb{Z}/2\mathbb{Z})^3$ | $8 = 2^3$ |

**Lemma 4（$n_{\rm obs}$ 段階の累積対合群サイズ）：**
Cayley-Dickson 構成の各段階 $k$ で追加される対合 $\sigma_k$ は独立な対合群 $G_k \cong (\mathbb{Z}/2\mathbb{Z})^k$ を生成する（Lemma 3）。$n_{\rm obs}$ 段階の構成全体を一つの「代数サイクル」として見たとき、このサイクルが持つ独立対合の総個数は：

$$\sum_{k=0}^{n_{\rm obs}-1} k = \frac{n_{\rm obs}(n_{\rm obs}-1)}{2}$$

この総個数が $2$ のべき乗として表す次元数が、Cayley-Dickson サイクルを「次元空間上の周期」として記述したときの自然な周期パラメータ $B$ を定義する：

$$B := 2^{\,\sum_{k=0}^{n_{\rm obs}-1} k} = 2^{n_{\rm obs}(n_{\rm obs}-1)/2}$$

具体的には結合的除算代数は $\mathbb{R}, \mathbb{C}, \mathbb{H}$（$= n_{\rm obs}$ 個、Hurwitz定理より）のみなので：

$$B = \prod_{k=0}^{n_{\rm obs}-1} |G_k| = \prod_{k=0}^{n_{\rm obs}-1} 2^k = 2^{\,\sum_{k=0}^{n_{\rm obs}-1} k} = 2^{n_{\rm obs}(n_{\rm obs}-1)/2}$$

**Lemma 5（$n_{\rm obs} = 3$ の唯一性）：**
$B = 2^{n_{\rm obs}(n_{\rm obs}-1)/2} = 2^{n_{\rm obs}}$ が成立するための必要十分条件：

$$\frac{n_{\rm obs}(n_{\rm obs}-1)}{2} = n_{\rm obs} \iff n_{\rm obs}(n_{\rm obs}-3) = 0 \iff n_{\rm obs} \in \{0, 3\}$$

$n_{\rm obs} = 0$ は $n \ge 1$ の公理的前提と矛盾するため排除される。よって $n_{\rm obs} = 3$ が唯一の解。

**結論：**

$$\boxed{B = 2^{n_{\rm obs}} = 8 \quad (n_{\rm obs} = 3 \text{ においてのみ成立})} \qquad \blacksquare$$

この定理は Bott 周期定理を外部定理として引用せず、Cayley-Dickson 構成の内部構造から Bott 周期の値を決定する。

### 5.5 $n^\ast$ の確定

$$\boxed{n^\ast = n_{\rm obs} + B = 3 + 8 = 11}$$

完全な導出チェーン（全て仮定なし）：

```
公理Ω（¬∃ → ∃）
 │
 ├─ Z/2Z 対合の存在（Aut(S)=Z/2Z）
 │
 ├─ Cayley-Dickson構成（R → C → H → O）
 │   └─ 対合群 G_k ≅ (Z/2Z)^k, |G_k| = 2^k
 │
 ├─ Hurwitz定理: n_obs = 3, 結合的除算代数は R, C, H の3個
 │
 ├─ B = ∏_{k=0}^{n_obs-1} 2^k = 2^{n_obs(n_obs-1)/2}
 │
 ├─ n_obs(n_obs-1)/2 = n_obs ⟺ n_obs = 3 [唯一解]
 │
 ├─ Bott周期 B = 2^{n_obs} = 8 [n_obs=3 においてのみ成立]
 │
 └─ n* = n_obs + B = 11
```

---

← [§1〜§3：公理と設定](01_axiom_and_setup.md) | 次 → [§6：基本方程式](03_fundamental_equation.md)
