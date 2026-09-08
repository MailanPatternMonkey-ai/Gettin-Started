# Earlier mathematical review: sections 2–3 only

CC0-1.0. Explicit excerpt from the September 8 review, retained as historical context.
Its statement that higher order remains open predates the separate all-orders theorem.
The introduction and sections 1, 4–6 are omitted; nothing below is a fresh execution claim.

**2. The “weak lumpability under equilibrium is open” entry can be strengthened.**
This is a deduction made in this review from the specified kernel, not a newly discovered simulation result.
The [Toroidal Dynamics specification, §§1, 3–5](https://docs.google.com/document/d/1jDBi4zR7W4fkJ_1F_gKU-RQPfkBgiBllXF5Pw1onP1Q/edit) gives a normalizable, positive target on a countable state space and a reversible attempted-microtick kernel \(K\). Use the cosine model TD-COS-FH-001, \(J=1\), \(t=1/2\), \(h_6=0\), fixed-reference \(Z_{000}\), and unbounded currents.
For a reference cycle with currents \(a_1,\ldots,a_L\), the probability of flipping its sector bit at one microtick is
\[
p_\alpha(X)=\frac1{2B}\sum_{s=\pm1}
\min\!\left(1,\prod_{j=1}^L
\frac{I_{|a_j+s|}(1)}{I_{|a_j|}(1)}\right),
\qquad B=8L^3+7.
\]
Independent rational Bessel enclosures reproduce the pasted L=2 witness:
| State, both with \(M=0,q=000\) | Reference x currents | \(W\) | Next-\(q=e_x\) probability |
|---|---|---|---:|
| \(I=0\) | (0,0) | (0,0,0) | 0.00280653523455 |
| \(I=2\Gamma_x\) | (2,2) | (2,0,0) | 0.00723006259189 |
Now set \(Y_n=q(X_n)\), \(b=000\), \(a=e_x\), and \(p(X)=K(X,q^{-1}\{a\})\). In stationarity, reversibility and conditional independence of past and future given \(X_0\) yield
\[
\operatorname{Cov}\!\left(
\mathbf1_{\{Y_{-1}=a\}},
\mathbf1_{\{Y_1=a\}}\mid Y_0=b
\right)
=\operatorname{Var}_\pi(p(X_0)\mid Y_0=b)>0.
\]
Both witness states have positive equilibrium mass and different \(p\), so the variance is strictly positive. A first-order Markov process would make that conditional covariance zero. Therefore the stationary sector process is not first-order Markov.
This argument works directly on the countable state space; it needs no finite-current truncation and no estimate of the equilibrium mixture. The related finite-chain result is [Kemeny–Snell, Theorem 6.4.8](https://www.math.pku.edu.cn/teachers/yaoy/Fall2011/Kemeny-Snell_Chapter6.3-4.pdf). The proof above supplies the countable-state application.
The kernel is irreducible, aperiodic and positive recurrent. Consequently no other initial distribution can make the sector process a time-homogeneous first-order Markov chain either: if one did, taking its late-time three-symbol distributions to equilibrium would give a stationary Markov factor, contradicting the displayed identity. This applies to the specified eight Dirac starts as well.
**The saved sweep clock can also be addressed.** A sweep is \(K^{71}\) at L=2. Let \(H\) be the closed subspace of square-integrable functions depending only on \(q\). Strong lumpability is \(K H\subseteq H\). If \(K^{71}H\subseteq H\), self-adjointness makes \(H\) reducing for \(K^{71}\). The continuous real odd-root function recovers \(K\) from \(K^{71}\) by functional calculus, forcing \(K H\subseteq H\), a contradiction. Thus the failure persists at fixed 71-microtick sweeps. The stationary covariance argument then applies to the sweep kernel too.
The same numerical witness is separated at L=3 and L=4, and their prescribed sweep lengths 223 and 519 are also odd:
| L | Attempts per sweep | \(p_x(I=0)\) | \(p_x(I=2\Gamma_x)\) |
|---:|---:|---:|---:|
| 2 | 71 | 0.002806535235 | 0.007230062592 |
| 3 | 223 | 0.000398876461 | 0.002251917472 |
| 4 | 519 | 0.000076505091 | 0.000964076329 |
This does not establish failure of every finite Markov order. The higher-order sector question still needs its own argument.
**3. Retaining winding is useful, but it is not a complete repair.**
On the L=2 torus, compare \(I=0\) with \(I=2\partial P_{xy}\), where the face is based at the origin. The latter has currents +2 on the x edge at (0,0,0), +2 on the y edge at (1,0,0), −2 on the x edge at (0,1,0), and −2 on the y edge at (0,0,0).
Both states have \(M=0\), divergence zero, even currents, \(q=000\), and \(W=(0,0,0)\). The second state's reference x cycle has currents (2,0), giving
\[
p_x(0)=0.00280653523455,\qquad
p_x(2\partial P_{xy})=0.00755562121318.
\]
Thus even \((q,W)\) merges states with different next-sector laws. I checked the periodic edge identities, divergence, both cuts on every axis, and acceptance bounds independently. This is an exact counterexample with decimal displays, not a sampling discrepancy.
For present one-step prediction, the reference-cycle current lists determine the cycle acceptances. Making those lists into an autonomous state for the full kernel is a further problem: plaquette updates couple them to surrounding currents and membranes. The safe exact state remains the specified full state, or a causally updated conditional distribution over it when only sector observations are available.
The original two-state witness also forces a worst-case total-variation error of at least 0.002211763679 for any single q-only microtick law at q=000, approximately 0.2212 percentage points. This is a worst-case bound, not an average predictive error or a claim about the size of observed correlations.
