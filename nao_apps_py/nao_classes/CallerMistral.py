from mistralai import Mistral

#Need testing for image format

class CallerMisTral:
    def __init__(self, key, model="gpt-4o-mini"): #model choice arbitrary
        self.client = Mistral(api_key=key)
        self.model = model

    def enter_prompt(self, prompt):
        response = None
        try :
            response = self.client.chat.complete(
                model=self.model,
                messages=[
                    {"role": "user",
                    "content": prompt}
                ]
            )

        except Exception as e:
             print(e)
        return response