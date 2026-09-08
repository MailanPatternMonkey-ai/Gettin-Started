# Proof and reproduction audit

Author: Anonymous · 8 September 2026 · CC0-1.0

**Disposition: the analytical claim survives review under its stated
ideal-kernel hypotheses.** No mathematical correction to the all-orders
argument was needed. The publication repair recovers the missing code,
separates fresh execution from historical evidence, and makes the claim's
scope explicit. This is a mathematical review with finite supporting
checks, not a machine-checked formal proof.

## Proof obligations checked

| Obligation | Audit finding |
|---|---|
| State space and target | Integer divergence-free currents, binary membranes and three binary sector bits with the declared parity constraint. On a fixed finite lattice the target is normalizable and every valid state has positive mass. |
| Kernel and clock | The seven proposal weights sum to $B=8L^3+7$. Each signed axis-specific unit cycle has probability $1/(2B)$. Only accepted unit cycles change $q$. The self-loop from the identity family is at least $L^3/B$. |
| Reversibility | Symmetric inverse descriptors and Metropolis acceptance give detailed balance for the ideal probabilities. Hence $K^d$ and $A=DK^dD$ are bounded self-adjoint operators on $L^2(\pi)$. |
| All-orders implication | Finite stationary order makes continuation of the constant word eventually constant, $s_{n+1}=cs_n$. For sufficiently large $m$, the resulting norm $\|A^m(A-cI)u\|^2$ vanishes. The spectral theorem gives $\ker A^m=\ker A$; therefore $A^2u=cAu$. No invertibility, positive spectrum, or finite-state entropy theorem is assumed. |
| Pointwise use of the identity | Every valid state is an atom of positive equilibrium mass. An $L^2(\pi)$ equality therefore holds at each such state. $Au$ is positive on the retained sector because $d$ consecutive identity moves have positive probability. |
| Witness validity | $I_e=2N$, $M=0$, $q=000$ has zero divergence and satisfies parity. Its cut windings are $2NL^2$, even on every cut. These are ordinary finite-current states, not a newly added state at infinity. |
| Reachable-state bound | Fix $L$ and $d$ before increasing $N$. Every stored edge changes by at most 2 per microtick, so offsets over $2d$ steps are bounded by $4d$. The distinct periodic-bond convention is essential at $L=2$. |
| Bessel correction | The positive series gives $1\le S_n\le\exp[1/(4(n+1))]$. Upward unit-cycle acceptance is $(4N)^{-L}(1+O(N^{-1}))$ uniformly over the finite reachable set; downward acceptance is exactly 1 for sufficiently large $N$. The coefficient of the positive correction must be retained. |
| Hidden-state dependence | Other moves can change currents and membranes, but the next-sector estimate is uniform over all reachable full histories. For fixed $d$, the sector path-law error is $O_d(\varepsilon_N/N)$ over the first $2d$ microticks. No uniform assertion for growing $d$ is used. |
| Saved endpoints | $DK^dD$ allows intermediate excursions and returns. Replacing it by $(DKD)^d$ would change the event and invalidate the sweep argument; the proof does not make that substitution. |
| Nonconstant ratio | Character diagonalization of the comparison walk gives $r_d'(0)<0$ for every fixed $d\ge1$, since $B\ge71$. Thus $A^2u(x_N)/Au(x_N)=r_d(0)+r_d'(0)\varepsilon_N+o(\varepsilon_N)$ cannot be constant in $N$. |
| Initial-law corollary | The specified irreducible, aperiodic, positive recurrent countable chain converges in total variation. A fixed finite-history transition rule from any initial law would pass to stationary finite-block limits and contradict the theorem. This needs time homogeneity; it provides no warmup adequacy or mixing-time estimate. |

The supporting Bessel definition was checked against
[NIST DLMF 10.25.2](https://dlmf.nist.gov/10.25.E2).
[Geiger–Temmel](https://arxiv.org/html/1212.4375v6) is a terminology source;
its finite-state entropy results are not used to prove a countable-state
claim. The asymptotic and killed-operator arguments are supplied in
[PROOF.md](PROOF.md).

## Recovery and provenance

The readable native Drive note ends at `assert a` inside its Python block.
The complete earlier file `TD-COS-FH-001_No_Finite_Markov_Order.md`, created
at 2026-09-08T05:50:04.005771Z, contains the remaining verifier and output.
It is preserved byte for byte as `source_note.md` (25,675 bytes).

After removal of whitespace, the retrieved Drive text is a prefix of
that complete copy. This comparison is deliberately weaker than byte
identity: it supports recovery of the missing continuation while
preserving their distinct origins. The publication does not silently
replace or edit the Drive document.

Extracting the fenced Python block with one terminal LF produces
SHA-256 `96c2d72c9e1e0de55e86392cc1f2546633d4a076f5f580e7408990aa13166e8f`.
Extracting the embedded output JSON with one terminal LF produces
`25ea6e583f75ac5dafcd88761e1f4499d91fbe20f273613db5f682a00c9eb48a`.
Both match the hashes declared in the note. Fresh execution reproduces
the latter hash exactly.

This establishes the recovered supplementary code/output identity and a
fresh execution result. The old review/specification snapshot hashes in
the source note remain historical declarations: this update records new
readable-snapshot hashes and does not claim to have recovered those
original snapshot bytes. It also does not recover `DYNAMICS.json`, an
original sampler archive, its complete configuration, or its execution
provenance. The historical deterministic mismatch remains unresolved.

The preceding review contains material beyond this theorem. Only its
mathematical sections 2–3 are included as an explicitly identified
excerpt; its broader application discussion and local-machine paths are
omitted. Kernel-snapshot relative links are preserved source pointers,
not claims that their targets are present in this package.

## Fresh finite checks

| Check | Result | What it supports |
|---|---|---|
| Recovered verifier | PASS: six exact character/convolution comparisons and three Decimal local checks; output byte-identical | Recovery and reproducibility of the supplementary arithmetic |
| New clock certificates | PASS: exact integer path counts and their derivatives agree with the character formula for $L=2,3,4$, each at $d=1,2,B$ | Nine finite arithmetic certificates, including an even clock |
| New local certificates | PASS: 123 descriptors at each of three $L=2$ uniform-current states, $N=10,100,1000$ | Exact proposal normalization, candidate divergence/parity/all-cut consistency, and inverse current changes |
| Local return ratios | PASS: three pairwise-disjoint rational intervals; each scaled correction is strictly negative | A finite certified demonstration that the microtick ratio is nonconstant |
| Comparison with recovered Decimal values | PASS: every reported $A1$, $A2/A1$, and scaled correction lies inside its fresh rational enclosure | The numerical illustrations agree with independent certified bounds |

The new checker is independently written and does not import `verify.py`.
It uses the positive Bessel series through term 24 with a rational
geometric upper bound on the remaining tail. Interval operations round
outward to a rational grid of denominator $10^{60}$; that rounding is
included in the enclosure. JSON rational endpoints are authoritative;
floating-point midpoint/width displays are informational.

For the local two-step calculation, all seven proposal families are
enumerated at the first step. Only unit-cycle acceptance enters the next
sector-survival probability; it depends on currents, not membranes.
Thus cube and sheet outcomes can share the same continuation value even
though their full states differ. Accepted unit cycles are removed at the
intermediate sampled endpoint. This is an exact reduction for this local
calculation, not an asserted autonomous current or sector dynamics.

No finite check proves the universal quantifiers over $L$, $d$, or Markov
order. The new certificates do not validate sampler implementation,
equilibrium coverage, production mixing, physical Q2, empirical global
geometry, or chemistry claims. The older one-step $(q,W)$ result is
preserved with its original scope; no higher-order result for $(q,W)$ is
introduced.
