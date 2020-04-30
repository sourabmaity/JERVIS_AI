from fuzzywuzzy import fuzz,process
import find

for l in find.list:
    print(process.extractOne("today news", l))