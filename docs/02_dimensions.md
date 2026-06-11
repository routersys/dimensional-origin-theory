# §4〜§5：観測次元数 $n_{\rm obs}=3$ および観測限界次元数 $n^\ast=11$ の導出

← [§1〜§3：公理と設定](01_axiom_and_setup.md) | 次 → [§6：基本方程式](03_fundamental_equation.md)

---

## 4. 観測次元数 $n_{\rm obs} = 3$ の導出

### 4.1 要請O1・O2の公理Ωからの演繹

要請O1・O2は外部仮定なしに公理Ωから演繹される。これらは課す要請ではなく公理Ωの帰結である。

#### 定理4.1.0（要請O1の演繹）

定理： 要請O1（物理的測定の合成の可逆性と結合則）は公理Ωから演繹される。

**証明：**

Step 1：公理Ωは状態空間 $S = \{\neg\exists, \exists\}$ と変換 $\sigma: \neg\exists \mapsto \exists$ , $\exists \mapsto \neg\exists$ を定める。 $\sigma^2 = \mathrm{id}$ , $\sigma \neq \mathrm{id}$ より $\sigma \in \mathrm{Aut}(S)$ 。

Step 2：物理的測定とは状態空間 $S$ の上の準同型 $\varphi: S \to S$ であり、その全体を $\mathrm{End}(S)$ とする。公理Ωの変換 $\sigma$ は全単射であるから $\sigma \in \mathrm{Aut}(S) \subset \mathrm{End}(S)$ 。

Step 3： $\mathrm{Aut}(S)$ は群である。群の公理のうち結合則 $(\sigma \circ \tau) \circ \rho = \sigma \circ (\tau \circ \rho)$ は写像の合成の結合則であり、これは集合論の定理であって外部仮定を含まない。

Step 4：測定が物理的に意味を持つ条件は、(i) 測定の合成が $S$ 上で閉じている（要請B1の帰結）、(ii) 逆測定が存在する（ $\sigma \in \mathrm{Aut}(S)$ の帰結）、(iii) 合成の結合則（Step 3の帰結）である。これら全てが公理Ωから従う。 $\square$

したがって測定の代数は結合的除算代数でなければならず、非結合的代数である八元数は公理Ωにより排除される。

#### 定理4.1.1（要請O2の演繹）

定理： 公理Ωが課す対称性の実現には観測空間の回転群 $SO(n_{\rm obs})$ が非アーベルである必要があり、非アーベルである最小次元は $n_{\rm obs} = 3$ である。

**証明：**

**Lemma 4.1.1（公理Ωのパリティ構造）：** $\sigma$ は対合（ $\sigma^2 = \mathrm{id}$ , $\sigma \neq \mathrm{id}$ ）であり、 $\neg\exists \neq \exists$ （状態の非同値性）を意味する。これは空間においてパリティ反転 $P: \mathbf{x} \mapsto -\mathbf{x}$ として実現される。

**Lemma 4.1.2（2次元でのパリティ消滅）：** 2次元空間では $P: (x,y) \mapsto (-x,-y)$ と $\pi$ 回転 $R(\pi) \in SO(2)$ が一致する。

$$P = R(\pi) \in SO(2) \quad (2\text{次元})$$

すなわち2次元では空間反転が回転対称性の元と同一視され、公理Ωのパリティ（ $\neg\exists \neq \exists$ ）を空間に実現できない。

**Lemma 4.1.3（ $SO(n)$ 非アーベル $\Leftrightarrow n \geq 3$ ）：**

$(\Leftarrow)$ ： $n \geq 3$ のとき $SO(3) \subset SO(n)$ に非可換元が存在する。例として $R_x(\pi/2) R_y(\pi/2) \neq R_y(\pi/2) R_x(\pi/2)$ （数値確認済 付録C）。

$(\Rightarrow)$ ： $SO(1) = \{e\}$ は1元群であり自明にアーベル。 $SO(2) \cong U(1) = \{e^{i\theta}\}$ は積が $e^{i(\theta+\phi)} = e^{i(\phi+\theta)}$ で可換。

Lemma 4.1.2 より $n = 2$ ではパリティが $SO(2)$ に埋没して消えること、Lemma 4.1.3 より非アーベルの最小次元が $n = 3$ であることから、次が成立する。

$$\boxed{n_{\rm obs} = 3 \text{ が公理Ωのパリティ構造を真に非自明に実現できる最小次元}} \quad \square$$

旧来の要請O2（ $SO(3)$ 以上の立体的観測可能性）はこの定理の系として自動的に従う。公理ΩのパリティがLemma 4.1.2によって消滅する次元を排除すれば、最小次元として3が残る。

### 4.2 Hurwitz定理による $n_{\rm obs} = 3$ の確定

定理4.1.0より観測空間の代数は結合的除算代数でなければならない。

Hurwitz定理（1898）： 実数上の除算代数は次の4つのみ存在する。

| 代数 | 全次元 | 可換性 | 結合性 | 虚数部の次元 | 回転群 |
|------|--------|--------|--------|--------------|--------|
| $\mathbb{R}$ | 1 | ✓ | ✓ | 0 | $SO(1)$ （自明） |
| $\mathbb{C}$ | 2 | ✓ | ✓ | 1 | $SO(2)$ （1軸） |
| $\mathbb{H}$ （四元数） | 4 | ✗ | ✓ | 3 | $SO(3)$ （3軸） |
| $\mathbb{O}$ （八元数） | 8 | ✗ | ✗ | 7 | — |

各代数に対する要請の適用は次のとおりである。

$\mathbb{O}$ （八元数）は非結合的である。例えば基底元 $e_1, e_2, e_4$ に対して $(e_1 e_2)e_4 = e_3 e_4 = e_7$ だが $e_1(e_2 e_4) = e_1 e_6 = -e_7$ であり $(e_1 e_2)e_4 \ne e_1(e_2 e_4)$ 。要請O1により排除される。

$\mathbb{R}$ （虚数部0次元）は $SO(0)$ が自明群であり独立な回転を持たない。要請O2を満たさない。

$\mathbb{C}$ （虚数部1次元）は $SO(2)$ が1軸回転のみ（1パラメータ群）であり、独立した奥行き方向が存在しない。要請O2を満たさない。

$\mathbb{H}$ （虚数部3次元）は結合的であり要請O1を満たす。純虚四元数空間 $\mathrm{Im}\,\mathbb{H} \cong \mathbb{R}^3$ に $SO(3)$ が自然に作用し、独立な3次元回転が存在する。要請O1・O2を同時に満たす。

要請O1・定理4.1.1を同時に満たす唯一の除算代数は四元数 $\mathbb{H}$ であり、その虚数部の次元が観測空間の次元を与える。

$$\boxed{n_{\rm obs} = \dim_{\mathbb{R}}(\mathrm{Im}\,\mathbb{H}) = 3}$$

---

## 5. 観測限界次元数 $n^\ast = 11$ の導出

### 5.1 観測可能限界の最小性定理

#### 定義（観測可能限界次元）

$\mathrm{Cl}(n)$ は $\mathbb{Z}/2$ 次数付き代数（偶部 $\mathrm{Cl}^0$ ・奇部 $\mathrm{Cl}^1$ ）であり、次数付け自己同型は $\alpha: e_i \mapsto -e_i$ である。観測可能限界次元 $n^\ast$ を、 $\mathrm{Cl}(n)$ が $\mathrm{Cl}(n_{\rm obs})$ と次数付き森田同値（superalgebra としての森田同値）となる最小の $n > n_{\rm obs}$ として定義する。

$$n^\ast := \min\left\lbrace n > n_{\rm obs} \;\mid\; \mathrm{Cl}(n) \sim_{\rm gr} \mathrm{Cl}(n_{\rm obs})\right\rbrace$$

#### 次数付けの公理Ωからの必然性

次数付け自己同型 $\alpha: e_i \mapsto -e_i$ は、空間パリティ $P: \mathbf{x} \mapsto -\mathbf{x}$ がClifford代数に誘導する作用であり、Lemma 4.1.1 により $P$ は公理Ωの対合 $\sigma$ （ $\neg\exists \leftrightarrow \exists$ ）の空間的実現である。したがって観測の同値はΩパリティを保存しなければならず、許される同値関係は次数付き同値である。これは外部から課す選択ではなく公理Ωの帰結である。物理的には、次数はフェルミオンパリティの超選択則に対応する。

非次数付き同値を採れば反例が生じる。 $\mathrm{Cl}(3,0) \cong M_2(\mathbb{C})$ かつ $\mathrm{Cl}(7,0) \cong M_8(\mathbb{C}) \cong M_2(\mathbb{C}) \otimes M_4(\mathbb{R})$ であるから（実次元 $128 = 8 \times 16$ 、中心 $\mathbb{C} = \mathbb{C} \otimes \mathbb{R}$ 、構成的検証済み）、非次数付き同値では最小値が $11$ ではなく $7$ となる。次数付き同値はこの反例を排除する。

#### 定理5.2.1（ $n^\ast = 11$ の確定）

外部定理（Wall 1964、次数付きBrauer群）： 実数体上の次数付きBrauer群は $\mathrm{sBr}(\mathbb{R}) \cong \mathbb{Z}/8$ であり、 $\mathrm{Cl}(p) \sim_{\rm gr} \mathrm{Cl}(q)$ の必要十分条件は $p \equiv q \pmod 8$ である。これは確立された数学定理であり、本理論におけるHurwitz定理と同じ認識論的地位を持つ。

したがって次が成立する。

$$n^\ast = \min\{n > 3 \mid n \equiv 3 \pmod 8\} = 11 \qquad \blacksquare$$

反例 $n = 7$ は除外される。実際、次数付き不変量である偶部の型は $\mathrm{Cl}^0(3,0) \cong \mathbb{H}$ （除算代数・型 $\mathbb{H}$ 、双ベクトル $e_{12}, e_{13}, e_{23}$ の四元数関係を構成的に検証済み）に対し $\mathrm{Cl}^0(7,0) \cong M_8(\mathbb{R})$ （非自明冪等元 $(1+e_{1234})/2$ を持ち除算代数でない・型 $\mathbb{R}$ ）であり、型の相違が非同値を直接示す。一方 $\mathrm{Cl}^0(11,0) \cong M_{16}(\mathbb{H})$ は型 $\mathbb{H}$ で一致する。

$$\boxed{n^\ast = n_{\rm obs} + 8 = 11}$$

要請M（最小実現原理）： 観測限界は上記定義における最小値を採用する。 $n \equiv 3 \pmod 8$ の族で $n = 11$ を超える次元（ $19, 27, \ldots$ ）は同じ次数付き森田類の繰り返しであり、新しい独立な実現を与えない。

### 5.2 Frobenius定理との接続

Frobenius定理により除算代数の最大次元は8（八元数 $\mathbb{O}$ ）である。これがエネルギー収支完結の限界であり、Bott周期8の起源となる。

### 5.3 Bott周期 $B = 2^{n_{\rm obs}}$ の整合性

標準的なBott周期定理はClifford代数が次元 $n$ に関して周期8で代数型が繰り返すことを述べる外部定理である。

$$\text{Cl}(n+8) \cong \text{Cl}(n) \otimes M(16, \mathbb{R})$$

$n^\ast = 11$ の導出は定理5.2.1（Wallの次数付きBrauer群定理 $\mathrm{sBr}(\mathbb{R}) \cong \mathbb{Z}/8$ ＋公理Ωによる次数付けの必然性）が担う。これと独立に、Cayley-Dickson対合群の総位数が周期 $8$ と一致するという整合性が $n_{\rm obs} = 3$ でのみ成立する。以下にこれを示す。

**定理（Cayley-Dickson対合群の整合性）：** Cayley-Dickson構成の各段階の対合群の積が $2^{n_{\rm obs}}$ に一致するのは $n_{\rm obs} = 3$ においてのみである。

**証明（5つの補題による）：**

**Lemma 1（公理Ωの代数的実現）：**
公理Ω $\neg\exists \to \exists$ は2つの状態「無」 $(\neg\exists)$ と「有」 $(\exists)$ を定義する。これらは命題論理上、排他的かつ網羅的であるから、状態空間は2元集合 $S = \{0, 1\}$ と同型である。

$S$ の自己同型群は $\mathrm{Aut}(S) = \mathbb{Z}/2\mathbb{Z}$ （2元集合の全単射は恒等写像と置換の2つのみ）。公理Ωの変換は $S$ 上の置換、すなわち $\mathbb{Z}/2\mathbb{Z}$ の非自明元として一意的に実現される。二重否定律 $\neg(\neg\exists) = \exists$ から $\phi^2 = \mathrm{id}$ が従い、この写像は対合 $\sigma: A \to A$ , $\sigma^2 = \mathrm{id}$ , $\sigma \ne \mathrm{id}$ である。この対合がCayley-Dickson構成の二倍化写像の起源となる。

**Lemma 2（Cayley-Dickson構成の必然性）：**
対合 $\sigma$ を持つ代数 $A$ から、二倍化 $A' = A \oplus A\cdot e$ を構成し、新しい積

$$(a, b)(c, d) = (ac - db^{\ast}, da + bc^{\ast})$$

を定義する。ここで $b^{\ast} = \sigma(b)$ は対合である。

この二倍化によりノルム乗法性 $|ab|^2 = |a|^2|b|^2$ が保たれる間、演算は物理的測定の整合性（要請O1：全測定は可逆）を保持する。

外部定理（Hurwitz定理）：実数上でノルム乗法性を持つ除算代数は $\mathbb{R}, \mathbb{C}, \mathbb{H}, \mathbb{O}$ （次元 $1, 2, 4, 8$ ）の4種類のみ存在する。 $k=4$ 段階目の十六元数 $\mathbb{S}$ ではノルム乗法性が破れ、要請O1の代数的要件が失われる。したがってCayley-Dickson構成は $k = 3$ （八元数 $\mathbb{O}$ ）で停止する。

**Lemma 3（各段階の対合群の成長則）：**
各Cayley-Dickson段階 $k$ で新たに追加される対合 $\sigma_k$ を帰納的に定義する。

$$\sigma_k(a + b\cdot e_k) = \sigma_{k-1}(a) - b\cdot e_k \quad (a, b \in A_{k-1})$$

$G_k = \langle \sigma_0, \sigma_1, \ldots, \sigma_{k-1} \rangle$ とおく。

$G_k \cong (\mathbb{Z}/2\mathbb{Z})^k$ の証明は次の3点による。

(i) $\sigma_j^2 = \mathrm{id}$ （帰納法）： $k=0$ では $\sigma_0 = \mathrm{id}$ なので自明。 $\sigma_{k-1}^2 = \mathrm{id}$ を仮定すると、

$$\sigma_k^2(a + b\cdot e_k) = \sigma_k(\sigma_{k-1}(a) - b\cdot e_k) = \sigma_{k-1}^2(a) + b\cdot e_k = a + b\cdot e_k$$

よって $\sigma_k^2 = \mathrm{id}$ 。

(ii) $\sigma_i \sigma_j = \sigma_j \sigma_i$ （ $i < j$ ）： $A_j = A_{j-1} \oplus A_{j-1}\cdot e_j$ の任意の元 $x = a + b\cdot e_j$ に対し、 $\sigma_i$ （段階 $i \le j-1$ の対合）は $e_j$ の係数に独立に作用するから、

$$\sigma_i(\sigma_j(x)) = \sigma_i(\sigma_{j-1}(a) - b\cdot e_j) = \sigma_i\sigma_{j-1}(a) - \sigma_i(b)\cdot e_j$$

$$\sigma_j(\sigma_i(x)) = \sigma_j(\sigma_i(a) + \sigma_i(b)\cdot e_j) = \sigma_{j-1}\sigma_i(a) - \sigma_i(b)\cdot e_j$$

両者の一致は $A_{j-1}$ 内での $\sigma_i$ と $\sigma_{j-1}$ の可換性に帰着し、帰納的に示される。

(iii) 独立性： $\sigma_j$ は $e_j$ の符号を反転し $e_i$ （ $i < j$ ）には作用しない。 $e_j$ は段階 $j$ に新たに追加される基底元であるから、 $\sigma_j$ は $\sigma_0, \ldots, \sigma_{j-1}$ の積では表せない。

(i)(ii)(iii) より $G_k \cong (\mathbb{Z}/2\mathbb{Z})^k$ 、したがって $|G_k| = 2^k$ 。 $\square$

| 段階 $k$ | 代数 | $G_k$ | $\|G_k\|$ |
|---------|------|--------|---------|
| 0 | $\mathbb{R}$ | $\{\mathrm{id}\}$ | $1 = 2^0$ |
| 1 | $\mathbb{C}$ | $\mathbb{Z}/2\mathbb{Z}$ | $2 = 2^1$ |
| 2 | $\mathbb{H}$ | $(\mathbb{Z}/2\mathbb{Z})^2$ | $4 = 2^2$ |
| 3 | $\mathbb{O}$ | $(\mathbb{Z}/2\mathbb{Z})^3$ | $8 = 2^3$ |

**Lemma 4（ $n_{\rm obs}$ 段階の累積対合群サイズ）：**
結合的除算代数は $\mathbb{R}, \mathbb{C}, \mathbb{H}$ （ $n_{\rm obs}$ 個、Hurwitz定理より）のみなので、累積対合群サイズは次のとおりである。

$$B = \prod_{k=0}^{n_{\rm obs}-1} |G_k| = \prod_{k=0}^{n_{\rm obs}-1} 2^k = 2^{\,\sum_{k=0}^{n_{\rm obs}-1} k} = 2^{n_{\rm obs}(n_{\rm obs}-1)/2}$$

**Lemma 5（ $n_{\rm obs} = 3$ の唯一性）：**
$B = 2^{n_{\rm obs}(n_{\rm obs}-1)/2} = 2^{n_{\rm obs}}$ が成立するための必要十分条件は次のとおりである。

$$\frac{n_{\rm obs}(n_{\rm obs}-1)}{2} = n_{\rm obs} \iff n_{\rm obs}(n_{\rm obs}-3) = 0 \iff n_{\rm obs} \in \{0, 3\}$$

$n_{\rm obs} = 0$ は $n \ge 1$ の公理的前提と矛盾するため排除される。よって $n_{\rm obs} = 3$ が唯一の解。

**結論：**

$$\boxed{B = 2^{n_{\rm obs}} = 8 \quad (n_{\rm obs} = 3 \text{ においてのみ成立})} \qquad \blacksquare$$

この等式

$$\prod_{k=0}^{n_{\rm obs}-1} 2^k = 2^{n_{\rm obs}(n_{\rm obs}-1)/2} = 2^{n_{\rm obs}}$$

は厳密に成立する代数的事実であり、 $n_{\rm obs} = 3$ でのみCayley-Dickson対合群の総位数が周期 $8$ と一致するという整合性を与える。

### 5.4 $n^\ast$ の確定

$$\boxed{n^\ast = n_{\rm obs} + 8 = 3 + 8 = 11}$$

完全な導出チェーンは次のとおりである。

```
公理Ω（¬∃ → ∃）
 │
 ├─ Z/2Z 対合 σ の存在（Aut(S)=Z/2Z, Lemma 1）
 │
 ├─ σ の空間的実現 = パリティ P（Lemma 4.1.1）
 │   └─ Clifford代数への誘導作用 α: e_i → -e_i = Z/2 次数付け
 │
 ├─ Hurwitz定理: n_obs = 3（結合的除算代数は R, C, H）
 │
 ├─ 観測の同値はΩパリティ（次数）を保存 ⟹ 次数付き森田同値
 │
 ├─ Wall定理: sBr(R) ≅ Z/8 ⟹ Cl(p) ~gr Cl(q) ⟺ p ≡ q (mod 8)
 │
 └─ n* = min{n > 3 | n ≡ 3 (mod 8)} = 11
     （整合性注記: ∏ 2^k = 2^{n(n-1)/2} = 2^n = 8 は n_obs = 3 のみ, §5.3）
```

外部定理はHurwitz定理・コーシー関数方程式・Wall定理の3つであり、全て確立された数学定理である。

---

← [§1〜§3：公理と設定](01_axiom_and_setup.md) | 次 → [§6：基本方程式](03_fundamental_equation.md)
