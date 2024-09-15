from pydub import AudioSegment
from pydub.playback import play
import time
import re

lst_sound = {
    "m" : "m",
    "d" : "d",                
    "m" : "m",          
    "t" : "t",          
    "s" : "s",            
    "q" : "k",             
    "a" : "a",              
    "z" : "z",               
    "ion" : "j-ɔ̃_tild",        
    "ieu" : "j-ø",             
    "io" : "j-o",             
    "p" : "p",              
    "e" : "ə̠_bottom_line", 
    "x" : "k-s",           
    "n" : "n",             
    "u" : "y",               
    "l" : "l",               
    "b" : "b",                
    "p" : "p",                
    "o" : "o",               
    "i" : "i",               
    "v" : "v",                
    "g" : "g",                
    "k" : "k",                
    "è" : "ɛ:",               
    "é" : "e",                   
    "on" : "ɔ̃_tilde",            
    "o" : "o",               
    "spc" : "separator",       
    "ian" : "ɥ-ɑ̃_tild",          
    "ou" : "u",              
    "ai" : "ɛ",              
    "ê" : "ɛ:",                
    "an" : "ɑ̃_tilde",              
    "eu" : "ø",                 
    "à" : "a",                 
    "ain" : "ɛ̃_tild",            
    "ean" : "ɑ̃_tilde",               
    "eam" : "ɑ̃_tilde",             
    "au" : "o",                 
    "ié" : "j-e",                
    "iai" : "ɥ-ɛ",                  
    "iè" : "j-ɛ:",                
    "ue" : "y",              
    "ett" : "ɛ-t",             
    "epp" : "ɛ-t",              
    "err" : "ɛ-r",                 
    "ch" : "ʃ",                   
    "et" : "e",               
    "es" : "ɛ",                
    "ess" : "ɛ-s",                
    "enn" : "ɛ-n",                
    "f" : "f",                
    "ph" : "f",                 
    "oin" : "o-ɛ̃_tilde",               
    "ec" : "ɛ-c",                  
    "ecc" : "ɛ-c",                 
    "off" : "o-f",                 
    "onn" : "o-n",                  
    "ott" : "j",                    
    "omm" : "ɔ-m",                
    "oss" : "ɔ-s",                  
    "ô" : "o",                   
    "y" : "j",                  
    "ll" : "j",                   
    "ep" : "e-p",                   
    "oo" : "u:",                   
    "ann" : "a-n",                 
    "â" : "ɑ",                   
    "ein" : "ɛ̃_tilde",               
    "os" : "ɔ-s",                  
    "w" : "w",                  
    "or" : "ɔ-r",                 
    "c" : "k",                 
    "un" : "œ̃_tild",                
    "in" : "ɛ̃_tild",                
    "ci" : "si",             
    "j" : "ʒ",                
    "r" : "ʀ",               
    "gn" : "ɲ",                
    "ing" : "ŋ",                 
    "ang" : "ŋ",                  
    "ong" : "ŋ",               
    "ung" : "ŋ",                  
    "h" : "'",                   
    "ï" : "i"                   
}

sound_keys_lst = list(lst_sound.keys())
sound_values_lst = list(lst_sound.values())

voy_l = ["a", "e", "i", "o", "u"]
voy_l2 = ["a", "e", "i", "o", "u", "à", "é", "è", "ô", "ê", "y"]
spe_csn = ["r", "t", "p", "s", "n", "c", "f", "m"]

except_dct = {
        "héros" : "héro",    
        "monsieur" : "monsieu", 
        "eau" : "au",      
        "elle" : "aile",  
        " ce " : " ceu ",
        "^ce " : "ceu ",
        " ce$" : " ceu",
        " te " : " teu ",
        "^te " : "teu ",
        " te$" : " teu",
        " me " : " meu ",     
        "^me " : "meu ",    
        " me" : " meu",    
        " re " : " reu ",     
        " re$" : " reu",    
        "^re " : "reu ",     
        " le " : " leu ",    
        "^le " : "leu ",     
        " le$" : " leu",     
        " pe " : " peu ",    
        "^pe " : "peu ",     
        " pe$" : " peu",     
        " be " : " beu ",    
        " be$" : " beu",     
        "^be " : "beu ",     
        "pays" : "paiï",    
        " je " : " jeu ",
        "^je " : "jeu ", 
        " je$" : " jeu",
        "^je$" : "jeu", 
        "^re$" : "reu",  
        "^me$" : "meu",      
        "^te$" : "teu",      
        "^le$" : "leu",
        "^te$" : "teu"      
        }

keys_lst = list(except_dct.keys())
values_lst = list(except_dct.values())

all_txt = str(input("Text? "))

for i in range(0, len(except_dct), 1):
    all_txt = re.sub(keys_lst[i], values_lst[i], all_txt)

all_txt = "spc".join(list(all_txt)).split("spc")

t = 0
cur_lettr = ""
phonetic_rtn = ""

while t < len(all_txt):
    if all_txt[t] not in [" ", ",", "'"]:
        cur_lettr = all_txt[t]
        if cur_lettr == "h":
            t += 2
            cur_lettr = all_txt[t - 1]
        elif cur_lettr in voy_l and t + 1 < len(all_txt):
            if t + 1 < len(all_txt):
                if all_txt[t + 1] in voy_l:
                    no_stop = True
                    t += 1
                else:
                    no_stop = False
                while no_stop:
                    cur_lettr += all_txt[t]
                    if t + 1 < len(all_txt):
                        if all_txt[t + 1] not in voy_l:
                            no_stop = False
                        else:
                            t += 1
                    else:
                        no_stop = False
                if t + 2 < len(all_txt) and all_txt[t]:
                    if all_txt[t + 1] == all_txt[t + 2]:
                        cur_lettr += all_txt[t + 1] + all_txt[t + 1]
                        t += 3
                        if t < len(all_txt):
                            if all_txt[t] == "e":
                                t += 1
                    elif all_txt[t + 1] in ["t", "s", "c", "z", "r"] and all_txt[t + 2] == " " and cur_lettr == "e":
                        t += 1
                        cur_lettr += all_txt[t]
                    elif cur_lettr == "e" and all_txt[t + 1] == "s" and all_txt[t + 2] not in voy_l2:
                        cur_lettr = "es"
                        t += 1
                    elif all_txt[t + 1] == "n" and all_txt[t + 2] not in voy_l2:  
                        t += 2
                        cur_lettr += "n"
                    elif all_txt[t] == "o" and all_txt[t + 1] == "r":
                        cur_lettr = "or"
                        t += 2
                    elif all_txt[t + 1] == "s" and all_txt[t + 2] in voy_l:
                        t += 1
                        all_txt[t] = "z"
                    else:
                        t += 1
                elif t + 1 < len(all_txt):
                    if all_txt[t + 1] in ["t", "s", "c", "z", "r"] and cur_lettr == "e":
                        t += 1
                        cur_lettr += all_txt[t]
                    elif all_txt[t + 1] == "n":   
                        cur_lettr += all_txt[t + 1]
                        t += 2
                    elif all_txt[t + 1] == "r" and cur_lettr == "o":
                        t += 2
                        cur_lettr = "or"
                    elif all_txt[t + 1] == "s" and cur_lettr == "o":
                        t += 2
                        cur_lettr = "os"
                    else:
                        t += 1
                else:
                    t += 1
        elif cur_lettr == "g" and t + 1 < len(all_txt):
            if all_txt[t + 1] == "e":
                cur_lettr = "j"
                t += 2
            else:
                t += 1
        else:
            t += 1
            if t + 1 < len(all_txt):
                if all_txt[t] == "u" and all_txt[t + 1] == "e":
                    t += 2
                    if t + 1 < len(all_txt):
                        if all_txt[t + 1] == " " and all_txt[t] in ["x", "s"]:
                            t += 1
                    elif t + 1 == len(all_txt):
                        if all_txt[t] in ["x", "s"]:
                            t += 1
                elif cur_lettr == "p" and all_txt[t] == "h":
                    cur_lettr = "ph"
                    t += 1
                elif cur_lettr == "c" and all_txt[t] == "u":
                    cur_lettr = "cu"
                    t += 1
                elif cur_lettr == "c" and all_txt[t] == "h":
                    cur_lettr = "ch"
                    t += 1
                elif cur_lettr == "t" and all_txt[t] == "i" and all_txt[t + 1] in voy_l:
                    cur_lettr = "s"
                elif cur_lettr == "c" and all_txt[t] == "e" and all_txt[t + 1] == "p":
                    cur_lettr = "ep"
                elif cur_lettr == "l" and all_txt[t] == "l":
                    cur_lettr = "ll"
                    t += 2
                elif all_txt[t] == "e" and all_txt[t + 1] == " ":
                    t += 1
            elif t < len(all_txt):
                if all_txt[t] == "e":
                    t += 1
                elif cur_lettr == "l" and all_txt[t] == "l":
                    cur_lettr = "ll"
                    t += 2
        if t + 1 < len(all_txt):
            if t + 2 < len(all_txt):
                if all_txt[t] in ["d", "t", "p"] and all_txt[t + 1] == "s" and all_txt[t + 2] == " ":
                    t += 2
                elif all_txt[t] in ["t", "s", "h", "p", "x", "d", "l"] and all_txt[t + 1] == " ":
                    t += 1
            elif all_txt[t] in ["t", "s", "h", "p", "x", "d", "l"] and all_txt[t + 1] == " ":
                t += 1
        elif t + 1 == len(all_txt):
            if all_txt[t] in ["t", "s", "h", "p", "x", "d", "l"]:
                t += 1
        time.sleep(.2)
        phonetic_rtn += cur_lettr + "-"
        print(sound_values_lst[sound_keys_lst.index(cur_lettr)])
    elif t - 1 > 0:
        t += 1
        if all_txt[t - 2] == "n":
            if t < len(all_txt):
                if all_txt[t] in voy_l2:
                    phonetic_rtn += "n-"
                    print("n")
    else:
        phonetic_rtn += " "
        print(" ")
        time.sleep(0.2)
        t += 1

print(phonetic_rtn[0:(len(phonetic_rtn) - 1)])








