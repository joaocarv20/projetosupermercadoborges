# Regras do projeto

- **Toda mudança no sistema atualiza `docs/DOCUMENTACAO.md` no mesmo commit:** uma linha no "Histórico de mudanças"
  (data, mudança, detalhe; mais recente primeiro) e a seção que ela afeta (arquivos, tabelas, telas, regras,
  pendências, perguntas respondidas). Mudança no computador do mercado (instalação, permissões, problemas) também vai
  para o `INSTALACAO.md`.
- Testes: `.venv/bin/python -m testes.test_<peça>` para cada arquivo de `testes/`.
- O Oracle do Cefas só é alcançado do computador do mercado; daqui não dá para testar contra ele.
