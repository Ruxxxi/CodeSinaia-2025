countries = set() #create an empty set to store the unique countries
missing_altitude = 0
with open('IntroToPy/mountains_db.tsv', 'r', encoding='utf-8') as f:
#only want the data rows, not the column names
    for row in f: #each 'row' is a list: [mountain_name, height, country, country_code]
        parts = row.strip().split('\t') # Split by tab character
        if len(parts) >= 2: #make sure we have at least mountain name and height
            height = parts[1]
            if height == "NULL" or height == '' or height.strip() == '':
                missing_altitude +=1
            country = parts[2]
            countries.add(country)

print("Done running")   
#print(len(countries))
print(f"Mountains with missing altitude: {missing_altitude}")
#print("Done running!")

'''
#de ce git?
#game rts?
#a inceput sa foloseasca git pentru ca a pierdut tot progresul pe 1 luna
#a dat commit fara push, a pierdut 2 luni de munca (50 commit-uri)
#git? -> colaborare in echipa, rollback la versiuni anterioare, backup in cloud al proiectelor
#git VS github
#git provine de la git good (injuratura)
concepte din git
- branches si commit tree
branch main/master
lazygit
git checkout <nume branch>
-rollback si rollforward
git log --oneline
git stash
git checkout
git stash pop
git fetch
git pull
git push
git remove -v
- Staging
commit?
-merge conflict
- pull requests
'''