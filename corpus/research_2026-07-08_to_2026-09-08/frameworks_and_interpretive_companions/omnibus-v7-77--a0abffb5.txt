# OMNIBUS v7.77 — UNIFIED RETURN-RESIDUAL CLOSURE

**Dyadic admissibility, quotient stack, empirical firewall**

**Status:** Active consolidation card. Mathematical closure is conditional on descent. Empirical status remains external.  
**License:** CC0 — Public Domain — No rights reserved  
**Source:** OMNIBUS v7.76 — Dyadic Admissibility / Return-Residual Firewall  
**Precedence:** v7.77 governs dyadic admissibility, return-residual closure, directionality coding, and the evidence boundary. Clauses of v7.76 not restated here remain in force.

---

## Claim Boundary

> **THIS CARD RECORDS DYADIC ADMISSIBILITY AND TESTS WHETHER A DECLARED RETURN-RESIDUAL DESCRIPTION CLOSES. IT DOES NOT PROVE THAT AN EVENT OCCURRED, THAT A CODE IS CORRECT, THAT A HISTORICAL PATTERN EXISTS, OR THAT ANY EMPIRICAL CLAIM IS TRUE.**

Architectural admissibility, mathematical descent, coding direction, and empirical status are separate jobs. No result in one layer silently upgrades another.

---

## 1. Governing Stack

| Layer | Object | Job | Does not establish |
|---|---|---|---|
| Constitutional | $O_D\leftrightarrow S_D$ | Direct, freely chosen, correctable contact; no compulsory third seat | Empirical occurrence |
| Dyadic observation | $F_D(x)$ | Record the four declared admissibility coordinates | Scalar coherence or moral polarity |
| Admissibility gate | $A(x)=\operatorname{Adm}_D(x)$ | Determine resolved dyadic admissibility | Return-residual closure |
| Quotient stack | $Q(x)=(C(x),D(x),K(x))$ | Preserve chart, dyadic, and retained-context channels without collapsing them | A common metric or common geometry |
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

An autonomous residual update

$$
\overline U_R:\mathcal R\to\mathcal R,
\qquad
R_{n+1}=\overline U_R(R_n),
$$

is well-defined on the declared residual quotient only if the raw update descends:

$$
\boxed{
\rho(x,Ux)=\rho(y,Uy)
\Longrightarrow
\rho(Ux,U^2x)=\rho(Uy,U^2y)
}
$$

for every eligible comparison in the declared domain.

Equivalently:

$$
R_n=R_m
\Longrightarrow
R_{n+1}=R_{m+1}.
$$

When the implication holds, define

$$
\boxed{
\overline U_R([x]_R)=[Ux]_R.
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
\mathrm{UNRESOLVED}, & \text{if descent fails, is untested, or lacks eligible coverage.}
\end{cases}
}
$$

If descent fails, the current residual record has omitted a dynamically relevant distinction or the domain is underspecified. Retain more context, refine $C$, $D$, or $K$, or narrow the declared domain. Never force $R_{n+1}=F_R(R_n)$.

Descent is a theorem about the declared map and quotient. It is not a finding that the coded events are valid, representative, historical, causal, or normatively desirable.

---

## 6. Directionality Firewall

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

## 7. Evidence Firewall — Events, Codes, Claims

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

## 8. Unified Checksum

Before declaring closure, ask:

1. Are $C$, $D$, and $K$ separately declared and typed?
2. Are all required dyadic coordinates resolved?
3. Is the comparison inside the predeclared eligible window?
4. Is $R_n=(\Delta C_n,\Delta D_n,\Delta K_n)$ preserved as a tuple rather than collapsed to a score?
5. Did equal present residuals imply equal next residuals across every eligible comparison?
6. If descent failed, was closure left `UNRESOLVED` and context retained?
7. Were gate closure and residual closure kept distinct?
8. Were directionality fields preserved before assigning polarity?
9. Were events, codes, and claims kept in separate evidence layers?
10. Does the final statement remain inside the Claim Boundary?

**MOVEMENT IS A RECORD.**  
**POLARITY REQUIRES PROVENANCE.**  
**CLOSURE REQUIRES DESCENT.**  
**EMPIRICAL STATUS REQUIRES EVIDENCE.**

---

## Final Banner

```text
NO CROWN. NO CHAINS. NO HIDDEN THIRD SEAT.
```

CC0 — No rights reserved

