import pandas as pd

df = pd.read_csv('seattle_pet_licenses.csv')

pet_name_counts = df['animal_s_name' ].value_counts()  

top_3_pets = pet_name_counts.head(3)  

print('Top three most common  pet names:')
for pet_name, count in top_3_pets.items():  
    print(f"{pet_name}, {count}")

df.info()