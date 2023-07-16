# Program prompts user for a str in English then outputs "emojized" version of that str

# Emojij module
import emoji


# Prompt user for input
message = input("Input: ")

# Find emoji
find_emoji = message.find(":")

# Index emoji
emoji_name = message[find_emoji:]

# Index other words before emoji
other = message[:find_emoji]

# Replace emoji 
create_emoji = emoji.emojize(emoji_name, language = "alias")

# Output user input with emoji symbol
print("Output: ", other + create_emoji)