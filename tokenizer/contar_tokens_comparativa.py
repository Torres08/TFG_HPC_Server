from transformers import AutoTokenizer

model_names = [
    'deepseek-ai/deepseek-llm-67b-chat',
    'deepseek-ai/deepseek-llm-7b-chat'
]

posts = [
    {
        "content": "¿Cuál es la capital de España y su moneda actual?",
        "max_tokens": [32]
    },
    {
        "content": "Explica el proceso de fotosíntesis en detalle, mencionando las etapas clave (fase luminosa y fase oscura), los componentes necesarios, y la ecuación química general. ¿Por qué es fundamental para la vida en la Tierra?",
        "max_tokens": [64, 128, 256]
    },
    {
        "content": "Detalla los desafíos éticos y de seguridad asociados con el desarrollo y la implementación de la inteligencia artificial generativa a gran escala. Considera aspectos como el sesgo en los datos de entrenamiento, la privacidad de la información, el uso indebido (deepfakes, desinformación), la propiedad intelectual y la responsabilidad legal. Proporciona soluciones o mitigaciones para cada uno de estos desafíos.",
        "max_tokens": [256]
    }
]

lines = []

for model_name in model_names:
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    lines.append(f"Modelo: {model_name}")
    total_prompt_tokens = 0
    total_tps = 0
    for i, post in enumerate(posts, 1):
        tokens = tokenizer.encode(post["content"], add_special_tokens=False)
        num_prompt_tokens = len(tokens)
        for max_tok in post["max_tokens"]:
            tps = num_prompt_tokens + max_tok
            total_prompt_tokens += num_prompt_tokens
            total_tps += tps
            lines.append(f"POST {i} (max_tokens={max_tok}):")
            lines.append(f"  Tokens en el prompt: {num_prompt_tokens}")
            lines.append(f"  Tokens totales (prompt + max_tokens): {tps}\n")
    lines.append(f"Total tokens en los prompts (sumados): {total_prompt_tokens}")
    lines.append(f"Total tokens (prompts + max_tokens, sumados): {total_tps}")
    lines.append("\n" + "-"*40 + "\n")

with open("resultados_tokens_comparativa.txt", "w", encoding="utf-8") as f:
    for line in lines:
        f.write(line + "\n")
