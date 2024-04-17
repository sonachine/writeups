#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <ctype.h>
#include <time.h>

char *find_little_endian(const char *word)
{
    size_t word_len = strlen(word);
    char *little_endian = (char *)malloc((2 * word_len + 1) * sizeof(char));

    for (size_t i = word_len; i-- > 0;)
    {
        snprintf(&little_endian[(word_len - 1 - i) * 2], 3, "%02X", (unsigned char)word[i]);
    }

    little_endian[2 * word_len] = '\0';
    return little_endian;
}

char *find_big_endian(const char *word)
{
    size_t length = strlen(word);
    char *big_endian = (char *)malloc((2 * length + 1) * sizeof(char));

    for (size_t i = 0; i < length; i++)
    {
        snprintf(&big_endian[i * 2], 3, "%02X", (unsigned char)word[i]);
    }

    big_endian[2 * length] = '\0';
    return big_endian;
}


int main()
{
    // char *challenge_word = generate_random_word();
    char challenge_word[50];
    scanf("%s", challenge_word);

    printf("Word: %s\n", challenge_word);
    fflush(stdout);

    char *little_endian = find_little_endian(challenge_word);
    size_t user_little_endian_size = strlen(little_endian);
    char user_little_endian[user_little_endian_size + 1];
    bool correct_flag = false;

    printf("%s\n", find_little_endian(challenge_word));
    printf("%s\n", find_big_endian(challenge_word));

    return 0;
}
