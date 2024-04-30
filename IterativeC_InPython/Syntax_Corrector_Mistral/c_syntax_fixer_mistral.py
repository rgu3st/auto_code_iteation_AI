import subprocess
import ollama

CODE_DELIM_START = "/*START C CODE*/"
CODE_DELIM_END = "/*END C CODE*/"

CODE_DELIM_START = "```c\n"
CODE_DELIM_END = "```\n"

GOOD_RETURN_CODE = 0
BAD_RETURN_CODE = 1


def get_message_response(messages_in):
    response = ollama.chat(
        model='mistral', 
        messages=messages_in,
    )
    print(f"Returning response:\n{response['message']['content']}")
    return response['message']['content']


def Tests_quick(return_code:int)->bool:
    if return_code == GOOD_RETURN_CODE:
        print("Test passed")
        return True
    else:
        print("Test failed")
        return False


def main():
    count = 0
    return_code = BAD_RETURN_CODE
    star_count = 45
    cfile_in = "S:/repos/auto_code_iteation_AI/IterativeC_InPython/Take2/t.c"
    cfile_out = './c_code_scratch.c'
    c_executable = './c_code.exe'
    c_code:str = None
    with open(cfile_in, 'r') as file:
        c_code = file.read()

    with open(cfile_out, 'w') as f:
        f.write(c_code)
    
    # Run multiple times until we get a good return code, based on command args:
    while return_code == BAD_RETURN_CODE:

        print(f"\n\n\n\n{'*'*star_count}\nTesting the following C code. Attempt {count}\n{'*'*star_count}\n{c_code}")
        result = subprocess.run(['cl', cfile_out, '/Fe:', c_executable], capture_output=True, text=True)
        print(f"Attempt number: {count}")
        count += 1
        if "error" not in result.stdout:
            result = subprocess.run([c_executable, f'{count}'], capture_output=True, text=True)
            # print(f"Returned result code: {result.returncode}")
            return_code = result.returncode
        test_result = Tests_quick(return_code)
        if test_result == True or count > 10:  # Let's give GPT 10 tries to fix the intentional error from the initial prompt.
            break

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

        response = get_message_response(iterative_message)

        try:
            c_code = response.split(CODE_DELIM_START)[1].split(CODE_DELIM_END)[0]
        except IndexError:
            print(f"Failed to extract C code from response.")
            return

        with open(cfile_out, 'w') as f:
            f.write(c_code)

    print(f"\nSuccess! At count {count}.\nResult code: {return_code}\nCaptured stdout: \n{result.stdout}\nCaptured stderr: \n{result.stderr}")

if __name__ == '__main__':
    main()