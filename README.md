# Puutarhasovellus
## Vaatimusmäärittely  
https://github.com/rundtjan/ot-harjoitustyo/blob/master/puutarhasovellus/dokumentaatio/vaatimusmaarittely.md  
## Asennus
1. Siirry kansioon "Puutarhasovellus"
```bash
cd puutarhasovellus
```
2. Asenna riippuvuudet:
```bash
poetry install
```
3. Suorita alustustoimenpiteet, HUOM! on olemassa kaksi vaihtoehtoa, jos sinun terminaalissa toimii python toimii komennolla "py" käytä:  
```bash
poetry run invoke build   
```
Jos taas python toimii komennolla "python3" käytä:
```bash
poetry run invoke alt-build
```
4. Käynnistä joko komennolla
```bash
poetry run invoke start
```
tai (jos python toimii komennolla "python3" sinun terminaalissa):
```bash
poetry run invoke alt-start
```
