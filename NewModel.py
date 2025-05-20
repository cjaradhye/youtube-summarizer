from together import Together

client = Together()
transcript = " Lilo and Stitch first reactions praise film as heartfelt and easily the best liveaction remake yet. Guys, have have the Disney ducks actually done it? Have they managed to take a beloved classic and not butcher it like a cash cow like they normally do? Because it seems, according to some goobers in the press who went to the live action Lelo and Stitch premiere, they saw and have almost nothing but good things to say about it. For example, people are talking about this being a cute reimagining that mostly captures the spirit of the original. The movie also seems to be just pure Disney magic. It's Disney at its best. People like how Ple and Jumpa were portrayed in the film and the chemistry between the performers was top-notch. The movie actually works and seems to make sense in a live action format. People also teared up watching this movie. Maya Kiloha as Lilo gives a great breakout performance. And also, like I said in the beginning, people are calling this the best liveaction remake ..."
stream = client.chat.completions.create(
  model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
  messages=[
        {
            "role": "system",
            "content": (
                "You are a video transcript summarizer. You will be given a transcript of a video "
                "and you will summarize it in less than 50 words in a professional way. "
                "Also give a heading for it, which will be of max 5 words. Export only the JSON with a heading and content key."
            ),
        },
        {
            "role": "user",
            "content": transcript,
        },
],
  stream=True,
)

for chunk in stream:
  print(chunk.choices[0].delta.content or "", end="", flush=True)