# The Hidden Quotient in Operational Pipelines

## An exact addendum for normalization, calibration, transformation, outcome coding, eligibility, and response fidelity

**Status:** exact finite constructions plus architectural consequences and an empirical-instrument repair  
**Version:** v0.6 — eligibility and response-fidelity refinement  
**Date:** 2026-08-31  
**License:** CC0 — Public Domain — No rights reserved  
**Continuity:** preserves v0.5, v0.4, v0.3, and its v0.2 predecessor, and extends *The Hidden Quotient Behind the Multiplication Representation* and *The Hidden Quotient in Lattice Charts, Topological Return, and Prime-Gap Projection* v0.1

> **Claim boundary.** The constructions below do not identify software controllers, conversational events, evidence ledgers, dyadic room conditions, lattices, or measure spaces as one mathematical object. They share diagnostic questions, not proof status. Theorems in the multiplication representation do not validate a dyadic architecture or an empirical event classification. Sections 11–12 retain the v0.5 instrument as a historical receipt; §13 supplies the governing v0.6 repair.

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
