# Example user query requiring weather check + scheduling
prompt = "Check the weather in Chicago tomorrow, and if it's clear, schedule a 'Morning Jog' at 8:00 AM."

response = run_agent(prompt)
print("\n🤖 [Final Response]:", response)
