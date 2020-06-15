""" 
Definice: procedura nebo funkce nazveme skupinu příkazů, které tvoří logický blok neboli podprogram 

Slouží ke zjednodušení kódu – podprogram se definuje jen jednou a následně se v programu už jen deklaruje jeho název (odkazuje se na něj) 

Charakteristika procedury, charakteristika funkce Parametry a způsob jejich volání 

Názorné je C:
Před deklarací se musí určit, jestli bude procedura něco vracet
- void pokud nebude
- int, float, uint16_t, struct, ... pokud bude

int nth_fibonacci(int n)
{
    if (n <= 1) 
        return n; 
    return nth_fibonacci(n-1) + nth_fibonacci(n-2); 
}

"""


def nth_fibonacci(n):
    if (n <= 1):
        return n
    return nth_fibonacci(n-1) + nth_fibonacci(n-2)

print(nth_fibonacci(10))

# nevím prostě něco tě napane ne

