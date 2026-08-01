import os
import json
from openai import OpenAI
from dotenv import load_dotenv
from tools import tools, tool_map

load_dotenv()

# Pass xAI's base_url and API key to the OpenAI client
client = OpenAI(
    api_key=os.getenv("XAI_API_KEY"),
    base_url="https://api.x.ai/v1"
)

def run_agent(user_prompt: str, max_iterations: int = 5):
    messages = [
        {"role": "system", "content": "You are a helpful executive personal assistant powered by Grok."},
        {"role": "user", "content": user_prompt}
    ]

    for _ in range(max_iterations):
        # Call Grok model via OpenAI compatibility interface
        response = client.chat.completions.create(
            model=os.getenv("LLM_MODEL", "grok-2"),
            messages=messages,
            tools=tools
        )
        
        message = response.choices[0].message
        messages.append(message)

        # Return answer if no tool calls requested
        if not message.tool_calls:
            return message.content

        # Execute tools requested by Grok
        for tool_call in message.tool_calls:
            func_name = tool_call.function.name
            arguments = json.loads(tool_call.function.arguments)
            
            print(f"🔧 [Grok Tool Execution]: {func_name}({arguments})")
            
            result = tool_map[func_name](**arguments)

            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": result
            })
