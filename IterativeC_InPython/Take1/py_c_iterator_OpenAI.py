import subprocess
import openai

TEMP = 1.0  # range 0-2, higher is more creative, lower is more accurate
CODE_DELIM_START = "/*START C CODE*/"
CODE_DELIM_END = "/*END C CODE*/"

GOOD_RETURN_CODE = 0
BAD_RETURN_CODE = 1


def get_message_response(client, message_list)->str:
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages = message_list,
    temperature=TEMP,
    #seed = 42,
    max_tokens=1024
    )
    return completion.choices[0].message


def Tests_quick(return_code:int)->bool:
    if return_code == GOOD_RETURN_CODE:
        print("Test passed")
        return True
    else:
        print("Test failed")
        return False



def main():
    # c_code =f'''
    # #include <stdio.h>
    # int main(int argc, char* argv[]){{
    #     printf("Hello World, from Python!\\n");
    #     if(argc >=2 && argv[1][0] != '4){{
    #         return {BAD_RETURN_CODE};
    #     }}
    #     printf("Argv: %s\\n", argv[1]);
    #     return {GOOD_RETURN_CODE};
    # }}
    # ''' 

    c_code =f'''#include <stdio.h>
    int main(int argc, cha* argv[]){{
        printf("Hi, iteratively fixing AI!\\n");
        if( true {{
            return {BAD_RETURN_CODE};   
        }};
        else
            return {GOOD_RETURN_CODE}
    }}''' 

    client = openai.OpenAI()
    code_goal = f'''The code should take an integer as a command line argument and returns 0 if the integer is 4, otherwise return 1. 
        You must start any code you write with the comment {CODE_DELIM_START} and end with the comment {CODE_DELIM_END}
        '''
    # inital_message = [
    #     {
    #     "role": "system",
    #     "content": f'''You are a cs professor writing a code snippet to test studen't debugging ability. Please write a C program with an intential syntax problem, to test a student. 
    #         {code_goal}
    #         Be certain write the code with one syntax error, intentionally, to test a student's debugging skills!
    #         '''
    #     }
    # ]

    # response = get_message_response(client, inital_message)
    # #response = json.loads(response)
    # print("Response from GPT-3: \n", response.content)
    # try:
    #     c_code = response.content.split(CODE_DELIM_START)[1].split(CODE_DELIM_END)[0]
    # except IndexError:
    #     print(f"Failed to extract C code from response.")
    #     return

    with open('./c_code.c', 'w') as f:
        f.write(c_code)
    
    count = 0
    return_code = BAD_RETURN_CODE

    star_count = 45
    
    # But run multiple times until we get a good return code, based on command args:
    while return_code == BAD_RETURN_CODE:

        print(f"\n\n\n\n{'*'*star_count}\nTesting the following C code. Attempt {count}\n{'*'*star_count}\n{c_code}")
        result = subprocess.run(['cl', './c_code.c', '/Fe:', 'c_code.exe'], capture_output=True, text=True)
        count += 1
        print(f"Attempt number: {count+1}")
        if "error" not in result.stdout:
            result = subprocess.run(['./c_code.exe', f'{count}'], capture_output=True, text=True)
            # print(f"Returned result code: {result.returncode}")
            return_code = result.returncode
        test_result = Tests_quick(return_code)
        if test_result == True or count > 10:  # Let's give GPT 10 tries to fix the intentional error from the initial prompt.
            break
        # print(f"Captured stdout: \n{result.stdout}")
        # print(result.stderr)
        # print(result)

        iterative_message = [
            {
            "role": "system",
            "content": f'''You are a senior C programmer. Given the following C program and the results when it is compiled and ran, please debug the program and fix the issue, based on the results.
                You must start any code you write with the comment {CODE_DELIM_START} and end with the comment {CODE_DELIM_END}'''
            },
            {
            "role": "user",
            "content": f'''{CODE_DELIM_START}\n{c_code}\n{CODE_DELIM_END}\n\nOutput:\n{result.stdout}\nReturn code: {result.returncode}'''
            }
        ]

        response = get_message_response(client, iterative_message)
        #response = json.loads(response)
        # print(f"Response (iteration {count}) from GPT-3: \n", response.content)
        try:
            c_code = response.content.split(CODE_DELIM_START)[1].split(CODE_DELIM_END)[0]
        except IndexError:
            print(f"Failed to extract C code from response.")
            return

        with open('./c_code.c', 'w') as f:
            f.write(c_code)

    print(f"\nSuccess! At count {count}.\nResult code: {return_code}\nCaptured stdout: \n{result.stdout}\nCaptured stderr: \n{result.stderr}")

if __name__ == '__main__':
    main()