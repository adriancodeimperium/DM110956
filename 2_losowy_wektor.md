# Losowy wektor
## Co oznacza, że wygenerowana wartość jest losowa?
Od strony użytkownika losowość wygenerowanej zmiennej oznacza, że jej wartość nie została z góry zadana, a za każdym uruchomieniem programu przyjmie pewną, praktycznie nieprzewidywalną wartość. 

W rzeczywistości wartość zmiennej jest jedynie pseudolosowa - t.j. znając pewien stan początkowy można przewidzieć (dokładniej - wyliczyć/wyznaczyć) liczby, które będą generowane.

## O jaki parametr rozszerzyłbyś swoją funkcję?
Przydatnymi do generowania losowego wektora parametrami są:
* długość wektora
* zakres, z którego odbywa się losowanie liczb
* pożądany rozkład zmiennej

## Jak zweryfikował byś stwierdzenie, że otrzymane dane to zmienne losowe o zadanym rozkładzie? 
Za pomocą odpowiednich estymatorów, np. w przypadku rozkładu normalnego można oczekiwać, że średnia arytmetyczna i odchylenie standardowe otrzymanych wartości będą różnić się niewiele od zadanych (uwaga na boku - jeżeli powtarzalnie nie różniłyby się wcale, tj. otrzymywano by dane idealnie pasujące do zadanych parametrów, świadczyłoby, poniekąd paradoksalnie, o tym, że funkcja generująca nie jest godna zaufania).

## Po co weryfikować z jakiego rozkładu otrzymywane są dane skoro tworzymy je ze z góry ustalonej funkcji? 
> "Zaufanie jest dobre ale kontrola lepsza" - W. Lenin

Przykładowe powody:
* funkcja może być błędnie zaimplementowana
* funkcja może być zaimplementowana poprawnie dla większości przypadków ale trafiliśmy na przykład brzegowy, gdzie zachowanie funkcji jest niezgodne z zamierzonym
* dokumentacja funkcji mogła zostać błędnie napisana bądź zrozumiana
* wygenerowane dane (prawie) nigdy nie będą miały **dokładnie** takiego rozkładu jak zadany
