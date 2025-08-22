# 🤝 Contributing to Law Enforcement MMLU

Thank you for your interest in contributing to the **Law Enforcement Massive Multitask Language Understanding** project!  
We welcome contributions from law enforcement professionals, researchers, legal experts, educators, and developers.

This file provides an overview of how to contribute — whether you're submitting questions, improving documentation, or helping with code.

---

## 📋 How to Contribute

### 📌 For Question Contributors (MCQs)
We accept multiple-choice questions in both `.jsonl` and `.xlsx` formats.

➡️ Please refer to the full [Submission Guide](submissions.md) for:
- Example format
- Required metadata
- Validation instructions

---

### 💻 For Code & Repo Contributors

#### 1. Fork the Repository
Click on "Fork" at the top-right corner to create a copy under your GitHub account.

#### 2. Clone Your Fork
```bash
git clone https://github.com/YOUR_USERNAME/MMLU-Law-Enforcement.git
cd MMLU-Law-Enforcement
```

#### 3. Create a New Branch
```bash
git checkout -b feature/your-feature-name
```

#### 4. Make Changes and Commit
Use clear commit messages, such as:
```bash
git commit -m "Add validation for category field in submission script"
```

#### 5. Push to Your Fork
```bash
git push origin feature/your-feature-name
```

#### 6. Submit a Pull Request
Go to the original repo and open a PR from your branch. Include a brief description.

---

## ✅ Validation Tools

Before submitting your `.jsonl` file, run the validation script:

```bash
python scripts/validate_submission.py path/to/your_file.jsonl
```

This will check:
- JSON validity
- 4-option structure
- Required metadata
- Proper difficulty labels

---

## 💬 Communication

- For issues or bugs: open a GitHub Issue
- For general questions: email us at [ai.team@elmu.edu.my](mailto:ai.team@elmu.edu.my)
- We also encourage discussions via PR comments or GitHub Discussions (if enabled)

---

## ⚖️ Licensing & Attribution

By contributing, you agree to license your content under the MIT License, and allow your submissions to be included in official or community datasets with attribution to your GitHub username unless stated otherwise.

---

## 🙌 Acknowledgements

Your contribution supports the development of trustworthy, domain-specific AI for public safety and governance. Thank you!
