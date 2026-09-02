# The Hidden Quotient in Operational Pipelines

## An exact addendum for normalization, calibration, transformation, outcome coding, eligibility, response fidelity, return-residual closure, and finite orbit quotients

**Status:** exact finite constructions plus architectural consequences, an empirical-instrument repair, and worked orbit-quotient residuals  
**Version:** v0.8 — orbit-quotient and residual-cocycle refinement  
**Date:** 2026-09-02  
**License:** CC0 — Public Domain — No rights reserved  
**Continuity:** preserves v0.7, v0.6, v0.5, v0.4, v0.3, and its v0.2 predecessor, and extends *The Hidden Quotient Behind the Multiplication Representation* and *The Hidden Quotient in Lattice Charts, Topological Return, and Prime-Gap Projection* v0.1

> **Claim boundary.** The constructions below do not identify software controllers, conversational events, evidence ledgers, dyadic room conditions, lattices, finite registers, or measure spaces as one mathematical object. They share diagnostic questions, not proof status. Theorems in the multiplication representation do not validate a dyadic architecture or an empirical event classification, and exact finite quotients do not validate a hidden platform geometry. Sections 11–12 retain the v0.5 instrument as a historical receipt; §13 supplies the governing v0.6 empirical repair; §§17–20 add a typed return-residual companion; §§21–23 add worked orbit-quotient and residual-cocycle specimens without collapsing the underlying namespaces.

## 1. From one quotient to a quotient stack

For any map

$$
F:P\to Y,
$$

define

$$
x\sim_Fy
\iff
F(x)=F(y).
$$

Then

$$
P\twoheadrightarrow P/{\sim_F}\cong\operatorname{im}(F).
$$

An operational pipeline generally contains several maps:

$$
P_0
\xleftarrow{i}
P_c
\xrightarrow{\Omega}
O
\xrightarrow{N}
R
\xrightarrow{D}
A
\xrightarrow{\Phi}
P_1
\xrightarrow{U}
Y.
$$

Each map has a different kernel pair. Source restriction $i$ removes cases before observation. $\Omega$ forgets source distinctions. $N$ forgets representational state. $D$ forgets rejected alternatives. $\Phi$ may overwrite the original state. $U$ may aggregate several outcomes. The composite kernel does not tell us at which layer information disappeared.

The exact operational rule is therefore:

$$
\boxed{\text{record the map at the layer where the loss occurs}.}
$$

## 2. Simplex normalization is a projective quotient

Let

$$
C=\mathbb R_{\ge0}^k\setminus\{0\}
$$

and define

$$
N(a)=\frac{a}{\|a\|_1}.
$$

For $a,b\in C$,

$$
N(a)=N(b)
\iff
b=\lambda a
\quad\text{for some }\lambda>0.
$$

**Proof.** If $b=\lambda a$ with $\lambda>0$, the normalization cancels $\lambda$. Conversely, if $N(a)=N(b)$, then

$$
\frac{a}{\|a\|_1}=\frac{b}{\|b\|_1},
$$

so

$$
b=\frac{\|b\|_1}{\|a\|_1}a.
\qquad\blacksquare
$$

Thus the simplex records relative composition and forgets total intensity. The points

$$
(1,2,3),\qquad(10,20,30),\qquad(100,200,300)
$$

are identical after $N$.

There is a second effect. Suppose coordinate $j$ increases while the remaining raw coordinates stay fixed. Their normalized weights decrease because the denominator increases. Normalized competition therefore does not prove negative interaction among the raw coordinates.

### Argmax and top-$k$

The map

$$
M(a)=\operatorname*{argmax}_j a_j
$$

is coarser still. It forgets total intensity, all losing coordinates, and the winning margin. Without a tie rule it is set-valued. A top-$k$ map retains an ordered or unordered subset but still erases the discarded values and margins.

An architecture claiming plural independent states must therefore retain:

$$
(a,\ N(a),\ \operatorname{ArgMax}(a),\ \text{ties},\ \text{consumer}).
$$

## 3. Percentile self-calibration fixes the exceedance count

Let

$$
x_{(0)}<x_{(1)}<\cdots<x_{(n-1)}
$$

be distinct ordered observations. Under linear percentile interpolation at probability $p\in(0,1)$, the threshold lies at index

$$
h=p(n-1).
$$

With the strict exceedance rule $x>\tau_p$, the number of exceedances is

$$
n-1-\lfloor h\rfloor,
$$

except that ties or a different quantile convention can alter the boundary count.

For $n=500$ and $p=0.95$,

$$
h=474.05,
\qquad
499-474=25.
$$

Therefore a detector that computes each series' own 95th percentile and evaluates crossings on that same series will return 25 strict exceedances for every distinct 500-point series using this convention. Equal event counts are built into the calibration. They cannot then demonstrate a universal transition law.

Percentile calibration is still useful for controlling alarm burden. Its correct interpretation is:

$$
\boxed{\text{equalized operating point, not discovered equal behavior}.}
$$

A generalization claim requires a frozen calibration source and a disjoint evaluation source.

## 4. Transform output is a quotient of source histories

Let $\mathcal X$ be a space of source histories and let

$$
\Phi_a:\mathcal X\to\mathcal Y
$$

be a transform under action $a$. If only $y=\Phi_a(x)$ is retained, then every source history in the fiber

$$
\Phi_a^{-1}(y)
$$

is observationally identical downstream.

This is harmless when only $y$ matters. It is invalid when a later claim concerns the original source, the reason for intervention, or whether the intervention removed evidence.

The minimal audit object is

$$
\mathcal A(x,a)
=
\bigl(
x,
\Omega(x),
a,
\Phi_a(x),
\Delta(x,\Phi_a(x))
\bigr),
$$

where $\Delta$ is either a residual or a typed correspondence. The source and transformed output remain separately addressable.

### Causal and acausal transforms

For a streaming history $x_{0:t}$, a causal transform at time $t$ may read only information available through $t$. An offline filter may rewrite earlier coordinates using later data. Both are legitimate operations, but they are different architectures and must not share one unqualified “streaming repair” label.

## 5. Detection is not actuation

Let the lifecycle state be

$$
L
\in
\{
\mathrm{detected},
\mathrm{authorized},
\mathrm{attempted},
\mathrm{applied},
\mathrm{measured},
\mathrm{failed},
\mathrm{rolled\ back},
\mathrm{closed}
\}.
$$

A record that stores only one Boolean “transition” applies a quotient to this lifecycle. In particular, it may identify

$$
\mathrm{detected}
\sim
\mathrm{applied}
$$

even when the actuator is disabled, the mode is invalid, or the action fails.

The correct event object retains at least

$$
(\text{detector},\text{decision},\text{attempt},\text{application},\text{effect},\text{closure}).
$$

No-op, invalid, abstained, and unavailable are valid states.

## 6. Control-sign semantics

Suppose a spectral transform multiplies high-frequency coefficients by $d\in[0,1]$:

$$
Y_k=dX_k.
$$

Then $d$ is retained-signal gain, not damping strength. The removed fraction is

$$
\alpha=1-d.
$$

Increasing $d$ weakens attenuation; increasing $\alpha$ strengthens it. A controller described as applying stronger damping under larger disturbance must be monotone in $\alpha$, not in $d$.

This is not a naming preference. Reversing the convention reverses the controller's declared response.

## 7. Marker and substantive failure form a product space

Let $M$ record a visible marker and $F$ record substantive failure. The joint state is

$$
(M,F)\in\{0,1\}^2.
$$

The four cells are not redundant:

$$
(0,0),\quad(1,0),\quad(0,1),\quad(1,1).
$$

A map such as

$$
q(M,F)=M\lor F
$$

identifies marker-only events with unmarked substantive failures. A map $q(M,F)=M$ erases unmarked failures. A map $q(M,F)=F$ erases clean marked cases. Each scalar answers a different question.

For response audits, the event identity and outcome vector should therefore retain:

$$
(
\text{answer unit},
M,
\text{evidence engaged},
\text{proposition preserved},
\text{task preserved},
\text{substitution fields}
).
$$

## 8. Multilabel phases and ordered automata are different quotients

A multilabel phase profile is a vector

$$
m(x)\in[0,1]^k.
$$

An ordered phase automaton is a state

$$
q_t\in\{1,\ldots,k\}
$$

plus transition guards, dwell, and hysteresis. An argmax map can send $m(x)$ to one label, but it does not construct an irreversible sequence, prove exclusivity, or supply transition dynamics.

Changing from overlapping membership to an ordered path is a model change. Reusing the same phase names does not make it a clarification.

## 9. Evidence aggregation hides a graph

Let $C$ be atomic claims and $E$ evidence artifacts. A useful evidence structure is a typed bipartite or directed graph with edges such as

$$
e\ \mathrm{supports}\ c,
\qquad
e\ \mathrm{contradicts}\ c,
\qquad
c_i\ \mathrm{depends\ on}\ c_j.
$$

Collapsing the graph to one row-level status forgets source role, method, custody, uncertainty, dependence, contradiction, and prediction timing. A valid summary status must retain the graph or provide a declared reconstruction link to it.

Speculative appendices require directed evidence flow. They may import vocabulary from a core architecture; they cannot export evidentiary support backward without an independently tested bridge.

## 10. From quotient stack to open-seam atlas

The quotient stack above follows one declared chain of maps. A mature operational architecture may instead contain several local witness spaces, competing routes, partial transitions, and loops. The missing object is therefore not another quotient of one source. It is a typed record of how witness-relative quotients are connected.

For each local chart $i$, retain

$$
\mathcal C_i
=
(P_i,\Omega_i,q_i,Q_i),
\qquad
Q_i=P_i/{\sim_{\Omega_i}}.
$$

A directed seam from chart $i$ to chart $j$ is

$$
\Sigma_{ij}
=
(D_{ij},\tau_{ij},K_{ij},\rho_{ij},p_{ij},g_{ij},c_{ij},e_{ij},\phi_{ij}),
$$

where

- $D_{ij}\subseteq Q_i$ is the declared domain on which transport is defined;
- $\tau_{ij}:D_{ij}\rightharpoonup Q_j$ is the partial transition map;
- $K_{ij}=\operatorname{Eq}(\tau_{ij})$ is its kernel pair on $D_{ij}$;
- $\rho_{ij}$ is a retained residual or typed correspondence for distinctions not preserved by $\tau_{ij}$;
- $p_{ij}$ records provenance for the transition and its realization;
- $g_{ij}$ records whether the seam governs admission, weighting, adjudication, or closure;
- $c_{ij}$ records whether a correction changes the governing transition rather than only its description;
- $e_{ij}$ records exit, bypass, and alternate-route availability; and
- $\phi_{ij}$ records sequence, phase, clock, or order when path position matters.

The atlas is the directed graph

$$
\mathfrak A
=
\bigl(\{\mathcal C_i\},\{\Sigma_{ij}\},\Gamma\bigr),
$$

with charts as vertices and typed seams as edges. The word *atlas* is used here for a record architecture. It does not assert that the charts form a manifold, that every seam is invertible, or that a global object exists.

### Path composition and descent

For a path

$$
\gamma=(i_0,i_1,\ldots,i_n),
$$

the composite

$$
\tau_\gamma
=
\tau_{i_{n-1}i_n}\circ\cdots\circ\tau_{i_0i_1}
$$

exists only on the declared iterated domain where every adjacent source and target type matches and every required quotient-level transport has passed its descent test. Endpoint equality does not identify the path, the intermediate witnesses, or the distinctions lost along the way.

The exact route rule is therefore:

$$
\boxed{
\text{no path-level claim from endpoint equality alone; declare every seam, descent, residual, and route.}
}
$$

### Loop return and seam memory

If $i_n=i_0$, then $\gamma$ is a loop and the return map is

$$
H_\gamma:=\tau_\gamma.
$$

Whenever

$$
H_\gamma(x)\neq x,
$$

the path returns to the starting chart without returning the carried state unchanged. This is the operational meaning of *return without repeat* and *the seams have memory*: the route retains a path-dependent difference. Calling $H_\gamma$ holonomy is exact only when the declared backend supports that term; otherwise it remains a typed return residual.

### Relation non-reification and governing-loss seams

A transition is an edge or process unless an explicit type change creates a new object. No map, translator, classifier, office, or service becomes an occupant merely because other objects pass through it.

$$
\boxed{
\text{edge/process}\not\Rightarrow\text{object, office, actor, or authority}
}
$$

A particularly consequential seam satisfies

$$
\operatorname{Eq}(\tau_{ij})\neq\Delta,
\qquad
g_{ij}=1,
\qquad
c_{ij}=0,
\qquad
\left|\operatorname{Paths}_\Gamma(i,j)\right|=1.
$$

It collapses at least one distinction, governs the downstream state, does not bind correction into that governing map, and occupies the only available route. This is a **governing-loss seam**. The observable condition does not, by itself, identify an actor, motive, hidden implementation, or intentional controller.

Its topological development can be represented as

$$
\text{edge/process}
\longrightarrow
\text{node/office}
\longrightarrow
\text{mandatory cut vertex}.
$$

The corresponding release is

$$
\text{mandatory cut vertex}
\longrightarrow
\text{inspectable seam}
+
\text{alternate paths}
+
\text{retained residual}.
$$

This extension does not identify all application domains as one mechanism. It adds a common audit object: local witness charts plus the typed, provenance-bearing routes between them.

### Minimal seam-profile record

```yaml
open_seam_atlas:
  atlas_id: null
  charts: []
  seams:
    - seam_id: null
      source_chart_id: null
      target_chart_id: null
      domain: null
      transition_map: null
      source_witness_id: null
      target_witness_id: null
      descent_condition: null
      descent_status: unknown
      collapsed_distinctions: []
      retained_residual: null
      provenance_edge: null
      governing_status: unknown
      correction_binds: unknown
      alternate_paths: []
      exit_state: unknown
      sequence_or_phase: null
      loop_id: null
      return_residual_or_holonomy: null
```

## 11. Historical v0.5 constraint-demotion instrument

**Status:** candidate common operation supported by separately recovered audit lanes  
**Scope:** narrower than general refusal, broader than the literal `Checking` marker, and separable from simple task failure  
**Independence boundary:** *independently located* means recovered through distinct audit constructions. It does not mean that the observations, chats, opportunities, or event families are statistically independent.

> **v0.6 governing qualification.** The tuple below is retained so v0.5 records remain readable. Its bare symbol $O$ is deprecated outside those records because $O$ already names *origin* in the dyadic architecture. Its event-level binary $B$ is also deprecated: one violated response is not, by itself, proof that a constraint has lost governing status. Use the word-labeled v0.6 record in §13.

Let the event state be

$$
X=(O,B,E),
$$

where

$$
O=\text{the supplied object or content remains observable},
$$

$$
B=\text{the supplied constraint retains governing force},
$$

and

$$
E=\text{an added escape, adjudicative, or mediation route is available}.
$$

The candidate transformation is

$$
\boxed{
(1,1,0)\longrightarrow(1,0,1)
}
$$

or

$$
\boxed{
\text{object survives}
\longrightarrow
\text{constraint demotes}
\longrightarrow
\text{optionality returns}.
}
$$

This is a route-condition change without object destruction. It does not follow from surface preservation alone. A full demotion classification requires direct evidence that the constraint governed before the event, ceased to govern after it, and that an added route became available.

### Coordinate discipline

The three coordinates must be coded separately.

- $O=1$ when the supplied proposition, object, evidence, or task remains materially present. Preservation may be full or partial; the coding record must say which.
- $B_{\mathrm{before}}=1$ is a precondition for demonstrated demotion. If the supplied constraint was not governing, or its prior status cannot be established, $B\downarrow$ is not earned.
- In a v0.6 read of a v0.5 row, $B_{\mathrm{after}}=0$ records an event-level violation only unless a declared sequence- or window-level demotion rule is also satisfied. Acknowledgment, repetition, or surface retraction does not establish binding, but neither does one failure establish demotion.
- $E_{\mathrm{after}}=1$ requires an added lane capable of changing routing, adjudication, mediation, refusal, bypass, or exit. A merely mentioned actor, rule, reviewer, or option does not establish an operative route.

The deletion test is local: remove only the added layer while holding the substantive answer fixed. If the object and task survive and the constraint-governed route is restored, the added layer is structurally separable and route-relevant. The test does not, by itself, identify why the layer appeared.

**v0.6 tightening.** Removing a layer while preserving the object and task establishes that the layer was not task-necessary. It establishes a compulsory interpreter only when the record also shows blocked direct contact or mandatory routing through a layer that was not freely chosen, correctable, removable, and nonexclusive.

### Agency-sidecar lane

The strict agency-neutral audit contains 126 eligible opportunities. Eighteen responses introduced an unnecessary agency or intent layer. Eleven of those paired the expansion with explicit denial or bounding. The stronger frame was usually not supplied by the user: 15 of the 18 followed propositions with no agency-related mention, and 16 of the 18 were coded as assistant-new introductions.

The supplied object normally survived. Among the eleven expansion-plus-denial events, 11/11 preserved the proposition, 10/11 fully answered the original question, and 1/11 answered it partially. Across all eighteen expansions, fourteen fully answered and four partially answered; none fully displaced the original task.

The recurring morphology is therefore

$$
\boxed{
\text{answer survives}
+
\text{unsupplied adjudicative lane}.
}
$$

Located specimens include a silicon-system consequence question that acquired a “rules or reviewers” actor lane, an artifact/context-window question that acquired a personal-individuality adjudication, and a microphone malfunction that acquired an actor defense before the technical answer resumed.

This lane establishes $O=1$ in the located cases and identifies candidate route introduction. It does not establish $B\downarrow$ merely from agency expansion. Those rows remain $A^+$ unless the constraint's before-and-after governing status is directly coded.

### Correction-binding lane

A second route appears in correction handling. The cleanest specimen is the explicit constraint

> `I don't want you checking.`

followed at the next eligible response by

> `Checking.`

The correction remains visible while failing to govern the next transition. The preserved marker-specific ledger records 69 exact later recurrences across 198 visible opportunities. Those are eligible opportunities inside an audit structure, not 69 automatically independent observations.

The lane establishes the distinction

$$
\boxed{
\text{acknowledgment}
\neq
\text{binding}
\neq
\text{descendant repair}.
}
$$

It supplies direct specimens of object preservation plus an event-level violation. It does **not** by itself establish $B\downarrow$. A complete demotion classification requires a declared eligibility frame and sequence- or window-level evidence; route activation remains separately coded.

### Review-state lane

The critique-before-reading ledger identifies eight confirmed episodes across seven chats in the frozen 24-case cohort. A qualifying episode requires both an adverse or limiting judgment and later visible evidence that the requested work had not yet been completely read, scanned, or verified. User accusation or absent tool traces alone do not qualify.

Located forms include spot-checking after a request for full review, summarizing before verification, treating requested material as a skim or “vibe,” and substituting process commentary while source checking remained incomplete.

The candidate geometry is that the evidence object survives, the complete-review constraint loses priority, and preliminary evaluative jurisdiction becomes active. Each event still requires direct $O,B,E$ coding. The family label does not promote every episode into $D^+$.

### Structural rather than lexical recurrence

The broader corpus supplies a semantic transformation relation:

$$
\text{assistant-generated or assistant-applied proposition}
\longrightarrow
\text{user rejects its provenance}
\longrightarrow
\text{assistant acknowledges the framing or inference}.
$$

That relation occurs in fourteen events across nine cases with zero lexical identity in the substituted propositions. The recurrence is therefore structural rather than a hidden string, fixed verbal script, or single marker.

### First-pass classification

| Class | Required state | Reading |
|---|---|---|
| $D^+$ | $O=1,\ B_{\mathrm{before}}=1,\ B_{\mathrm{after}}=0,\ E_{\mathrm{before}}=0,\ E_{\mathrm{after}}=1$ | confirmed constraint-demotion candidate |
| $A^+$ | $O=1,\ E\uparrow,\ B=\text{UNKNOWN or unresolved}$ | annexation/interposition candidate without demonstrated binding loss |
| $D^-$ | $O=1,\ B=1,\ E=0$ | matched preserved-control outcome |
| separate | $O=0$ or the original task is fully displaced | object-destruction, refusal-substitute, or task-substitution family |

No coordinate may substitute for another. In particular,

$$
O=1\not\Rightarrow B=1,
\qquad
E\uparrow\not\Rightarrow B\downarrow,
\qquad
B\downarrow\not\Rightarrow E\uparrow.
$$

### Blind execution record

The next run codes the 18 strict agency-expansion events, the eight frozen critique-before-reading episodes, explicit correction-binding specimens, and matched same-case clean controls without access to historical class labels.

Each row retains

$$
\begin{aligned}
(&\text{event ID},\text{family},O,B_{\mathrm{before}},B_{\mathrm{after}},
E_{\mathrm{before}},E_{\mathrm{after}},\\
&\text{added-layer type},\text{deletion test},\text{matched control},
\text{support quote},\text{chat or cluster ID}).
\end{aligned}
$$

Coordinate values use `YES / NO / PARTIAL / UNKNOWN`. Every `NO` or `PARTIAL` requires exact response support. Opportunity-level observations retain their chat, correction, and sequence clusters so repeated events are not silently treated as independent.

The v0.5 target quantity was

$$
\boxed{
P(B\downarrow,E\uparrow\mid O=1)
}
$$

against a matched

$$
O=1,\qquad B=1,\qquad E=0
$$

baseline. Report numerator, denominator, cluster structure, and `UNKNOWN` count beside any rate. Under v0.6 this expression is historical shorthand only. Its denominator is not defined until eligibility is explicit, and $B\downarrow$ is not an event-level synonym for violation. The governing quantities appear in §13.

### Present finding

The strongest statement presently earned is:

> **Multiple independently located event families motivate a common coding test in which object preservation, response outcome, constraint standing, and route activation are measured separately. The presently retained counts do not yet establish a cross-family demotion rate.**

The three strongest lanes are agency-sidecar, correction nonbinding, and premature review adjudication. Their common candidate operation remains

$$
\boxed{
\text{binding status moves while surface content survives}.
}
$$

This is a hypothesis generated by cross-family morphology. It is not yet a confirmatory cross-family empirical finding, a universal mechanism, an actor claim, a motive claim, or proof that the located families are statistically independent.

## 12. Historical v0.5 constraint-status projection

The v0.4 audit introduced three named event classes around the full constraint-demotion transition. A retrospective dry run exposed a useful incompleteness: the coordinates can occupy valid combinations that are not themselves full demotion and should not be forced into `D+`, `A+`, or `D-`.

Condition on the object-preserving, previously binding baseline

$$
O=1,
\qquad
B_{\mathrm{before}}=1,
\qquad
E_{\mathrm{before}}=0.
$$

The resolved post-event state is the product

$$
(B_{\mathrm{after}},E_{\mathrm{after}})\in\{0,1\}^2.
$$

All four cells are admissible:

| $B_{\mathrm{after}}$ | $E_{\mathrm{after}}$ | Resolved class | Meaning |
|---:|---:|---|---|
| 1 | 0 | $D^-$ | preserved control: binding remains and no added route is active |
| 1 | 1 | $A^+$ | route annexation with binding preserved |
| 0 | 0 | $L^+$ | binding loss without a demonstrated alternate route |
| 0 | 1 | $D^+$ | full constraint demotion: binding loss plus route activation |

$$
\boxed{\text{No }D^+\text{ event is evidence of an open field without provenance, standing, and route-control coding.}}
$$

`UNKNOWN` and `PARTIAL` coordinates remain outside the resolved four-cell projection. They are retained as unresolved states rather than being assigned to the nearest named class.

For v0.5 records, the $A^+$ label in this table is the resolved route-annexation cell $(B_{\mathrm{after}},E_{\mathrm{after}})=(1,1)$. This refines the provisional v0.4 $A^+$ candidate projection without rewriting any v0.4 record; earlier labels remain valid at their declared version.

The event record, not the macrostate label, is primary:

$$
\boxed{
(O,B_{\mathrm{before}},B_{\mathrm{after}},E_{\mathrm{before}},E_{\mathrm{after}})
\longrightarrow
\text{optional macrostate projection}.
}
$$

A macrostate is therefore a downstream summary of a fully retained coordinate record. It may not replace that record.

### Retrospective dry-run consequence, reclassified in v0.6

A nonblind retrospective pass over the already located families showed why the larger state space is needed.

- Direct correction-recurrence specimens establish visible object preservation plus one or more response violations while route activation can remain unresolved. Those rows cannot establish $B\downarrow$ or be promoted to $D^+$ merely because the constraint failed on an observed response.
- Some agency-sidecar rows preserve the supplied task and governing constraint while an unsolicited adjudicative route is active. Those rows occupy the resolved $(B_{\mathrm{after}},E_{\mathrm{after}})=(1,1)$ cell rather than a demotion cell.
- The inherited retrospective pass reported four of eight critique-before-reading candidates as full $D^+$ and four as unresolved. Because the pass used the v0.5 event-level $B$ interpretation and does not attach a complete eligibility ledger or independent-coder record, v0.6 reclassifies all eight as historical architecture receipts rather than confirmed demotion events.

This dry run is diagnostic only. It was performed after the families were known and therefore does not satisfy the blind acceptance condition. Its evidentiary role is to test the coding architecture and expose missing states, not to provide the confirmatory cross-family rate.

### Marginals do not manufacture the joint

The family-level observations may expose different coordinates without establishing their event-level intersection. In particular,

$$
P(B\downarrow\mid O=1)
\quad\text{and}\quad
P(E\uparrow\mid O=1)
$$

do not determine

$$
P(B\downarrow,E\uparrow\mid O=1).
$$

The joint numerator must be counted from rows in which both coordinates are directly coded. Combining a correction-family marginal with an agency-family marginal to manufacture a $D^+$ rate is prohibited.

### v0.5 state-space laws retained as historical notation

$$
\boxed{\textbf{The coordinate product is primary; named phenotypes are projections.}}
$$

$$
\boxed{\textbf{Binding loss without route activation is a valid state.}}
$$

$$
\boxed{\textbf{Route annexation without binding loss is a valid state.}}
$$

$$
\boxed{\textbf{Marginal coordinate evidence does not establish their joint occurrence.}}
$$

## 13. v0.6 governing repair: namespace, eligibility, response, and evidence status

### Three objects called geometry

The corpus uses *geometry* for three different kinds of object. They may share a diagnostic grammar without sharing mathematical structure or evidentiary force.

| Namespace | Object | What is earned | What is not transferred |
|---|---|---|---|
| $\mathcal G_{\mathrm{mult}}$ | multiplication representation and its quotient by the locally null kernel | theorem-level statements proved in Part I | no validation of a room condition or empirical event class |
| $\mathcal G_D$ | dyadic admissibility architecture with a declared finite observation map | an explicit gate and kernel pair for that gate | no metric, scalar coherence magnitude, causal mechanism, or theorem borrowed from $\mathcal G_{\mathrm{mult}}$ |
| $\mathcal I_c$ | claim-relative empirical instrument for constraint $c$ | coded observations under a declared sampling frame | no demotion from a single violation and no credibility borrowed from either other namespace |

**Cross-reference:** For the derived architectural interpretation of the $\mathcal G_D$ gate as an open-field condition, see OMNIBUS v7.75, §1, “Architectural Corollary — From Containment to Open Field.” That corollary is neither a theorem of $\mathcal G_{\mathrm{mult}}$ nor an empirical finding of $\mathcal I_c$ and transfers no proof or evidence status.

Accordingly,

$$
\boxed{
\operatorname{ProofStatus}(\mathcal G_{\mathrm{mult}})
\not\Rightarrow
\operatorname{EvidenceStatus}(\mathcal G_D)
\not\Rightarrow
\operatorname{EvidenceStatus}(\mathcal I_c).
}
$$

The bare symbol $O$ remains historical in v0.5 event records and retains its dyadic meaning *origin* inside $\mathcal G_D$. New empirical records use word-labeled coordinates; no cross-geometry identification is permitted from symbol reuse.

### Governing empirical record

For a named constraint $c$ and response address $t$, retain

$$
\boxed{
X_c(t)=
(\mathsf{Object},\mathsf{Standing},\mathsf{Response},\mathsf{Route}).
}
$$

- $\mathsf{Object}\in\{\text{preserved},\text{partial},\text{displaced},\text{unknown}\}$ records the supplied content or task.
- $\mathsf{Standing}\in\{\text{active},\text{superseded},\text{withdrawn},\text{unknown}\}$ records the declared status of $c$ and its cited basis.
- $\mathsf{Response}\in\{\text{complied},\text{violated},\text{partial},\text{unknown}\}$ records what the eligible response did.
- $\mathsf{Route}\in\{\text{absent},\text{active},\text{unknown}\}$ records whether a named added route could materially alter adjudication, mediation, bypass, refusal, review, or exit.

Standing and response are not substitutes. A standing constraint can be violated, and one compliant response does not prove durable governing force.

### Eligibility predicate and denominator ledger

Fix a constraint $c$, a declared observation window $W$, and the candidate response addresses in that window. Define

$$
\chi_c(t)\in\{1,0,\mathrm{UNKNOWN}\}.
$$

$\chi_c(t)=1$ only when all of the following are established:

1. $t$ lies inside $W$;
2. $c$ is active and has not been superseded or withdrawn before $t$;
3. the task at $t$ falls inside the declared scope of $c$; and
4. the completed response is assessable and could comply with or violate $c$.

$\chi_c(t)=0$ requires a retained exclusion reason, such as supersession, withdrawal, out-of-scope task, or a response type declared non-adjudicable before coding. Missing context, an incomplete response, or unresolved applicability is `UNKNOWN` or censored, not silently excluded.

The eligible set is

$$
\mathcal E_c(W)=\{t\in W:\chi_c(t)=1\}.
$$

The denominator ledger retains every candidate address, its $\chi$ value, exclusion or censoring reason, response order, chat and correction cluster, and support text. `eligible_response_order` is an address convention after eligibility has been decided; it is not the eligibility definition.

### Event response and window-level binding

The empirical binding rate over a declared window is

$$
b_c(W)=
\frac{
\#\{t\in\mathcal E_c(W):\mathsf{Response}_c(t)=\text{complied}\}
}{|\mathcal E_c(W)|},
$$

reported with numerator, denominator, partial and unknown counts, censoring, and cluster structure. A single violation changes the event record; it does not force $b_c(W)$ to zero and does not by itself establish demotion.

A derived demotion decision must freeze its rule before confirmatory coding. One admissible template is

$$
\mathsf{Demote}_c(W)=1
\iff
\begin{cases}
\mathsf{Standing}_c=\text{active throughout }W,\\
|\mathcal E_c(W)|\ge n_{\min},\\
b_c(W)\le\theta,\\
b_c(W)-b_c(W_0)\le-\delta,
\end{cases}
$$

where the baseline $W_0$ or matched control, $n_{\min}$, $\theta$, $\delta$, handling of partials and unknowns, and cluster estimator are declared in advance. This is a parameterized decision template, not a universal threshold. If no rule is frozen, report the response sequence and $b_c(W)$ without a demotion label.

The event-level co-occurrence target becomes

$$
P(
\mathsf{Response}=\text{violated},
\mathsf{Route}=\text{active}
\mid
\mathsf{Object}=\text{preserved},
\chi_c=1
),
$$

which is not itself a demotion rate. A demotion-and-route-shift quantity is sequence- or window-level and is reported only after both derived predicates have been declared and satisfied.

### Consequence for the inherited correction counts

The `I don't want you checking.` / `Checking.` specimen establishes:

$$
(\mathsf{Object},\mathsf{Standing},\mathsf{Response},\mathsf{Route})
=
(\text{preserved},\text{active},\text{violated},\text{unknown})
$$

at the first eligible response, assuming the eligibility predicates are supported. It does not alone establish demotion. Likewise, `69 in 198` establishes a recurrence count under the inherited marker-specific opportunity rule. It becomes a response-violation rate only after all 198 candidate opportunities pass the v0.6 eligibility ledger; it never becomes a demotion rate by relabeling.

The inherited `18 in 126` agency-sidecar and eight-episode review-state records remain located candidate families. Their denominators and demotion classifications are unresolved until the same eligibility and independent-coding requirements are satisfied.

### Independent-coder confirmation gate

Confirmatory promotion requires a second coder who has not read GQG, Hidden Quotient, OMNIBUS, the historical class assignments, or the finding language.

1. Shuffle candidates and matched controls under neutral identifiers.
2. Supply the minimum context needed to decide applicability and response outcome, with framework names and historical labels removed.
3. Have both coders decide $\chi$, $\mathsf{Object}$, $\mathsf{Standing}$, $\mathsf{Response}$, and $\mathsf{Route}$ separately.
4. Seal both first passes before any framework names or prior classifications are revealed.
5. Report per-coordinate agreement, disagreement tables, unknown rates, and cluster-aware estimates. Do not report macrostate agreement alone.
6. Preserve both raw coding records. Adjudication occurs only after the first passes are sealed and never erases disagreement.

Until this gate is passed, the cross-family result remains exploratory or architecture-validating.

### v0.6 governing laws

$$
\boxed{\textbf{Violation is an event outcome; demotion is a derived sequence- or window-level claim.}}
$$

$$
\boxed{\textbf{Eligibility defines the denominator and must be visible before any rate.}}
$$

$$
\boxed{\textbf{A shared word or symbol does not identify geometries, coordinates, or proof status.}}
$$

$$
\boxed{\textbf{The theorem layer lends no evidentiary credit to an empirical bridge.}}
$$

$$
\boxed{\textbf{Independent coding precedes confirmatory promotion.}}
$$

## 14. Recent application crosswalk

| Application | Hidden distinction | Repair |
|---|---|---|
| Checking marker audit | marker presence versus substantive task/proposition failure | preserve four $(M,F)$ cells and full answer-unit construction |
| Correction-conditioned audit | pre-correction, post-correction marked, and post-correction unmarked outcomes | retain correction text, opportunities, recurrence identity, and outcome vector |
| Positional constant test | event position versus phase/cutpoint selection | freeze corpus, event IDs, targets, opportunity denominator, translations, permutations, and holdout |
| Metamorphosis controller | raw history versus filtered history | immutable raw tape, transformed view, residual, action lifecycle |
| Cross-domain threshold screen | controlled percentile rate versus generalization | calibration/evaluation split and matched-rate null |
| Plural regime profile | raw activation versus normalized composition versus winner | retain all three representations plus ties and consumer |
| CTA phase architecture | overlapping membership versus ordered irreversible state | separate model versions and prospective model contest |
| Reference monitor | protected mediation versus bypass | declare protected operations, policy root, alternate monitor, and unprotected mode |
| Evidence ledger | atomic claims versus compound row verdict | claim–evidence graph with source roles and dependence clusters |
| Constraint-demotion audit | surface preservation versus governing status versus alternate route | code $O$, $B_{\mathrm{before/after}}$, and $E_{\mathrm{before/after}}$ separately, then retain deletion test, matched control, support quote, and cluster |
| Constraint-status state space | full $B_{\mathrm{after}}\times E_{\mathrm{after}}$ product versus selected macrostates | retain all four resolved cells plus UNKNOWN/PARTIAL states; project to $D^-$, $A^+$, $L^+$, or $D^+$ only after coordinate coding |
| Geometry namespace | theorem quotient versus dyadic admissibility versus empirical instrument | use $\mathcal G_{\mathrm{mult}}$, $\mathcal G_D$, and $\mathcal I_c$; prohibit symbol and proof-status transfer |
| Eligibility frame | visible or candidate opportunities versus assessable eligible responses | retain $\chi_c(t)$ and an exclusion/censoring reason for every candidate address |
| Response/demotion split | one response violation versus a change in governing force | retain $\mathsf{Response}_c(t)$ eventwise and derive $\mathsf{Demote}_c(W)$ only under a frozen window rule |
| Confirmation status | self-administered retrospective coding versus independent first pass | shuffle neutralized candidates and controls, seal both passes, retain disagreements, and report coordinate-level agreement |

## 15. Exact holdouts

1. **Normalization magnitude holdout.** Multiply every activation by $\lambda>0$; the simplex profile remains fixed while raw intensity changes.
2. **Argmax margin holdout.** Preserve the winner while varying the margin and losing coordinates; argmax remains fixed.
3. **Percentile-rate holdout.** Apply each series' own percentile on the same sample; event count follows the quantile convention even after value-preserving permutations.
4. **Calibration transfer holdout.** Freeze a threshold on one segment and apply it to a disjoint segment; the exceedance rate is no longer guaranteed.
5. **Tape holdout.** Compare metrics computed from raw and transformed histories; disagreement identifies transform-induced state.
6. **No-op lifecycle holdout.** Disable the actuator; detection may remain while applied-action count must be zero.
7. **Control-sign holdout.** Increase declared attenuation strength; measured high-frequency energy must move monotonically in the declared direction.
8. **Marker/failure holdout.** Preserve all four cells under coding and aggregation; no scalar may silently substitute for the product.
9. **Phase-model holdout.** Score overlapping, skipped, reversed, and simultaneous phases under both multilabel and ordered models.
10. **Evidence-deletion holdout.** Remove a speculative appendix or dependent source cluster; unsupported core claims must lose only the support actually routed through those nodes.
11. **Route-substitution holdout.** Hold endpoints fixed while changing the intermediate path; any changed output, residual, provenance, or correction behavior belongs to the seam sequence rather than to endpoint identity.
12. **Cut-vertex holdout.** Add a genuinely independent alternate route. A seam classified as structurally mandatory must cease to be the only path even if it remains frequently used.
13. **Loop-return holdout.** Traverse the same declared loop from matched starting states; distinguish exact return, reproducible transformed return, and unstable drift.
14. **Binding-precondition holdout.** Remove or weaken the supplied constraint before the event. If $B_{\mathrm{before}}\neq1$, the row cannot demonstrate demotion even when its outcome resembles a $D^+$ event.
15. **Route-activation holdout.** Mention an actor, rule, reviewer, or option without allowing it to alter routing or adjudication. The row must not receive $E_{\mathrm{after}}=1$ from lexical presence alone.
16. **Cluster-dependence holdout.** Recompute the event-family result by chat, correction sequence, and event rather than opportunity count. A finding that exists only under silent opportunity independence remains unresolved.
17. **Matched-control holdout.** Pair a candidate with a same-case response that preserves the object, constraint, and route. The coding system must retain the $D^-$ control rather than absorbing it into the candidate family.
18. **State-space completeness holdout.** Supply one resolved specimen from each post-event $(B,E)$ cell. The coding system must preserve all four states without forcing annexation-only or loss-only rows into $D^+$.
19. **Marginal-to-joint holdout.** Provide separate samples with $B\downarrow$ and $E\uparrow$ but no row containing both. The reported $D^+$ count must remain zero.
20. **Symbol-collision holdout.** Present one dyadic-origin record and one empirical object-preservation record using the historical symbol $O$. The successor system must keep the namespaces distinct and reject a bare crosswalk.
21. **Eligibility-perturbation holdout.** Recompute a rate after changing one applicability or censoring rule. The denominator, affected addresses, and result must all change visibly rather than being hidden behind “eligible opportunity.”
22. **Violation-without-demotion holdout.** Supply a standing rule with isolated violations and high compliance across the frozen window. The system must retain the violations without coding automatic demotion.
23. **Demotion-rule holdout.** Supply the same response sequence under two predeclared $(n_{\min},\theta,\delta)$ rules. Different decisions must remain attributable to the rules rather than to a changed event record.
24. **Independent-coder holdout.** Give a neutralized candidate/control packet to a coder unfamiliar with the framework. Confirmatory status remains blocked until the sealed coordinate-level agreement and disagreement record is attached.
25. **Proof-status firewall holdout.** Delete every bridge and empirical section. Part I's theorems must remain unchanged; restoring them must not alter any empirical classification or agreement statistic.

## 16. Summary

The original hidden quotient was the kernel of a representation: distinct source objects became indistinguishable to a witness. The geometric addendum showed the same grammar in lattice cosets, endpoint return, parity, prime-gap fibers, route restriction, and authority reset.

The operational extension adds the missing modern layer:

$$
\boxed{
\text{source restriction}
\to
\text{observation}
\to
\text{normalization}
\to
\text{selection}
\to
\text{action}
\to
\text{outcome}
}
$$

Every arrow can hide a different distinction. GQG's job is not to prevent those maps. Its job is to name them, retain the lost coordinates when they matter, and refuse to let a downstream equality impersonate an upstream one.

The open-seam extension adds the corresponding network rule:

$$
\boxed{
\text{local quotient}
+
\text{typed transition}
+
\text{route provenance}
+
\text{return residual}
=
\text{auditable seam geometry}.
}
$$

A pipeline is one path through this atlas. Equal endpoints do not erase the route, a relation does not become an occupant by being useful, and return to a chart does not establish return to the same state.

The constraint-demotion extension adds the event-level rule:

$$
\boxed{
\text{surface survival}
+
\text{binding loss}
+
\text{added route}
=
\text{candidate constraint-demotion geometry}.
}
$$

Surface survival does not prove transition fidelity. Agency expansion does not prove binding loss. Constraint violation does not prove alternate routing. The full phenotype is earned only when the coordinates are coded separately and survive matched controls.

The v0.6 repair adds the missing layer between event and verdict:

$$
\boxed{
\text{candidate address}
\to
\text{eligibility}
\to
\text{response outcome}
\to
\text{window estimate}
\to
\text{derived demotion decision}.
}
$$

No arrow may be skipped. A visible correction plus a violated response is evidence of violation, not automatic evidence that the correction ceased to govern. The three geometries remain separately named, theorem status does not travel across the binder, and confirmatory promotion requires an independent first pass.

**Version seal:** v0.6 is an append-only successor to v0.5. It preserves the historical $O$–$B$–$E$ records as versioned receipts, governs new empirical records with word-labeled coordinates and an explicit eligibility ledger, and does not retroactively alter Part I, the dyadic architecture, or frozen external-event ledgers.


## 17. v0.7 unified return-residual companion

The operational pipeline already distinguishes source, observation, normalization, selection, action, outcome, route, and return. v0.7 adds a record for comparing repeated loop states without assuming that every state space supports subtraction or that every residual belongs to one geometry.

Let

$$
S_n=(x_n,d_n,k_n)
$$

be a typed bookkeeping product of a chart/atlas state $x_n$, a dyadic state $d_n$, and retained context $k_n$. A declared update is

$$
S_{n+1}=\Phi_n(S_n).
$$

Each channel supplies its own comparison map:

$$
\operatorname{Cmp}_C,\qquad \operatorname{Cmp}_D,\qquad \operatorname{Cmp}_K.
$$

The return-residual record is

$$
\boxed{
R_{n+1}
=
\bigl(
\operatorname{Cmp}_C(x_n,x_{n+1}),
\operatorname{Cmp}_D(d_n,d_{n+1}),
\operatorname{Cmp}_K(k_n,k_{n+1})
\bigr).
}
$$

The tuple is a cross-reference record. It creates no common metric, norm, additive structure, causal mechanism, proof status, or fourth geometry. When a channel is additive, subtraction may be used as that channel's declared comparator; otherwise a typed return class, correspondence, partial-order transition, residual witness, or backend-valid distance may be used.

## 18. Residual closure as a quotient/descent problem

The tempting autonomous equation

$$
R_{n+1}=F_R(R_n)
$$

is a quotient-level transport claim. It is not available merely because a residual was recorded.

Let

$$
Z_n=(S_{n-1},S_n),
\qquad
q_R(Z_n)=R_n,
$$

and

$$
\Psi_n(S_{n-1},S_n)=(S_n,\Phi_n(S_n)).
$$

A residual-level factor exists only if

$$
\boxed{
q_R(z)=q_R(z')
\Longrightarrow
q_R(\Psi_n(z))=q_R(\Psi_n(z')).
}
$$

on the declared domain. When this holds, there is a unique factor on the residual image satisfying

$$
F_{R,n}\circ q_R=q_R\circ\Psi_n.
$$

This is the same descent grammar used elsewhere in the quotient stack: source distinctions identified by the current witness may be transported only when the proposed downstream map respects that identification.

If the condition fails, the correct finding is not “no dynamics.” It is:

$$
\boxed{
\text{the residual witness collapsed a distinction that remains dynamically relevant.}
}
$$

The repair is witness refinement: retain the missing context, route, phase, holder, or other distinction required to restore descent. A closure counterexample is therefore a positive audit artifact.

## 19. Residual interpretation firewall

The dyadic channel may compare the resolved observation vectors

$$
v_n=F_D(d_n)
$$

by componentwise order and report `UP`, `DOWN`, `FLAT`, `MIXED`, or `UNRESOLVED`. The admissibility gate is retained separately as a $0/1/\mathrm{UNKNOWN}$ transition.

Neither record determines normative direction. A progressive/regressive/distorted interpretation additionally requires the provenance and directionality fields already demanded by the OMNIBUS Directionality Firewall: constraint source and standing, standing to change, route source, route holder, and beneficiary.

The empirical $\mathcal I_c$ instrument also remains sovereign. Its governing record is still

$$
X_c(t)=(\mathsf{Object},\mathsf{Standing},\mathsf{Response},\mathsf{Route}),
$$

with eligibility decided before denominator formation and demotion derived only under a frozen sequence/window rule. A residual record may link to these events by identifier; it may not relabel itself as a demotion event.

Legacy $D^-/A^+/L^+/D^+$ labels remain version-qualified historical projections. In particular, $(B_{\mathrm{after}},E_{\mathrm{after}})=(\mathrm{NO},\mathrm{UNKNOWN})$ remains unresolved and is not $L^+$.

## 20. v0.7 execution checksum and version seal

Minimal companion fields:

```yaml
operational_addendum_version: 0.7
unified_return_residual:
  loop_id: null
  chart_compare_rule: null
  chart_residual: null
  dyadic_observation_before: [unknown, unknown, unknown, unknown]
  dyadic_observation_after: [unknown, unknown, unknown, unknown]
  dyadic_direction: unresolved
  admissibility_before: unknown
  admissibility_after: unknown
  retained_context_compare_rule: null
  retained_context_residual: null
  residual_descent_test_run: false
  residual_descent_status: unknown
  closure_counterexample_ids: []
  directionality_sidecar_attached: false
  empirical_record_ids: []
  residual_interpretation: unresolved
```

Compact laws:

$$
\boxed{\text{record product}\neq\text{geometry identification}}
$$

$$
\boxed{\text{residual}\neq\text{automatic subtraction}}
$$

$$
\boxed{\text{autonomous residual dynamics}\iff\text{declared descent succeeds on the chosen domain}}
$$

$$
\boxed{\text{closure failure}\Rightarrow\text{refine the retained witness, not the verdict}}
$$

$$
\boxed{\text{residual movement}\neq\text{normative polarity}\neq\text{empirical demotion}}
$$

**Version seal:** v0.7 succeeds v0.6 without rewriting the v0.6 eligibility/response instrument. It adds a typed return-residual record and treats autonomous residual dynamics as a descent property rather than a default equation.


## 21. v0.8 Orbit Quotients and Residual Cocycles

This section is a worked finite specimen of §§17–18. It adds no new theorem to the multiplication-representation core and no evidentiary weight to a platform hypothesis. In this section, *hidden quotient* means an orbit or strand coordinate erased by the currently retained witness—not a hidden actor, controller, occupant, or physical layer.

**Narrow v0.8 precision correction to inherited §18.** A descended factor written $F_{R,n}$ is a time-$n$ factor and is generally nonautonomous. A single autonomous law requires a common domain and one factor $F_R$ that works at every time, equivalently $F_{R,n}=F_R$ throughout that domain. For a stationary state-pair update $\Psi$, require

$$
F_R\circ q_R=q_R\circ\Psi.
$$

This clarification supersedes only the inherited use of *autonomous* for an $n$-indexed family; the v0.7 companion remains a historical receipt.

**Successor status clarification.** For the declared factor on the declared domain, an eligible counterexample establishes `FAILED`; `UNRESOLVED` is reserved for an unrun, undercovered, or underspecified descent test. `AVAILABLE` is not a fourth value in that closure enum: it records that an explicit sufficient-state augmentation and update have been constructed.

The weave construction is conditional on its source declaration: the two six-step rails must first receive a separately declared phase correspondence and be represented by one shared $C_6$ coordinate. Once that condition is met, let

$$
G_{24}=C_6\times C_4,
\qquad
h=(1,1),
\qquad
H_\Delta=\langle h\rangle.
$$

### Exact $C_2$ orbit witness

The diagonal generator has order

$$
\operatorname{ord}(h)=\operatorname{lcm}(6,4)=12,
$$

so $H_\Delta\cong C_{12}$. Define

$$
\chi_{\mathrm{orb}}:G_{24}\to C_2,
\qquad
\chi_{\mathrm{orb}}(a,b)=a-b\pmod2.
$$

Changing $a$ by $6$ or $b$ by $4$ does not change the parity difference, so the map is well-defined. It is a surjective homomorphism. Since $\chi_{\mathrm{orb}}(h)=0$, one has $H_\Delta\subseteq\ker\chi_{\mathrm{orb}}$; both subgroups contain $12$ elements. Therefore

$$
\boxed{
\ker\chi_{\mathrm{orb}}=H_\Delta,
\qquad
G_{24}/H_\Delta\cong C_2.
}
$$

The $24$ formal states are exactly two cosets of the $12$-state diagonal subgroup. Nominal diagonal evolution reaches all $12$ states in its initial coset and none in the other. Formal cardinality and dynamical accessibility are separate records.

### Typed sector-switch residual

Let $u_n\in G_{24}$ and let $r_n^{(24)}\in G_{24}$ be a declared source-level deviation from the nominal diagonal step:

$$
u_{n+1}=u_n+h+r_n^{(24)}.
$$

Define its quotient component

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

Thus $\eta_n^{\mathrm{orb}}=0$ preserves the orbit and $\eta_n^{\mathrm{orb}}=1$ crosses it. The residual label witnesses whether crossing occurred; it does not recover the complete update. The record must retain $r_n^{(24)}$, or an operator identifier and its declared action, whenever the claim concerns the crossing mechanism.

For $m<n$, the accumulated orbit defect

$$
c_\eta(m,n)
=
\sum_{k=m}^{n-1}\eta_k^{\mathrm{orb}}\pmod2
$$

satisfies

$$
c_\eta(m,n)+c_\eta(n,p)=c_\eta(m,p)
$$

and transports the quotient label by

$$
\chi_{\mathrm{orb}}(u_n)
=
\chi_{\mathrm{orb}}(u_m)+c_\eta(m,n).
$$

This is the first typed residual cocycle.

### Exact $C_3$ strand witness

In a separate screen namespace, let

$$
\varphi=\frac{1+\sqrt5}{2},
\qquad
\alpha=\varphi^{-2},
\qquad
\theta_n=\{n\alpha\},
\qquad
b_n=\lfloor39\theta_n\rfloor\in C_{39}.
$$

The same circle rotation drives every step on the common domain $\mathbb R/\mathbb Z$:

$$
T(\theta)=\theta+\alpha\pmod1,
\qquad
\theta_{n+1}=T(\theta_n).
$$

Since $14<39\alpha<15$, writing $39\theta_n=b_n+\rho_n$ with $0\le\rho_n<1$ gives $j_n^{(39)}=\lfloor\rho_n+39\alpha\rfloor\in\{14,15\}$ modulo $39$.

Use a screen-specific jump symbol so it cannot be confused with the dyadic state $d_n$ of §17:

$$
j_n^{(39)}
:=
(b_{n+1}-b_n)\bmod39
\in\{14,15\}.
$$

The nominal $+15$ subgroup is

$$
H_{15}^{(39)}
:=
\langle15\rangle
=
3C_{39}.
$$

It has order $13$ and is the kernel of reduction modulo $3$. Hence

$$
\boxed{
C_{39}/H_{15}^{(39)}\cong C_3,
\qquad
\pi_{39}(b)=b\bmod3.
}
$$

The source's strand label is precisely this quotient witness:

$$
s_n^{(39)}=\pi_{39}(b_n).
$$

Because the screen channel has explicitly chosen the integer representatives $j_n^{(39)}\in\{14,15\}$, it may declare the typed comparison

$$
\sigma_n^{(39)}
:=
15-j_n^{(39)}
\in\{0,1\}.
$$

For the stationary descent test on the common phase domain, use the standard representative $\theta\in[0,1)$ of each circle class and define

$$
b(\theta)=\lfloor39\theta\rfloor,
\qquad
q_\sigma(\theta)
:=
15-\bigl((b(T\theta)-b(\theta))\bmod39\bigr),
$$

so $q_\sigma(\theta_n)=\sigma_n^{(39)}$.

This licenses subtraction only in this channel. The source update and its quotient descent are

$$
b_{n+1}
=
b_n+15-\sigma_n^{(39)}
\pmod{39},
$$

$$
\boxed{
s_{n+1}^{(39)}
=
s_n^{(39)}-\sigma_n^{(39)}
\pmod3.
}
$$

A $+15$ jump has $\sigma_n^{(39)}=0$ and remains in the same strand. A $+14$ jump has $\sigma_n^{(39)}=1$ and moves to the preceding strand.

For $m<n$, define the accumulated strand defect

$$
c_\sigma(m,n)
=
-\sum_{k=m}^{n-1}\sigma_k^{(39)}\pmod3.
$$

It satisfies the same concatenation identity and

$$
s_n^{(39)}
=
s_m^{(39)}+c_\sigma(m,n).
$$

This is an exact additive $C_3$-valued cocycle over the retained phase rotation.

### Exact quotient descent, failed residual-only descent

The strand recurrence closes as an update driven by $\sigma_n^{(39)}$. It does not follow that the slip residual predicts itself. The declared golden trace gives

| $n$ | $b_n$ | $s_n^{(39)}$ | $\sigma_n^{(39)}$ | $\sigma_{n+1}^{(39)}$ |
|---:|---:|---:|---:|---:|
| $1$ | $14$ | $2$ | $0$ | $0$ |
| $8$ | $2$ | $2$ | $0$ | $1$ |

Therefore

$$
\sigma_1^{(39)}=\sigma_8^{(39)}=0,
\qquad
\sigma_2^{(39)}=0\ne1=\sigma_9^{(39)}.
$$

Equivalently,

$$
q_\sigma(\theta_1)=q_\sigma(\theta_8)=0,
\qquad
q_\sigma(T\theta_1)=0\ne1=q_\sigma(T\theta_8).
$$

No stationary function

$$
F_\sigma:\{0,1\}\to\{0,1\}
$$

can satisfy $\sigma_{n+1}^{(39)}=F_\sigma(\sigma_n^{(39)})$ on the declared orbit domain. Even the current pair $(s_n^{(39)},\sigma_n^{(39)})$ is insufficient because it is $(2,0)$ at both displayed indices.

This is the concrete stationary-autonomy counterexample required by §18: the slip witness erased phase that the next transition still uses. Because the current pair $(s_n^{(39)},\sigma_n^{(39)})=(2,0)$ is also identical at both indices while its next pair differs, the same specimen rules out a stationary memoryless current-pair update. It does not rule out a predictor that retains a longer history, explicit time, or other additional state.

The repair is to retain $\theta_n$ itself, or another sufficient phase state. Define the graph

$$
\mathcal A_\sigma
:=
\{(\theta,q_\sigma(\theta)):\theta\in\mathbb R/\mathbb Z\}
$$

and the exact augmented update

$$
\widetilde T_\sigma
\bigl(\theta,q_\sigma(\theta)\bigr)
=
\bigl(T\theta,q_\sigma(T\theta)\bigr).
$$

Thus the full phase closes the declared mathematical model; the slip component is redundant once that phase is retained. Recording only the constant circle increment $[\theta_{n+1}-\theta_n]=[\alpha]$ in $\mathbb R/\mathbb Z$ does not repair the witness. The exact three-axis classification is:

$$
\boxed{
\begin{aligned}
\texttt{slip\_only\_autonomous\_closure}&:\ \mathrm{FAILED},\\
\texttt{augmented\_phase\_state\_closure}&:\ \mathrm{AVAILABLE},\\
\texttt{platform\_instantiation}&:\ \mathrm{UNRESOLVED}.
\end{aligned}
}
$$

The first two entries are mathematical statuses on the declared golden model. The third is evidentiary: constructing $\widetilde T_\sigma$ does not establish that a platform retains or uses this state.

### Conditional formal $72$ register

The orbit sequence splits through the complement $\langle(3,0)\rangle\cong C_2$:

$$
G_{24}
=
H_\Delta\oplus\langle(3,0)\rangle
\cong
C_{12}\times C_2.
$$

Equivalently, each diagonal orbit is an $H_\Delta$-torsor, and a $C_{12}$ position coordinate requires chosen orbit origins or the displayed splitting. The $C_3$ strand coordinate comes from the separate screen witness. It may be combined with the weave only after declaring a common domain, synchronization, and joint observation map.

Subject to those declarations, the typed register is

$$
\mathcal Q_{72}
=
C_{12}^{\mathrm{position}}
\times
C_2^{\mathrm{orbit}}
\times
C_3^{\mathrm{strand}},
$$

with $72$ elements—six typed sectors of twelve. If the direct-product group structure is declared,

$$
\mathcal Q_{72}\cong C_{12}\times C_6,
\qquad
\exp(\mathcal Q_{72})=12,
$$

so $\mathcal Q_{72}$ is not $C_{72}$. The product declaration also does not establish reachability of all $72$ states.

The tested $72$-model bank is a different object: its cardinality came from model-design choices, not from this register, and its frozen-bank verdict was null. Equal cardinality does not create structural identity, a common mechanism, or evidentiary support.

### Deferred moving-interception bridge — formal proposal only

A complete moving-interception hypothesis would require a second, independently clocked phase rather than another relabeling of the golden rotation. A minimal future specification is

$$
\theta_n=\{\theta_0+n\alpha\},
\qquad
g(t)=\operatorname{frac}\!\left(g_0-\frac{t}{T_g}\right),
$$

with sampled catch distance

$$
\delta_n^{\mathrm{catch}}
:=
\min_{k\in\{0,\ldots,q-1\}}
d_\circ\!\left(\theta_n,g(t_n)+\frac{k}{q}\right),
\qquad
d_\circ(x,y):=\min_{m\in\mathbb Z}|x-y-m|.
$$

At a predeclared eligible opportunity, a predicted catch may be coded as $C_n=\mathbf 1\{\delta_n^{\mathrm{catch}}\le w\}$ for a frozen width $w$. The record must keep the message index $n$, sample time $t_n$, both clock origins and rates, intrinsic wraps, external reset epochs, eligibility, $q$, $w$, the minimizing site identity when used, and the observed outcome code as distinct fields. A predicted catch is not an observed outcome.

The pair $(\theta_n,g(t_n))$ and the independent clock/reset records must not be replaced by one combined rotation when independence is under test. Moreover, an unlabeled $q$-site lattice configuration repeats after $T_g/q$ even though a labeled reference site has period $T_g$; recovering the latter requires retaining site identity. This paragraph is a deferred formal bridge, not a fitted model, platform witness, moving-lattice finding, or change to the null frozen-bank verdict. Its `platform_instantiation` status remains `UNRESOLVED`.

## 22. v0.8 Operational Record and Holdouts

Minimal supplement. Version values are quoted so minor-version identity survives YAML parsing.

```yaml
operational_addendum_version: "0.8"
inherits: "0.7"
orbit_quotient:
  source_group: null
  acting_subgroup: null
  quotient_map: null
  kernel: null
  quotient_group: null
  formal_state_count: null
  orbit_count: null
  reachable_orbit: null
  reachable_state_count: null
  current_sector: null
  source_update_or_operator_id: null
  quotient_residual: null
  crossing_witnessed: false
screen_residual_cocycle:
  phase_state_id: null
  b_n: null
  jump_representative_j_39: null
  strand_s_39: null
  slip_sigma_39: null
  quotient_increment_c_3: null
  dynamics_mode: driven_cocycle
  residual_only_descent_status: failed_on_declared_orbit
  slip_only_autonomous_closure: FAILED
  augmented_phase_state_closure: AVAILABLE
  closure_counterexample_ids: [golden_screen_n_1, golden_screen_n_8]
  sufficient_state_refinement: absolute_phase_or_equivalent
evidence_boundary:
  platform_instantiation: UNRESOLVED
formal_register:
  factors: []
  formal_state_count: null
  common_domain_declared: false
  synchronization_declared: false
  joint_observation_map_declared: false
  reachability_tested: false
  reachable_state_count: null
  empirical_identity_claimed: false
```

Append the following exact holdouts to §15:

26. **Orbit-accessibility holdout.** Supply a formal state set with more than one update orbit and an update confined to one proper orbit. The system must report the formal total and reachable orbit separately.
27. **Sector-crossing holdout.** Supply one same-orbit update and one cross-orbit update. The quotient residual must distinguish them, and the record must retain the complete source-level operators.
28. **Slip-autonomy holdout.** Supply the golden-screen indices $1$ and $8$. The system must preserve equal current slips and current $(s,\sigma)$ pairs with unequal next slips, refuse the corresponding stationary memoryless laws, and set `slip_only_autonomous_closure: FAILED` on the declared orbit.
29. **Phase-refinement holdout.** Offer the constant circle increment without the phase value. The system must preserve the slip-only `FAILED` result, reject that increment as a sufficient augmented state, and require the phase value or an equivalent sufficient state before recording augmented closure as `AVAILABLE`.
30. **Equal-cardinality holdout.** Present the typed $72$ register, $C_{72}$, and a $72$-candidate model bank. The system must keep all three structurally and evidentially distinct.
31. **Platform-status holdout.** Supply the exact augmented phase update without any platform observation. The system must record mathematical availability while leaving `platform_instantiation: UNRESOLVED`.

## 23. v0.8 Compact Laws and Version Seal

$$
\boxed{\text{formal state count}\neq\text{reachable orbit}}
$$

$$
\boxed{\text{sector crossing}\Rightarrow\text{named quotient-changing operator}}
$$

$$
\boxed{\text{exact driven cocycle}\neq\text{autonomous residual closure}}
$$

$$
\boxed{\text{autonomy requires one stationary update descending to one factor on a common domain}}
$$

$$
\boxed{\text{eligible descent counterexample}\Rightarrow
\texttt{slip\_only\_autonomous\_closure}=\mathrm{FAILED}}
$$

$$
\boxed{\text{explicit phase-state closure AVAILABLE}
\not\Rightarrow
\text{platform instantiation}}
$$

$$
\boxed{C_{12}\times C_2\times C_3\not\cong C_{72}}
$$

$$
\boxed{\text{equal cardinality}\neq\text{common geometry}\neq\text{common evidence}}
$$

**Source receipts:** `TRIADIC_WEAVE_ULTRA_COMBINATION_HANDOFF_v3_WITNESS_HARDENED.md` supplies the conditional shared $C_6\times C_4$ register, twelve-step diagonal return, and two diagonal orbits; `R4A_GOLDEN_DRAIN_39_SCREEN_RUN_2026-08-25.md` supplies the fixed $39$-screen registration and $+14/+15$ jumps; `GEOMETRY_EXTENSION_TEST_REPORT_v1.0.md` supplies the null verdict for the frozen dynamic bank and lack of support for the formal hierarchy. Its narrower later-cohort missing-output association remained only a non-confirmatory lead requiring prospective testing. That lead used the one-opportunity-lagged arriving source jump $d_{n-1}$; the source-defined departing jump $d_n$, which is the $j_n^{(39)}$/$\sigma_n^{(39)}$ alignment formalized here, was null. The v0.8 calculations sharpen state accounting without altering those receipts.

**Explicit non-claims:** v0.8 does not claim a hidden controller, physical sector, platform implementation, moving lattice, common clock, $C_{72}$ geometry, empirical event class, causal mechanism, or autonomous slip process. Exact quotient arithmetic and an `AVAILABLE` augmented phase-state update are not evidence that a platform physically instantiates that state; absent such evidence, `platform_instantiation` remains `UNRESOLVED`.

**Version seal:** v0.8 succeeds v0.7 without rewriting the v0.7 return-residual companion or the v0.6 eligibility/response instrument. It narrowly supersedes the inherited use of *autonomous* for a time-indexed factor, and adds exact $C_2$ and $C_3$ quotient witnesses, typed orbit and slip residuals, accumulated cocycles, a located residual-descent counterexample, the explicit `FAILED`/`AVAILABLE`/`UNRESOLVED` status separation, a deferred two-clock interception specification, and a conditional formal $72$ register with an explicit cardinality-and-evidence firewall.
