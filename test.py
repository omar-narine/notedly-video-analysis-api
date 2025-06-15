from google import genai
from google.genai import types

import os
from dotenv import load_dotenv

load_dotenv()

testing_url = "https://www.youtube.com/watch?v=BD-rLIz9XUo&t=1059s"

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

print("\n****** RESPONSE 1 *****")

# response = client.models.generate_content(
#     model="models/gemini-2.5-pro-preview-05-06",
#     contents=types.Content(
#         parts=[
#             types.Part(
#                 file_data=types.FileData(file_uri=testing_url)
#             ),
#             types.Part(text="Please summarize this video in a short paragraph. Who are the two Elliots?")
            
#         ]
#     )
# )

print("\n****** RESPONSE 2 *****")

response = client.models.generate_content(
    model="models/gemini-2.5-flash-preview-05-20",
    contents=types.Content(
        parts=[
            types.Part(
                file_data=types.FileData(file_uri=testing_url)
            ),
            types.Part(text="Please summarize this video in a short paragraph. Then explain who are the two 'Elliots'?")
            
        ]
    )
)


print("\n****** RESPONSE 3 *****")

# response = client.models.generate_content(
#     model="models/gemini-2.0-flash",
#     contents=types.Content(
#         parts=[
#             types.Part(
#                 file_data=types.FileData(file_uri=testing_url)
#             ),
#             types.Part(text="Please summarize this video in a short paragraph. Who are the two Elliots?")
            
#         ]
#     )
# )


# response = client.models.generate_content(
#     model='models/gemini-2.0-flash',
#     contents=types.Content(
#         parts=[
#             types.Part(
#                 file_data=types.FileData(file_uri='https://www.youtube.com/watch?v=9hE5-98ZeCg')
#             ),
#             types.Part(text='Please summarize the video in 3 sentences.')
#         ]
#     )
# )

print(response.text)




