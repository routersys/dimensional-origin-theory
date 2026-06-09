# 付録A〜D

← [§10〜§11：数値検証・完成度評価](07_verification_and_completeness.md) | [README（トップ）](../README.md)

---

## 付録A：方程式体系（v3.0完全版）

$$\text{公理Ω}: \quad \neg\exists \;\rightarrow\; \exists$$

$$\text{E-0（エネルギー密度）}: \quad \varepsilon(n) = E_0 \cdot n^{-\alpha}$$

$$\text{基本方程式}: \quad \alpha \cdot \ln n^\ast = (n^\ast-1)(n^\ast-2)\pi \quad \Rightarrow \quad \alpha = \frac{90\pi}{\ln 11}$$

$$\text{E-}\Lambda\text{（宇宙論的定数）}: \quad \Lambda = 2(n^\ast-2) \cdot \frac{(n^\ast)^{-\alpha}}{l_P^2}$$

$$\text{E-}H\text{（ハッブル定数）}: \quad H_0 = \sqrt{\frac{8\pi G\,\rho_\Lambda}{3\,\Omega_\Lambda}}, \quad \rho_\Lambda = \frac{\Lambda c^2}{8\pi G}$$

$$\text{E-CMB（第1ピーク）}: \quad \ell_1 = D_3(S^9) + D_1(S^9) = \binom{12}{3} = 220$$

$$\text{E-CMB（全ピーク・v2.0）}: \quad \ell_k = \binom{n^\ast+1}{n_{\rm obs}} + (k-1) \cdot \frac{D_{n_{\rm obs}+1}(S^{n^\ast-2}) - D_{n_{\rm obs}-1}(S^{n^\ast-2})}{2} = 220 + (k-1) \times 303$$

$$\text{E-}R\text{（バリオン-光子比・v3.0）}: \quad R_{\rm dec} = \frac{3(n^\ast - n_{\rm obs})}{4(n^\ast - 1)} = \frac{3}{5}$$

$$\text{E-}z\text{（脱結合赤方偏移・v3.0）}: \quad z_{\rm dec} = \frac{n^\ast-1}{2} \cdot \binom{n^\ast+1}{n_{\rm obs}} - n^\ast = 1089$$

$$\text{E-}r\text{（テンソル・スカラー比）}: \quad r = \frac{1}{D_2(S^9)} = \frac{1}{54} \approx 0.0185$$

$$\text{E-}w\text{（暗黒エネルギー）}: \quad w = -1 \quad (\rho_\Lambda = \mathrm{const} \text{ の証明済み帰結})$$

$$\text{E-}N_{\rm eff}\text{（有効ニュートリノ数）}: \quad N_{\rm eff} = 3\left(1 + \frac{1}{D_2}\right) = 3.056$$

$$\text{E-}n_t\text{（重力波指数）}: \quad n_t = -\frac{1}{8 D_2} = -\frac{1}{432} \approx -0.00231$$

$$\text{E-}T\text{（CMB温度・v4.0）}: \quad T_{\rm CMB} = T_P \cdot \left[(n^\ast)^{-\alpha} \cdot \frac{2}{n_{\rm obs}\,\pi} \cdot \frac{30}{\pi^2(n^\ast-1)^2} \cdot \left(\frac{4n^\ast-1}{n^\ast(n^\ast-1)^2}\right)^{4/3}\right]^{1/4} \approx 2.7285\,{\rm K}$$

---

## 付録B： $S^9$ の球面調和縮重度の導出公式

$S^9 \subset \mathbb{R}^{10}$ （埋め込み空間次元 $n=10$ ）における $\ell$ 次球面調和の縮重度：

$$D_\ell(S^9) = \binom{9+\ell}{\ell} - \binom{7+\ell}{\ell-2}, \quad \ell \ge 2$$

$$D_0 = 1, \quad D_1 = 10$$

---

## 付録C： $\mathrm{so}(10)$ チャンネル位相定理の数値確認

$\text{so}(10)$ の生成子 $L_{ij}$ （ $1 \le i < j \le 10$ ）全45個に対して：

$$\exp(2\pi \cdot L_{ij}) = I_{10\times 10}$$

Python/numpyによる数値計算で全45個 True を確認（行列指数関数のTaylor展開、収束判定 $\|e^{2\pi L} - I\| < 10^{-12}$ ）。

---

## 付録D：全ピーク式 v2.0 の代数的証明の詳細

定理： $n_{\rm obs}=3$ , $n^\ast=11$ のとき

$$\ell_k = 220 + (k-1) \times 303 \quad (k = 1, 2, 3, \ldots)$$

**証明：**

ステップ1： $\ell_1 = 220$ は [§8.4](../docs/05_cmb_peaks.md#84-cmb第1ピークの代数的証明) で代数的に証明済みである。

ステップ2： 音響スケール $\Delta\ell = 303$ の計算。

$$D_4(S^9) = \binom{13}{4} - \binom{11}{2} = 715 - 55 = 660$$

$$D_2(S^9) = \binom{11}{2} - \binom{9}{0} = 55 - 1 = 54$$

$$\Delta\ell = \frac{D_{n_{\rm obs}+1} - D_{n_{\rm obs}-1}}{2} = \frac{660 - 54}{2} = 303$$

ステップ3： $\Delta\ell$ の音響スケールとしての同定。

$S^9$ 上の偶パリティモードは静的背景場を記述し、そのモード密度の変化 $D_4 - D_2 = 606$ が「次の音響振動が起こるための空間的容量の増分」を表す。音響定在波はその進行波2方向の重ね合わせであるから、実効的な $\ell$ 空間間隔は $606/2 = 303$ となる。

ステップ4： 全ピーク式の成立。

第1ピーク $\ell_1 = 220$ から始まり、間隔 $\Delta\ell = 303$ で等差数列をなす：

$$\ell_k = \ell_1 + (k-1)\Delta\ell = 220 + (k-1) \times 303 \qquad \blacksquare$$

---

← [§10〜§11：数値検証・完成度評価](07_verification_and_completeness.md) | [README（トップ）](../README.md)

---

*本稿は独自研究の記録（v4.4）である。数値検証コードを含め、独立した検証・批判・議論を歓迎する。*
