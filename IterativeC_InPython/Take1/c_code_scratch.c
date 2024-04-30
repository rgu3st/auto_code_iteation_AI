#include <stdio.h>
#include <stdbool.h> // Include this header for the bool and true data types

#define BAD_RETURN_CODE 1
#define GOOD_RETURN_CODE 0

int main(int argc, char* argv[]) {
    printf("Hi, iteratively fixing AI!\n");
    int userInput;
    scanf("%d", &userInput); // Get user input as an integer

    if (userInput < 0) { // Replace 'if (true)' with a valid boolean expression
        return BAD_RETURN_CODE;    
    } else {
        return GOOD_RETURN_CODE;
    }
}
