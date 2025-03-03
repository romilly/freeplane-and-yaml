import os
import openai

from dotenv import load_dotenv
api_key = os.getenv('OPENAI_API_KEY')


response = openai.Completion.create(
    model="o3-mini",
    prompt="Here is your data: [Your Large Text Input]. Please generate a YAML output that conforms to the following JSON schema: [Your JSON Schema].",
    max_tokens=100000,
    temperature=0.5,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
)
print(response.choices[0].text.strip())
