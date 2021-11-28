# Gardening application
## System requirements  
https://github.com/rundtjan/ot-harjoitustyo/blob/master/puutarhasovellus/dokumentaatio/vaatimusmaarittely.md 
## Application architecture
https://github.com/rundtjan/ot-harjoitustyo/blob/master/puutarhasovellus/dokumentaatio/architecture.md 
## For the course : työaikakirjanpito
https://github.com/rundtjan/ot-harjoitustyo/blob/master/puutarhasovellus/dokumentaatio/tyoaikakirjanpito.md 
## Installation
1. Change directory to the folder "Puutarhasovellus"
```bash
cd puutarhasovellus
```
2. Install dependencies:
```bash
poetry install
```
3. Build database, NB! if python is accessed with the command "py" in your terminal, use the command:  
```bash
poetry run invoke build   
```
If python is accessed with the command "python3" in your terminal, use the command:
```bash
poetry run invoke alt-build
```
4. Run the application either (if python is called "py" in your terminal):
```bash
poetry run invoke start
```
or (if python is called "python3" in your terminal):
```bash
poetry run invoke alt-start
```
## Command line usage  
Start the application with:  
```bash
poetry run invoke start
```
Or if your terminal uses "python3" to access python use:  
```bash
poetry run invoke alt-start
```
To run tests:
```bash
poetry run invoke test
```
To analyze test coverage:
```bash
poetry run invoke coverage-report
```
To check the quality of the code with pylint
```bash
poetry run invoke pylint
```
Or then enter the poetry shell with
```bash
poetry shell
```
So you can leave out "poetry run" in all the commands above.
