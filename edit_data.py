import pandas
from langdetect import detect

data = pandas.read_csv('quotes.csv')

# print(data['text'].to_list())
english_only =[]
for paragraph in data['text'].to_list():

    if detect(paragraph) == 'en':
        english_only.append(paragraph)

new_data = {
    'Thomas_Sowel_Quotes':english_only,
}
create_list = pandas.DataFrame(new_data)

create_list.to_csv('thomas_sowell_quotes.csv',index=False)