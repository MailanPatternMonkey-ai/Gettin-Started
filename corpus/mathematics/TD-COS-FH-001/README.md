# TD-COS-FH-001: no finite Markov order for the sector process

Author: Anonymous · 8 September 2026 · CC0-1.0

**Analytical result for a specified ideal stochastic kernel.** At cosine
weights $J=1$, $t=1/2$, $h_6=0$, in the fixed-reference $Z_{000}$ ensemble
with unbounded integer currents, on every fixed cubic torus of side
$L\ge2$, the stationary sector process $q(X_{dn})$ has no finite Markov
order for every fixed integer $d\ge1$. Here $X=(I,M,q)$ is the full state
and one attempted microtick applies the kernel $K$.

This includes microticks ($d=1$) and prescribed sweeps
($d=B=8L^3+7$, hence 71, 223 and 519 for $L=2,3,4$). Rejections and
identity moves advance this clock. A sweep is $K^B$, not one compulsory
pass through every move family. Equilibrium convergence also excludes an
**exactly time-homogeneous** finite-order sector law from any initial
full-state distribution, including the eight specified starts and any
fixed warmup. Time-inhomogeneous finite-order laws are not settled here.

The [proof](PROOF.md) derives a necessary identity for *any* finite order,
$A^2u=cAu$ with $A=DK^dD$ and $u=\mathbf1_{q=000}$. Positive-mass,
uniform-current states contradict that identity through a nonzero
Bessel-tail correction. This is an all-orders analytical argument;
finite computations below check supporting arithmetic.

## Evidence boundary

| Object or claim | Status after this update |
|---|---|
| Sector-only process, specified kernel and fixed clocks | No finite stationary Markov order; no time-homogeneous finite-order law under another initialization |
| Full $X=(I,M,q)$ | Remains the specified exact Markov state; no minimality claim |
| Causal conditional distribution over full states | Remains a sufficient predictive state for sector observations; no finite-dimensional representation is established |
| Augmented observation $(q,W)$ | Earlier $L=2$ one-step counterexample preserved; higher-order question for this observation is not settled |
| Exact phase constructions and algebra | Preserved; this theorem does not invalidate or physically validate them |
| Historical deterministic mismatch | UNRESOLVED; no original sampler replay is claimed |
| Production authorization | NOT_AUTHORIZED; this mathematical publication supplies no authorization |
| Physical Q2 | NOT_RUN |
| Global shape, unobserved connectivity, global holonomy, hidden platform geometry | UNRESOLVED / NOT_ESTABLISHED by this result |
| Chemistry-controlled comparisons | No change to the chemistry freeze, pairing requirements or empirical claims |

Irreducibility concerns the explicitly defined full-state mathematical
kernel. It is not evidence for connectivity of an empirical space or a
hidden system. The torus and reference cycles are model inputs; this
proof does not infer physical toroidal shape or path-independent holonomy.

The theorem does not cover finite-current boxes, altered or Villain
weights, accepted-move clocks, adaptive sampling, physical-time dynamics,
or other models. It supplies no mixing time, typical prediction error,
practical memory length, equilibrium correlation magnitude, finite-size
scaling result, or proof that every finite-dimensional sufficient statistic
or finite latent-state representation is impossible. A finite recorded
sequence and a seeded pseudorandom implementation are not the ideal
infinite stochastic process of the theorem.

## Sources and verification

- [PROOF.md](PROOF.md): reviewed mathematical edition, with GitHub math formatting.
- [AUDIT.md](AUDIT.md): proof audit, recovery details and verification limits.
- [source_note.md](source_note.md): byte-preserved complete earlier Markdown record.
- [sources/drive_note_snapshot.txt](sources/drive_note_snapshot.txt): current readable Drive snapshot, ending mid-verifier.
- [sources/kernel_snapshot.txt](sources/kernel_snapshot.txt): retrieved kernel specification, with historical statuses and unresolved source pointers retained.
- [sources/review_math_excerpt.md](sources/review_math_excerpt.md): only the preceding review's relevant mathematical sections, 2–3.
- [verify.py](verify.py): recovered original verifier, matching its declared SHA-256.
- [verification_original.json](verification_original.json): extracted historical embedded output.
- [verification_fresh.json](verification_fresh.json): newly executed output; byte-identical to the embedded output.
- [verify_certificates.py](verify_certificates.py) and [certificates.json](certificates.json): newly written independent finite rational certificates.
- [provenance.json](provenance.json): source identities, transformations, hashes, execution receipt and preserved statuses.

Run from this directory with Python 3 and its standard library:

```bash
python3 verify.py > /tmp/td-cos-fh-001-verification.json
cmp verification_original.json /tmp/td-cos-fh-001-verification.json
python3 verify_certificates.py > /tmp/td-cos-fh-001-certificates.json
cmp certificates.json /tmp/td-cos-fh-001-certificates.json
```

Run without Python's `-O` option, because the checkers use assertions.
The recovered verifier reports six exact clock comparisons and three
70-digit Decimal local checks. The new verifier reports nine exact clock
comparisons, including even spacing 2, and outward rational enclosures
for three local witnesses. These programs do not execute a Monte Carlo
sampler or a physical experiment. Identical supplementary output does
not establish the provenance or conformance of the historical sampler.

The separate remaining mathematical target is a sufficient reduced state
for the full kernel, or a quantitative approximation bound for the causal
filter under a declared law and error criterion. No such bound is supplied
by this obstruction.
