# Using AI across the research lifecycle: An eight-stage guide

Updated: 2026-09-11

## About this document

This guide organizes cognitive neuroscience research into eight connected stages. Each stage explains the research work, useful AI assistance, risks and verification, and a practical check of understanding. The Claude and OpenAI/ChatGPT tables use the same stage numbers throughout.

The lab principle:

> Members of my research team may use AI as much as they like at every stage of research, but each person must be able to answer for the truth and accuracy of the content, and must be able to explain everything that was generated.

Being able to explain includes the evidence for claims, reasons for design choices, what code does to data, and the limits of inference. Members may ask AI to propose, draft, or critique, but must understand and appropriately verify anything they adopt. For trainees, recording an initial judgment before comparing it with AI is one way to practice understanding.

This guide integrates the original lifecycle document's discussion of accountability and verification with the eight-stage discussion document's research tasks. The academic discussion draws on those materials; individual studies were not re-verified for this revision, and precise percentages not rechecked here have been omitted. See the [research synthesis](AI-research-accountability-literature-review-en.md), [annotated bibliography](annotated-bibliography-AI-accountability-epistemics-en.md), and sources below. A [Traditional Chinese version](AI-across-the-research-lifecycle.md) is available.

## Part I: The eight-stage cycle and shared principles

Research moves back and forth: pilot findings can change a design, interpretation can initiate another study, and public scrutiny and replication can reshape the question. Preserve the timing of these decisions so readers can distinguish advance commitments from ideas formed after results became available.

| Stage | Research task | Main verification or deliverable |
|---|---|---|
| 1. Research positioning and question formation | Develop an answerable question from phenomena, theory, and literature | Question memo, sources, exploratory questions and confirmatory hypotheses |
| 2. Research design and planning | Operationalize constructs and plan sampling, quality criteria, and analysis | Design rationale, power or precision planning, analysis and ethics documents |
| 3. Pilot study and method confirmation | Test tasks, equipment, and the complete pipeline | Timing and quality tests, change log, executable pipeline version |
| 4. Registration and formal data collection | Confirm the registered plan and collect data under the approved procedure | Timestamped plan, raw data, experiment and deviation logs |
| 5. Data preparation, preprocessing, and quality control | Create a traceable analysis dataset under explicit rules | Data dictionary, QC reports, exclusions and processing logs |
| 6. Statistical analysis and result evaluation | Estimate effects, uncertainty, and robustness | Reproducible results, code tests, separately labelled confirmatory and exploratory analyses |
| 7. Interpretation, theory revision, and future research | Evaluate alternatives, delimit inference, and plan further tests | Claim–evidence mapping, specific limitations, new hypotheses |
| 8. Reporting, sharing, and scientific communication | Report faithfully, preserve or share materials, respond to review | Manuscript, AI-use statement, reproducibility materials and responses |

Researchers must be able to justify each adopted claim and decision. Fluent explanations and expensive models do not replace evidence. Keep records of substantive AI assistance and verify against original sources, data, simulations, or independent reruns. Specify confirmatory hypotheses, primary analyses, and exclusions in advance; if changes become necessary, retain the original plan, timing, rationale, and information already seen, and disclose deviations or exploration.

Exploration and revision are valuable. The problem is presenting hypotheses developed after seeing results as advance predictions—HARKing—or selecting only the analysis producing a preferred result. Current data can generate new hypotheses, but data already used to develop those hypotheses do not constitute independent confirmation.

## Part II: Research work, AI assistance, and verification

### 1. Research positioning and question formation {#stage-1}

**Research work.** Establish the field, phenomenon, and theoretical background; map agreements, contradictions, and gaps; assess importance and feasibility. Distinguish exploratory questions from confirmatory hypotheses and translate theory into predictions that evidence could contradict.

**AI assistance.** Cluster literature, compare theories, build topic maps, suggest candidate gaps and questions from adjacent fields. Ask what would undermine an explanation or which existing study may already answer the question. Keep a question memo before asking AI for counterexamples so that changes in your judgment remain visible.

**Risks and verification.** AI may fabricate references, overstate agreement, flatter a proposal, or turn an ordinary question into an apparently important gap. The original review's discussion of homogenization and outsourced understanding (Messeri & Crockett, 2024; Tang, 2025) motivates caution without predicting every user's outcome. Check authors, dates, titles, identifiers, and the original texts supporting key claims. People must judge the gap's reality, importance, and feasibility.

**Understanding check.** Without reading AI output, explain why the question matters, how it differs from the closest work, and what evidence would change your view. Keep a memo that links claims to sources.

### 2. Research design and planning {#stage-2}

**Research work.** Translate constructs into measurable variables; choose tasks, manipulations, controls, and behavioral or neural measurements. Examine construct, measurement, and manipulation validity. Plan recruitment, sample size, power or precision, randomization, balancing, counterbalancing, and blinding. Specify QC, exclusions, primary/secondary/exploratory analyses, resources, and ethics documentation.

**AI assistance.** Compare paradigms, identify validity threats and confounds, generate balanced sequences, simulation-based power code, stimuli and task drafts, and clarify the analysis plan. AI may draft or check ethics documents and SOPs, provided the team verifies every commitment and procedure.

**Risks and verification.** Complete formatting can conceal incorrect effect-size definitions, unsupported defaults, or weak operationalization. Ground effect assumptions in literature, pilot data, or explicit scenarios; compare sample requirements when assumptions are uncertain. Test whether simulated data recover known effects and calculate whether sequences are balanced. Simulation checks behavior under assumptions; it does not by itself establish construct validity.

**Understanding check.** Defend key design choices and alternatives, including sample size, exclusion thresholds, and primary analysis. Retain a decision log, analysis plan, and inspectable simulation results.

### 3. Pilot study and method confirmation {#stage-3}

**Research work.** Run the procedure, instructions, stimuli, equipment, triggers, and data recording before formal collection. Check task comprehension, signal quality, artifacts, and the complete preprocessing and analysis pipeline. Return to stage 2 when needed and determine whether ethics documents require updating.

**AI assistance.** Develop and debug experimental software such as PsychoPy, improve instructions, inspect recording fields, draft QC scripts, and explain indicators in fMRIPrep or EEG quality reports. Iterative coding assistance is particularly useful for testing the pipeline.

**Risks and verification.** Plausible code cannot establish actual timing or trigger accuracy; measure these on the equipment and test comprehension with people. Evaluate QC with known problematic and acceptable examples, checking missed and false flags. Processing options create analytic flexibility (Carp, 2012), so record the chosen formal pipeline, parameters, versions, and rationale. If pilot data informed design changes, specify how those data will subsequently be used.

**Understanding check.** Demonstrate measured timing, QC reports, and a full trial run. Explain repaired problems, remaining limitations, and why this version is ready for formal research.

### 4. Registration and formal data collection {#stage-4}

**Research work.** In the applicable preregistration or registered-report process, specify hypotheses, primary outcomes, sampling and stopping rules, exclusions, and analyses. Recruit, screen, obtain informed consent, and run the approved procedure. Record quality, equipment problems, attrition, and deviations; preserve raw data and materials. Registered reports additionally require the journal's prospective review process.

**AI assistance.** Format registration text, identify ambiguous commitments and missing fields, draft recruitment materials, checklists and logs, and assist with routine post-collection QC. Researchers record actual observations and decide how to handle participants and on-site events.

**Risks and verification.** Ensure registration matches the intended study. Preserve the original when a correction requires a new version. Distinguish asking AI to write data-reading code from granting it access to participant files. Names, contact information, consent forms, and potentially identifying DICOM information must follow the approved data process. Local program execution does not establish that an external model receives no file content. Test backup restoration.

**Understanding check.** Compare the registration, SOP, and one experiment log. Explain what followed the plan, when and why deviations occurred, and where raw data and backups are stored.

### 5. Data preparation, preprocessing, and quality control {#stage-5}

**Research work.** Organize participants, conditions, and trials; establish a data dictionary and file structure. Clean behavioral data and handle artifacts, missingness, and outliers in EEG, fMRI, eye-tracking, or other neural data. Apply planned exclusion criteria and preserve the processing decisions linking analysis data to raw records.

**AI assistance.** Help convert BIDS structures, check fields and naming, connect tools such as fMRIPrep, MNE, and EEGLAB, generate exclusion reports and logs, document code, add tests, prepare containers, or refactor scripts. Researchers determine tool suitability and parameter choices.

**Risks and verification.** Incorrect condition mappings, mask spaces, or processing order may alter results without an error. Sample-check participant and trial mappings, inspect before/after data and quality plots, and examine every exclusion reason. Preserve raw data so derived files can be rebuilt. If existing rules fail to handle an unexpected issue, record the change and rationale, assess its consequences, and disclose the deviation; do not tune thresholds for significance.

**Understanding check.** Trace one participant or trial from the original record to the analysis dataset, explaining transformations, parameters, and exclusions. Reproducible execution must be accompanied by checks of correct mapping and logic.

### 6. Statistical analysis and result evaluation {#stage-6}

**Research work.** Inspect descriptive statistics, visualizations, and model assumptions; run planned primary analyses, neural-data models, and multiple-comparison correction. Report effect sizes, confidence intervals, and uncertainty. Conduct secondary, robustness, and sensitivity analyses, labelling exploratory and confirmatory results separately.

**AI assistance.** Draft GLM, mixed-model, MVPA/RSA, and plotting code; explain assumptions; compare reasonable analysis paths; flag departures from preregistration. The different conclusions reached in NARPS (Botvinik-Nezer et al., 2020) motivate reporting analytic choices rather than selecting a favorable result.

**Risks and verification.** Check leakage across cross-validation folds, contrast direction, units of analysis, repeated measures, and correction scope. Use simulated effects as positive controls, and repeated null simulations or permutations to assess error behavior. One nonsignificant shuffled-label run cannot establish correctness. Have a second person rerun or independently implement key analyses. Link figures and reported numbers to outputs. When AI directly labels or scores data, validate against a human-labelled subset and record the model, prompts, settings, and version limitations (Abdurahman et al., 2024).

**Understanding check.** Explain the path from analysis data to the statistic, the assumptions, how tests detect errors, and whether conclusions change across defensible analysis choices.

### 7. Interpretation, theory revision, and future research {#stage-7}

**Research work.** Relate behavioral and neural results to theory and literature; evaluate alternatives, confounds, and generalizability. Distinguish statistical support, psychological interpretation, and causal claims. Activity in a brain region alone does not identify a unique mental process. Plan replications, extensions, or triangulation with different methods.

**AI assistance.** Request strong alternative explanations, gaps between results and conclusions, and evidence that would distinguish competing accounts. Compare new hypotheses and follow-up designs. Recording your own explanation and limitations first helps identify both your blind spots and the model's.

**Risks and verification.** AI criticism can rely on invented references or unsuitable methods. Fluent explanations can also encourage reliance on erroneous judgments (Kim et al., 2025). Check each criticism and explain acceptance or rejection. Make limitations specific to this study. Mark revised hypotheses as needing confirmation and plan independent data or another study.

**Understanding check.** Explain what the study changed in your thinking, the strongest alternative account, and the missing evidence. Justify rejected AI criticism too. Review AI errors and effective checks with the team before the next study.

### 8. Reporting, sharing, and scientific communication {#stage-8}

**Research work.** Write the paper, thesis, or report; assemble figures and supplementary materials; report planned and post hoc analyses, nonsignificant and negative results, and deviations. Share or preserve data, code, materials, and protocols within consent and applicable requirements. Respond to review and enable scrutiny, replication, and extension.

**AI assistance.** Organize the argument, draft, translate, edit, check consistency, prepare READMEs and AI-use statements, and structure responses to reviewers. Researchers must reconstruct the core argument, verify generated content, and decide what to adopt.

**Risks and verification.** Check each method statement against actual execution so AI does not invent procedures. Trace references to original sources or trusted indexes and numbers to analysis outputs. Label exploration and retain uncertainty. Follow submission requirements for disclosing tools, purposes, and verification. Check confidentiality before sharing review material; do not send unauthorized material to external systems. Inspect de-identification, licenses, and files before release, and ask another person to rerun the README.

**Understanding check.** For any paragraph, figure, or response, identify its source, the work actually performed, and the reasoning. Others should be able to reconstruct key results from public or appropriately accessible materials.

### Records and handoff across all eight stages

Match record detail to AI involvement. Simple formatting may need a short note; contributions to hypotheses, code, analyses, figures, or arguments require tool and identifiable model versions, prompts, outputs, edits, and a verifier. State reproducibility limits when versions cannot be fixed. AI-use records, processing logs, and registration deviations serve distinct purposes and should cross-reference one another.

Use consistent questions in meetings and before submission: Can major decisions be explained? When was the confirmatory plan formed? Are exploration and deviations marked? Can sources and numbers be traced? Is material used within its approved scope? Supervisors must support trainees with the domain knowledge and verification resources these checks require.

## Part III: Claude plans and the eight research stages

### Plan overview

Basic prices and features were checked on 2026-09-11; prices are USD. Benefits and limitations below are judgments about research workflows, not measured model rankings. Account availability, usage limits, and promotions can change.

| Plan | Price | Models / capacity | Research-related features | Benefits and limitations | Data handling |
|---|---|---|---|---|---|
| Free | 0 | Sonnet, Haiku; lower allowance | Search, writing, files, code execution | Useful for short trials; limited continuity for debugging | Check consumer privacy settings |
| Pro | 20 monthly; about 17/month annually | Adds Opus; at least 5x Free per five-hour session | Projects, Research, Code, Cowork, Science, Design | Useful for regular work; session and weekly limits remain | Consumer settings |
| Max | From 100/month | 5x or 20x Pro usage | Pro features, higher output limits | Useful for sustained stages 3, 5, 6; justify cost with observed use | Consumer settings |
| Team | Standard 20 annually / 25 monthly; Premium 100 / 125 per seat-month | Standard exceeds Pro; Premium 5x Standard | Shared workspace, search, administration | Useful for teamwork; manage access and costs | No content training by default |
| Enterprise | 20/seat plus usage | Model- and task-dependent billing | Team plus SCIM, audit, retention controls | Useful for governance; budget variable usage | Workspace controls |
| Team plan for scientists | Verified groups: Standard 0; Premium 15/month for 12 months | 1–25 seats; higher Premium allowance | Science, Code, Cowork, shared projects | Lower trial cost; eligibility, places, and promotion not guaranteed | Program and workspace terms |
| Education / API | Institutional quote / separately metered API | Contract or endpoint-specific | Campus deployment / custom batch pipelines | Integration benefits; administration or development required | Check contract, retention, and transfer conditions |

Sources: [Claude pricing](https://claude.com/pricing), [Team plan for scientists](https://claude.com/programs/team-plan-for-scientists). Education and API are different adoption routes; subscription seats should not be treated as API credits.

At the time checked, Fable access carried additional conditions: Pro listed usage credits, while Max listed a weekly-allowance condition. Model availability does not mean unlimited use. Model names do not establish better scientific criticism or correct analysis. Verify platform support and data flows before adopting tools such as Science.

### Eight-stage feature mapping

These are suggested uses of available functions, not guaranteed task counts. Capacity depends on files, model, tools, and task length.

| Stage | Tasks to try with Free | Additional work with Pro / Max | Team / Enterprise use | Verify |
|---|---|---|---|---|
| 1. Research positioning and question formation | Search, theory comparison, counterarguments | Research sources; Projects for context | Shared reading and evidence | References, gaps, significance |
| 2. Research design and planning | Design discussion, short simulations | Code tests, method documents | Approved plans and decisions | Validity, effects, balanced sequences |
| 3. Pilot study and method confirmation | Instructions and QC drafts | Code / Science trial runs and debugging | Capacity for intensive testing | Timing, triggers, quality, pipeline |
| 4. Registration and formal data collection | Registration templates and logs | Projects to compare plans; Code for checks | Approved data and access | Consent, deviations, backups |
| 5. Data preparation, preprocessing, and quality control | Dictionaries and short scripts | Code / Cowork pipelines; Max for longer work | Shared code and processing records | Mappings, parameters, exclusions |
| 6. Statistical analysis and result evaluation | Model explanations and plot drafts | Code / Science tests and sensitivity analyses | Analysis capacity and records | Leakage, numbers, confirmation boundaries |
| 7. Interpretation, theory revision, and future research | Alternatives and criticism | Projects to compare theories and sources | Shared review and next questions | Inference and independent confirmation |
| 8. Reporting, sharing, and scientific communication | Editing, figures, formatting | Research sources; Code for reproducibility materials | Collaborative revision and preservation | Methods, disclosure, permissions, reruns |

### Tradeoffs and data responsibility

Iterative debugging in stages 3, 5, and 6 often consumes more capacity than brief discussion. In stages 1 and 7, evidence and judgment remain decisive. Measure interruptions, completion time, and verification effort on a real task before upgrading. Consider the scientist promotion without assuming eligibility.

Check file permissions individually. A locally executed program may still send content to a remote model. A no-training policy and authorization to upload specific material are separate questions. Handle collaborators' materials, participant data, and review manuscripts under their approved conditions.

## Part IV: OpenAI / ChatGPT plans and the eight research stages

### Plan overview

Basic prices and Work/Codex capacity were checked on 2026-09-11. Chat, deep research, file tools, and Work/Codex can have different availability and limits. Multipliers below concern Codex capacity, not every ChatGPT model or feature.

| Plan | Price | Models / capacity | Research-related features | Benefits and limitations | Data handling |
|---|---|---|---|---|---|
| Free | 0 | Short tasks; account tool limits | Chat and lightweight Work/Codex | Suitable for initial trials; monitor long-task limits | Check personal settings |
| Go | Official listing: 8/month | Lightweight capacity | Everyday and small coding tasks | Lower cost; do not assume all Plus research features | Personal settings |
| Plus | 20/month | Paid baseline Work/Codex allowance | File and coding workflows; available research tools | Starting point for individual work; limits remain | Personal settings |
| Pro | 100 or 200/month | Codex 5x or 20x Plus | Higher-capacity multistep work | Useful for intensive debugging; not all models unlimited | Personal settings |
| Business | Standard 20 annually / 25 monthly per seat-month; higher capacity by quote | Seat allowances, optional credits | Workspace, Work/Codex, SSO/MFA | Team administration; budget seats and usage | Business data not trained on by default |
| Enterprise / Edu | Contact sales | Contract and permission-dependent | Central administration, audit, retention | Institutional governance; not automatic analytical improvement | Institutional agreement |
| API | Separately metered | Separate from ChatGPT subscription | Custom batch annotation, scoring, pipelines | Programmable records; development and validation needed | Check endpoint data controls |

Source: [official Work/Codex pricing](https://learn.chatgpt.com/docs/pricing). Check the product for your account's actual models and features; this table does not guarantee rollout in every region or workspace.

### Understanding research functions and usage

Chat can clarify questions, compare explanations, and inspect text. Source-based search or deep research can support reading, but citations still require original-source checks. Context features such as Projects can hold questions, plans, and documents where available.

Work supports multistep information organization and document creation. Codex supports reading code, modifying pipelines, debugging, running tests, and recording changes. These research applications are workflow recommendations, not certification of neuroimaging or statistical correctness. [Product overview](https://learn.chatgpt.com/docs/overview), [Work usage and cost](https://learn.chatgpt.com/docs/enterprise/chatgpt-work-usage-and-cost).

Work and Codex share usage. Models, input length, reasoning effort, tools, and local/cloud tasks can consume different amounts. Institutional credits may also be shared with other features. Distinguish subscriptions, purchased allocations, and additional invoices. Measure a complete stage 3, 5, or 6 task rather than comparing one nominal message count.

### Eight-stage feature mapping

Use these tasks only within actual feature availability and allowances. Institutional plans primarily add collaboration, permissions, and governance.

| Stage | Tasks to try with Free / Go | Additional work with Plus / Pro | Business / Enterprise / Edu use | Verify |
|---|---|---|---|---|
| 1. Research positioning and question formation | Concepts and candidate questions | Source search, research tools, document comparison | Approved shared readings | References, gaps, questions |
| 2. Research design and planning | Design discussion, small scripts | Codex simulations, balancing, plan checks | Design materials and collaboration | Operationalization, effects, assumptions |
| 3. Pilot study and method confirmation | Instructions and checklists | Codex debugging and tests | Shared tested versions | Timing, QC, complete procedure |
| 4. Registration and formal data collection | Registration and log drafts | Plan, file, and quality checks | Approved connectors and access | Execution, deviations, personal data |
| 5. Data preparation, preprocessing, and quality control | Dictionaries and short scripts | Work / Codex file organization and pipelines | Shared code, standards, usage controls | Mappings, parameters, exclusions |
| 6. Statistical analysis and result evaluation | Models and plot drafts | Codex reruns; Work result organization | Capacity and records | Assumptions, numbers, leakage |
| 7. Interpretation, theory revision, and future research | Alternatives and criticism | Cross-document comparison and design drafts | Shared reflection and context | Reverse inference, evidence, new tests |
| 8. Reporting, sharing, and scientific communication | Editing and formatting | Work documents; Codex reproducibility materials | Collaboration, access, preservation | Methods, citations, disclosure, reruns |

### Tradeoffs and data responsibility

For occasional reading, questions, and writing, first determine whether an existing account completes the work. Compare Plus and Pro capacity when coding sessions become sustained. Consider institutional plans when collaboration or governance requires them. A plan name does not establish that a tool is approved for a particular participant dataset.

Apply the same research criteria to both providers: explain adopted content, trace sources, validate code, distinguish exploration from confirmation, and use materials within authorization. Additional capacity can reduce waiting; evidence must still support conclusions.

## Sources and verification scope

The research discussion integrates the project's original lifecycle guide with `research-stage-ai-Luna-light-Fable51-Extra.md` in the adjacent research folder. References inherited from the original review are in the [annotated bibliography](annotated-bibliography-AI-accountability-epistemics-en.md); the individual studies were not re-verified for this revision. The eight-stage source additionally supplies:

- Carp, J. (2012). On the plurality of (methodological) worlds: Estimating the analytic flexibility of fMRI experiments. *Frontiers in Neuroscience*, 6, 149. [DOI](https://doi.org/10.3389/fnins.2012.00149).
- Botvinik-Nezer, R., et al. (2020). Variability in the analysis of a single neuroimaging dataset by many teams. *Nature*, 582, 84–88. [DOI](https://doi.org/10.1038/s41586-020-2314-9).

Official product sources appear beside the relevant sections and were checked on 2026-09-11. Prices, capacity, and features change. Confirm retention and deployment conditions for the actual product, account, and institution. Stage mappings and upgrade suggestions are judgments about workflows, not results of a comparative model-performance experiment.
