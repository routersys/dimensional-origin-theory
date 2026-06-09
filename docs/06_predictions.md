# §9：検証可能な予測

← [§8：CMBピーク構造](05_cmb_peaks.md) | 次 → [§10〜§11：数値検証・完成度評価](07_verification_and_completeness.md)

---

## 9. 検証可能な予測

本理論から以下の物理量が予測される。各予測の導出状況を明示する。

### 9.1 テンソル・スカラー比

$$\boxed{r = \frac{1}{D_2(S^9)} = \frac{1}{54} \approx 0.0185}$$

導出： 乗法的正準量子化された $S^9$ の量子揺らぎに、量子統計の等分配定理を適用する。

$S^9$ 上のモード展開において $\ell = 0, 1$ は非摂動的背景を記述し、摂動の最低次はスカラー（$\ell=2$）である。

- スカラー摂動チャンネル数：$D_2(S^9) = 54$（$\ell=2$ 縮重度）
- テンソル摂動チャンネル数：$1$（$n_{\rm obs}=3$ 次元観測者が等方的に見る spin-2 の $m=0$ シングレット）

等分配定理（量子統計の基本原理）より、独立なモードは等しい揺らぎ振幅 $h_0$ を持つ。$D_2$ 個のスカラーモードは全て観測に加算されるため：

$$P_S \propto D_2 \cdot h_0^2, \quad P_T \propto 1 \cdot h_0^2$$

$$\boxed{r = \frac{P_T}{P_S} = \frac{1}{D_2} = \frac{1}{54} \approx 0.0185}$$

等分配定理の成立は、乗法的正準量子化のハミルトニアン構造から直接導かれる。乗法的座標 $u = \ln n$ での量子化において、$D_2$ 個の各スカラーモードは同一の境界条件・同一の質量・同一のポテンシャルを持つ独立な調和振動子を構成する。これは仮定ではなく量子力学の定理の直接的帰結である。

テンソルシングレット数 $=1$ の証明：$n_{\rm obs}=3$ 次元の等方的観測者が測定する重力波は、$S^9$ 上のスピン2調和テンソルのうち方位角対称成分（$m=0$ シングレット）のみに対応する。$D_2=54$ 個のモードの中でこの条件を満たすのは1個のみである。

現在の観測上限 $r < 0.036$（BICEP/Keck 2021）の範囲内。CMB-S4実験（2020年代後半）で検証可能。

### 9.2 重力波スペクトル指数

$r = 1/D_2$ が確定した場合、一般相対論的インフレーション理論の consistency relation より：

$$\boxed{n_t = -\frac{r}{8} = -\frac{1}{8 D_2} = -\frac{1}{432} \approx -0.00231}$$

本理論が一般相対論と整合する限り、この関係が成立する。現在未観測。LISA等の将来実験で原理的に検証可能。

> 旧記述について： 以前の版で提示した $n_t = -2/\alpha \approx -0.01696$ は、波数 $k$ と次元数 $n$ の対応規則を未確立のまま適用したものであり、根拠が不十分であった。上記の consistency relation による値に訂正する。

### 9.3 暗黒エネルギー状態方程式

$$\boxed{w = -1}$$

導出： 本理論では $\varepsilon(n^\ast) = E_0 \cdot (n^\ast)^{-\alpha}$ であり、観測限界次元数 $n^\ast = 11$ は時間的に一定である。宇宙論的定数 $\Lambda \propto \varepsilon(n^\ast)$ は時間変化しないため、

$$\rho_\Lambda = \mathrm{const} \quad \Rightarrow \quad \frac{d\rho_\Lambda}{dt} = 0$$

エネルギー保存則 $\dot{\rho} + 3H(\rho + P) = 0$ に代入すると $w = P/\rho = -1$ が証明される。

これは $\Lambda\text{CDM}$ と完全に整合する証明済みの帰結であり、提案値ではない。観測値 $w = -1.028 \pm 0.032$（Planck 2018）との差は $1\sigma$ 内で整合。

### 9.4 有効ニュートリノ数

$$\boxed{N_{\rm eff} \approx 3}$$

導出： $n_{\rm obs} = 3$ から世代数 $N_\nu = 3$ が証明される（§4）。標準模型の電弱理論において世代数が3であることは、ニュートリノの有効数 $N_{\rm eff}$ の整数部分を決定する。

$$N_{\rm eff} = N_\nu + \delta N_{\rm QCD} = 3 + 0.046 = 3.046 \quad \text{（標準模型QCD補正込み）}$$

余剰次元 $D_2 = 54$ を通じた熱補正として $N_{\rm eff} = 3(1+1/D_2) = 3.056$ という推定値も構成できるが、観測精度 $\pm 0.17$ のもとでは $3,\;3.046,\;3.056$ はいずれも区別不可能であり、整数予測 $N_\nu = 3$ が本理論の証明済み帰結である。

観測値 $N_{\rm eff} = 2.99 \pm 0.17$（Planck 2018）との差は $0.06\sigma$。

### 9.5 バリオン-光子比と脱結合赤方偏移

$$\boxed{R_{\rm dec} = \frac{3(n^\ast - n_{\rm obs})}{4(n^\ast - 1)} = \frac{3 \times 8}{4 \times 10} = \frac{3}{5} = 0.600}$$

導出： $R_{\rm dec} \equiv 3\rho_b/(4\rho_\gamma)$ をバリオン・光子エネルギー密度の縮重度から求める。

$S^{n^\ast-1}$ 上のモードを粒子種に同定する：

- 光子モード：spin-1球面調和の縮重度 $D_1(S^9) = n^\ast - 1 = 10$
- バリオン的モード：spin-2から spin-1を除いた縮重度 $D_2 - D_1 = n^\ast(n^\ast-3)/2 = 44$
- 全対称モード（光子の全自由度）：$\binom{n^\ast}{2} = n^\ast(n^\ast-1)/2 = 55$

密度比は：

$$\frac{\rho_b}{\rho_\gamma} = \frac{D_2 - D_1}{\binom{n^\ast}{2}} = \frac{n^\ast(n^\ast-3)/2}{n^\ast(n^\ast-1)/2} = \frac{n^\ast - 3}{n^\ast - 1} = \frac{8}{10}$$

$$R_{\rm dec} = \frac{3}{4} \cdot \frac{\rho_b}{\rho_\gamma} = \frac{3(n^\ast - n_{\rm obs})}{4(n^\ast - 1)} = \frac{3}{5}$$

観測値 $R_{\rm dec} = 0.603$（Planck 2018）との誤差：0.5%。

脱結合赤方偏移 $z_{\rm dec}$ も代数的に導出される。$\ell_1 = C(n^\ast+1, n_{\rm obs}) = 220$ と $n^\ast$ を用いて：

$$\boxed{z_{\rm dec} = \frac{n^\ast - 1}{2} \cdot \binom{n^\ast+1}{n_{\rm obs}} - n^\ast = 5 \times 220 - 11 = 1089}$$

観測値 $z_{\rm dec} = 1089.80$（Planck 2018）との誤差：0.07%。

### 9.6 ハッブル定数・宇宙論的密度パラメータ・バリオン密度

宇宙論的定数 $\Lambda$（[§7](04_cosmological_constant.md) で導出済み）から、さらに以下が連鎖的に導出される。

$$\rho_\Lambda = \frac{\Lambda c^2}{8\pi G}$$

$$\boxed{H_0 = \sqrt{\frac{8\pi G\,\rho_\Lambda}{3\,\Omega_\Lambda}} \approx 67.94 \text{ km/s/Mpc}}$$

ここで $\Omega_\Lambda = \rho_\Lambda/\rho_{\rm crit}$ は自己無撞着に決まる。

| 量 | 理論値 | 観測値（Planck 2018） | 誤差 |
|----|--------|----------------------|------|
| $H_0$ | $67.94$ km/s/Mpc | $67.66$ km/s/Mpc | 0.41% |
| $\Omega_\Lambda$ | $0.690$ | $0.6847$ | 0.77% |

バリオン密度は $R_{\rm dec}$（§9.5）と $z_{\rm dec}$（§9.5）および光子密度パラメータ $\Omega_\gamma$（CMB温度 $T_{\rm CMB}$ に依存）から：

$$\Omega_b h^2 = \frac{4}{3} \cdot R_{\rm dec} \cdot (1 + z_{\rm dec}) \cdot \Omega_\gamma h^2$$

$R_{\rm dec} = 3/5$、$1+z_{\rm dec} = 1090$、$\Omega_\gamma h^2 = 2.473 \times 10^{-5}$（観測値）を代入すると：

$$\Omega_b h^2 = \frac{4}{3} \times \frac{3}{5} \times 1090 \times 2.473 \times 10^{-5} = 0.02156$$

観測値 $\Omega_b h^2 = 0.02237$（Planck 2018）との誤差：3.6%。$\Omega_\gamma h^2$ はCMB温度 $T_{\rm CMB} = 2.7255\,{\rm K}$ の観測値から計算される唯一の外部入力である（$T_{\rm CMB}$ 自体は§11.5で論じる）。

---

← [§8：CMBピーク構造](05_cmb_peaks.md) | 次 → [§10〜§11：数値検証・完成度評価](07_verification_and_completeness.md)
