# 🔒 Law Enforcement MMLU Dataset

Welcome to the official repository of the **Law Enforcement Massive Multitask Language Understanding** dataset.  
This open-source initiative is designed to benchmark language models and human reasoning in domains related to law enforcement, governance, criminal justice, and compliance.

---

## 🌍 Project Purpose

- 📊 **Benchmarking** large language models (LLMs) like GPT-5, Claude, and ELMU Insights.Akta
- 🧠 **Crowdsourcing** multiple-choice questions from law enforcement professionals and subject matter experts
- 🧪 **Evaluating** model reasoning across legal acts, police SOPs, forensic procedures, cybercrime laws, and more

---

## ✍️ How to Contribute

We welcome contributors of all backgrounds — enforcement officers, legal scholars, data scientists, and researchers.

You can:
- Submit your own MCQ questions (`.jsonl` or `.xlsx`)
- Run evaluations using our scripts
- Propose enhancements to evaluation logic

👉 See [`CONTRIBUTING.md`](CONTRIBUTING.md) for repo guidelines  
👉 See [`submissions.md`](..\submissions\submissions.md) for MCQ format and templates

---

## 📄 Sample Question Format (JSONL)

```json
{
  "id": "LE001",
  "question": "What is the maximum remand period under Section 117 of the CPC?",
  "options": ["7 days", "14 days", "15 days", "21 days"],
  "answer": "C) 15 days",
  "category": "Criminal Procedure",
  "difficulty": "Advanced",
  "reference": "Section 117 Criminal Procedure Code (CPC)",
  "explanation": "The law permits up to 15 days for serious offences."
}
```

Or see: [`samples/sample_question.jsonl`](samples/sample_question.jsonl)

---

## 📈 Zero-Shot Evaluation Results

See [`evaluations/zero_shot_results.md`](evaluations/zero_shot_results.md) for model comparisons on 100-question zero-shot benchmark.

<details>
<summary>📊 Click to expand evaluation scores</summary>

| Model                          | Questions | Errors | Correct | Accuracy |
|-------------------------------|-----------|--------|---------|----------|
| ELMU Insights (English, May 7) | 29        | 10     | 19      | 65.5%    |
| ELMU Insights (English, May 20)| 100       | 14     | 86      | 86.0%    |
| ELMU Insights (BM, June 25)    | 100       | 3      | 97      | 97.0%    |
| ELMU Insights (English, July 9)| 100       | 1      | 99      | 99.0%    |
| ChatGPT (English, July 9)      | 100       | 3      | 97      | 97.0%    |
| Claude (English, July 9)       | 100       | 3      | 97      | 97.0%    |
| ChatGPT (BM, July 9)           | 100       | 2      | 98      | 98.0%    |
| Claude (BM, July 9)            | 100       | 6      | 94      | 94.0%    |

</details>

---

## 📬 Contact & Feedback

For questions or collaboration requests, reach out to us at  
📧 [ai.team@elmu.edu.my](mailto:ai.team@elmu.edu.my)

---

## ⚖️ License

This project is licensed under the **MIT License**.  
Attribution required when reusing the dataset or tools.

---

## 🚨 Powered by ELMU Insights.Akta

A benchmark aligned with real-world law enforcement reasoning and Malaysia's legal ecosystem.
