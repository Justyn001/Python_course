import math

pi = 3.14
e = 2.71
pi2 = 6.24

print(round(pi))
print(math.ceil(pi))    #Zaokrągla do góry
print(math.floor(pi))   #Zaokrągla w dół
print(abs(pi))          #Wartość bezwzględna z liczby
print(pow(pi,2))        #Podnosi do potęgi którą się wpisze
print(math.sqrt(420))    #Pierwiastek
print(max(pi,e,pi2))
print(min(pi,e,pi2))



name = "Maciek Kurdziel"
slice_name = name[:6]   #W drugim argumencie dodawać jeden czyli jak chce do 5 znaku do wpisuje 6
slice_surname = name[7:]
cut_name = name[::2]
reversed_name = name[::-1]
print(slice_name + " " + slice_surname)
print(cut_name + " " + reversed_name.lower())

website = "https://MaciekKurdziel.pl"
website_ = "https://www.youtube.com/watch?v=XKHEtdqhLK8&t=2312s"
slice = slice(12,-32)
print(website[slice])
print(website_[slice])
