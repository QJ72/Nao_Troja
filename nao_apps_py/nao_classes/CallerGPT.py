from openai import OpenAI

#Need testing for image format

class CallerGPT:
    def __init__(self, key, model="gpt-4o-mini"): #model choice arbitrary
        self.client = OpenAI(api_key=key)
        self.model = model

    def enter_prompt(self, prompt, image=None):
        response = None
        try :
            if image is not None:
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=[
                        {
                            "role": "user",
                            "content": [
                                {"type": "text", "text": prompt},
                            ],
                        },
                    ],
                )
            else :
                response = self.client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {
                            "role": "user",
                            "content": [
                                {"type": "text", "text": prompt},
                                {"type": "input_image", "image_url": f"data:image/png;base64,{image}"},
                            ],
                        },
                    ],
                )
        except Exception as e:
             print(e)
        return response