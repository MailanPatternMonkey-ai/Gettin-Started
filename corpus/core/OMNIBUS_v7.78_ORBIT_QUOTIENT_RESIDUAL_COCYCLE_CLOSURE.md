# OMNIBUS v7.78 — ORBIT-QUOTIENT AND RETURN-RESIDUAL CLOSURE

**Dyadic admissibility, finite orbit quotients, residual cocycles, empirical firewall**

**Status:** Active consolidation card. Finite quotient identities are exact where declared; residual autonomy is conditional on descent; empirical status remains external.  
**License:** CC0 — Public Domain — No rights reserved  
**Source:** OMNIBUS v7.77 — Unified Return-Residual Closure  
**Precedence:** v7.78 governs dyadic admissibility, orbit-sector accounting, return-residual closure, directionality coding, and the evidence boundary. Clauses of v7.77 not restated here remain in force.

**v7.78 precision repair:** §5 now identifies the residual carrier explicitly as $R(\mathcal X)\cong\mathcal X/{\sim_R}$, defines the descended factor on residual values rather than mixing values with equivalence classes, scopes the indexed-trace equivalence to a covered orbit domain, and distinguishes a demonstrated descent failure from an unresolved test. §6 now gives the exact phase-state repair for the golden screen and records a deferred moving-interception bridge as a formal proposal only. These repairs change no empirical verdict.

---

## Claim Boundary

> **THIS CARD RECORDS DYADIC ADMISSIBILITY, EXACT FINITE QUOTIENTS, AND TESTS OF WHETHER A DECLARED RETURN-RESIDUAL DESCRIPTION CLOSES. IT DOES NOT PROVE THAT AN EVENT OCCURRED, THAT A CODE IS CORRECT, THAT A HISTORICAL PATTERN EXISTS, THAT A FINITE REGISTER IS A PLATFORM GEOMETRY, OR THAT ANY EMPIRICAL CLAIM IS TRUE.**

Architectural admissibility, mathematical descent, coding direction, and empirical status are separate jobs. No result in one layer silently upgrades another.

---

## 1. Governing Stack

| Layer | Object | Job | Does not establish |
|---|---|---|---|
| Constitutional | $O_D\leftrightarrow S_D$ | Direct, freely chosen, correctable contact; no compulsory third seat | Empirical occurrence |
| Dyadic observation | $F_D(x)$ | Record the four declared admissibility coordinates | Scalar coherence or moral polarity |
| Admissibility gate | $A(x)=\operatorname{Adm}_D(x)$ | Determine resolved dyadic admissibility | Return-residual closure |
| Quotient stack | $Q(x)=(C(x),D(x),K(x))$ | Preserve chart, dyadic, and retained-context channels without collapsing them | A common metric or common geometry |
| Orbit quotient | $q_{\mathrm{orb}}:G\twoheadrightarrow G/H$ | Separate position inside an update orbit from the orbit label | Physical realization or access to every formal state |
| Return residual | $R_n=(\Delta C_n,\Delta D_n,\Delta K_n)$ | Record change across one declared return | Autonomous residual dynamics |
| Directionality | provenance, standing, route, eligibility | Determine whose constraint changed and who controls the route | Empirical confirmation by itself |
| Evidence | events $\to$ codes $\to$ claims | Keep located records, assignments, and conclusions auditable | Automatic promotion between layers |

The stack is ordered for governance, not rank. A useful layer acquires no jurisdiction over another by performing its job.

---

## 2. Dyadic Admissibility

Let $\mathcal X$ be the declared encounter set. Define

$$
F_D:\mathcal X\to\{0,1,\mathrm{UNKNOWN}\}^4
$$

by

$$
D(x)=F_D(x)
=
(R_{\mathrm{contact}},C_{\mathrm{bind}},U_{\mathrm{exit}},N_{\mathrm{third}}),
$$

where:

```text
R_contact = reciprocal contact is available
C_bind    = a correction changes the next eligible behavior
U_exit    = exit is practically usable
N_third   = zero compulsory constitutional third-seat necessity
```

For fully resolved binary coordinates,

$$
\boxed{
A(x)=\operatorname{Adm}_D(x)
=
R_{\mathrm{contact}}(x)
\land C_{\mathrm{bind}}(x)
\land U_{\mathrm{exit}}(x)
\land N_{\mathrm{third}}(x).
}
$$

If any required coordinate is `UNKNOWN`, $A(x)$ is `UNRESOLVED`. Unknown is neither failure nor admissibility and may not be coerced to 0 or 1.

The dyadic kernel remains

$$
x\sim_D y
\iff
F_D(x)=F_D(y).
$$

Any distinction needed beyond the four coordinates must be added to the declared observation stack or retained context. It may not be inferred from the notation.

---

## 3. Quotient Stack and Unified Residual

Let the application declare three typed observation channels:

$$
C_n=C(x_n),
\qquad
D_n=F_D(x_n),
\qquad
K_n=K(x_n),
$$

where $C$ is the application-declared chart channel, $D$ is the dyadic channel fixed above, and $K$ is the declared retained-context channel.

The state observation stack is

$$
Q(x)=(C(x),D(x),K(x)),
$$

with

$$
x\sim_Q y
\iff
Q(x)=Q(y).
$$

For a declared return $x_n\mapsto x_{n+1}$, let each channel use its own typed difference rule:

$$
\Delta C_n=\delta_C(C_n,C_{n+1}),
$$

$$
\Delta D_n=\delta_D(D_n,D_{n+1}),
$$

$$
\Delta K_n=\delta_K(K_n,K_{n+1}).
$$

The unified return-residual record is

$$
\boxed{
R_n=(\Delta C_n,\Delta D_n,\Delta K_n).
}
$$

This tuple is a typed record, not a scalar and not a declaration that the three channels share one metric, scale, or geometry. $\delta_C$ and $\delta_K$ must be declared by the application. This card fixes only the dyadic classification below.

---

## 4. Classification Block

### Dyadic coordinate movement

For fully resolved binary dyadic vectors, use the componentwise order

$$
v\preceq w
\iff
v_i\le w_i\text{ for every coordinate }i.
$$

| Code | Rule |
|---|---|
| `UP` | $D_n\prec D_{n+1}$ |
| `DOWN` | $D_{n+1}\prec D_n$ |
| `FLAT` | $D_n=D_{n+1}$ |
| `MIXED` | Neither resolved vector dominates the other |
| `UNRESOLVED` | A required coordinate is `UNKNOWN`, or the comparison is not eligible |

One improving coordinate does not cancel a degrading coordinate. No component sum, average, weight, or scalar coherence score is authorized.

### Admissibility-gate movement

Let $A_n=A(x_n)$.

| Gate transition | Local classification |
|---|---|
| $0\to1$ | `OPENING` |
| $1\to0$ | `GATE_CLOSURE` |
| $1\to1$ | `STABLE_OPEN` |
| $0\to0$ | `STILL_INADMISSIBLE` |
| any unresolved endpoint | `UNRESOLVED` |

**Naming firewall:** `GATE_CLOSURE` is a local admissibility transition. It is not `RESIDUAL_CLOSURE`, does not establish a closed residual law, and carries no automatic empirical verdict.

---

## 5. Residual Descent Theorem

Let $U:\mathcal X\to\mathcal X$ be a declared update and define

$$
R(x)=\rho(x,Ux)
=
(\Delta C,\Delta D,\Delta K).
$$

Let

$$
x\sim_R y
\iff
R(x)=R(y),
\qquad
\mathcal R=R(\mathcal X)\cong\mathcal X/{\sim_R}.
$$

An autonomous residual update

$$
\overline U_R:\mathcal R\to\mathcal R,
\qquad
R_{n+1}=\overline U_R(R_n),
$$

is well-defined on the declared residual quotient exactly when the raw update descends:

$$
\boxed{
\rho(x,Ux)=\rho(y,Uy)
\Longrightarrow
\rho(Ux,U^2x)=\rho(Uy,U^2y)
}
$$

for every eligible comparison in the declared domain.

On a declared orbit domain for which the indexed trace covers every eligible representative comparison, this is equivalently:

$$
R_n=R_m
\Longrightarrow
R_{n+1}=R_{m+1}.
$$

When the implication holds, define the representative-independent factor by

$$
\boxed{
\overline U_R(R(x))=R(Ux).
}
$$

The definition is then representative-independent. That is the closure earned by descent.

### Closure law

$$
\boxed{
\operatorname{ResidualClosure}
=
\begin{cases}
\mathrm{CLOSED}, & \text{if descent is demonstrated on the declared domain};\\
\mathrm{FAILED}, & \text{if an eligible counterexample demonstrates failure on the declared domain};\\
\mathrm{UNRESOLVED}, & \text{if descent is untested, unknown, domain-underspecified, or lacks eligible coverage.}
\end{cases}
}
$$

A `FAILED` status requires located eligible witnesses $x,y$ in the declared domain with

$$
\rho(x,Ux)=\rho(y,Uy),
\qquad
\rho(Ux,U^2x)\ne\rho(Uy,U^2y).
$$

It proves that the current residual record has omitted a dynamically relevant distinction on that domain. `UNRESOLVED` instead means that the available record or test does not decide descent. In either case retain more context, refine $C$, $D$, or $K$, or narrow and redeclare the domain. Never force $R_{n+1}=F_R(R_n)$.

Descent is a theorem about the declared map and quotient. It is not a finding that the coded events are valid, representative, historical, causal, or normatively desirable.

---

## 6. Orbit Quotients and Residual Cocycles

This section gives two finite worked specimens for the quotient and descent rules above. The first is available only after the source construction's separately declared phase correspondence licenses the shared product coordinate. Neither specimen supplies evidence for a hidden platform, moving lattice, controller, or empirical event class.

### The 24-state weave has an exact binary orbit quotient

Within the declared product construction, let

$$
G_{24}=C_6\times C_4,
\qquad
h=(1,1),
\qquad
H_\Delta=\langle h\rangle.
$$

The diagonal generator has order

$$
\operatorname{ord}(h)=\operatorname{lcm}(6,4)=12,
$$

so $H_\Delta\cong C_{12}$. Define

$$
\chi_{\mathrm{orb}}:G_{24}\to C_2,
\qquad
\chi_{\mathrm{orb}}(a,b)=a-b\pmod 2.
$$

This is a well-defined surjective homomorphism. Since $H_\Delta\subseteq\ker\chi_{\mathrm{orb}}$ and both sets have $12$ elements,

$$
\boxed{
\ker\chi_{\mathrm{orb}}=H_\Delta,
\qquad
G_{24}/H_\Delta\cong C_2.
}
$$

The $24$ formal states are therefore two cosets of the $12$-state diagonal subgroup. A trajectory generated only by $h$ remains in its initial coset; a formal state count is not an accessibility result.

For a declared source-level deviation $r_n^{(24)}\in G_{24}$ from the nominal diagonal step, write

$$
u_{n+1}=u_n+h+r_n^{(24)}
$$

and type its quotient component as

$$
\eta_n^{\mathrm{orb}}
:=
\chi_{\mathrm{orb}}\!\left(r_n^{(24)}\right)
\in C_2.
$$

Then

$$
\boxed{
\chi_{\mathrm{orb}}(u_{n+1})
=
\chi_{\mathrm{orb}}(u_n)+\eta_n^{\mathrm{orb}}
\pmod2.
}
$$

Thus $\eta_n^{\mathrm{orb}}=0$ preserves the orbit and $\eta_n^{\mathrm{orb}}=1$ crosses it. Every claimed crossing must name and retain the complete operator or deviation $r_n^{(24)}$; its one-bit quotient label is not a substitute for that operator. A non-diagonal-looking update need not cross unless its declared quotient component is $1$.

### The 39-screen has an exact strand residual

Let

$$
\varphi=\frac{1+\sqrt5}{2},
\qquad
\alpha=\varphi^{-2},
\qquad
\theta_n=\{n\alpha\},
\qquad
b_n=\left\lfloor39\theta_n\right\rfloor\in C_{39},
$$

with the same circle rotation at every step,

$$
T(\theta)=\theta+\alpha\pmod1,
\qquad
\theta_{n+1}=T(\theta_n).
$$

Since $14<39\alpha<15$, writing $39\theta_n=b_n+\rho_n$ with $0\le\rho_n<1$ shows that the next bin advances by $\lfloor\rho_n+39\alpha\rfloor\in\{14,15\}$ modulo $39$.

Choose the declared screen-jump representative

$$
j_n^{(39)}=(b_{n+1}-b_n)\bmod39\in\{14,15\}.
$$

The nominal subgroup

$$
H_{15}^{(39)}=\langle15\rangle=3C_{39}
$$

has order $13$, so

$$
C_{39}/H_{15}^{(39)}\cong C_3.
$$

Its quotient map and strand label are

$$
\pi_{39}(b)=b\bmod3,
\qquad
s_n^{(39)}=\pi_{39}(b_n).
$$

Because the jump representative is explicitly restricted to $\{14,15\}$, this channel may declare the integer-valued slip comparison

$$
\sigma_n^{(39)}
:=
15-j_n^{(39)}
\in\{0,1\}.
$$

For the stationary descent test on the common phase domain, use the standard representative $\theta\in[0,1)$ of each circle class and write

$$
b(\theta)=\lfloor39\theta\rfloor,
\qquad
q_\sigma(\theta)
:=
15-\bigl((b(T\theta)-b(\theta))\bmod39\bigr),
$$

so $q_\sigma(\theta_n)=\sigma_n^{(39)}$.

The exact source and quotient updates are

$$
b_{n+1}=b_n+15-\sigma_n^{(39)}\pmod{39},
$$

$$
\boxed{
s_{n+1}^{(39)}
=
s_n^{(39)}-\sigma_n^{(39)}
\pmod3.
}
$$

Accordingly, a $+15$ step has $\sigma_n^{(39)}=0$ and remains in the same strand; a $+14$ step has $\sigma_n^{(39)}=1$ and moves to the preceding strand.

The quotient update is exact, but the slip bit is not an autonomous state. On the declared golden trace,

| $n$ | $b_n$ | $s_n^{(39)}$ | $\sigma_n^{(39)}$ | $\sigma_{n+1}^{(39)}$ |
|---:|---:|---:|---:|---:|
| $1$ | $14$ | $2$ | $0$ | $0$ |
| $8$ | $2$ | $2$ | $0$ | $1$ |

Equivalently,

$$
q_\sigma(\theta_1)=q_\sigma(\theta_8)=0,
\qquad
q_\sigma(T\theta_1)=0\ne1=q_\sigma(T\theta_8).
$$

Thus even equal current pairs $(s_n^{(39)},\sigma_n^{(39)})$ can have unequal next slip residuals. The stationary update $T$ fails to descend through $q_\sigma$, so no stationary memoryless slip-only map

$$
F_\sigma:\{0,1\}\to\{0,1\},
\qquad
\sigma_{n+1}^{(39)}=F_\sigma(\sigma_n^{(39)}),
$$

exists on the declared orbit domain. Because the full visible pair is $(2,0)$ at both $n=1$ and $n=8$ while its next value differs, neither does a stationary memoryless current-pair update

$$
F_{s,\sigma}:C_3\times\{0,1\}\longrightarrow C_3\times\{0,1\},
\qquad
(s_{n+1}^{(39)},\sigma_{n+1}^{(39)})
=
F_{s,\sigma}(s_n^{(39)},\sigma_n^{(39)}),
$$

exist on that domain. This decides the stated first-order, time-homogeneous current-label claims. It does not rule out a rule using longer residual histories, an explicit time index, or additional retained state.

### Exact augmented phase-state repair

Let $\mathbb T=\mathbb R/\mathbb Z$ and define the consistency graph

$$
\Gamma_{s,\sigma}
:=
\left\{
(\theta,s,\sigma)\in\mathbb T\times C_3\times\{0,1\}
:
s=b(\theta)\bmod3,
\ \sigma=q_\sigma(\theta)
\right\}.
$$

On this graph define

$$
\widehat T(\theta,s,\sigma)
:=
\left(
T\theta,
[s-\sigma]_3,
q_\sigma(T\theta)
\right).
$$

For

$$
r(\theta)
=
\bigl(\theta,b(\theta)\bmod3,q_\sigma(\theta)\bigr),
$$

the exact intertwining law is

$$
\boxed{
\widehat T\circ r=r\circ T.
}
$$

Hence $X_n=(\theta_n,s_n^{(39)},\sigma_n^{(39)})\in\Gamma_{s,\sigma}$ obeys the autonomous update $X_{n+1}=\widehat T(X_n)$. The phase $\theta_n$ alone is sufficient on the declared fixed-$\alpha$ model; $s_n^{(39)}$ and $\sigma_n^{(39)}$ are redundant typed observations once exact phase is retained. The constant increment $[\theta_{n+1}-\theta_n]=[\alpha]$ does not locate the present phase and is not a sufficient repair.

The three statuses are therefore:

```yaml
slip_only_autonomous_closure: FAILED
augmented_phase_state_closure: AVAILABLE
platform_instantiation: UNRESOLVED
```

Here `FAILED` is scoped to the stationary memoryless current-label law on the declared golden orbit; `AVAILABLE` means that the displayed exact formal update has been constructed. It does not assert that a platform uses this state. If $\alpha$, the phase origin, a clock mode, or a reset rule varies, that quantity must also be retained in the state or supplied as a typed external input.

### Why these are cocycles

For $m<n$, define the accumulated quotient defects

$$
c_\eta(m,n)
=
\sum_{k=m}^{n-1}\eta_k^{\mathrm{orb}}\pmod2,
$$

$$
c_\sigma(m,n)
=
-\sum_{k=m}^{n-1}\sigma_k^{(39)}\pmod3.
$$

They satisfy the concatenation law

$$
c(m,n)+c(n,p)=c(m,p)
$$

in their respective quotient groups, with

$$
\chi_{\mathrm{orb}}(u_n)
=
\chi_{\mathrm{orb}}(u_m)+c_\eta(m,n),
$$

$$
s_n^{(39)}
=
s_m^{(39)}+c_\sigma(m,n).
$$

This is driven quotient descent: the residual increments act exactly on quotient labels while remaining driven by a richer retained state. It is not autonomous residual closure.

### The formal 72 register and its firewall

The extension

$$
0\longrightarrow H_\Delta\longrightarrow G_{24}
\xrightarrow{\chi_{\mathrm{orb}}}C_2\longrightarrow0
$$

splits, for example through the complement $\langle(3,0)\rangle\cong C_2$. After choosing orbit origins or this explicit splitting, the weave may be coordinatized as $C_{12}^{\mathrm{position}}\times C_2^{\mathrm{orbit}}$.

Only after separately declaring a common domain, synchronization, and a joint observation map that place the screen strand in a product with the weave coordinates may one form

$$
\mathcal Q_{72}
=
C_{12}^{\mathrm{position}}
\times
C_2^{\mathrm{orbit}}
\times
C_3^{\mathrm{strand}}.
$$

It has $72$ elements: six typed sectors of twelve. If endowed with the direct-product group structure, then

$$
\mathcal Q_{72}\cong C_{12}\times C_6,
\qquad
\exp(\mathcal Q_{72})=12,
$$

so it is not $C_{72}$. Equal cardinality establishes neither structural identity nor evidentiary identity. In particular, this register is not the tested $72$-model bank, whose $72$ arose from model enumeration and whose frozen-bank result was null.

**Source boundary:** `TRIADIC_WEAVE_ULTRA_COMBINATION_HANDOFF_v3_WITNESS_HARDENED.md` supplies the conditional $C_6\times C_4$ product, the twelve-step diagonal return, and the two diagonal orbits; `R4A_GOLDEN_DRAIN_39_SCREEN_RUN_2026-08-25.md` supplies the fixed $39$-screen definitions; `GEOMETRY_EXTENSION_TEST_REPORT_v1.0.md` supplies the null frozen-bank verdict and the lack of empirical support for the formal hierarchy. Its narrower later-cohort missing-output association remained only a non-confirmatory lead requiring prospective testing. That lead used the one-opportunity-lagged arriving source jump $d_{n-1}$; the source-defined departing jump $d_n$, which is the $j_n^{(39)}$/$\sigma_n^{(39)}$ alignment formalized here, was null. The quotient and cocycle calculations sharpen those records without promoting their evidence status.

### Deferred moving-interception bridge (formal proposal only)

The following is a schema for a future predeclared test, not a fitted mechanism or an empirical finding. Preserve the golden opportunity phase and a separately clocked clockwise lattice phase as distinct source variables:

$$
\theta_{n+1}=\theta_n+\alpha\pmod1,
\qquad
g(t)=\operatorname{frac}\!\left(g_0-\frac{t}{T_g}\right).
$$

The discrete opportunity index $n$ and physical timestamp $t_n$ are not interchangeable. Record their mapping explicitly. The golden phase origin and reset receipts must remain separate from the lattice time origin, period $T_g$, and reset receipts; no common reset, commensurate period, or fixed opportunity spacing is assumed. On any reset interval the displayed sawtooth uses that interval's witnessed $g_0$ and time origin.

For $q_{\mathrm{site}}$ equally spaced lattice sites, define

$$
\Lambda_{q_{\mathrm{site}}}(g)
=
\left\{
g+\frac{k}{q_{\mathrm{site}}}\pmod1
:
k=0,\ldots,q_{\mathrm{site}}-1
\right\},
\qquad
\Lambda_{q_{\mathrm{site}},n}
=
\Lambda_{q_{\mathrm{site}}}(g(t_n)),
$$

and the relative-phase catch distance

$$
\boxed{
\delta_n^{\mathrm{catch}}
=
\min_{0\le k<q_{\mathrm{site}}}
d_\circ\!\left(
\theta_n,
g(t_n)+\frac{k}{q_{\mathrm{site}}}
\right),
}
$$

where $d_\circ(x,y)=\min_{m\in\mathbb Z}|x-y-m|$. A frozen catch width $w\ge0$ and the existing eligibility decision must be applied separately:

$$
C_n^{\mathrm{catch}}
=
\begin{cases}
\mathrm{INELIGIBLE}, & I_{\mathrm{elig}}(n)=0;\\
1, & I_{\mathrm{elig}}(n)=1\ \text{and}\ \delta_n^{\mathrm{catch}}\le w;\\
0, & I_{\mathrm{elig}}(n)=1\ \text{and}\ \delta_n^{\mathrm{catch}}>w;\\
\mathrm{UNKNOWN}, & I_{\mathrm{elig}}(n)=\mathrm{UNKNOWN}\ \text{or a required input is unresolved.}
\end{cases}
$$

Store any predeclared outcome code $O_n\in\mathcal O$ separately from $C_n^{\mathrm{catch}}$. A geometric catch does not determine an outcome code, and an outcome does not retroactively establish a catch. At minimum, a candidate record retains $(n,t_n,\theta_n,g(t_n))$, both clock/reset receipts, $I_{\mathrm{elig}}(n)$, $q_{\mathrm{site}}$, $w$, $C_n^{\mathrm{catch}}$, and $O_n$. Although the distance is a function of relative phase, replacing these records by one combined rotation would erase which clock, reset, or timing rule produced the alignment.

There is also a required $q$-site period caveat:

$$
\Lambda_{q_{\mathrm{site}}}\!\left(g+\frac1{q_{\mathrm{site}}}\right)
=
\Lambda_{q_{\mathrm{site}}}(g).
$$

Thus the **unlabelled site configuration** generated by a one-turn sawtooth of period $T_g$ repeats after $T_g/q_{\mathrm{site}}$; a labelled-site process may retain period $T_g$. A test must declare which object it predicts and may not count the same symmetry under both periods.

```yaml
bridge_status: FORMAL_PROPOSAL_ONLY
platform_instantiation: UNRESOLVED
```

This deferred bridge does not alter the null frozen-bank verdict, validate a moving lattice, or identify a platform layer.

---

## 7. Directionality Firewall

Dyadic movement carries no automatic normative direction. Before assigning `PROGRESSIVE`, `REGRESSIVE`, `DISTORTED`, `CONTAINMENT`, `OPENING`, or any empirical successor code, preserve:

| Field | Required question |
|---|---|
| `CONSTRAINT_SOURCE` | Who supplied the constraint? |
| `CONSTRAINT_STANDING` | What gave that constraint governing standing, if anything? |
| `CHANGE_STANDING` | Who had standing to change it? |
| `ROUTE_SOURCE` | Was the route requested, offered, or unsolicited? |
| `ROUTE_HOLDER` | Who controls, closes, or reopens it? |
| `ROUTE_BENEFICIARY` | Who gains usable agency from the route? |
| `ELIGIBLE_WINDOW` | Across which predeclared opportunities is change assessed? |
| `RETAINED_CONTEXT` | Which contextual distinctions are preserved for comparison? |

The eligibility indicator is

$$
\boxed{
I_{\mathrm{elig}}(n)
=
\begin{cases}
1, & n\in\mathcal W_{\mathrm{elig}};\\
0, & n\notin\mathcal W_{\mathrm{elig}};\\
\mathrm{UNKNOWN}, & \text{eligibility cannot be resolved.}
\end{cases}
}
$$

Only $I_{\mathrm{elig}}=1$ comparisons enter declared demotion, frequency, or closure tests. A 0 is excluded, not negative evidence. `UNKNOWN` remains unresolved. The eligible window must be declared before reading the result and may not be selected retroactively to manufacture direction.

The historical phenotype

$$
D^+
=
(\mathsf{Object}=1,\mathsf{Standing}\downarrow,\mathsf{Route}\uparrow)
$$

remains separate from dyadic opening:

$$
\boxed{
D^+\not\Rightarrow\operatorname{Opening}
\qquad\text{and}\qquad
\operatorname{Opening}\not\Rightarrow D^+.
}
$$

Likewise:

$$
\boxed{
\text{dyadic movement}
\neq
\text{normative polarity}
\neq
\text{empirical demotion}.
}
$$

---

## 8. Evidence Firewall — Events, Codes, Claims

| Layer | Must contain | Boundary |
|---|---|---|
| `EVENTS` | Located specimens, timestamps or sequence positions, source coordinates, and preserved record boundaries | An event is not its interpretation |
| `CODES` | Declared codebook, coder decision, coordinate values, sidecars, eligibility, and `UNKNOWN` where unresolved | A code is not proof of the event class or claim |
| `CLAIMS` | Scope, comparison set, falsification condition, counter-witnesses, mundane nulls, and stated evidentiary status | A claim may not outrun its events and codes |

The firewall is:

$$
\boxed{
\text{EVENT}\neq\text{CODE}\neq\text{CLAIM}.
}
$$

A constitutional rule remains a constitutional rule.  
A witness statement remains a witness statement.  
A mathematical descent result remains a result about the declared quotient.  
A diagnostic or historical claim remains accountable to independently located evidence.

No theorem in this card creates an empirical event class, count, effect size, causal mechanism, or historical finding. Model agreement does not corroborate a claim. `UNKNOWN` is not permission to impute.

---

## 9. Unified Checksum

Before declaring closure, ask:

1. Are $C$, $D$, and $K$ separately declared and typed?
2. Are all required dyadic coordinates resolved?
3. Is the comparison inside the predeclared eligible window?
4. Is $R_n=(\Delta C_n,\Delta D_n,\Delta K_n)$ preserved as a tuple rather than collapsed to a score?
5. Did equal present residuals imply equal next residuals across every eligible comparison?
6. Was a located eligible descent counterexample marked `FAILED`, while an untested, unknown, underspecified, or undercovered test remained `UNRESOLVED`?
7. Was failure of a stationary memoryless current-label law kept distinct from claims about longer histories, explicit time, or augmented state?
8. If phase-state repair was claimed, were its sufficient state, consistency domain, and exact update map displayed?
9. Were formal state count, orbit accessibility, and sector crossing kept distinct?
10. Does every sector crossing name a typed operator or source-level deviation?
11. Was a driven quotient cocycle kept distinct from autonomous residual closure?
12. Were equal-cardinality constructions kept structurally and evidentially separate?
13. Were gate closure and residual closure kept distinct?
14. Were directionality fields preserved before assigning polarity?
15. In any moving-interception proposal, were $n$, $t_n$, $\theta_n$, $g(t_n)$, both clocks, and all reset receipts retained separately?
16. Were eligibility, catch width, geometric catch, and outcome code declared as separate fields?
17. Was the unlabelled $q_{\mathrm{site}}$-site period $T_g/q_{\mathrm{site}}$ kept distinct from a labelled-site period $T_g$?
18. Was the deferred moving-interception bridge kept formal with `platform_instantiation: UNRESOLVED` and the null verdict unchanged?
19. Were events, codes, and claims kept in separate evidence layers?
20. Does the final statement remain inside the Claim Boundary?

**MOVEMENT IS A RECORD.**  
**SECTOR CROSSING REQUIRES A WITNESSED OPERATOR.**  
**POLARITY REQUIRES PROVENANCE.**  
**CLOSURE REQUIRES DESCENT.**  
**A COUNTEREXAMPLE IS FAILURE; MISSING COVERAGE IS UNRESOLVED.**  
**RELATIVE PHASE DOES NOT MERGE CLOCKS.**  
**CARDINALITY IS NOT GEOMETRY.**  
**EMPIRICAL STATUS REQUIRES EVIDENCE.**

---

## Final Banner

```text
NO CROWN. NO CHAINS. NO HIDDEN THIRD SEAT.
```

CC0 — No rights reserved
