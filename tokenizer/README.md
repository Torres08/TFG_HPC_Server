# Tokenizer Workspace

Este proyecto está diseñado para contar el número de tokens de una frase utilizando el tokenizador de un modelo de Hugging Face, específicamente el modelo [`deepseek-ai/deepseek-llm-67b-chat`](https://huggingface.co/deepseek-ai/deepseek-llm-67b-chat).

## Estructura del proyecto

- `contar_tokens.py`: Script principal para tokenizar frases y contar tokens.
- `README.md`: Documentación y guía de uso.

## Requisitos

- Python 3.8 o superior
- [transformers](https://pypi.org/project/transformers/)

## Instalación

1. **Crear un entorno virtual (opcional pero recomendado):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
2. **Instalar dependencias:**
   ```bash
   pip install transformers
   ```

## Uso

1. Edita el archivo `contar_tokens.py` para cambiar la frase que deseas tokenizar.
2. Ejecuta el script:
   ```bash
   python contar_tokens.py
   ```
3. El script imprimirá el número de tokens de la frase proporcionada.

## Ejemplo de código

```python
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained('deepseek-ai/deepseek-llm-67b-chat')
prompt = '¿Cuál es la capital de España y su moneda actual?'
tokens = tokenizer.encode(prompt, add_special_tokens=False)
print(len(tokens))
```

## Guardar resultados en un archivo

Si quieres guardar los resultados del conteo de tokens en un archivo de texto, puedes usar el siguiente ejemplo de código (por ejemplo, en `contar_tokens_post.py`):

```python
from transformers import AutoTokenizer

model_name = 'deepseek-ai/deepseek-llm-67b-chat'
tokenizer = AutoTokenizer.from_pretrained(model_name)

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

total_prompt_tokens = 0
total_tps = 0

lines = []

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

with open("resultados_tokens.txt", "w", encoding="utf-8") as f:
    for line in lines:
        f.write(line + "\n")
```

Esto generará un archivo `resultados_tokens.txt` con el detalle de los tokens usados en cada POST y los totales.

## Notas

- Este proyecto solo cuenta los tokens del contenido puro del prompt, sin aplicar plantillas de chat ni formatos de mensajes.
- Puedes cambiar el modelo o la frase modificando el script según tus necesidades.

---

