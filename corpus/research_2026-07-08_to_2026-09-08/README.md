# Geometry, timekeepers and cosmic time: research archive

Anonymous · 8 September 2026

This archive adds **144 unique readable text snapshots** from Drive records modified between **8 July and 8 September 2026**, inclusive. It includes finished documents and substantive research records, including drafts, corrections, protocols, failed tests and unresolved investigations. Publication does not mean that every research question is finished.

Start with the [catalog](CATALOG.md). The [manifest](manifest.json) records each source's title, Drive identity, creation/modification and retrieval timestamps, available revision, extraction method, byte count and hashes. Three additional source files have identical extracted text and are mapped to one snapshot each. Fifteen source records are represented by existing repository references. Four updated validation scaffolds are archived here alongside, rather than substituted for, their earlier repository versions.

## Reading and evidence boundaries

These are historical source records. Their original draft, speculative, provisional, superseded, `PASS`, `UNRESOLVED`, `NOT_RUN`, `NOT_AUTHORIZED` and other labels remain in the text. Statements that a run was executed or a claim was proved are the source's statements; this bulk archive did not rerun their experiments or audit every proof. A newer timestamp or a source calling itself “current” does not establish precedence over the repository's adopted governing documents. Conflicting versions remain distinct records.

| Lane | What the archive supports | What remains unresolved or unestablished |
|---|---|---|
| Exact geometry and quotient mathematics | Inspectable definitions, derivations, corrections and recorded checks under their stated assumptions | Physical realization, universal geometry or claims beyond those assumptions |
| Toroidal stochastic models | Declared full-state models and separately labeled engineering-validation records | Physical Q2 remains `NOT_RUN`; the historical accepted-update mismatch remains `UNRESOLVED`; production remains `NOT_AUTHORIZED` |
| Cosmic recurrence | Source-bounded exploratory angular calculations, methods and provenance investigations | Causal or predictive effects of planetary patterns; missing original execution provenance |
| Historical timekeepers | Scholarly working records distinguishing calendars, scribal roles, converters, authority and implementation evidence | An inferred common operator, organization, transmission route or historical implementation without independent support |
| Frameworks and symbolic companions | Explicitly labeled conceptual, pedagogical and interpretive records | Promotion of metaphor into theorem, empirical mechanism or institutional fact |
| Embedded research code | Preserved code text and reported receipts | A complete executable package, successful execution or recovered historical software provenance merely from this upload |

### Finite-Markov result: separate audited edition

The proof audit and freshly run supporting checks are in [PR #6](https://github.com/MailanPatternMonkey-ai/Gettin-Started/pull/6), not duplicated or replaced by this archive.

For the specified ideal cosine-weight TD-COS-FH-001 kernel at `J=1`, `t=1/2`, `h_6=0`, in the fixed-reference `Z_000` ensemble with unbounded integer currents, on each fixed cubic torus `L >= 2`, the stationary sector observation `q(X_dn)` has no finite Markov order for every fixed integer spacing `d >= 1`. Attempted microticks, including rejected and identity moves, define the clock. The audited extension excludes an exactly time-homogeneous finite-order sector law under other full-state initializations; time-inhomogeneous finite-order laws are not settled there.

The full state `X=(I,M,q)` remains the specified exact Markov state. No minimality or universal impossibility of finite-dimensional sufficient statistics is established. Finite recorded traces and seeded pseudorandom programs are not the ideal infinite stochastic process. Altered weights, finite-current boxes, accepted-move clocks, adaptive sampling and physical-time dynamics are outside that theorem.

The theorem does not determine physical Q2, global shape, unobserved connectivity, global holonomy, hidden platform geometry or chemistry. The torus and reference cycles are model inputs. Exact-state evidence stays within that boundary.

## Selection and privacy

The date-only inventory contained 629 accessible document records. Keyword searches and title review identified 450 for content retrieval. The publication review used whole-text and native-payload scans plus contextual review of personal references, hyperlinks, relevance and source status. Documents with personal information or uncleared private context were excluded in full: 108 records. Another 179 records were screened out by metadata/topic, 170 retrieved records were outside scope or insubstantial, and nine were unreadable or contained unreviewed non-text content. One source is handled by the separate finite-Markov audit.

Excluded titles, source IDs, excerpts and account-owner metadata are not published. The review is a documented screening process, not a guarantee of anonymity. The selection concerns this upload; it does not retroactively certify or remove material already present elsewhere in the repository.

## Representation and provenance limits

Snapshots are UTF-8 text, not native or binary backups. Native Docs extraction retains paragraph text, tab sections, table text, headers, footnotes, footers, displayed dates and hyperlink targets. Automatic page fields are represented explicitly. Spreadsheet snapshots contain connector-readable table values; original workbook formulas and native functionality are not preserved. Other exports retain connector-readable text rather than the original binary container.

Line endings are normalized to LF and an initial BOM, if present, is removed. The text is otherwise preserved without redaction or prose correction. Exact-duplicate matching uses those normalized bytes, not approximate similarity or whitespace deletion. Distinct revisions and differently extracted exports may therefore remain separate. Native layout, comments and unrepresented features are not certified. Known unreviewed visual or native-equation payloads were excluded.

Source links, relative package references, damaged glyphs and incomplete pasted code remain as recovered. They are not promises that linked files or complete runnable packages are included. Per-file extraction flags identify detected damage and source-ending concerns. Retrieval hashes identify the saved extraction records; snapshot hashes certify the published text, not the truth of its claims or the historical provenance of an asserted computation.

The repository's CC0-1.0 terms continue to apply to contributed work. Public scholarly names, citations and quoted third-party material retain their source attribution; archiving is not a new rights claim over third-party works.

## Verify the archive

From this directory, run:

```bash
python3 verify_archive.py
```

The checker verifies all 144 snapshot byte counts, SHA-256 hashes and Git blob identities, plus duplicate mappings and safe file paths. Its fresh output is in [verification.json](verification.json). This is an archive-integrity check, not a scientific validation run.
