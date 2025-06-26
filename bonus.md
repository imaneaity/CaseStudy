# Bonus – Theoretical Computer Science Concepts

This section highlights theoretical computer science concepts that relate to the implementation and design choices made in this SRE/DevOps case study. It has been written with the help of AI tools.

---

## 1. **Regular Languages & Finite Automates**

- Tools like `grep`, `sed`, and `awk` are grounded in **regular expressions**.
- Regular expressions correspond to **regular languages**, which are recognized by **finite automates**.
- Domain extraction in Part 4 uses regex patterns that simulate automate behavior.

---

## 2. **Parsing and Lexical Analysis**

- The process of extracting links from HTML is an example of **lexical analysis** and **parsing**.
- `BeautifulSoup` functions similarly to a lexer/parser by tokenizing HTML tags and attributes.

---

## 3. **Graph Theory**

- Hyperlinks between websites form a **directed graph**, where:
  - Nodes = webpages
  - Edges = links between them
- Crawling links is analogous to traversing a graph (e.g., DFS or BFS).

---

## 4. **Concurrency and Distributed Systems**

- CI/CD pipelines involve distributed components (GitHub, DockerHub, Kubernetes).
- Concepts such as **asynchronous execution**, **event triggers**, and **job dependency graphs** relate to concurrent system design.

---

## 5. **Security Models and Access Control**

- Running containers as non-root maps to **least privilege principles** in system security.
- Secret management and access tokens tie into **authorization models** and **identity verification**.

---

## 6. **Automates in Workflow Engines**

- GitHub Actions workflows can be modeled as **state machines**:
  - Jobs represent states.
  - Transitions are defined by triggers and conditions (`on:`, `needs:`).

---

## 7. **Complexity Considerations**

- Tools used (e.g., `tr`, `awk`) are highly optimized for linear scans (`O(n)` time).
- Efficient algorithms ensure scalability across larger inputs and automation pipelines.

---

This case study blends theory and practice, applying foundational CS principles to modern DevOps workflows.
