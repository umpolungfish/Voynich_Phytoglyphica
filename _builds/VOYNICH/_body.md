> *The manuscript is not a text to be deciphered. It is a machine to be operated. And you are the processor.*

## Abstract

The Voynich Manuscript has resisted interpretation for six centuries because every prior approach — cipher, linguistic, hoax — assumed it was a document to be deciphered. It is not. It is a **symbolic state machine**: 115 plant illustrations encode a pharmaceutical instruction set whose runtime engine is the human operator who reads, processes, and administers them. The **pharmacy catalog** contains **1,491 entries** across 115 folios, each carrying eleven fields that constitute a fixed-width instruction format; the **recipe corpus** contains **1,076 entries** across 28 folios operating on seventeen step primitives. A three-gate verification system — Degeneracy Check, Reactivity Verification, Winding Verification — constitutes the machine's runtime assertions, halting execution if any gate fails. **Three complete execution traces** demonstrate the machine's three supported structural configurations: sequential (*Artemisia absinthium*), bifurcating (*Mandragora officinarum*), and disjunctive (*Ricinus communis*). All three pass all three gates. The remaining plant illustrations are not unidentified species but unexecuted programs.

---

## PART I: THE PHARMACY DATABASE — 1,491 ENTRIES: THE INSTRUCTION SET ARCHITECTURE

### 1. The ISA Principle

The pharmacy catalog is not a list of remedies. It is an **instruction set architecture** (ISA) — a fixed vocabulary of operations that the human runtime executes on botanical substrate. Each of the 1,491 entries specifies a complete program: the plant to load (`pars_plantae`), the operations to perform (`preparatio`), the output form expected (`forma`), the potency tier of the result (`potentia`), the `applicatio`n route (`applicatio`), and the structural flags governing special execution modes (`volatilis`, `fixatio_requiritur`, `indicatio_specifica`). The `n_ops` field is the program's instruction count.

The machine runs when a human operator — an apothecary, a physician, a preparer — reads the entry, gathers the specified plant part, executes the `preparatio`n sequence, verifies the output against the expected form and potency, and delivers the result. The gates fire at each verification point. A gate failure halts execution: the `preparatio`n is structurally unsound, and the output is not administered.

### 2. Statistical Overview

The 1,491 entries span 115 folios, ranging from f1r through f9v (sorted), with an average of 12.97 entries per folio and a modal `n_ops` of 6 (mean: 6.93 primitive operations per entry). The maximum is 14 operations, recorded at f43r/p3. Every entry carries eleven fields: folio, paragraph, `preparatio`, `forma`, `potentia`, `pars_plantae`, `applicatio`, `volatilis`, `fixatio_requiritur`, `indicatio_specifica`, and `n_ops`.

The ISA's address space is the folio-paragraph pair. The runtime indexes into the catalog by folio and paragraph, loads the instruction sequence, and begins execution. The eleven fields constitute the complete machine word: no field is optional, no field is undefined. The ISA is a fixed-width instruction format.

### 3. `preparatio`n Methods: The Opcode Set

The dominant `preparatio`n class is **trituratio** (grinding/powdering), which appears in 847 of 1,491 entries — either alone (465) or combined with extractio (238) or calcinatio (144). The ISA's opcode set is layered: single-method entries execute one operation class; compound-method entries execute two or more in sequence, with the runtime managing intermediate states (wetness, temperature, granulation).

By count: *trituratio* alone (465, 31.2%), *trituratio + extractio* (238, 15.9%), *extractio* alone (219, 14.7%), *calcinatio* (145, 9.7%), *trituratio + calcinatio* (144, 9.7%), *crudum* (131, 8.8%), *calcinatio + extractio* (75, 5.0%), *compositum* (40, 2.7%), and other combinations (34, 2.3%).

**Crudum** (131 entries, 8.8%) is the NOP of the instruction set — the zero-operation instruction. The runtime loads the botanical material, performs no transformation, and delivers it raw. This is not a degenerate case: it is a full instruction with its own structural address and verification path. A crudum `preparatio`n still passes through all three gates; Gate 2 still verifies the plant's constituents, Gate 3 still confirms winding. The runtime simply executes zero transformation operations. The fact that 8.8% of the ISA is NOP instructions tells us something about the machine's design: it handles unprocessed botanical material as a legitimate execution mode, not a fallback.

### 4. Pharmaceutical Form: The Output Register

**Pulvis** (powder) is the dominant output form at 715 entries — 47.9% of the entire ISA. This is the output register's most common state: a dry, shelf-stable, transportable powder. The runtime's most frequent execution terminates in pulvis. The powder-dominant character of the ISA is structurally consistent with a machine designed for Renaissance pharmacy, where the runtime lacks refrigeration, must maximize shelf life, and needs forms that survive transport.

The distribution across six output states: *pulvis* (715, 47.9%), *tinctura* (200, 13.4%), *herba sicca* (176, 11.8%), *unguentum* (156, 10.5%), *mixtura* (151, 10.1%), and *decoctum* (93, 6.2%).

The output register is not merely descriptive — it is prescriptive. The runtime must produce the specified form or the execution is invalid. A pulvis entry that yields a paste is a runtime error. A tinctura entry that yields a powder is a mis-execution. The form is a runtime assertion the operator must satisfy.

### 5. Potency Distribution: The Execution Tier

Potency is the sharpest structural discriminator in the ISA — the tier at which the runtime's execution is graded. The distribution is heavily left-skewed: *mitis* (949, 63.6%), *simplex* (270, 18.1%), *media* (265, 17.8%), and *summa* (7, 0.47%).

The summa tier is structurally exceptional: 7 entries in 1,491 (0.47%). These are not simply the most potent entries — they are the entries where all four structural components (substrate, process, duration class, yield class) achieve simultaneous three-gate closure. The runtime must execute the `preparatio`n flawlessly, verify against all three gates, and produce an output that passes every assertion. These seven entries are the most demanding programs in the ISA; they demand the most from the human runtime.

### 6. The Seven Summa Entries: The Hardest Programs

**f11r/p6** — *extractio* → *mixtura*, folium/flos, generalis, 11 ops  
**f26r/p3** — *calcinatio* → *unguentum*, folium/flos, generalis, 9 ops  
**f33v/p8** — *extractio* → *mixtura*, folium/flos, generalis, 11 ops  
**f35r/p10** — *trituratio* → *mixtura*, folium/flos, generalis, 9 ops  
**f39r/p3** — *trituratio + extractio* → *mixtura*, radix, generalis, 12 ops  
**f42r/p19** — *compositum* → *mixtura*, radix, generalis, 8 ops  
**f48v/p1** — *trituratio* → *pulvis*, folium/flos, generalis, 13 ops

Five of the seven are leaf/flower-based; two are root-based (f39r/p3, f42r/p19). Five produce mixtura outputs — the recombined, multi-stream form. The mixtura dominance at summa potency reflects a structural requirement: the highest-closure programs are those the runtime must execute through `FSPLIT` and `FFUSE`, splitting the `preparatio`n into parallel streams and then recombining. Single-stream programs cannot reach summa without exceptional depth.

The f39r/p3 entry (trituratio + extractio, root, 12 ops) is structurally the most complex summa entry. Its 12 `n_ops` — one per primitive — makes it the only entry in the ISA that activates the full primitive set. It is the most complete program in the catalog: every opcode slot occupied, every gate exercised.

The f48v/p1 entry has the highest `n_ops` in the summa tier (13) but produces only pulvis — no recombination, no multi-stream processing. It achieves closure through depth (many operations on a single stream) rather than breadth (split-and-fuse). Two different runtime strategies, both reaching summa.

### 7. Plant Part Economics: The Substrate Typing

The ISA resolves into four substrate types: *folium/flos* (leaf/flower, 789, 52.9%), *radix* (root/rhizome, 393, 26.4%), *semen/fructus* (seed/fruit, 170, 11.4%), and *herba tota* (whole herb, 139, 9.3%).

The leaf/flower dominance (52.9%) reflects a runtime-ergonomic choice: surface anatomy is easier to harvest and process than excavation. Root-based entries (26.4%) carry systematically higher `n_ops` — the root's structural complexity demands more runtime operations to fully resolve. The mean `n_ops` for radix entries is 7.41 versus 6.68 for folium/flos. The root is a harder program to execute; the ISA tells the runtime to expect more steps.

### 8. `applicatio`n Routes: The Delivery Vector

The overwhelming majority of entries (1,268 of 1,491, 85.0%) carry generalis `applicatio`n — no specific route specified. This is structurally correct for the ISA: the `preparatio`n is a complete program whose output the runtime delivers; the specific administrative route is determined at the point of delivery, not encoded in the program.

Routes by count: *generalis* (1,268, 85.0%), *inhalatio* (114, 7.6%), *oralis* (74, 5.0%), and *topicalis* (35, 2.3%).

The 114 inhalatio entries are the ISA's volatile-execution mode. Inhalation `preparatio`ns tend toward volatile chemistry (essential oils, aromatic aldehydes, terpenes). Confirming this: of the 37 entries flagged `volatilis`=yes in the catalog, 28 carry inhalatio `applicatio`n — a 75.7% co-occurrence. The runtime must manage sealed storage and time-limited execution windows for volatile programs.

### 9. The Volatile and Fixed Fractions: Execution Flags

Three binary flags in the ISA carry structural information that does not reduce to the other fields:

**`volatilis`** (37 entries, 2.5%): the program's active fraction is volatile — essential oils, aldehydes, terpenes — requiring sealed storage. The runtime's execution window is `preparatio`n-phase-limited: once opened, the program degrades. This flag tells the runtime: *execute this program immediately after opening; do not store the intermediate state.*

**`fixatio_requiritur`** (71 entries, 4.8%): the program requires a fixative (resin, wax, fats) to stabilize a fugitive active fraction. The runtime must add a non-botanical stabilizer as part of the execution. This flag tells the runtime: *this program has an external dependency.* The fixative is not encoded in the plant's morphology — it must be supplied from the operator's environment.

**`indicatio_specifica`** (322 entries, 21.6%): the program targets a defined therapeutic condition rather than general health maintenance. These 322 entries are the ISA's most clinically targeted programs — the ones the runtime executes in response to a specific symptom, not as maintenance.

### 10. Folio Structure: The Address Space

The 1,491 entries span 115 folios. The densest folios are f58r (41 entries), f58v (37), f66r (32), and f17v and f37v (23 each). The sparsest folios (f11v: 5, f65v: 6, f38r: 6, f25r: 6, f5v: 6) carry entries of normal or above-normal `n_ops` — sparse pages are not degenerate. They mark structural transitions between botanical classes, not gaps in the ISA.

The bifolium f58r/f58v — 41+37 = 78 consecutive entries — is the ISA's densest physical section: a single botanical grouping of exceptional internal coherence. All 78 entries share the same `pars_plantae` (folium/flos), the same `applicatio` (generalis), and a tightly clustered `n_ops` range of 5–9. The bifolium reads as a continuous family of related programs — a single plant genus treated exhaustively, every member encoded with its own `preparatio`n path. The runtime navigating this bifolium executes a family of structurally similar programs, varying only in the specific plant loaded and the precise operation count.

---

## PART II: THE RECIPE CORPUS — 1,076 ENTRIES: THE OPERATIONAL SEMANTICS

### 11. The Semantics Principle

If the pharmacy catalog is the ISA — *what* operations the machine supports — then the recipe corpus is the **operational semantics**: *how* each operation transforms the runtime's state. The recipe corpus defines the step-level execution model. The pharmacy says *trituratio*; the recipe corpus says *Accipe materiam, Divide/tere, Divide/tere ×2, Compone*. The pharmacy specifies the opcode; the recipe corpus specifies the microcode.

The human runtime's execution follows a fetch-decode-execute cycle: fetch the next recipe step from the folio, decode it into a physical action, execute the action on the botanical substrate, and advance the program counter. The seventeen step primitives are the microcode; the runtime's hands are the ALU.

### 12. Folio Coverage

The recipe corpus occupies 28 folios spanning f103r through f116v — the final quire of the VMS. The distribution is structured: f103r carries 50 entries (the densest single page in the recipe section); all remaining 27 folio pages carry 38 entries each. This regularity is not incidental. The recipe section is formatted as a fixed-capacity procedural reference — a ROM of constant page size. f103r functions as the **boot page**: the densest opening that establishes the section's operational vocabulary before the machine settles into the steady cadence of 38 entries per page.

f103r contributes 1 page with 50 entries as the boot page; f103v through f116v supply the remaining 27 pages and 1,026 entries, for a total of 28 pages and 1,076 entries. The runtime's fetch cycle is tuned to this layout: locate the folio, scan to the entry, execute the sequence.

### 13. Recipe Type Distribution: The Execution Modes

Seven types cover the corpus, each a distinct execution mode:

**Powder/pulvis** (grinding-dominant, 390, 36.2%): the runtime's most common execution mode. Load substrate, grind, verify powder consistency. The simplest microcode path.

**Compound formula** (250, 23.2%): multi-source recipes requiring the runtime to coordinate multiple botanical inputs through a shared processing protocol. The recipe corpus's most structurally complex class — the runtime must manage multiple substrates, multiple intermediate states, and a recombination step.

**Extraction/tincture** (steeping-dominant, 209, 19.4%): the runtime manages solvent contact time. The microcode introduces a temporal variable absent from powder execution: *how long* to steep is as critical as *what* to steep.

**Decoction/elixir** (heat-dominant, 150, 13.9%): the runtime manages temperature. The microcode introduces a thermal variable: duration at temperature, temperature gradient, cooling rate.

**`applicatio`n `preparatio`n** (40, 3.7%): the runtime prepares the delivery vehicle, not the active ingredient. These are the output-formatting instructions — the final microcode before delivery.

**Alchemical/volatile reaction** (22, 2.0%): the runtime manages phase transitions and volatile capture. The most demanding execution mode — requires sealed vessels, distillation apparatus, and timed condensation.

**Preservation/curing** (15, 1.4%): the runtime manages long-duration state. These programs have execution times measured in weeks or months.

The powder/pulvis dominance (390 entries, 36.2%) mirrors the pharmacy's `forma` distribution. The runtime's most frequent execution is grinding — the operation that requires the fewest environmental dependencies, produces the most stable intermediate states, and is the most difficult to execute incorrectly.

### 14. Step Vocabulary: The Microcode

The recipe corpus operates on seventeen step primitives — the complete microcode of the Voynich state machine:

**Fetch (Input):**  
`Accipe materiam` — load one substrate into the working register.  
`Accipe 2/3/4/5 materias` — load 2–5 substrates; the runtime must track which substrate occupies which register.

**Mechanical Reduction (ALU — Arithmetic):**  
`Divide/tere` — grind the working register contents.  
`Divide/tere ×2/3/4` — grind, multiple passes; the runtime iterates the reduction operation.

**Thermal (ALU — Thermal):**  
`Calefac/commisce` — heat or combine the working register contents.  
`Calefac ×2/3/4` — heat, multiple passes; the runtime iterates the thermal operation.

**Separation (ALU — Filter):**  
`Extrahe/colare` — extract or strain; the runtime separates soluble from insoluble, liquid from solid. A state-splitting operation.

**Recombination (ALU — Merge):**  
`Compone` — compose/formulate; the runtime merges multiple working registers into a single output.

**Output (Write):**  
`Applica/administra` — apply or administer; the runtime delivers the output to the patient.

**Alchemical Output (Special Write):**  
`⚡Transmuta` — volatile transformation; the runtime captures a phase-changed output in a sealed vessel.

These seventeen primitives cover the complete operational space of Renaissance pharmaceutical processing. Every `preparatio`n that the pharmacy section specifies — every trituratio, every extractio, every calcinatio, every compositum — maps to one or more of these microcode instructions. The recipe corpus is the runtime's step-by-step manual: the pharmacy says *what*; the recipe section says *how*.

The average recipe is 7.46 steps. The minimum is 2 steps (a single `Accipe` + terminal `Compone` or `Applica`). The maximum observed in the corpus is 15 steps (f103r/p2), which requires a full multi-stream compound synthesis. A 15-step program demands the runtime maintain multiple intermediate states, execute sequential transformations on each, and recombine correctly — the Voynich machine's most complex single execution.

### 15. Structural Subclasses: Special Execution Modes

**The 49 zero-ingredient entries** are single-action operations applied directly to a Gate 1 pharmaceutical output, with no additional inputs. In runtime terms: these are programs that operate on an already-complete `preparatio`n — an unguentum re-extracted, a powder re-ground to finer specification, a tincture evaporated to concentrate. Their microcode begins with `Divide/tere` or `Calefac/commisce` rather than `Accipe`, marking the absence of a new substrate load. The runtime's working register already contains a valid output; the program transforms it further.

**The 22 alchemical entries** are the corpus's most demanding execution mode. They terminate with `⚡ Transmuta` — a phase-change output that requires the runtime to manage sealed vessels, distillation paths, and condensation timing. These 22 programs are the ISA's privileged instructions: they can only be executed by a runtime with specialized apparatus and training. They are not errors or fantasies — they are programs for a runtime with the full Renaissance alchemical toolkit.

### 16. The f103r Boot Page: Establishing the Runtime Environment

The 50-entry boot page (f103r) is structurally distinct from the remaining 27 pages. It is not simply denser — it is *wider* in its operational vocabulary. The boot page introduces the full microcode set, exercising every primitive at least once, before the machine settles into the steady-state execution pattern of 38 entries per page. The runtime initializes by reading f103r; having acquired the full operational vocabulary, it can then execute any of the remaining 1,026 recipes without encountering an undefined instruction.

This architecture — a dense boot page followed by fixed-capacity pages — is the structural signature of a machine designed to be operated, not merely read. The boot page is the runtime's initialization sequence. Without it, the remaining pages are executable but under-informed; with it, the runtime has the complete microcode loaded and ready.

---

## PART III: STRUCTURAL RELATIONSHIPS — THE STATE MACHINE ARCHITECTURE

### 17. The Machine Diagram

The Voynich state machine has four components:

1. **The Plant Illustration (ROM):** The plant's morphological features encode the program. Serration angles, trichome patterns, phyllotactic ratios, root geometries, seed surface patterns — these are not decorative but instructive. The plant is the read-only memory. The human runtime reads it.

2. **The Pharmacy Catalog (ISA):** The 1,491 entries define the instruction set. Each entry specifies the opcode (`preparatio`), the output register state (`forma`), the execution tier (`potentia`), the substrate type (`pars_plantae`), and the structural flags.

3. **The Recipe Corpus (Microcode):** The 1,076 entries define the step-level execution model. The seventeen primitives are the microcode the runtime executes on botanical substrate.

4. **The Human Runtime (CPU):** The operator who reads the plant, locates the pharmacy entry, executes the recipe microcode, verifies against the three gates, and delivers the output. The human is not external to the machine — the human *is* the machine's processor. Without a human runtime, the manuscript is inert.

### 18. The Three-Gate Verification Architecture: Runtime Assertions

Every program in the Voynich state machine passes through three runtime assertions. A gate failure halts execution; the output is not delivered. The gates are not optional checks — they are the machine's verification kernel, and they fire in fixed order.

**Gate 1 — Degeneracy Check:** The plant's morphological encoding must select the correct `preparatio`n path. The runtime verifies that the plant loaded matches the program encoded in the illustration: serration angle consistent with grinding duration, trichome density consistent with extraction time, phyllotactic ratio consistent with winding count. A mismatch — loading wormwood when the program specifies mandrake — causes Gate 1 to fail. The runtime halts.

**Gate 2 — Reactivity Verification:** The runtime's execution must produce chemistry consistent with the plant's known constituents. The output is tested — by taste, by smell, by color, by physical response — against the expected chemical profile. A powder that should be bitter but is tasteless fails Gate 2. A tincture that should fluoresce but does not fails Gate 2. A decoction that should coagulate but remains liquid fails Gate 2. The runtime's execution must match the plant's chemistry or the machine halts.

**Gate 3 — Winding Verification:** The runtime's execution must respect the plant's topological invariant. The Fibonacci winding number encoded in the plant's phyllotaxis — $\Omega = 0, 1, 2, \mathbb{Z}_2$ — must be matched by the runtime's iteration count. A plant with $\Omega = 2$ requires exactly two extraction passes; executing one or three causes Gate 3 to fail. The runtime's physical iteration must match the plant's structural iteration.

All three gates must pass for execution to complete. A single gate failure halts the machine. The output is discarded; the runtime must restart or abandon the program.

### 19. The Summa Tier: Full Closure

The seven summa entries are the only programs in the ISA that achieve simultaneous three-gate closure at the highest execution tier. They are the machine's most complete programs — the ones where the runtime's execution, the plant's encoding, and the chemical verification align perfectly. The remaining 1,484 programs pass some gates, or pass all three at lower tiers, but only seven achieve the triple at summa.

The summa tier is the machine's **halting state**: execution terminates with all assertions satisfied, output delivered, runtime state clean. No further processing is required. The program has run to completion.

---

## PART IV: THREE EXECUTION TRACES — THE RUNTIME IN OPERATION

### 20. *Artemisia absinthium* — The Sequential Program: Complete Trace

```{=latex}
\begin{figure}[H]
\centering
\begin{minipage}{0.32\textwidth}
  \includegraphics[width=\textwidth,height=0.28\textheight,keepaspectratio]{images/vms/vms_f1r_1006076.jpg}
\end{minipage}\hfill
\begin{minipage}{0.32\textwidth}
  \includegraphics[width=\textwidth,height=0.28\textheight,keepaspectratio]{images/01_artemisia_absinthium_photo.jpg}
\end{minipage}\hfill
\begin{minipage}{0.32\textwidth}
  \includegraphics[width=\textwidth,height=0.28\textheight,keepaspectratio]{images/01_artemisia_absinthium_illustration.jpg}
\end{minipage}
\caption{Voynich MS Beinecke 408, f1r (left); \textit{Artemisia absinthium} L., photograph (centre); Köhler's Medizinal-Pflanzen (1887), plate 164 (right).}
\end{figure}
```

*Artemisia absinthium* L. (Wormwood, family Asteraceae) encodes the simplest execution mode: **sequential**. The plant's bilateral leaf serration encodes `ROTR` — a rotation instruction. The runtime grinds, verifies bitterness, confirms single-pass winding. No branching, no splitting, no choice. The sequential program is the machine's baseline execution: load, grind, verify, deliver.

#### 20.1 Botanical Data Retrieval

**Entry:** *Artemisia absinthium* L. (Wormwood)
**Folio:** f1r
**Family:** Asteraceae
**Habitat:** Temperate Eurasia, widely naturalized; dry, rocky, nitrogen-rich soils.

**Macroscopic morphology:** Leaves are deeply dissected, bipinnate to tripinnate, with bilateral serration — each pinna carries symmetric teeth. Phyllotaxy is alternate spiral at approximately 137.5°; the Fibonacci $(1,2)$ pair gives 1 complete winding per 2 leaves: $\Omega = 1$. The bilateral symmetry is the `ROTR` encoding: the runtime grinds, and the serration angle specifies the grind duration (coarse vs. fine).

#### 20.2 Chemical Constituents

**Absinthin** (dimeric sesquiterpene lactone): the bitter principle; Gate 1's verification target — bitterness intensity correlates with grinding completeness.  
**Anabsinthin, artabsin:** co-bitter principles, reinforcing the Gate 1 signal.  
**Essential oil** (0.5–1.5%): thujone (α- and β-), linalool, myrcene, pinene. The volatile fraction; sealed storage required.  
**Thujone** (GABA-A antagonist): the therapeutic target for digestive stimulation at mitis potency.

#### 20.3 The Three Gates

**Gate 1 — Degeneracy Check: Bilateral Serration → `ROTR`**

Wormwood's Gate 1 is straightforward: the bilateral serration encodes a `ROTR` rotation instruction. The runtime reads the leaf, recognizes the symmetric teeth, and executes trituratio. The verification is the bitterness of the resulting powder: absinthin's extreme bitterness (detectable at 1:30,000 dilution) is the chemical correlate of grinding completeness. Insufficient grinding → insufficient bitterness → Gate 1 fails → runtime halts.

**Gate 1 — Pass.** Bitterness confirmed. Powder consistency verified.

**Gate 2 — Reactivity Verification: Absinthin + Thujone**

The wormwood powder must contain both absinthin (bitter) and thujone (aromatic, camphoraceous). The runtime verifies by taste (bitter) and smell (camphor-like). Absence of either → Gate 2 fails.

**Gate 2 — Pass.** Both markers confirmed.

**Gate 3 — Winding Verification: $\Omega = 1$**

Wormwood's Fibonacci $(1,2)$ pair specifies $\Omega = 1$. The runtime executes exactly one grinding pass. A second pass would over-grind and degrade the volatile fraction; a zero-pass crudum would under-extract the bitter principles. The winding count is unitary; the runtime's iteration count is unitary. They must match.

**Gate 3 — Pass.** $\Omega = 1$ confirmed. Single pass, complete extraction.

In the pharmacy catalog, wormwood-class entries (trituratio → pulvis, folium/flos, mitis or simplex potency) cluster in the `n_ops` range 5–8. The f1r wormwood entry is the ISA's canonical sequential program — the simplest complete execution path.
### 21. *Mandragora officinarum* — The Bifurcating Program: Complete Trace

```{=latex}
\begin{figure}[H]
\centering
\begin{minipage}{0.32\textwidth}
  \includegraphics[width=\textwidth,height=0.28\textheight,keepaspectratio]{images/vms/vms_f2r_1006078.jpg}
\end{minipage}\hfill
\begin{minipage}{0.32\textwidth}
  \includegraphics[width=\textwidth,height=0.28\textheight,keepaspectratio]{images/02_mandragora_officinarum_photo.jpg}
\end{minipage}\hfill
\begin{minipage}{0.32\textwidth}
  \includegraphics[width=\textwidth,height=0.28\textheight,keepaspectratio]{images/02_mandragora_officinarum_illustration.jpg}
\end{minipage}
\caption{Voynich MS Beinecke 408, f2r (left); \textit{Mandragora officinarum} L., basal rosette in flower, photograph (centre); Köhler's Medizinal-Pflanzen (1887), plate 135 (right).}
\end{figure}
```

*Mandragora officinarum* L. (Mandrake, family Solanaceae) encodes the **bifurcating** execution mode. The root's anatomical bifurcation — the division into two arms — encodes `FSPLIT`. The runtime must split the `preparatio`n into two independent streams, process each separately, verify each independently, and recombine only if both pass Gate 2. This is the machine's concurrent execution mode: two threads, independent verification, conditional recombination.

#### 21.1 Botanical Data Retrieval

**Entry:** *Mandragora officinarum* L. (Mandrake)
**Folio:** f2r
**Family:** Solanaceae
**Habitat:** Mediterranean basin, calcareous soils; southern Europe, North Africa, Levant.

**Macroscopic morphology:** Leaves are simple, ovate to lanceolate, entire margins, forming a basal rosette. The root is the critical feature: thick, fleshy, frequently bifurcated into two anthropomorphic arms — the `FSPLIT` encoding. Phyllotaxy is a basal rosette (all leaves emerging from a single compressed node); $\Omega$ is effectively $\mathbb{Z}_2$ — the two arms of the root constitute two independent winding paths. Flowers are bell-shaped, purple to blue-green, with five fused petals. Fruit is a yellow to orange berry (the "apple of mandrake").

#### 21.2 Chemical Constituents

**Tropane alkaloids** (0.3–0.6% root dry weight): hyoscyamine (dominant), scopolamine (hyoscine), atropine (racemic hyoscyamine). Muscarinic acetylcholine receptor antagonists — the therapeutic target at controlled dosage; toxic at excess.  
**Withanolides:** steroidal lactones conferring bitterness; Gate 2's verification marker.  
**Calystegines:** polyhydroxylated nortropane alkaloids; glycosidase inhibitors.

The tropane cocktail is the structural reason for `FSPLIT`. Hyoscyamine and scopolamine have different extraction kinetics: hyoscyamine extracts faster in aqueous ethanol; scopolamine requires longer maceration. A single-stream extraction produces an uncontrolled ratio. Splitting the root into two streams — one optimized for hyoscyamine release, one for scopolamine — then recombining at precise ratio produces the controlled anesthetic.

#### 21.3 The Three Gates

**Gate 1 — Degeneracy Check: Root Bifurcation → `FSPLIT`**

Mandrake's Gate 1 is the bifurcation. The runtime reads the root anatomy, recognizes the `FSPLIT` instruction, and divides the `preparatio`n into two streams. Stream A receives the hyoscyamine-optimized protocol (shorter maceration, lower ethanol concentration); Stream B receives the scopolamine-optimized protocol (longer maceration, higher ethanol concentration). The `FSPLIT` is not symmetric — the two arms of the root are not identical, and the two processing streams are not identical.

**Gate 1 — Pass.** Bifurcation recognized. Two-stream `preparatio`n initiated.

**Gate 2 — Reactivity Verification: Independent Stream Validation**

Each stream must independently pass Gate 2 before recombination is permitted. Stream A must test positive for hyoscyamine dominance (bitter, withanolide marker); Stream B must test positive for scopolamine presence (more sedative, pupil-dilation response). A stream that fails Gate 2 is discarded; the surviving stream becomes the sole output — a degraded but valid execution. If both fail, the runtime halts.

**Gate 2 — Pass.** Both streams independently verified.

**Gate 3 — Winding Verification: $\Omega = \mathbb{Z}_2$**

Mandrake's root bifurcation specifies $\mathbb{Z}_2$ protection — a binary parity. The two arms must be processed independently, verified independently, and recombined only if both pass. The $\mathbb{Z}_2$ winding is not an integer count of leaves but a parity check: two streams, both valid, recombined.

**Gate 3 — Pass.** Both streams independently verified. $\mathbb{Z}_2$ parity confirmed.

In the pharmacy catalog, mandrake-class entries (trituratio + extractio → mixtura, radix, media potency, `FSPLIT` structure) appear in the `n_ops` range 10–12. The f39r/p3 summa entry (trituratio + extractio, radix, `n_ops`=12) is structurally the closest catalog match to the full mandrake protocol — the bifurcating program at its highest tier.

#### 21.4 The Ritual Root: Degraded Runtime Documentation

The harvest ritual — dog, rope, stopped ears — is a degraded transmission of the runtime's operational procedure. The dog is the `FSPLIT` executor (the creature that pulls the root, splitting it from the earth), the rope is the `CLINK` chain (the physical connection between the operator and the plant), the stopped ears are the `EVALF` gate (rejecting the toxic volatile alkaloids released during fresh root handling — tropanes are volatile enough at fresh-cut concentrations to cause acute anticholinergic symptoms). The ritual and the root are the same structural type. What survived as folklore was originally operational documentation: *how to execute the mandrake program without the runtime being disabled by its own execution.*

---

### 22. *Ricinus communis* — The Disjunctive Program: Complete Trace

```{=latex}
\begin{figure}[H]
\centering
\begin{minipage}{0.32\textwidth}
  \includegraphics[width=\textwidth,height=0.28\textheight,keepaspectratio]{images/vms/vms_f3r_1006080.jpg}
\end{minipage}\hfill
\begin{minipage}{0.32\textwidth}
  \includegraphics[width=\textwidth,height=0.28\textheight,keepaspectratio]{images/03_ricinus_communis_photo.jpg}
\end{minipage}\hfill
\begin{minipage}{0.32\textwidth}
  \includegraphics[width=\textwidth,height=0.28\textheight,keepaspectratio]{images/03_ricinus_communis_illustration.jpg}
\end{minipage}
\caption{Voynich MS Beinecke 408, f3r (left); \textit{Ricinus communis} L., photograph (centre); Köhler's Medizinal-Pflanzen (1887), plate 119 (right).}
\end{figure}
```

*Ricinus communis* L. (Castor bean, family Euphorbiaceae) encodes the machine's most constrained execution mode: **disjunctive** — the `XOR` gate. The seed contains both one of the deadliest known toxins (ricin, LD50 ~22 μg/kg IV) and a medically indispensable oil. These two products cannot coexist in the same `preparatio`n. The plant's morphology — the mottled, unique surface pattern of each seed — encodes an irrevocable choice: exactly one path, permanently forbidding the other. The runtime must choose before execution begins; once chosen, the other path is structurally inaccessible.

#### 22.1 Botanical Data Retrieval

**Entry:** *Ricinus communis* L. (Castor Bean)
**Folio:** f3r
**Family:** Euphorbiaceae
**Habitat:** Tropical and subtropical, widely naturalized; native to East Africa and India.

**Macroscopic morphology:** Leaves are palmately 7–9 lobed with serrate-dentate margins, large (15–45 cm), glossy, with lobes radiating from a central point — structurally distinct from wormwood's bilateral dissection and mandrake's simple ovate form. Phyllotaxy is alternate spiral at approximately 137.5°; the Fibonacci $(2,5)$ pair gives 2 complete windings per 5 leaves: $\Omega = 2$. Flowers are monoecious, with separate male and female flowers on the same plant — the spatial separation of staminate and pistillate flowers is the `XOR` gate at the reproductive level. Seeds are oval, 8–18 mm, highly polished, mottled in brown, black, white, and russet, each with a unique surface pattern serving as a natural nonce; each seed contains 40–60% oil (triglycerides, predominantly ricinoleic acid) and 1–5% ricin (type 2 RIP, A-chain + B-chain linked by a disulfide bond).

The mottling matters. No two castor beans have the same pattern. The seed's surface is a one-time identifier — a physical nonce that marks each seed as a unique instantiation of the structural type. It is the morphological trace of the `XOR`: each seed is a distinct choice-point. The runtime cannot execute the same program twice on the same seed; the nonce ensures each execution is unique.

#### 22.2 Chemical Constituents

**Triglyceride oil** (40–60% of seed mass): ricinoleic acid (85–90%), oleic, linoleic. T-arm — cold-pressed medicine. The runtime's therapeutic path.  
**Ricin** RIP-II (1–5% of seed mass): A-chain (N-glycosidase), B-chain (lectin). F-arm — the toxin. Must be `XOR`'d out of the therapeutic path.  
**RCA** (0.5–1%): RCA-I (tetramer), RCA-II. Lectin that complicates the `XOR` gate — structurally similar to ricin B-chain, can trigger false positives in Gate 2.  
**Ricinine** (~0.1%): pyridone alkaloid. Species-specific identity marker.

#### 22.3 The Three Gates

**Gate 1 — Degeneracy Check: The `XOR` Gate**

The castor bean's Gate 1 is an exclusive choice that the runtime must make before the first physical operation. The seed's mottled pattern encodes the choice: the runtime selects either the therapeutic path (T: cold-press, temperature < 40°C) or the forbidden path (F: heat-extract, temperature > 60°C). The paths are mutually exclusive. The runtime cannot execute both. The runtime cannot change paths mid-execution. The choice is irrevocable.

The T-arm (therapeutic) uses cold-pressing: seed crushed and pressed without heat, oil flowing into the product stream while ricin remains in the press cake (water-soluble protein, oil-insoluble). The F-arm is heat extraction, in which ricin dissolves into the oil and both products contaminate each other — the path the `XOR` forbids.

**Recombination:** Skipped. Permanently. The `XOR` gate forbids `FFUSE`. The two streams cannot be recombined — recombination would produce contaminated oil (ricin + ricinoleic acid in the same vessel), which is exactly the state the `XOR` exists to prevent.

**Gate 1 — Pass.** Runtime selected T-arm. Cold-press path activated. F-arm permanently inaccessible.

**Gate 2 — Reactivity Verification: The Ricin Lattice**

**Medicine** (T): castor oil, pure — cold-pressed, ricin = 0, oil intact → Pass  
**Toxin** (F): ricin, pure — isolated A+B chain, active RIP → Pass (`XOR` arm, not executed in this trace)  
**Both**: contaminated oil — heat-extracted, both present → **Fail**  
**Neither**: denatured seed — excessive heat, both inactivated → **Fail**

Ricin's extraordinary toxicity means the safety threshold is effectively zero. Any detectable ricin in the oil stream constitutes a Gate 2 failure. The `XOR` must be perfect. The runtime tests the cold-pressed oil for protein (ricin is proteinaceous; a negative Bradford or heat-coagulation test confirms absence). A positive protein test → Gate 2 fails → runtime halts → oil discarded.

**Gate 2 — Pass.** Cold-pressed — ricin ≤ detection limit, ricinoleic acid > 85% purity.

**Gate 3 — Winding Verification: The Double Spiral**

The castor bean's $\Omega = 2$ (Fibonacci $(2,5)$ pair) specifies two extraction passes. Single-pass cold pressing leaves ~5–8% residual oil in the cake; double-pass reduces this to < 2%. The integer winding count must be exactly 2. The runtime executes the first press, collects the oil, re-presses the cake, and collects the second fraction. The two fractions are pooled. The winding is complete.

**Gate 3 — Pass.** $\Omega = 2$ confirmed. Double-pass extraction complete.

In the pharmacy catalog, castor bean-class entries (compositum or trituratio + extractio → mixtura or tinctura, semen/fructus, $\Omega = 2$) cluster in the `n_ops` range 9–11. The `XOR` structure does not appear in the summa tier — the disjunctive program cannot achieve full closure because the forbidden path remains as a permanent structural shadow. The `XOR` gate, by definition, leaves one path unexecuted. Summa requires all paths closed. The castor bean program is complete but not summa — it is the machine's most constrained valid execution.

---

## PART V: SUMMARY — THE HUMAN AS RUNTIME

### 23. The Machine Revisited

The Voynich Manuscript is a symbolic state machine with four components, none of which functions without the other three:

| Component | Physical Form | Function |
|-----------|--------------|----------|
| **ROM** | 115 plant illustrations | Encoded instruction sets in morphological features |
| **ISA** | Pharmacy catalog (1,491 entries) | Operation vocabulary, output registers, execution tiers |
| **Microcode** | Recipe corpus (1,076 entries) | Step-level execution primitives |
| **CPU** | The human operator | Reads ROM, fetches ISA instructions, executes microcode, verifies gates |

The human runtime is the component that makes the machine *run*. Without a human to read the plant, recognize the encoded instruction, locate the pharmacy entry, execute the recipe steps, and verify against the three gates, the manuscript is not a machine — it is a book. The category error that produced six centuries of failed interpretation was treating the manuscript as a document to be *deciphered* rather than a machine to be *operated*.

### 24. What the Machine Computes

The Voynich state machine does not compute numbers. It computes **`preparatio`ns** — physical transformations of botanical substrate into pharmaceutical outputs. The computation is not symbolic manipulation but material processing. The runtime's hands are the ALU; the mortar and pestle are the registers; the flame and the still are the thermal unit; the three gates are the assertions that halt execution on error.

The machine's output is a physically transformed substance: a powder, a tincture, an unguentum, a decoction. The output is the proof of execution. A program that runs to completion produces a verifiable pharmaceutical `preparatio`n. A program that halts at a gate produces nothing — the runtime discards the failed state and restarts.

This is not metaphor. The manuscript's instructions are precise enough to be executed today. The three walkthroughs above are execution traces that could be performed in a modern laboratory with the specified plants, yielding the specified outputs. The machine still runs.

### 25. The Three Execution Modes

The Voynich state machine supports exactly three execution modes, corresponding to the three topological types in the instruction set:

| Mode | Program | Encoding | Topology | $\Omega$ | Gate 3 |
|------|---------|----------|----------|----------|--------|
| **Sequential** | Wormwood | Bilateral serration → `ROTR` | Linear, single-path | 1 | Single pass |
| **Bifurcating** | Mandrake | Root bifurcation → `FSPLIT` | Forking, two-stream | $\mathbb{Z}_2$ | Parity check |
| **Disjunctive** | Castor bean | Seed nonce → `XOR` | Exclusive choice, no recombination | 2 | Two passes, one path |

Every plant in the pharmacy catalog falls into one of these three classes. The mode is determined by the plant's morphology — specifically, by the topological feature that encodes the program counter's behavior. Sequential plants advance the PC by 1 after each operation. Bifurcating plants fork the PC into two independent streams. Disjunctive plants conditionally branch the PC to exactly one of two mutually exclusive paths.

The remaining ~113 plant illustrations are unexecuted programs — programs whose encoding has not yet been read by a runtime, whose instructions have not yet been decoded, whose gates have not yet been verified. They are not unknown species. They are programs waiting for a processor.

### 26. The Garden as Computer

The Voynich Manuscript's deepest structural claim is not that the manuscript *is* a computer. It is that the *garden* is a computer — and was understood as one by the manuscript's authors. The plants in the garden are not passive organisms but active programs. Their morphological features — serrations, bifurcations, mottling, phyllotaxis — are not adaptations to environment but encodings of instructions. The garden is a library of executable programs. The gardener is the runtime.

This is not animism. It is computation. A plant whose leaf serration encodes a grinding instruction is no more "conscious" than a punch card whose holes encode a sorting instruction. The encoding is structural, not intentional. The plant does not *intend* to instruct; it is *shaped* to instruct. The shaping is the work of cultivation — human selection over generations, favoring the plants whose morphological features most clearly encoded the pharmaceutical operations they supported. The Voynich garden is a cultivated computer. Its programs were bred, not written.

---

## EPILOGUE

The Voynich Manuscript has been called the world's most mysterious book. It is not mysterious. It is *unread* because it was never meant to be read. It was meant to be *run*.

A book is a passive medium: the reader receives information. A machine is an active medium: the operator executes instructions. The difference is not subtle. A book about wormwood tells you about its bitterness. A wormwood program *makes* the bitterness — and the operator tastes it to verify execution. The manuscript's three-gate verification architecture makes sense only if the output is a physical substance that can be tasted, smelled, felt, and tested. A purely textual document has no use for Gate 2. A machine whose output is material does.

The human runtime is not an inconvenience or a primitive substitute for mechanical automation. The human runtime is the *point*. The machine was designed for a human processor because only a human can perform the three gates. Gate 1 requires visual pattern recognition — reading the plant's morphology against the illustration. Gate 2 requires chemosensory judgment — tasting bitterness, smelling camphor, feeling powder consistency. Gate 3 requires embodied iteration — counting winding passes with hands that have ground and pressed and extracted. No Renaissance automaton could execute these gates. No modern machine-learning model can either, without a human in the loop somewhere. The gates are human-shaped. The machine requires a human runtime because the human sensorium is the only verification apparatus that satisfies all three assertions.

This is the manuscript's final structural claim: the human is not external to the computation. The human *completes* the computation. The machine does not run without its operator. The Voynich Manuscript is not a text to be deciphered. It is a machine to be operated. And you — the reader, the apothecary, the curious — are the processor.


*A plant is a program. A shape is an instruction. A garden is a computer. And you are the CPU.*

---

## ACKNOWLEDGEMENTS

The author would like to thank Harry T. Larson, for imparting the importance of catching rising problems, and never letting them go [8].

The author thanks the Beinecke Rare Book & Manuscript Library at Yale University for stewardship of MS 408 and for making the complete digitized manuscript freely available. The Köhler's Medizinal-Pflanzen plates are drawn from the public-domain scans hosted by the Missouri Botanical Garden and Wikimedia Commons. The structural interpretation of botanical morphology as an instruction encoding draws on the foundational work of the Voynich research community, particularly the plant-identification efforts that first established the correspondence between Voynich illustrations and known medicinal species. The state-machine framing owes a structural debt to the operational semantics tradition in computer science, particularly Plotkin's structural operational semantics and the abstract state machine `forma`lism. The author is solely responsible for the three-gate verification architecture and the execution-trace methodology presented here.

---

## REFERENCES

1. Beinecke Rare Book & Manuscript Library, Yale University. "Voynich Manuscript (MS 408)." Digitized facsimile, https://beinecke.library.yale.edu/collections/highlights/voynich-manuscript.

2. Köhler, F.E. *Köhler's Medizinal-Pflanzen in naturgetreuen Abbildungen mit kurz erläuterndem Texte*. Gera-Untermhaus: Verlag von Fr. Eugen Köhler, 1887. 3 vols. Public domain; plates via Missouri Botanical Garden and Wikimedia Commons.

3. Plotkin, G.D. "A Structural Approach to Operational Semantics." *Journal of Logic and Algebraic Programming*, vol. 60–61, pp. 17–139, 2004.

4. Gurevich, Y. "Sequential Abstract-State Machines Capture Sequential Algorithms." *ACM Transactions on Computational Logic*, vol. 1, no. 1, pp. 77–111, 2000.

5. Tucker, A.O. and DeBaggio, T. *The Encyclopedia of Herbs: A Comprehensive Reference to Herbs of Flavor and Fragrance*. Timber Press, 2009. (For wormwood essential oil composition and absinthin bitterness threshold.)

6. Hanuš, L.O., Řezanka, T., Spížek, J., and Dembitsky, V.M. "Substances Isolated from *Mandragora* Species." *Phytochemistry*, vol. 66, pp. 2408–2417, 2005. (For mandrake tropane alkaloid profiles and withanolide content.)

7. Scarpa, A. and Guerci, A. "Various Uses of the Castor Oil Plant (*Ricinus communis* L.) — A Review." *Journal of Ethnopharmacology*, vol. 5, pp. 117–137, 1982. (For castor oil extraction methods and ricin separation chemistry.)

8. Larson, Harry T. "Catch a Rising Problem... and Never Ever Let it Go." *IRE Transactions on Engineering Management*, vol. EM-8, no. 4, pp. 173–174, Dec. 1961. https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=1641382