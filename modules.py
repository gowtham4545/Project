import pyttsx3 as pts
from openai import OpenAI
import requests
KEY = requests.get('https://gowtham-api.vercel.app/keys').json()['key']
engine = pts.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
client = OpenAI(api_key=KEY)


async def sentence(seq: list) -> None:
    response = await client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[

            {"role": "user", "content": "I will give some keywords and form a meaningful sentence from that"},
            {"role": "assistant", "content": "Of course, please provide me with the keywords, and I'll help you form meaningful sentences using them."},
            {"role": "user", "content": "i , innocent"},
            {"role": "assistant", "content": '''"I was falsely accused of a crime I didn't commit, but I knew in my heart that I was innocent."'''},
            {"role": "user", "content": '''not to generate a sentence which contains these keywords, just study the given keywords and give me the sentence'''},
            {"role": "assistant", "content": '''Understood, here's a sentence using the keywords "I" and "innocent":
"She insisted that I was innocent."'''},
            {"role": "user", "content": '''suppose a person is dumb and he cant speak, so he is making sentences via these keywors. He will give only nouns and verbs. generate sentence so that he can show that sentence to communicate with others '''},
            {"role": "assistant", "content": '''Certainly, if someone can only provide nouns and verbs to form sentences, here's an example of a sentence they could use to communicate:
"Dog chase cat."
In this simple sentence, "dog" is the subject (noun), and "chase" is the verb, indicating an action. "Cat" is the object (noun) of the action. This sentence conveys the idea that a dog is chasing a cat.'''},
            {"role": "user", "content": '''exactly, i will give those keywords to you, tell me what would be the sentence he is willing to communicate'''},
            {"role": "assistant", "content": '''Of course, please provide the nouns and verbs, and I'll help you form a sentence based on those keywords.'''},
            {"role": "user", "content": '''i, innocent'''},
            {"role": "assistant", "content": '''With the keywords "I" and "innocent," a simple sentence could be:
"I am innocent."
             Give me only the generated phrase and not the explanation'''},
            {"role": "user", "content": str(seq)}
        ]
    )
    sentence = response.choices[-1].message.content
    return sentence


def speech(buffer: list):
    text = sentence(seq=buffer)
    engine.say(text)
    engine.runAndWait()
