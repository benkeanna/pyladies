# Už jsi Ježíškovi napsala dopis, co si letos přeješ pod stromeček?
# Došlé dopisy Ježíškovi pomocníci šifrují pomocí takzvané Caesarovy šifry.
# Ta funguje tak, že se písmena v textu nahradí za písmena, která jsou v abecedě o zvolený počet míst za nimi.
# Například při použití čísla 2 se slovo „jezisek” zašifruje jako „lgbkugm”.
# Pozor, všimni si, že pomocníci nepoužívají v šifrovaných textech háčky a čárky a protože chtějí být světoví, tak používají anglickou abecedu bez písmene „ch”.
# Pokud by při posouvání písmene narazili na konec abecedy, pokračují od jejícho začátku. V textu šifrují pouze písmena.
# Vše ostatní (číslice, tečky, čárky, ...) nechávají tak, jak je. Abychom jim usnadnili práci, vytvoř nástroj, který bude takto šifrovat texty.
# Vstupem je řetězec a celé číslo, které určuje, o kolik míst se písmeno posune. Výstupem je zašifrovaný text.
# Například: encrypt(“mily jezisku, prines mi prosim super pocitac.”, 2) vrátí: “okna lgbkumw, rtkpgu ok rtquko uwrgt rqekvce.”
