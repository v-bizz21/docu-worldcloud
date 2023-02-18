import pandas as pd
import spacy
import PyPDF2 as pf
import matplotlib.pyplot as plt
from wordcloud import WordCloud
nlp = spacy.load(r'C:\Users\utente\AppData\Local\Programs\Python\Python38\Lib\site-packages\en_core_web_sm\en_core_web_sm-2.3.1')
p = input("\nInserire percorso file\n")
p1 = p[:-1]
path = p1[1:]
pdf = pf.PdfFileReader(open(r'%s' % path, 'rb'))
starting_page = int(input("\n Da quale pagina si desidera partire?\n"))
end_page = int(input("\n Fine a che pagina si desidera convertire?\n"))
i = starting_page
txt = str('')
while i <= end_page:
    pdf_get_page = pdf.getPage(i)
    text = pdf_get_page.extractText()
    txt = txt + text
    i = i + 1

print("\nYour text is:\n", txt)
doc = nlp(txt)
token_list = [token for token in doc]
print('\n LIST OF TOKENS', token_list)
df = pd.DataFrame(token_list, columns=['token'])
print(df)
filtered = [token for token in token_list if not token.is_stop]
print('\n FILTERED TOKENS', filtered)
lemma = [token.lemma_ for token in filtered]
punct = ["?", ".", ";", ":", "!",'"', '\n', '\n\n', '...', '-', '_', ',', '(', ')', 'Ł', '%']
for token in lemma:
    if token in punct:
        lemma.remove(token)
print('\n TOKEN LEMMAS', lemma)
df1 = pd.DataFrame(lemma, columns=['filtered_lemmas'])
print('\n', df1)
df2 = df1.groupby(['filtered_lemmas']).size().sort_values(ascending=False)
print('\n', df2)
wordcloud = WordCloud(width=1280, height=853, margin=0, colormap='Reds').generate(txt)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.margins(x=0, y=0)
plt.show()
