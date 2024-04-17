import openai
import os 
import dotenv



message=[{'role':'system','content':'You are bot'}]

def main(inputs, message):

 
    message.append({'role':'user','content':inputs})

    completion=openai.chat.completions.create(
        model='gpt-4',
        messages=message
    
    )
    result=completion.choices[0].message.content

    
    message.append({'role':'assistant','content':result})

    return result



if __name__=='__main__':

    dotenv.load_dotenv()

    openai.api_key=os.environ['OPENAI_API_KEY']

    message=[{'role':'system','content':'You are bot'}]

    while True:
        inputs=input()
        
        print(main(inputs,message))

        if inputs=='quit()':
            break
        


        

        


