""" example_007: How to use chat streaming """

from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    HumanMessage,
)


if __name__ == '__main__':
    # Print the product name
    from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

    chat = ChatOpenAI(streaming=True, callbacks=[StreamingStdOutCallbackHandler()], temperature=0)
    resp = chat([HumanMessage(content="Write me a song about elon musk landing on the mars with a tesla.")])



# 28-05-2023: First output of the prompt:
# Verse 1:
# He's a man with a vision, a dreamer with a plan
# He's got his sights set high, reaching for the stars
# He's Elon Musk, the man with the Tesla in his hand
# And he's headed for Mars, to make history once again
#
# Chorus:
# Elon Musk, he's on a mission
# To land on Mars with his Tesla
# He's gonna make the impossible happen
# And leave us all in awe and wonder
#
# Verse 2:
# He's got the rockets ready, the engines all fired up
# He's got his team behind him, ready to take the leap
# He's got the world watching, waiting for the moment
# When he touches down on Mars, with his Tesla in tow
#
# Chorus:
# Elon Musk, he's on a mission
# To land on Mars with his Tesla
# He's gonna make the impossible happen
# And leave us all in awe and wonder
#
# Bridge:
# He's a pioneer, a trailblazer
# A man who never settles for less
# He's gonna change the world, one step at a time
# And we're all lucky to witness his greatness
#
# Chorus:
# Elon Musk, he's on a mission
# To land on Mars with his Tesla
# He's gonna make the impossible happen
# And leave us all in awe and wonder
#
# Outro:
# He's done it again, he's made history
# Elon Musk, the man with the Tesla
# He's landed on Mars, and we're all amazed
# At the incredible things he can do.
