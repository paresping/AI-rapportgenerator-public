from openai import OpenAI

from config import DEFAULT_MODEL


def generate_report(prompt: str, model: str = DEFAULT_MODEL) -> str:
    client = OpenAI()
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": "You are a professional financial analyst. Use only the supplied data.",
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0.2,
    )
    return response.choices[0].message.content or ""
