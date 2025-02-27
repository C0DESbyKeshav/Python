# Write a program to print the pyramid star pattern.

limit = int(input("Enter the limit: "))

i = 1
j = 1
k = limit - 1;
pattern = []

    for (int i = 0; i < limit; i++)
    {
        for (int j = 0; j < (((limit * 2) - 1) + (2 * i)); j++)
        {
            if (j < (2 * k) || ((j > (2 * k)) && (j % 2 != 0)))
            {
                cout << " ";
            }
            else
            {
                cout << "*";
            }
        }
        k--;
        cout << "\n";
    }
