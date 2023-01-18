'''
This program allows us to search from a txt file and choose the best option through a parameter input.
'''
import spacy  # importing spacy
nlp = spacy.load('en_core_web_md') # specifying the model we want to use. Remember to install this model by typing python -m spacy download en_core_web_md into your command line

'''
This function allows us sort a list in reverse order.
'''
def Sort(sub_li):       
    sub_li.sort(key = lambda x: x[0], reverse=True)
    return sub_li

v_list=[]
def wich_movie_next(f_descripcion):
    f=open("movies.txt","r")                    # I open the txt file
    for line in f:
        movies=line.strip("\n")
        v_value=0
        g1=nlp(f_descripcion)                   
        g2=nlp(movies)
        v_value=g2.similarity(g1)               # I search the best option.
        v_list.append([v_value,movies])
    Sort(v_list)
    print(v_list[0][1])                         # I print the first option.  

v_description=input("Which wovie would you like to watch:")
wich_movie_next(v_description)                  # I call the function.

