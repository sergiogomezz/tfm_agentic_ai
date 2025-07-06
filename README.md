Welcome to Elvex! 🧠 The reasoning LLM Agentic AI for high-level planning tasks.

WORKFLOW:

1. Task Specifier --> 2. Task Divider --> 3. Task Evaluator -->
4. Orchestator (creator) --> 5. Worker Agents (auto-created) --> 6. Gatherer (agents) --> RESULT


MEJORAS



1. Incluir ejemplos en los prompt y técnicas CoT

crear tests para correr la app

FALLO:
    1. How can I make a cheesecake? Divide las tareas en la receta, cuando lo que quiere el usuario es eso mismo, no significa que el sistema deba hacer esas tasks. Para cosas en las que debe planificar, tipo un viaje, una economia o una temporada deportiva, funciona bien.
    En este caso, debe solo pensar en: genera los pasos para la cheesecake --> devuelve la receta. y no generar la receta como las subtasks


    2. Está demasiado enfocado en planificación de cosas. Sería interesante que pudiese responder a cualquier cosa, sea de planificación o no.
    MEJORA: PONER UN BOOLEANO Y SI LA RESPUESTA SÓLO REQUIERE DAR UNA INFO, DEVOLVERLA Y PUNTO

    3. MEJORAR EL EVALUADOR -- MEJORAR EL PROMPT