from openai import OpenAI
import dotenv
import os 

dotenv.load_dotenv()


# gets OPENAI_API_KEY from your environment variables
#OPENAI_API_KEY=os.environ['secret_key']

openai = OpenAI()

prompt = 'I have a startup name goldfitch ai, its a AI start up that helps to use prompt engineeirng to query relational database. I want an image i can post on instagram that advertises this company..I also want a logo made..'
model = "dall-e-3"


def main() -> None:
    # Generate an image based on the prompt
    response = openai.images.generate(prompt=prompt, model=model)

    # Prints response containing a URL link to image
    print(response)


if __name__ == "__main__":
    main()