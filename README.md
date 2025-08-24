# HUSM - Previsão de Estoque e Otimização Logística de Medicamentos

Este projeto faz parte do desenvolvimento inicial do **mestrado acadêmico em Ciência da Computação** (UFSM, linha de Computação Aplicada), cujo objetivo é aplicar técnicas de **Inteligência Artificial**, com foco em **aprendizado não-supervisionado (clustering)**, para apoiar a **gestão de estoque de medicamentos** em hospitais universitários, como o HUSM.

O protótipo simula previsão de demanda e estratégias de reposição de estoque, permitindo testes e análise de cenários para melhorar a tomada de decisão na farmácia hospitalar.

---

## Contexto do Projeto

Hospitais universitários enfrentam desafios na logística de medicamentos críticos, onde decisões manuais ou baseadas em histórico limitado podem gerar:

- Falta de medicamentos essenciais em situações de urgência;
- Desperdício financeiro com medicamentos vencidos ou não utilizados.

Estudos mostram que perdas com medicamentos vencidos podem representar **2% a 5% dos gastos totais com aquisição**, ou até **meio milhão de reais por ano**, dependendo da instituição.  

O projeto busca:

- Identificar padrões de consumo e urgência de medicamentos;
- Auxiliar a tomada de decisão sobre reposição e distribuição;
- Aplicar técnicas de IA adaptadas à realidade hospitalar brasileira.

---

## Funcionalidades do Protótipo

1. **Clusterização de medicamentos**
   - Agrupa medicamentos com padrões similares de consumo e urgência usando **K-Means**.
   - Permite identificar grupos de medicamentos que devem ser tratados de forma similar na gestão de estoque.

2. **Simulação de reposição**
   - Calcula um **estoque mínimo ajustado** com base no nível de urgência.
   - Cria uma coluna `repor` indicando quais medicamentos precisam ser repostos.
   - Permite testar estratégias antes de implementá-las na prática.

3. **API RESTful com FastAPI**
   - Disponibiliza resultados de clusterização e simulação em formato JSON.
   - Endpoints principais:
     - `GET /` → Verifica se a API está ativa.
     - `GET /cluster` → Executa o pipeline completo:
       1. Lê dados do CSV (`estoque.csv`);
       2. Cria clusters de medicamentos;
       3. Simula reposição de estoque;
       4. Retorna resultados com: `medicamento`, `estoque_atual`, `urgencia`, `cluster`, `estoque_minimo_ajustado`, `repor`.

---
## Motivação Acadêmica

O protótipo integra:

- **Aplicação prática de IA na saúde pública**  
- **Uso de aprendizado não-supervisionado para previsão de demanda**  
- **Teste de estratégias logísticas em ambiente simulado antes da implementação real**

Este projeto foi desenvolvido com foco em aplicações práticas de Computação Aplicada para a linha de pesquisa do Mestrado em Ciência da Computação, oferecendo modelos adaptados à realidade brasileira e auxiliando na gestão eficiente de recursos hospitalares.

---

👨‍💻 Autor

Julio Cesar Salerno da Silva

Projeto desenvolvido no contexto do Mestrado em Ciência da Computação - Linha de Pesquisa: Computação Aplicada.
