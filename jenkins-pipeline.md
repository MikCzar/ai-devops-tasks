flowchart TD
    Start([Git Push / Trigger]) --> Checkout[1. Checkout Kodu]
    Checkout --> Build[2. Budowanie Aplikacji<br/>npm install & build]
    Build --> Test[3. Testy Jednostkowe<br/>Jest / Unit Tests]
    Test --> Lint[4. Analiza Statyczna Kodu<br/>SonarQube / Lintery]
    Lint --> Security[5. Skanowanie Bezpieczeństwa<br/>Snyk / Trivy (Dependencies)]
    Security --> DockerBuild[6. Budowanie Obrazu Docker<br/>docker build]
    DockerBuild --> IntTest[7. Testy Integracyjne<br/>Testy na kontenerze]
    IntTest --> Staging[8. Wdrożenie na Staging<br/>Automatyczny Deploy]
    Staging --> Approval{Ręczna akceptacja<br/>Quality Gate / Approval?}
    
    Approval -->|Tak| Production[9. Wdrożenie na Produkcję<br/>Production Deploy]
    Approval -->|Odrzucone| Fail([Przerwane / Anulowane])
    
    Production --> Success([Sukces / Wdrożone])
    
    style Start fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    style Success fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px
    style Fail fill:#ffebee,stroke:#c62828,stroke-width:2px
    style Production fill:#fff9c4,stroke:#fbc02d,stroke-width:2px
    style Approval fill:#ede7f6,stroke:#512da8,stroke-width:2px