# TD-COS-FH-001: the sector process has no finite Markov order

Author: Anonymous · 8 September 2026 · CC0-1.0

Reviewed mathematical edition of [the preserved source note](source_note.md), sections 1–7. Mathematical claims are unchanged; display delimiters are adapted for GitHub. See [AUDIT.md](AUDIT.md) for the fresh review and [README.md](README.md) for all evidence boundaries.

**Result.** For the ideal, unbounded-current TD-COS-FH-001 kernel at J=1, t=1/2, h6=0, on every fixed cubic torus of side L≥2, the stationary sector process has no finite Markov order. This holds when observing every attempted microtick and when observing after each prescribed sweep. More generally it holds at every fixed positive integer spacing d of attempted microticks. It also rules out an exactly time-homogeneous finite-order sector process under any initial full-state distribution, including the eight specified starts and any fixed warmup.

This is an independent analytical deduction from the retrieved specification. It closes the review’s higher-order sector question for these clocks without changing the full-state model, the exact phase results, or any empirical/replay status. The separately packaged numerical checks support the arithmetic; they do not supply the all-orders proof.

## 1. Sources, scope, and the claim being tested

The sources read for this follow-up were:

- [Geometry review — what the last three days add](https://docs.google.com/document/d/11nOlChBSZwKD8xm-mu6uQ-JFVYPdLkSK8nL1_9yJGXk/edit), Drive modification time 2026-09-08T05:27:01.077Z. An older same-title copy also exists; the cited later record was used. Section 2 establishes stationary first-order failure; section 3 gives the separate (q,W) counterexample; section 6 preserves the higher-order distinction.
- [Toroidal Dynamics v0.1, TD-COS-FH-001](https://docs.google.com/document/d/1jDBi4zR7W4fkJ_1F_gKU-RQPfkBgiBllXF5Pw1onP1Q/edit), especially §§1–7: target, labelled periodic cells, proposals, reversibility, reachability, and observation clock. The mathematical result is conditional on that explicitly specified ideal kernel. The linked DYNAMICS.json and an original execution archive were not recovered or replayed in this follow-up.
- [NIST DLMF 10.25.2](https://dlmf.nist.gov/10.25.E2), the positive modified-Bessel series. The asymptotic estimate needed here is derived directly below.
- [Geiger–Temmel, Definitions 5 and 7](https://arxiv.org/html/1212.4375v6), for finite-order and lumpability terminology. Their finite-state entropy theorems are not being imported as a proof for this countable state space.

Let K be the attempted-microtick kernel and B=8L³+7. A prescribed sweep is K^B; it is not a deterministic pass through the move families. Rejections and identity moves advance the clock. For a fixed integer d≥1, define

$$
R=K^d,\qquad Y_n=q(X_{dn}).
$$

Order k means that the exact conditional law of the next sector, given any positive-probability finite sector history of at least k symbols, depends only on its last k symbols. The stationary result excludes every finite k≥1; order zero is consequently excluded too. It concerns the infinite stochastic process defined by ideal probabilities, not the formal memory order of one finite recorded sequence or a deterministic seeded pseudorandom generator.

The full state remains X=(I,M,q), with unbounded integer currents, the two declared constraints, and the positive normalized equilibrium law π. Reversibility makes R self-adjoint on L²(π). Positivity means every individual valid state has strictly positive mass, however small.

## 2. A necessary identity for any finite Markov order

Set b=000, let u=1_{q=b}, and let D multiply functions by u. Define the bounded self-adjoint contraction

$$
A=DRD.
$$

This operator retains paths at their sampled endpoints only when they remain in sector b. For the sweep clock, intermediate microticks may leave b and return. In particular, D K^d D is generally different from (D K D)^d.

In stationarity, the probability of a run of n+1 copies of b is

$$
s_n=P_\pi(Y_0=\cdots=Y_n=b)
=\langle u,A^n u\rangle_\pi.
$$

All s_n are positive because the identity family has positive probability. If Y were stationary of finite order k, then for some c>0,

$$
s_{n+1}=c\,s_n\qquad(n\ge k-1).
$$

The last k observations are the same word b^k, so the continuation probability must eventually be constant. Choose an integer m≥1 large enough that this recurrence applies to s_{2m}, s_{2m+1}, and s_{2m+2}. Self-adjointness gives

$$
\begin{aligned}
\|A^m(A-cI)u\|_\pi^2
&=s_{2m+2}-2c\,s_{2m+1}+c^2s_{2m}\\
&=0.
\end{aligned}
$$

For a bounded self-adjoint operator, ker(A^m)=ker(A) for every m≥1. For example, its spectral representation identifies both kernels with the part supported at eigenvalue zero. This uses neither invertibility nor nonnegative spectrum. Hence

$$
\boxed{A^2u=cAu.}\tag{1}
$$

Because π assigns positive mass to every valid state, this L² identity must hold at every such state. Also Au(x)>0 for every x in sector b, by the d consecutive identity moves. Therefore the function

$$
\mathcal R_d(x)=\frac{A^2u(x)}{Au(x)}
=P_x(Y_2=b\mid Y_1=b),\qquad q(x)=b,
\tag{2}
$$

would have to be the same constant c throughout that sector.

Equation (1) is a necessary consequence of *any* finite order, not a claim that it is sufficient. This is the additional argument missing from a first-order counterexample.

## 3. Valid states that test the identity

For each positive integer N, let x_N have current 2N on every positively oriented stored edge, M=0 and q=000. These are valid labelled states:

- At each vertex, incoming and outgoing currents cancel.
- Every current is even, so the mod-two constraint holds with M=0 and q=000.
- On each axis the signed cut winding is 2NL², consistently across cuts and even.

Every x_N has positive equilibrium mass. No state at “N=infinity” is added to the model; N indexes ordinary finite-current states in its existing support.

In H attempted microticks a given stored edge changes by at most 2H in absolute value. This follows directly from the proposal table and its distinct periodic-edge convention. Thus all states reachable from x_N in H≤2d microticks have

$$
I_\ell=2N+\delta_\ell,\qquad |\delta_\ell|\le4d.
\tag{3}
$$

Fix L and d first, then send N to infinity. All reference-cycle currents stay positive in this finite reachable set. Membranes and sectors can change, but unit-cycle acceptance depends only on the currents on the reference cycle.

## 4. The Bessel estimate, including its nonzero correction

At J=1, write the positive series as

$$
I_n(1)=\frac{1}{2^n n!}S_n,\qquad
S_n=\sum_{j\ge0}\frac{n!}{4^j j!(n+j)!}.
$$

Since n!/(n+j)!≤(n+1)^{-j},

$$
1\le S_n\le \exp\!\left(\frac1{4(n+1)}\right).
$$

It follows that

$$
\frac{I_{n+1}(1)}{I_n(1)}
=\frac1{2(n+1)}\bigl(1+O(n^{-1})\bigr),\qquad
\frac{I_{n-1}(1)}{I_n(1)}
=2n\bigl(1+O(n^{-1})\bigr).
\tag{4}
$$

The estimates are uniform for n=2N+δ with δ in the fixed range (3). Put

$$
\varepsilon_N=(4N)^{-L}>0.
$$

For every state in that reachable set, a unit reference-cycle move in the positive direction has acceptance

$$
\varepsilon_N\bigl(1+O(N^{-1})\bigr),
$$

while its negative-direction inverse has acceptance exactly one for all sufficiently large N. Both signs flip the same sector bit. The proposal probability of each signed axis-specific unit cycle is 1/(2B). Consequently, uniformly over those reachable states and all three axes,

$$
P(q' = q+e_\alpha\mid X)
=\frac{1+\varepsilon_N}{2B}
+O\!\left(\frac{\varepsilon_N}{N}\right).
\tag{5}
$$

Every other proposal preserves q. The membrane acceptance factors therefore do not enter (5). They affect which hidden state is reached, but the estimate already holds uniformly over every reachable hidden state.

Keeping the positive correction ε_N is essential: the leading limit alone would only select a candidate c and would not contradict (1).

## 5. Attempted microticks

Take d=1. Let

$$
h(\varepsilon)=1-\frac{3(1+\varepsilon)}{2B}.
$$

Equation (5) holds initially and at every state reachable after one attempted update. Summing over the first update yields

$$
Au(x_N)=h(\varepsilon_N)+O(\varepsilon_N/N),
$$

$$
A^2u(x_N)=h(\varepsilon_N)^2+O(\varepsilon_N/N).
$$

The denominator is bounded away from zero, so

$$
\boxed{\mathcal R_1(x_N)
=1-\frac3{2B}-\frac3{2B}\varepsilon_N
+o(\varepsilon_N).}\tag{6}
$$

If (1) held, taking N→∞ would force c=1−3/(2B). Dividing the remaining difference by ε_N would then force 0=−3/(2B), a contradiction. Thus the stationary microtick sector process has no finite Markov order for every fixed cubic L≥2.

## 6. Saved sweeps and every other fixed spacing

For ε sufficiently small, define a homogeneous comparison walk on (Z/2)³ by

$$
T_\varepsilon(q,q+e_\alpha)=\frac{1+\varepsilon}{2B},\qquad
T_\varepsilon(q,q)=1-\frac{3(1+\varepsilon)}{2B}.
$$

This comparison walk is used only to evaluate the finite-horizon asymptotic behavior from x_N. It is not asserted to be the exact sector dynamics.

By (5), for the first 2d microticks, each next-sector conditional distribution differs from the corresponding row of T_{ε_N} by O(ε_N/N), uniformly over all full histories reachable from x_N. Iterating these finite conditional probabilities, or telescoping their path laws, bounds the difference of their sector path distributions by O_d(ε_N/N). All implied constants may depend on the fixed L and d; no bound uniform over growing d is claimed.

Write

$$
r_d(\varepsilon)=(T_\varepsilon^d)(b,b).
$$

Translation invariance and the Markov property of the comparison walk give

$$
Au(x_N)=r_d(\varepsilon_N)+O(\varepsilon_N/N),
$$

$$
A^2u(x_N)=r_d(\varepsilon_N)^2+O(\varepsilon_N/N).
\tag{7}
$$

The second expression allows excursions between sampled times. It concerns the event q(X_d)=q(X_{2d})=b, not survival in b at every microtick.

The eight characters of (Z/2)³ diagonalize T_ε. A character supported on j axes has eigenvalue 1−j(1+ε)/B, with multiplicity binomial(3,j). Therefore

$$
r_d(\varepsilon)
=\frac18\sum_{j=0}^3{3\choose j}
\left(1-\frac{j(1+\varepsilon)}B\right)^d,
\tag{8}
$$

$$
r_d'(0)=-\frac{d}{8B}\sum_{j=1}^3{3\choose j}j
\left(1-\frac jB\right)^{d-1}<0.
\tag{9}
$$

Every term in the sum in (9) is positive because B≥71. Also r_d(0)>0. Dividing (7) and expanding the finite polynomial (8) gives

$$
\boxed{\mathcal R_d(x_N)
=r_d(0)+r_d'(0)\varepsilon_N+o(\varepsilon_N).}\tag{10}
$$

If the necessary identity (1) held, its constant would have to be c=r_d(0) by the limit N→∞. But (10), divided by ε_N after subtracting that constant, gives the strictly negative limit r_d'(0). Contradiction.

This proves the result for every fixed positive integer d. In particular choose d=B for the saved sweeps: 71 at L=2, 223 at L=3, and 519 at L=4. Oddness of those sweep lengths is not needed here. The earlier odd-root first-order proof remains valid; this is a separate all-orders proof directly for D K^d D.

## 7. Initial distributions and exact-state conclusions

The specification proves irreducibility, aperiodicity and a normalized positive invariant probability. Thus the full-state distribution converges to π in total variation from every initial distribution; the same is true along each fixed sampling clock. Finite sector-block laws consequently converge to their stationary laws.

Suppose some initial law made the observed sector process an exactly time-homogeneous chain of finite order k, with a fixed k-history transition rule Q. For any finite history w of length at least k and symbol a, every sufficiently late shifted block would satisfy

$$
P(w,a)=P(w)\,Q(\operatorname{suffix}_k(w),a).
$$

Passing to stationary block limits preserves this equality for every positive-probability stationary word. It would make the stationary factor order k, contradicting the theorem. This excludes the specified eight initial states as well as any fixed burn-in. No mixing-time estimate or claim that the prescribed warmup has reached equilibrium is used.

The conclusions now stand as follows:

| Object or status | Disposition |
|---|---|
| q at attempted microticks | No finite stationary Markov order; no homogeneous finite-order law from another initialization |
| q at prescribed saved sweeps | Same result, including L=2,3,4 |
| q at any other fixed integer spacing d | Same result for the ideal kernel |
| Full X=(I,M,q) | Still the specified exact Markov state |
| A finite window of sector observations | Cannot supply an exact autonomous sector transition law |
| (q,W) | Earlier L=2 one-step counterexample remains; no higher-order theorem for this augmented observation is asserted here |
| Exact phase model and its algebra | Preserved; this proof concerns the stochastic toroidal kernel |
| Finite-current boxes, accepted-move clocks, adaptive sampling | Outside this theorem; they change the support, kernel or observation rule |
| Historical deterministic mismatch | Remains unresolved by this mathematical result |
| Production authorization and physical Q2 | No status upgrade: NOT_AUTHORIZED and physical Q2 NOT_RUN remain in force where recorded |

The argument uses positive-mass states whose equilibrium weights can be extremely small. It does not quantify typical predictive error, detectable correlation, practical memory length, entropy rate, or mixing time. The supplementary return values describe the large-current comparison limit; they are not equilibrium sector probabilities, observed correlations, or simulation estimates.
