# 📤 Submitting Questions to Law Enforcement MMLU

We welcome public contributions to help grow the **Law Enforcement Massive Multitask Language Understanding** dataset. All valid submissions will be reviewed and merged into future dataset releases.

---

## ✅ Submission Guidelines

To submit your multiple-choice questions (MCQs):

1. **Fork this repository**

2. Create a new branch:
   ```
   git checkout -b feature/your-contribution-name

3. Add your questions in one of the following formats:

   * `.jsonl` (preferred)
   * `.xlsx` (Excel spreadsheet)

   Save your file inside:

   ```
   data/community/

4. For `.jsonl` format, follow the structure in [`samples/sample_question.jsonl`](../samples/sample_question.jsonl)

5. For `.xlsx` format:

   * Make sure each row contains the following columns:

     * `id`, `question`, `options`, `answer`, `category`, `difficulty`, `reference`, `explanation`
   * Save as `.xlsx` with a descriptive filename

6. Run the validation script (only for `.jsonl`) before submitting:

   ```
   python scripts/validate_submission.py data/community/your_file.jsonl

7. Submit a **pull request** (PR) with:

   * **Title**: `New LEMMLU Questions - [Your Topic]`
   * **Label**: `new-question`

---

## 📄 Submission Format

### Option 1: JSONL

Each line in your `.jsonl` file should look like this:

```
{
  "id": "LE999",
  "question": "Your MCQ question here?",
  "options": ["Option A", "Option B", "Option C", "Option D"],
  "answer": "B) Correct Answer",
  "category": "Knowledge-based",
  "difficulty": "Intermediate",
  "reference": "Section 23 MACC Act 2009 (Act 694)",
  "explanation": "Provide a short, factual explanation of the correct answer."
}
```

### Option 2: XLSX

Each row in your `.xlsx` file should have the following columns:

| id    | question                | options               | answer            | category        | difficulty   | reference                          | explanation                       |
| ----- | ----------------------- | --------------------- | ----------------- | --------------- | ------------ | ---------------------------------- | --------------------------------- |
| LE999 | Your MCQ question here? | \["A", "B", "C", "D"] | B) Correct Answer | Knowledge-based | Intermediate | Section 23 MACC Act 2009 (Act 694) | Provide a short explanation here. |

We will convert `.xlsx` submissions to `.jsonl` internally before evaluation.

---

## 🔍 Validation Checklist

✅ Before submitting, confirm:

* [ ] Each question has exactly **4 options**
* [ ] Each question has **one correct answer**
* [ ] All required fields (`id`, `question`, etc.) are present
* [ ] You’ve run `validate_submission.py` (for `.jsonl`)

---

## 📬 What Happens After Submission?

* Your PR will be reviewed by the Law Enforcement MMLU admin team.
* If approved, it will be merged into the `data/community/` folder.
* Exceptional contributions may be included in future `official` releases and added to the leaderboard.

---

📧 Questions? Contact us at [ai.team@elmu.edu.my](mailto:ai.team@elmu.edu.my)
