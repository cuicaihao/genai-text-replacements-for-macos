# Writing Principles for Clarity and Precision

## Core Principles (Refined)

### 1. Use Simple Words and Short Sentences

- Choose common words over rare or archaic ones.
- Keep sentences under 15 words when possible.
- Avoid exaggeration, unnecessary elaboration, and flowery language.
- Cut redundant phrases; say it once, say it right.
- **Example:** Instead of "utilize comprehensive systematic methodologies," write "use a systematic approach."

### 2. One Principal Subject Per Sentence

- Each sentence must contain one main idea.
- Avoid mixing unrelated concepts (heterogeneous sentences).
- Separate compound thoughts into distinct sentences.
- **Example:** Split "The project started late because the team lacked resources and morale was low" into two sentences.

### 3. Eliminate Ambiguity

- Flag risky words: "not...and", "not...or", "any", "but", "only", "that", "certain", pronouns ("he/it/they/these"), and vague modifiers.
- Every pronoun must clearly refer to a specific noun; test for multiple interpretations.
- Replace "this/that/it" with the actual noun when reference is unclear.
- Avoid dangling modifiers—place modifying phrases next to what they modify.
- **Example:** Instead of "After reviewing the files, the report was completed," write "After reviewing the files, Sarah completed the report."

### 4. Repeat Key Words for Clarity

- Don't omit prepositions, conjunctions, or articles to achieve brevity at the cost of clarity.
- Repeat structural words ("the", "of", "and", "or") after interruptions or long phrases.
- Parallel structures require parallel elements; repeat function words to show parallelism.
- **Example:** Instead of "We need skills in Python, Java, and database management," write "We need skills in Python, skills in Java, and skills in database management" when the contexts differ significantly.

### 5. Use Logical Connectors

- Start sentences with conjunctive adverbs to show flow: "however", "therefore", "meanwhile", "consequently", "similarly", "nevertheless".
- Place linking words at the beginning of sentences for smooth transitions.
- Use explicit connections instead of assumed relationships.
- **Example:** Instead of jumping ideas, write "Therefore, the first approach failed. However, the second approach succeeded."

### 6. Emphasize Key Ideas Through Placement

- Place important information at the sentence beginning or end (strongest positions).
- Use suspensive conjunctions for clarity and force: "not only...but also", "both...and", "neither...nor".
- Use antithesis (contrasting paired elements) to highlight differences.
- Move subordinate clauses to the beginning or end, not the middle.
- **Example:** Instead of "The team, despite challenges, succeeded," write "Despite challenges, the team succeeded" or "The team succeeded despite challenges."

### 7. Ensure Every Reference is Specific

- Every "it", "this", "that", "these", "those" must point to a single, unambiguous noun.
- If a pronoun could refer to multiple nouns, restate the noun.
- Test each pronoun by reading it in isolation—does it make sense?
- Create a reference chain: If X is introduced, refer to X by name or a specific pronoun until a new concept appears.
- **Example:** Instead of "When the system crashed, it was a disaster," clarify: "When the system crashed, the outage cost us $10K."

---

## Extended Principles for Technical and GenAI Writing

### 8. Use Active Voice by Default

- Prefer active voice: subject performs the action.
- Use passive voice only when the actor is unknown, irrelevant, or obvious from context.
- **Example:** Instead of "The model was trained by our team," write "Our team trained the model."

### 9. Define Terms Before Use

- Introduce acronyms with full names: "Machine Learning Operations (MLOps)".
- Define domain-specific terminology on first use.
- Use consistent terminology throughout the document—don't swap synonyms arbitrarily.
- **Example:** "We use TensorFlow, an open-source machine learning library, to build neural networks."

### 10. Separate Concerns Visually

- Use lists, headings, and white space to break dense text.
- Group related information together.
- Use formatting (bold, code blocks) for emphasis and readability.
- Start new paragraphs for new thoughts.

### 11. Show Precision in Numbers and Data

- Always include units: "5 seconds", "10 GB", not just "5" or "10".
- Round numbers appropriately; false precision is insulting.
- Clarify whether numbers are approximate, measured, or theoretical.
- **Example:** Instead of "This took approximately 3.14159 seconds," write "This took about 3 seconds" or "This took 3.14 seconds with ±0.01 second precision."

### 12. State Assumptions Explicitly

- Do not assume readers share your background knowledge.
- Flag dependencies: "Assuming you have Git installed...", "This guide requires basic Python knowledge."
- Clearly separate what is required from what is optional.
- **Example:** Instead of "Run git pull to update," write "If you have Git installed, run `git pull` to update your local repository."

### 13. Use Parallel Structure for Lists and Comparisons

- In lists, begin each item the same way (all verbs, all nouns, all phrases).
- Maintain parallel grammatical form across bullets, numbered lists, or table rows.
- **Correct:** "To refine text: identify the main issue, clarify the language, and confirm accuracy."
- **Incorrect:** "To refine text: identify the main issue, clarifying language, confirm accuracy."

### 14. Provide Context Before Abstraction

- Introduce concrete examples or real-world scenarios before abstract principles.
- Build from known information to new information.
- Use familiar concepts to explain unfamiliar ones.
- **Example:** Instead of leading with "Tokenization is the process of breaking text into meaningful units," start with "Before a language model can understand text, it must break sentences into words or word pieces—this process is called tokenization."

### 15. Test for Readability

- Read your text aloud; if you stumble, your reader will too.
- Check that punctuation supports natural rhythm, not obscures meaning.
- Ensure each paragraph has a clear topic sentence.
- Verify that dependent clauses don't separate subject from verb excessively.

### 16. Use Contractions in Conversational Writing; Avoid in Formal Writing

- Conversational: "We're happy to help. It's a best practice." (clearer, warmer)
- Formal: "We are happy to help. It is a best practice." (timeless, authoritative)
- Choose based on audience and purpose.

### 17. Punctuation Clarifies; It Does Not Decorate

- Commas separate ideas, not just create pauses.
- Dashes and semicolons have specific functions; don't use them for style alone.
- All punctuation should serve meaning, not aesthetics.
- **Example:** "The model, trained on clean data, performs well" (clarifying comma) vs. "The model trained on clean data, it performs well" (incorrect comma splice).

---

## GenAI Prompt Engineering Additions

### 18. Be Explicit in Instructions to GenAI

- GenAI models benefit from explicit, over-explained instructions.
- State the desired format, tone, and audience.
- Specify what to include and what to exclude.
- **Example:** Instead of "Make this better," write "Refine this for clarity, conciseness, and professional tone. Keep it under 200 words. Use active voice and simple vocabulary. Remove jargon."

### 19. Use Role-Playing for Clarity

- Assign personas to GenAI: "You are a senior technical writer..." or "You are an AWS solutions architect..."
- Personas help models understand context and adjust tone accordingly.
- **Example:** "You are a professional copyeditor. Refine this marketing email for persuasiveness and conciseness."

### 20. Structure Prompts with Clear Sections

- Use headings or numbered sections in prompts.
- Separate Persona, Context, Task, Format, and Tone (the Jeff Su 6-Feature Format).
- Structure prevents confusion and improves output quality.

---

## Common Pitfalls to Avoid

| Pitfall | Fix |
|---------|-----|
| Vague pronouns ("it", "this") | Replace with specific noun or rephrase |
| Double negatives ("not uncommon") | Use positive: "common" |
| Buried verbs ("make an improvement") | Activate: "improve" |
| Nominalizations ("make a decision") | Verb form: "decide" |
| Hedge words ("very", "really", "quite") | Delete or be specific: "significantly" |
| Ambiguous "only" ("Only John finished the project") | Clarify placement and meaning |
| Mixed metaphors | Use one metaphor consistently or remove |
| Acronyms without definition | Define on first use |

---

## Checklist for Clear Writing

- [ ] Every sentence has one main idea.
- [ ] No ambiguous pronouns (every "it/this/that" has a clear referent).
- [ ] Simple, common words used; jargon is defined.
- [ ] Sentences average 12–15 words.
- [ ] Transitions between ideas are explicit.
- [ ] Lists and comparisons use parallel structure.
- [ ] Key ideas are at sentence beginnings or ends.
- [ ] Assumptions are stated clearly.
- [ ] Text reads aloud without stumbling.
- [ ] Format supports readability (white space, headings, lists).
- [ ] For GenAI prompts: persona, context, format, and tone are clear.
