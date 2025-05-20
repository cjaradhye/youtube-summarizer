# from huggingface_hub import InferenceClient
# import json
# import re
# import os
# import dotenv
# dotenv.load_dotenv()
# HF_token = os.getenv("HF_TOKEN")

# client = InferenceClient(
#     provider="sambanova",
#     api_key=HF_token
# )

# def extract_summary(message) -> str:
#     """
#     Extracts heading and content from the assistant's message,
#     ignoring any inner thoughts like <think> tags.
#     """
#     content = message.get("content") if isinstance(message, dict) else message.content

#     # Remove any <think> blocks
#     content = re.sub(r"<think>.*?</think>", "", content, flags=re.DOTALL).strip()

#     # Extract heading in markdown bold (e.g., **Heading**)
#     heading_match = re.search(r"\*\*(.*?)\*\*", content)
#     heading = heading_match.group(1).strip() if heading_match else "Summary"

#     # Extract summary body after heading
#     summary_start = heading_match.end() if heading_match else 0
#     body = content[summary_start:].strip()

#     return {
#         "heading": heading,
#         "content": body
#     }

# def summarize_transcript(transcript: str) -> dict:
#     """
#     Given a video transcript, returns a JSON with heading and summary.
#     """
#     completion = client.chat.completions.create(
#         model="deepseek-ai/DeepSeek-R1",
#         messages=[
#             {
#                 "role": "system",
#                 "content": (
#                     "You are a video transcript summarizer. You will be given a transcript of a video "
#                     "and you will summarize it in less than 50 words in a professional way. "
#                     "Also give a heading for it, which will be of max 5 words"
#                 ),
#             },
#             {
#                 "role": "user",
#                 "content": transcript,
#             },
#         ],
#     )

#     message = completion.choices[0].message
#     return extract_summary(message)

# # Example usage:
# # transcript = "Lilo and Stitch first reactions praise film as heartfelt ..."
# # print(json.dumps(summarize_transcript(transcript), indent=4))


from together import Together
import json

def summarize_transcript(transcript: str) -> dict:
    client = Together()

    stream = client.chat.completions.create(
        model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a video transcript summarizer. You will be given a transcript of a video "
                    "and you will summarize it in less than 30 words in a professional way. "
                    "Also give a heading for it, which will be of max 5 words. "
                    "Export only the JSON with a heading and content key."
                ),
            },
            {
                "role": "user",
                "content": transcript,
            },
        ],
        stream=True,
    )

    response_text = ""
    for chunk in stream:
        if chunk.choices[0].delta.content:
            response_text += chunk.choices[0].delta.content

    # Try to parse the response into JSON
    try:
        summary_data = json.loads(response_text)
        return summary_data
    except json.JSONDecodeError:
        raise ValueError(f"Model response was not valid JSON:\n{response_text}")