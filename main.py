from agent import agent_reply

print("Meeting Scheduler Started (type exit to stop)")

while True:
    user = input("You: ")
    if user.lower() == "exit":
        break
    print("Agent:", agent_reply(user))
