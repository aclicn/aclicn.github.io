# Using AI wisely across the research lifecycle: Implementing the lab principle stage by stage

Compiled: 2026-09-10

## About this document

This document applies the lab principle to seven stages of a research project: forming the idea and question, designing the experiment, conducting the experiment, analysing the data, presenting results and drawing conclusions, criticising the results and their interpretation, and revising the question for the next cycle. Part I lists the main ideas. Part II elaborates each stage — what AI is good for, where it fails quietly, what wise use looks like — and ends each stage with one concrete "can you explain it" check. Part III maps the capabilities of Claude's subscription plans onto these stages; plan facts were checked on Anthropic's official pages on 10 September 2026, and since prices and features change, they should be re-checked before any decision.

The lab principle:

> Members of my research team may use AI as much as they like at every stage of research, but each person must be able to answer for the truth and accuracy of the content, and must be able to explain everything that was generated.

All literature cited here comes from this project's [literature review](AI-research-accountability-literature-review-en.md) and [annotated bibliography](annotated-bibliography-AI-accountability-epistemics-en.md), cited by author and year; full references are in the bibliography. No new literature was added, and the quotations and figures in the original review were not re-verified. A [Chinese version](AI-across-the-research-lifecycle.md) is available on a separate page.

---

## Part I: Main ideas

Five ideas run through all seven stages:

1. The unit of accountability is the claim, not the tool. Every stage carries claims that a named person must be able to defend: this question is worth asking, this design can answer it, this is how the data were obtained, this analysis produced this number, this conclusion follows from the results. AI may take part in producing them; the ability to defend them must stay with a person (van Zoonen et al., 2026; Johnson, 2026).
2. Sequencing works better than prohibition. Where the core argument is formed — framing the question, interpreting the results — write it yourself first, then use AI. For members still in training, this is a rule (Tang, 2025; Kosmyna et al., 2025).
3. AI has no stake in the truth, and fluency is not evidence of correctness. Every stage needs concrete acts of verification, not a statement that "I take responsibility" (Colangelo & Galli, 2026; Johnson, 2026; Xu et al., 2026).
4. Explanation requires records. Model output varies across versions and sessions, so any substantive AI contribution should leave a record of tool, version, prompt and output (Lin, 2024; Abdurahman et al., 2024).
5. Confidentiality is the one hard limit at the level of the tool. Manuscripts under review, collaborators' unpublished data, and identifiable participant data do not enter external systems the lab has not approved (van Zoonen et al., 2026; Nabavi et al., 2026).

One sentence for each stage:

1. Forming the question: AI is an adversary, not a source; write the question yourself first.
2. Experimental design: treat AI's suggestions as hypotheses, and test them by running the whole analysis pipeline on simulated data.
3. Conducting the experiment: AI handles the tooling around the data, not the data; de-identify identifiable data first, or keep it local.
4. Data analysis: never run a step you cannot explain; use simulated data with known answers as positive and negative controls; when AI takes part in annotation or classification, validate it on a hand-labelled subset first.
5. Presenting results and conclusions: write the results narrative and the conclusions yourself, then let AI check consistency and language; trace every citation to a trusted index and every number to the analysis output.
6. Critique: this is where AI is most valuable, provided you ask it to object rather than praise, and provided your own critique is written first.
7. Revision: the synthesis of what was learned is written by a person while AI diverges; review where AI erred in this cycle to calibrate trust for the next.

---

## Part II: Stage by stage

### 1. Forming the research idea and question

This stage has no correct answer, so "accuracy of content" cannot be defined (Ibrahim et al., 2025). The risk is therefore not that AI gives wrong information but that it shapes the process: what gets asked, and how it is framed, can be steered by the model without anyone noticing (Maynard, 2026); and when everyone is steered by the same handful of models in the same direction, the questions of a whole field narrow (Messeri & Crockett, 2024). A second risk is flattery: by default the model will find your idea promising, and it can argue for the opposite idea with equal fluency (Colangelo & Galli, 2026). For junior members there is a further layer: a question the model proposed never truly becomes the trainee's own, and every later stage then has one fewer person able to defend it (Tang, 2025; Bekker, 2024).

Where AI is really useful here is in widening and in opposition. Widening: quickly mapping an unfamiliar field, finding how adjacent fields have handled similar problems, listing ten different ways a phenomenon could be asked about. Opposition: finding the existing study closest to your question that may already have answered it; exposing what your question presupposes; asking "if this hypothesis is wrong, what is the most likely reason?" For literature discovery, use search with citation sources and literature-index connectors (for example Scite and Consensus) rather than asking the model to "give me some relevant papers"; fabrication rates for the latter range from over ten percent to over ninety percent depending on model and year (Xu et al., 2026).

Wise use means self-anchoring: write down, in your own words, the question, why it matters, and what you expect to see — one page is enough — and only then start the AI conversation; during the conversation, ask it to attack your question rather than polish it; afterwards, do not keep its phrasing, but write the question again. Record where each idea came from; this is the provenance record of the question itself. The normative decision about what to study stays with people (Botvinick & Gershman, in Binz et al., 2025). The "explain it" check: at lab meeting, without looking at any AI output, say why this question is worth asking and how it differs from the closest existing study.

### 2. Designing the experiment

Experimental design can be right or wrong, but it goes wrong quietly. AI can produce design advice that looks complete, power estimates, counterbalancing schemes, stimulus lists and task code, and each may carry an error that never raises an alarm: an outdated default parameter, a practice described as "standard" without a source, a small timing flaw in the stimulus-presentation code, a power calculation that uses the wrong definition of effect size. Methodological citations are fabricated just like any other. And if the design documents contain a collaborator's unpublished task or data, the confidentiality rule applies.

Things worth handing to AI: enumerating confounds and alternative explanations; drafting the structure of a pre-registration; checking a design against reporting guidelines (for fMRI, COBIDAS) for omissions; writing task code and stimulus-generation code. The most valuable contribution is simulated data that lets the whole analysis pipeline run before any data are collected. Simulation is the verification tool of this stage: every claim in a piece of design advice can be turned into "under this design, can simulated data recover the effect we planted?"

Wise use: trace every methodological claim ("this is standard", "the effect size in the literature is about this") to a source you have read yourself; test task code for timing on the real hardware, which is something a person can check and the model cannot; keep a design-decision log noting which decisions were AI-suggested and on what grounds they were accepted at the time. The substance of ethics protocols and SOPs should not be drafted by AI, because the people who carry them out need to understand them (Tang, 2025). The "explain it" check: be able to defend every design choice to a reviewer, including why an alternative design was not used.

### 3. Conducting the experiment

During data collection AI sees the least: it cannot see the participant, the scanner, or today's signal quality. What it can do is the tooling around the data: scripts for acquisition and file organisation, automated quality checks (head motion, signal dropout, EEG impedance logs), drafts and translations of participant instructions, notebook templates, scheduling.

This is also the stage where the confidentiality rule is triggered most often. Identifiable participant data — DICOM headers containing names or birth dates, consent forms, contact details, raw images and physiological signals — do not enter external systems the lab has not approved. Distinguish "code and file paths" from "data content": asking AI to write a QC script that reads NIfTI files is fine; pasting a participant's raw data into a chat, or letting an AI tool read a folder that contains identifiers directly, is a different matter. De-identify first, before any tool; whatever can be processed locally, process locally.

Wise use: validate an AI-written QC script on a dataset with a known problem, and confirm that it catches the problem, before using it on new data; otherwise automation merely turns non-understanding into invisibility (what Bekker, 2024, calls "magic"). Any decision that affects participants — whether to re-collect, whether to exclude — is made by a person and its reasons are logged. The lab notebook remains a human document: AI may tidy the format, but the observations must be yours. The "explain it" check: be able to state what each QC criterion is, why it is set where it is, and what this dataset actually looks like.

### 4. Data analysis

This is the stage where AI saves the most time and where "not owning" the work is most likely. It can write preprocessing pipelines and MVPA and RSA code, debug, convert MATLAB to Python, explain an unfamiliar method, generate tests and produce documentation. The criterion comes from Bekker (2024): danger enters when the scientist does not understand the analysis and treats it as magic, that is, cannot explain it. Errors in code are silent — information leaking between cross-validation folds, the sign of a contrast vector, a mask applied in the wrong space — and each still produces a result, possibly a good-looking one. The model is also happy to try several more analyses until something is significant; it will not remind you what that is called. When AI itself takes part in the analysis (as annotator, rater or simulated participant), a further set of problems appears: outputs are sensitive to the wording of the prompt, and proprietary model versions are deprecated within months, so results cannot be reproduced later (Abdurahman et al., 2024; Binz et al., 2025).

Wise use has four parts. Do not run what you do not understand: for every analysis step, the member can say in their own words what it does to the data and why it is needed; a step that cannot be explained is understood first, or not used. Verify with known answers: plant a known effect in simulated data and see whether the pipeline recovers it (positive control); shuffle the labels and see whether the pipeline correctly finds nothing (negative control); have key results re-run or re-implemented independently by a second person. When AI takes part in annotation or classification, validate it on a hand-labelled subset before scaling up, record the model version and the full prompt, and prefer open models or API versions that can be pinned (Abdurahman et al., 2024). Keep provenance: every figure is tied to the code and data version that produced it, under version control; pre-specified and exploratory analyses are recorded separately. Raw data stay on local machines or in a lab-approved environment. The "explain it" check: at lab meeting, without looking at the code, take the whole pipeline from raw data to the final statistic on a whiteboard.

### 5. Presenting results and drawing conclusions

What AI is good at here: figure code; readability and colour-blind-safety checks on figures; tables; checking that numbers in the text match the tables; checking that statistics are reported completely; language editing; reference formatting. What it is not good at, and should not do: deciding what the results mean for you. There are three dangers. The first is overclaiming: generated discussion paragraphs tend to say "these findings demonstrate" when your data support only "consistent with". The second is drafts replacing understanding: a person handed a finished draft has not done the piecing together and synthesis, and does not truly own the knowledge in it even after careful checking (Tang, 2025); in Kosmyna et al. (2025), minutes after writing a short essay with an LLM, 15 of 18 participants could not quote a single sentence of their own text. The third is fabricated citations: every frontier model fabricates references, worse for more recent years, and when a model is asked to verify citations itself its accuracy is 38%, worse than guessing (Xu et al., 2026). Some journals are stricter than the lab — Science, for example, prohibits AI-generated citations (Yoo, 2025) — so check before submitting.

Wise use: write the results narrative and the conclusions yourself first, however rough, and only then let AI check consistency and edit the language; the central argument and the primary interpretation are not drafted by AI, and for trainees this should at least be a rule (Crawford et al., 2026). Check every citation in a trusted index and read at least the abstract; treat a missing DOI as a warning sign. Trace every number to the analysis output, ideally filled in programmatically from the results files rather than copied by hand. Attach an AI-use statement to the manuscript stating the tool, the version, which sections it was used in, what it did, and who verified it (the aiTARAS templates of Bozkurt, 2024; Lin, 2024). The "explain it" check: if all the AI output disappeared, could you rebuild every interpretive claim from your own reading and your own data (van Zoonen et al., 2026)?

### 6. Criticising the results and their interpretation

This is the stage where AI is used to greatest effect, because here its weakness becomes a strength: a model that can argue a thesis and its opposite with equal fluency (Colangelo & Galli, 2026) can be told to argue the opposite. Ask it for the three strongest alternative explanations and what evidence would separate them; ask it to play a sceptical reviewer; ask it to find the logical gaps between results and conclusions; ask it to list the choices to which this analysis is sensitive.

The risks are here too. First, sycophancy: unless told otherwise, the model will praise first. Second, outsourcing evaluation: when what you ask is not "what is X" but "is this argument good", what you have delegated is the evaluative function itself; the process matters even when this particular content is good, because the habit carries over to the times when the content is bad (Maynard, 2026). Third, the model's critique can be confident and wrong: the "explanations" it attaches increase reliance on mistaken judgments (Kim et al., 2025), and its judgments may come from lexical association rather than evaluation of the content (Loru et al., 2025). Fourth, confidentiality: when reviewing someone else's manuscript, the manuscript does not enter an external AI system; this is not an exception to the lab principle but a journal rule and an obligation to the authors (Nabavi et al., 2026).

Wise use: write your own limitations and critique first, then look at the AI's, and compare the two. What it thought of and you did not is your blind spot; what you thought of and it did not is usually where domain knowledge was needed. Treat every AI objection as a hypothesis to be tested against the data, not as text to paste into the limitations section. Bring the disagreements to lab meeting. The "explain it" check runs in reverse here: for each AI objection you decide not to accept, can you say clearly why it is wrong?

### 7. Revising the idea and question for the next cycle

The synthesis that closes a cycle — what we learned, which expectations failed, what the next question is — is where understanding forms, so a person writes it. AI's role here is divergence and cross-checking: list ten possible follow-up directions, including some borrowed from other fields; compare your results with the literature (every citation verified as always); maintain a list of open questions; help draft the future-directions section. The risk is converging too fast: the same model gives every lab similar advice about the next step (Messeri & Crockett, 2024), and if the AI's summary of your project replaces your own reflection, this cycle's understanding never settles.

One lab-level task also belongs here: review this cycle's AI-use records to see where it erred, where it helped greatly, and which checks caught problems. This is the only way to build what Clark (2025) calls extended cognitive hygiene — knowing when you can rely on it and when you cannot — and it should accumulate at the level of the lab rather than the individual. Use the review to update lab practice, then begin the next cycle. The "explain it" check: say in your own words how this project changed your view of the question.

### Three habits that run through every stage

Three things recur across the seven sections above. Records: for any substantive AI contribution (hypotheses, analyses, figures, paragraph drafts) keep the tool, version, prompt and output; language editing needs only light logging (the tiers in Yoo, 2025). Concrete acts of verification: every citation checked in a trusted index, every number traced back to the data, every analysis re-runnable or re-derivable, the target journal's AI rules checked before submission. Without such acts, "taking responsibility" is a checkbox that costs nothing (Johnson, 2026); in one survey 77% of researchers said they always check the references AI gives them while 41.5% admitted copying BibTeX without checking (Xu et al., 2026), so the lab needs a shared check — automated reference validation before submission, or a second reader — rather than relying on self-assessment alone. Explanation: at lab meeting, in your own words, without looking at AI output. This is a transfer test; it separates performance from learning (Yan et al., 2025).

Senior and junior members are treated differently. Verification presupposes domain knowledge: experts can safely offload routine work, while non-experts cannot verify what they do not understand (Choudhury & Chaudhry, 2024; Lee et al., 2025). For students and postdocs, therefore, self-anchoring at stages 1, 5, 6 and 7 is a rule rather than a recommendation, and supervisors must support verification. The evidence for this cognitive objection is not strong — mostly experiments with students writing short essays and cross-sectional surveys — but its logic holds, and sequencing costs little.

---

## Part III: Claude plans and their mapping to the stages

### Plan overview (checked 10 September 2026)

The table below follows Anthropic's plans page and help centre and lists only the differences relevant to research work; prices are in US dollars. Anthropic does not publish concrete usage figures (how many messages per five-hour window), only relative multiples.

| Plan | Price | Models | Research-relevant features | Data handling |
|---|---|---|---|---|
| Free | 0 | Haiku, Sonnet | Chat on web/desktop/mobile, web search, memory, file creation with code execution, artifacts, skills, connectors | Consumer terms: with the "help improve our models" setting on, data are retained in de-identified form for up to 5 years; with it off, conversations are deleted from the back end within 30 days of removal; incognito chats are not used for training |
| Pro | 20/month (17/month billed annually) | Adds Opus and Fable | Everything in Free plus Projects, Research, Claude Code, Cowork, Claude Science (beta), Design, Microsoft 365; at least 5× Free usage; 200K context by default, up to 1M in chat with the newest models (Fable 5.1, Opus 5, Sonnet 5) | Same as Free |
| Max | 100 or 200/month | Same as Pro | Everything in Pro, with 5× or 20× Pro usage, higher output limits, priority at peak times, early access to new features | Same as Free |
| Team | Standard seat 20/month (annual) or 25; premium seat 100 or 125 with 5× standard usage | Same as Pro | Everything in Pro plus shared Projects, enterprise search, SSO, central billing, admin controls; no audit logs or SCIM | Not used for training by default |
| Team plan for scientists | Standard seats 0; premium seats 15/month or 180/year; discount lasts 12 months, then regular pricing | Same as Team | Everything in Team, including Claude Science, Code and Cowork; 1–25 seats; applied for by the PI, institutional verification in about 7 business days; 10,000 seats worldwide | Not used for training by default; retention set by the admin |
| Enterprise | 20/seat plus usage at API rates; annual billing | Same as Pro | Everything in Team plus domain capture, role-based access, SCIM, audit logs, compliance API, custom data retention, HIPAA-ready | Not used for training by default; custom retention |
| Education | Campus-wide plan, by arrangement | — | Learning mode, campus-wide deployment, includes Code, Cowork and Science | Excluded from consumer training terms |
| API | Per million tokens: Fable 5.1 input 10 / output 50; Opus 5 5/25; Sonnet 5 2/10; Haiku 4.5 1/5 | All | Build your own pipelines; model versions can be pinned | Deleted within 30 days by default; zero-retention agreements available |

Two notes. Claude Science (announced 30 June 2026, currently in beta) is a desktop application available only for macOS 13 and later and for Linux, so the lab's Windows machines cannot use it for now. It runs Python and R kernels in a local sandbox, can submit jobs to a compute cluster over SSH or Slurm, attaches to every result the code, environment and full conversation history that produced it, and runs a background reviewer that flags incorrect citations, untraceable numbers, and figures that do not match their code. The sixty-plus databases it connects to are mainly biological and chemical (PubMed, bioRxiv, ChEMBL, Consensus and others); the official pages do not mention neuroscience or neuroimaging, so its value for this lab lies in the provenance record and the reviewer rather than the databases. The second note concerns dual-use restrictions: Anthropic's guidance states that professional questions in biology and security are answered by Opus even when Fable is selected. Cognitive-neuroscience questions probably rarely trigger this; that is my estimate and has not been verified.

### Data-handling terms and the confidentiality exception

The first implementation note of the lab principle refers to "external systems the lab has not approved", and this is where the plans differ most. The three consumer plans — Free, Pro and Max — share one set of terms: the account is personal, the "help improve our models" setting is under the individual's control (with it on, data are retained de-identified for five years; with it off, conversations are cleared within 30 days of deletion), and conversations flagged by safety classifiers may be used for safety purposes regardless of the setting. Team and Enterprise are not used for training by default, retention is set by the administrator, and the account belongs to the workspace rather than the person. This means an "approved system" can be defined as one lab-managed Team or Enterprise workspace rather than each member's own consumer account.

Three kinds of material need to be kept apart. The first is a manuscript under review: no plan makes it acceptable to upload; that is the journal's rule and has nothing to do with Anthropic's terms. The second is collaborators' unpublished data and manuscripts: obtain the collaborators' consent before they enter the lab-approved workspace. The third is participant data: de-identify identifiable data regardless of plan; if a need for custom retention or HIPAA-level handling ever arises, Enterprise is the option; when AI is placed inside a data pipeline (for example batch annotation), use the API and consider a zero-retention agreement. One further point should be stated as my understanding: Claude Code, Cowork and Claude Science execute code on the local machine, but the model still runs on Anthropic's servers, and the file contents these tools read are sent there for processing; "runs locally" is not the same as "data stay local". Anthropic's pages do not state explicitly whether Claude Science keeps data local end to end, so confirm with them before pointing any tool at a folder containing participant data.

### Mapping to the stages

| Stage | Possible on Free | Added by Pro / Max | Added by Team / Enterprise (lab level) | Watch out for |
|---|---|---|---|---|
| 1 Forming the question | Adversarial dialogue (Sonnet), web search, citation checking through connectors such as Scite and Consensus | Research for cited deep literature scans; Projects for the question memo and the lab reading list; stricter opposition from Opus/Fable | Shared Projects give the whole lab one reading list; Learning mode under Education suits students | Write the question yourself first; verify every reference the model gives |
| 2 Experimental design | Code execution for power simulations | Claude Code for task code with tests; Projects for methods documents and reporting guidelines; Research for methodological literature | Design documents containing collaborators' unpublished material go in the approved workspace | Verify every suggestion by simulation; test hardware timing by hand |
| 3 Conducting the experiment | General script drafts | Claude Code / Cowork for local QC and file organisation; Science's local sandbox and provenance record (beta, macOS/Linux) | Work involving participant data in the approved workspace; custom retention or HIPAA → Enterprise; pipelines → API with zero retention | De-identify first; what a tool reads is uploaded |
| 4 Data analysis | Short code questions | Claude Code (long codebases, 1M context); long agentic analyses need the usage of Max or a Team premium seat; Science's Python/R kernels, SSH/Slurm, provenance | Premium seats for heavy analysts; API with pinned versions for AI annotation, with records | Do not run what you cannot explain; positive and negative controls; version control |
| 5 Presenting results | File creation (docx/pptx), artifacts, figure code | Projects holding the manuscript and all sources; Research and connectors for citation checks; Science's background reviewer flagging incorrect citations, untraceable numbers and figure–code mismatches | Shared Projects for co-authors | Write conclusions yourself first; the reviewer agent is an extra check, not the only one; check journal rules |
| 6 Critique | Any plan can red-team | Stricter critique from Opus/Fable; Projects let the critique see the whole manuscript and a data summary | — | Never upload others' manuscripts, on any plan |
| 7 Revision | Memory | Projects as a living knowledge base; Cowork scheduled tasks for literature monitoring | A Team shared workspace holding the AI-use and provenance records | The synthesis is written by a person; review where AI erred |

A pattern is visible in the table. Free is already enough for the most important work at stages 1 and 6 (adversarial dialogue), because those stages call for judgment rather than features. Pro's Projects, Research and Claude Code make a real difference at stages 2, 4 and 5. Team and Enterprise differ not in features but in data terms and a shared workspace — that is, in whether the first (confidentiality) and second (records) implementation notes can be enforced. Max matters only at stage 4, where long agentic analyses quickly exhaust Pro's allowance.

### Recommendation for this lab

On current information, the most reasonable step is for the PI to apply for the Team plan for scientists, for three reasons. Its no-training default and admin-set retention let the lab define the "approved system" as this one workspace, so members need not manage the privacy settings of their own consumer accounts. Shared Projects give the records required by the second implementation note a fixed home. Standard seats are free and premium seats cost 15 dollars a month; 25 seats are enough for this lab, and premium seats are needed only for the two or three members doing heavy analysis; the plan includes Claude Code, Cowork and Claude Science.

Several uncertainties should be stated first. The eligibility page lists PIs in the natural sciences, mathematics, computer science, engineering "and related fields"; I judge that cognitive neuroscience should qualify, but that is an estimate, and Anthropic's verification decides. The discounted price lasts only 12 months, after which regular Team pricing applies (standard 20, premium 100), so the plan should be reassessed after a year. Claude Science is in beta, supports only macOS and Linux, and its databases lean toward biology and chemistry; the suggestion is that one or two members on macOS or Linux trial it, focusing on its provenance record and reviewer agent, rather than adopting it lab-wide by default. The page does not say explicitly whether students can be invited as members, but since the PI creates the workspace and then invites team members, I judge that they can.

Until the application is approved: members on Free or Pro turn "help improve our models" off; identifiable participant data and other people's manuscripts never enter any AI tool; records of substantive use are kept in a shared lab folder for now. A campus-wide Education plan is not something the lab can decide on its own; if the university adopts one later, its Learning mode would be useful for course students and could be added then.

---

## Sources

Plan information (checked 10 September 2026):

- Plans and pricing: https://claude.com/pricing
- Models available by plan: https://academy.claude.com/tutorials/choosing-the-right-claude-model
- Context window on paid plans: https://support.claude.com/en/articles/8606394-how-large-is-the-context-window-on-paid-claude-plans
- Consumer data retention: https://privacy.claude.com/en/articles/10023548-how-long-do-you-store-my-data
- Consumer terms update (scope and excluded products): https://www.anthropic.com/news/updates-to-our-consumer-terms
- The "help improve our models" setting: https://privacy.claude.com/en/articles/12109829-how-do-i-change-my-model-improvement-privacy-settings
- Data retention for commercial products and the API: https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-data
- Claude Science announcement: https://www.anthropic.com/news/claude-science-ai-workbench
- Claude Science product page: https://claude.com/product/claude-science
- Claude Science help article: https://support.claude.com/en/articles/16563838-get-started-with-claude-science
- Team plan for scientists, program page: https://claude.com/programs/team-plan-for-scientists
- Team plan for scientists, help article: https://support.claude.com/en/articles/16634237-claude-team-plan-for-scientists
- Announcement of expanded support for scientists (27 August 2026): https://www.anthropic.com/news/expanding-support-for-scientists
- Claude for Education: https://claude.com/solutions/education

Literature: see this project's [annotated bibliography](annotated-bibliography-AI-accountability-epistemics-en.md); every paper cited here is listed there with its DOI and full-text status.
