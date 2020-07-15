from pytest_bdd.feature import STEP_PREFIXES
from pytest_bdd import types

STEP_PREFIXES[:] = []  # clear existing translations to avoid conflicts.
STEP_PREFIXES.append(("@", types.TAG))
STEP_PREFIXES.append(("Funcionalidade:", types.FEATURE))
STEP_PREFIXES.append(("Contexto:", types.BACKGROUND))
STEP_PREFIXES.append(("Cenário:", types.SCENARIO))
STEP_PREFIXES.append(("Cenario:", types.SCENARIO))
STEP_PREFIXES.append(("Esquema do Cenário:", types.SCENARIO_OUTLINE))
STEP_PREFIXES.append(("Esquema do Cenario:", types.SCENARIO_OUTLINE))
STEP_PREFIXES.append(("Exemplos:", types.EXAMPLES))
STEP_PREFIXES.append(("Dado ", types.GIVEN))
STEP_PREFIXES.append(("Quando ", types.WHEN))
STEP_PREFIXES.append(("Então ", types.THEN))
STEP_PREFIXES.append(("Entao ", types.THEN))
STEP_PREFIXES.append(("E ", None))
