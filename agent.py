from openai import OpenAI

client = OpenAI()

def run_agent(user_prompt: str, max_iterations: int = 5):
    messages = [
        {"role": "system", "content": "You are an executive personal assistant. Be concise and accurate."},
        {"role": "user", "content": user_prompt}
    ]

    for _ in range(max_iterations):
        # 1. Call LLM with tool definitions
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            tools=tools
        )
        
        message = response.choices[0].message
        messages.append(message)  # Store assistant message in history

        # 2. Check if LLM requested tool execution
        if not message.tool_calls:
            return message.content  # Final answer generated!

        # 3. Execute requested tools
        for tool_call in message.tool_calls:
            func_name = tool_call.function.name
            arguments = json.loads(tool_call.function.arguments)
            
            print(f"🔧 [Agent Tool Call]: {func_name}({arguments})")
            
            # Run local Python function
            result = tool_map[func_name](**arguments)

            # Append tool result back into conversation state
            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": result
            })
